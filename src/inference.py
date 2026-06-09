import numpy as np
from scipy.stats import norm, beta

def ci_bernoulli(k, n, confidence=0.95):
    """
    Menghitung Frequentist Confidence Interval untuk distribusi Bernoulli.
    Referensi: Tsun (2020) halaman ... (isi sesuai instruksi dosen/modul)
    """
    # 1. Hitung proporsi (p_hat)
    p_hat = k / n
    
    # 2. Hitung Z-score berdasarkan tingkat confidence
    alpha = 1 - confidence
    z_score = norm.ppf(1 - alpha / 2)
    
    # 3. Hitung Standard Error dan Margin of Error (Masukkan rumus statistiknya)
    se = np.sqrt((p_hat * (1 - p_hat)) / n)
    margin_of_error = z_score * se
    
    # 4. Hitung batas bawah dan atas
    lower_bound = p_hat - margin_of_error
    upper_bound = p_hat + margin_of_error
    
    # 5. Kembalikan output dalam bentuk dictionary sesuai format di Notebook
    return {'lower_bound': lower_bound, 'upper_bound': upper_bound}

def credible_interval(alpha, beta_param, confidence=0.95):
    """
    Menghitung Bayesian Credible Interval menggunakan distribusi Beta.
    """
    # 1. Hitung tail (sisa probabilitas di ujung kiri dan kanan)
    alpha_tail = (1 - confidence) / 2
    
    # 2. Cari batas bawah dan atas menggunakan Inverse CDF (PPF) dari distribusi Beta
    # Kita menggunakan alpha dan beta_param sebagai parameter distribusinya
    lower_bound = beta.ppf(alpha_tail, alpha, beta_param)
    upper_bound = beta.ppf(1 - alpha_tail, alpha, beta_param)
    
    # 3. Kembalikan hasilnya dalam bentuk dictionary
    return {'lower_bound': lower_bound, 'upper_bound': upper_bound}