import numpy as np
import hashlib

# 1. MONTE CARLO SIMULATION

def estimate_probability(event_fn, n_trials=50000, seed=42):
    """
    Mengestimasi probabilitas suatu kejadian menggunakan simulasi Monte Carlo.

    Metode: Jalankan event_fn sebanyak n_trials kali, hitung proporsi True.
    Formula: P(event) ≈ (jumlah kejadian True) / n_trials
    Referensi: Tsun (2020), p. 325.

    Parameters
    ----------
    event_fn : callable
        Fungsi tanpa argumen yang mengembalikan bool.
        Dipanggil sekali per trial.
    n_trials : int
        Jumlah simulasi (default: 50000).
    seed : int
        Random seed untuk reproducibility.

    Returns
    -------
    dict
        {
          'probability': float,       # estimasi probabilitas
          'n_trials': int,            # jumlah trial
          'n_success': int,           # jumlah kejadian True
          'std_error': float          # standard error estimasi
        }
    """
    np.random.seed(seed)
    results = np.array([event_fn() for _ in range(n_trials)])
    n_success = int(results.sum())
    prob = n_success / n_trials
    std_error = np.sqrt(prob * (1 - prob) / n_trials)

    return {
        'probability': round(prob, 6),
        'n_trials': n_trials,
        'n_success': n_success,
        'std_error': round(std_error, 6)
    }


def make_issue_duration_event_fn(duration_array, threshold=30, seed=42):
    """
    Membuat event_fn untuk estimate_probability berdasarkan distribusi empiris
    duration_days dari dataset issues pandas-dev/pandas.

    Digunakan untuk menjawab RQ3:
    'Berapa probabilitas issue membutuhkan lebih dari 30 hari untuk ditutup?'

    Parameters
    ----------
    duration_array : array-like
        Array duration_days dari issues yang sudah closed (tanpa NaN).
    threshold : int
        Batas hari (default: 30).
    seed : int
        Random seed.

    Returns
    -------
    callable
        Fungsi event_fn siap pakai untuk estimate_probability().
    """
    rng = np.random.default_rng(seed)
    arr = np.array(duration_array)

    def event_fn():
        sampled = rng.choice(arr)
        return bool(sampled > threshold)

    return event_fn

# 2. BLOOM FILTER

class BloomFilter:
    """
    Implementasi Bloom Filter — struktur data probabilistik untuk keanggotaan.

    Digunakan dalam konteks audit untuk mengecek apakah suatu issue number
    pernah tercatat sebagai bug report secara efisien (tanpa menyimpan semua ID).

    Formula False Positive Rate (FPR):
        FPR = (1 - (1 - 1/m)^n)^k
    Referensi: Tsun (2020), p. 329.

    Parameters
    ----------
    k : int
        Jumlah fungsi hash yang digunakan.
    m : int
        Ukuran bit array.
    """

    def __init__(self, k, m):
        self.k = k          # jumlah hash functions
        self.m = m          # ukuran bit array
        self.bit_array = np.zeros(m, dtype=bool)
        self.n_items = 0    # jumlah item yang sudah di-add

    def _get_positions(self, item):
        """
        Menghasilkan k posisi index dari sebuah item menggunakan k hash functions.
        Setiap hash function dibedakan dengan prefix 'hash_i_'.
        """
        positions = []
        for i in range(self.k):
            hash_input = f"hash_{i}_{item}".encode('utf-8')
            hash_val = int(hashlib.md5(hash_input).hexdigest(), 16)
            positions.append(hash_val % self.m)
        return positions

    def add(self, item):
        """
        Menambahkan item ke Bloom Filter.
        Semua posisi hasil hash di-set True pada bit array.

        Parameters
        ----------
        item : any
            Item yang akan ditambahkan (akan dikonversi ke string).
        """
        for pos in self._get_positions(str(item)):
            self.bit_array[pos] = True
        self.n_items += 1

    def contains(self, item):
        """
        Mengecek apakah item mungkin ada dalam set (probabilistik).

        Returns True jika semua posisi hash bernilai True (mungkin ada / false positive).
        Returns False jika minimal satu posisi False (pasti tidak ada).

        Parameters
        ----------
        item : any
            Item yang akan dicek.

        Returns
        -------
        bool
            True = mungkin ada, False = pasti tidak ada.
        """
        return all(self.bit_array[pos] for pos in self._get_positions(str(item)))

    def theoretical_fpr(self, n):
        """
        Menghitung False Positive Rate (FPR) teoritis.

        Formula: FPR = (1 - (1 - 1/m)^n)^k
        Referensi: Tsun (2020), p. 329.

        Parameters
        ----------
        n : int
            Jumlah item yang sudah dimasukkan ke filter.

        Returns
        -------
        float
            Estimasi FPR teoritis.
        """
        return (1 - (1 - 1 / self.m) ** n) ** self.k

# 3. MCMC — KNAPSACK

def mcmc_knapsack(items, capacity, n_iter=100000, seed=42):
    """
    Mengestimasi solusi optimal knapsack problem menggunakan
    Markov Chain Monte Carlo (MCMC) dengan Metropolis-Hastings algorithm.

    Konteks: Digunakan untuk mengestimasi kombinasi issues yang bisa
    diselesaikan tim maintainer dalam kapasitas effort tertentu,
    memaksimalkan total 'nilai' (misal: jumlah bug yang ditutup).

    Metode: Mulai dari solusi awal acak, tiap iterasi flip satu item,
    terima perubahan jika meningkatkan objective atau dengan probabilitas
    Metropolis. Referensi: Tsun (2020), p. 331.

    Parameters
    ----------
    items : list of dict
        Setiap item berupa {'name': str, 'weight': float, 'value': float}.
    capacity : float
        Kapasitas maksimum (misal: total hari effort tim).
    n_iter : int
        Jumlah iterasi MCMC (default: 100000).
    seed : int
        Random seed untuk reproducibility.

    Returns
    -------
    dict
        {
          'best_items': list,         # nama item dalam solusi terbaik
          'best_value': float,        # total value solusi terbaik
          'best_weight': float,       # total weight solusi terbaik
          'acceptance_rate': float,   # proporsi proposal yang diterima
          'n_iter': int
        }
    """
    np.random.seed(seed)
    n = len(items)

    # Inisialisasi: semua item tidak dipilih
    current = np.zeros(n, dtype=bool)
    best = current.copy()

    def total_weight(state):
        return sum(items[i]['weight'] for i in range(n) if state[i])

    def total_value(state):
        return sum(items[i]['value'] for i in range(n) if state[i])

    best_value = 0.0
    n_accepted = 0

    for _ in range(n_iter):
        # Proposal: flip satu item secara acak
        flip_idx = np.random.randint(0, n)
        proposed = current.copy()
        proposed[flip_idx] = not proposed[flip_idx]

        # Cek feasibility
        if total_weight(proposed) > capacity:
            continue

        current_val = total_value(current)
        proposed_val = total_value(proposed)

        # Metropolis acceptance
        if proposed_val >= current_val:
            current = proposed
            n_accepted += 1
        else:
            # Terima dengan probabilitas exp(delta) / (1 + exp(delta))
            delta = proposed_val - current_val
            accept_prob = np.exp(delta) / (1 + np.exp(delta))
            if np.random.random() < accept_prob:
                current = proposed
                n_accepted += 1

        # Update solusi terbaik
        if total_value(current) > best_value:
            best = current.copy()
            best_value = total_value(current)

    return {
        'best_items': [items[i]['name'] for i in range(n) if best[i]],
        'best_value': round(best_value, 4),
        'best_weight': round(total_weight(best), 4),
        'acceptance_rate': round(n_accepted / n_iter, 4),
        'n_iter': n_iter
    }
