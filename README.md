# stat-audit--pandas-dev/pandas-2025
# Statistical Health Report — pandas-dev/pandas

> Audit statistik terhadap repository open-source **pandas-dev/pandas** menggunakan konsep Statistika dan Probabilitas (Minggu 11–14) STI 2025.  
> Analisis dilakukan menggunakan GitHub REST API untuk mengevaluasi kesehatan project, probabilitas merge PR, pola issue, dan performa maintenance repository.



# Research Questions

| ID | Pertanyaan | Teknik Statistik | Notebook |
|---|---|---|---|
| RQ1 | Berapa probabilitas Pull Request di pandas-dev/pandas berhasil di-merge? | Bernoulli MLE + CI | `02` + `03` |
| RQ2 | Apakah rata-rata jumlah issue mingguan berubah signifikan setelah major release tertentu? | Poisson MLE + Z-Test | `02` + `04` |
| RQ3 | Berapa probabilitas issue membutuhkan lebih dari 30 hari untuk ditutup? | Monte Carlo Simulation | P(issue > 30 hari) = 0,6677 (66,77%) - Diestimasi melalui simulasi Monte Carlo 50.000 trial. Sekitar 2 dari 3 issues di pandas-dev/pandas membutuhkan lebih dari 30 hari untuk ditutup. |



# Tim

| Member | Nama | NIM | Role |
|---|---|---|---|
| A | Tsabita Nuriska Ramadhani | 1519625050 | Data Engineer |
| B | Muhammad Nafilham Athaya | 1519625041 | Estimation Analyst |
| C | Daffa  Raditia Nova |  1519625058 | Inference Analyst |
| D | Muhammad Yunus Setiaji | 1519625043 | Hypothesis Analyst |
| E | Muhamad Bintang Ramadhan | 1519625031 | Computational Analyst |


# Temuan Utama

*(Bagian ini akan diisi setelah seluruh analisis selesai dilakukan)*

1. blabla
2. Analisis MLE dan Beta Posterior menghasilkan estimasi probabilitas keberhasilan Pull Request sebesar 62,09%, menunjukkan bahwa peluang Pull Request untuk di-merge lebih tinggi dibandingkan ditolak.
3. Perhitungan 95% Confidence Interval (Frequentist) dan Credible Interval (Bayesian) menunjukkan hasil yang konsisten, di mana probabilitas sebenarnya dari keberhasilan merge sebuah Pull Request berada pada rentang yang sempit, yaitu antara 60,6% hingga 63,6%.
4. 
5. Bloom Filter dengan parameter k=5 dan m=10.000 mampu mendeteksi bug report secara efisien dengan FPR teoritis hanya 0,0034%, layak diimplementasikan pada sistem triage otomatis.


# Cara Menjalankan

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Ambil data GitHub API
python fetch_data.py

# 3. Jalankan notebook secara berurutan
jupyter notebook
```

# Struktur Repository

```text
stat-audit-moby-sti-2025/
│
├── README.md
├── AI_USAGE_LOG.md
│
├── data/
│   ├── raw/
│   │   
│   │
│   └── clean/
│    
│
├── src/
│   ├── estimator.py
│   ├── inference.py
│   ├── hypothesis.py
│   └── simulation.py
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_estimation.ipynb
│   ├── 03_confidence_interval.ipynb
│   ├── 04_hypothesis_testing.ipynb
│   └── 05_simulation.ipynb
│
├── report/
│   └── statistical_health_report.pdf
│
├── presentation/
│   └── video_link.md
│
├── fetch_data.py
└── requirements.txt
