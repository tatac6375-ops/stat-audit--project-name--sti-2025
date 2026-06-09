# AI Usage Log
# AI Usage Log — stat-audit-project-name-sti-2025

## Summary

| Member | Role | Tools | ~% code AI-assisted | Interpretation cells AI-assisted? |
|---|---|---|---|---|
| Tsabita Nuriska Ramadhani | Data Engineer |  | -% | No |
| Muhammad Nafilham Athaya | Estimation Analyst |  | -% | No |
| Daffa Raditia Nova | Inference Analyst | Gemini | 40% | No |
| Muhammad Yunus Setiaji | Hypothesis Analyst | Gemini | 40% | No |
| Muhammad Bintang Ramadhan | Computational Analyst | Claude | 40% | No |

---

# Per-Member Detail

## Member A — Data Engineer

| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|---|---|---|---|
| 1 | Generate API lopp | Claude | Ambil data issues & PR pandas | Ya - disesuaikan |
| 2 | Pembersihan & pembuatan kolom statistik | Gemini | "Bantu susun ekstraksi data untuk kolom type, is_bug, is_merged, dan duration_days" | Ya - menyelaraskan penamaan variabel dengan kebutuhan analisis kelompok |
| 3 |  |  |  | TBD |
| 4 |  |  |  | TBD |
| 5 |  |  |  | TBD |

---

## Member B — Estimation Analyst

| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|---|---|---|---|
| 1 | Bantu nyusun estimator module  | ChatGPT | Membantu menyusun struktur fungsi MLE Bernoulli, Beta posterior, dan likelihood visualization pada phyton module | Ya - disesuaikan kembali dengan formula Tsun (2020) dan requirement project |
| 2 | Debugging Import sama notebook integration | ChatGPT | Bantuin debugging import src.estimator, kernel notebook, dan visualisasi likelihood | Ya - penyesuaian path, variabel, dan interpretasi dilakukan manual |
| 3 | Rapihin Visualisasi Likelihood | ChatGPT | Ngasih saran ngerapihin tampilan grafik Likelihood function | Ya - label, garis estimator, dan interpretasi diperbaiki ulang secara manual |
| 4 |   |   |   | TBD |
| 5 |   |   |   | TBD |

---

## Member C — Inference Analyst

| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|---|---|---|---|
| 1 | Scaffolding Sintaks Confidence Interval | Gemini | Meminta boilerplate kode Python (scipy.stats.interval dan norm.interval) untuk menghitung interval kepercayaan berdasar sampel data | Ya. Nilai alpha (tingkat kepercayaan), degrees of freedom (df), dan input variabel array (seperti data waktu close issue) disesuaikan secara mandiri. |
| 2 | Ekstrasi Credible Interval dari Posterior  | Gemini | Meminta referensi logika kode untuk mencari batas persentil (Highest Posterior Density / HPD) dari array distribusi posterior | Ya. Sintaks dirombak untuk menerima input array yang secara spesifik dihasilkan dari modul Estimation Analyst, lalu diintegrasikan dengan dataframe proyek. |
| 3 | Troubleshooting & Handling NaN/Error | Gemini | Meminta bantuan debugging ketika perhitungan interval menghasilkan nilai NaN (Not a Number) atau infinity pada dataset. | Ya. Solusi handling missing values tidak ditelan mentah-mentah; keputusan untuk melakukan drop atau imputasi didasarkan pada domain knowledge secara manual. |
| 4 |   |   |   | TBD |
| 5 |   |   |   | TBD |

---

## Member D — Hypothesis Analyst

| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|---|---|---|---|
| 1 | Coding boilerplate untuk pemanggilan fungsi Z-Test | Gemini | "Meminta kerangka kode Python untuk memanggil fungsi z_test_one_sample dari modul lokal" | Ya - Variabel disesuaikan dengan data riil n dan x_bar dari repositori Pandas. |
| 2 | Pembuatan struktur template (scaffolding) laporan | Gemini | "Meminta struktur kosong 6-step procedure uji hipotesis" | Ya - Mengisi seluruh teks narasi langkah dan kesimpulan secara mandiri tanpa AI. |
| 3 |  |  |  | TBD |
| 4 |  |  |  | TBD |
| 5 |  |  |  | TBD |

---

## Member E — Computational Analyst

| # | Task | Tool | Prompt | Cara output digunakan |
|---|---|---|---|---|
| 1 | Scaffolding struktur class BloomFilter | Claude | Meminta kerangka implementasi Bloom Filter dengan k hash functions menggunakan hashlib | Ya, logika `_get_positions`, pemilihan parameter k dan m, serta konteks dataset disesuaikan secara mandiri  |
| 2 | Boilerplate loop simulasi Monte Carlo | Claude | Meminta kerangka loop n_trials untuk estimasi probabilitas empiris |  Ya, `event_fn` berbasis `np.random.choice` dari distribusi empiris dan threshold 30 hari dirancang sendiri |
| 3 |  Scaffolding struktur fungsi MCMC | Claude | Meminta kerangka Metropolis-Hastings untuk knapsack problem | Ya, definisi items dari data bug issues nyata, nilai capacity, dan acceptance criterion disesuaikan sendiri  |
| 4 |  |  |  | TBD |
| 5 |  |  |  | TBD |

---

# Group Reflection (150–300 words)
his section will be completed collectively by all team members after the statistical audit project is finalized.
