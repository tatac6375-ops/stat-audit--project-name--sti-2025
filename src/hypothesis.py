import numpy as np
import scipy.stats as stats

def z_test_one_sample(x_bar, mu0, sigma, n, alternative='two-sided', alpha=0.05):
    """
    Melakukan uji Z satu sampel (one-sample Z-test) untuk rata-rata atau proporsi.
    
    Formula:
    Z = (x_bar - mu0) / (sigma / sqrt(n))
    
    Referensi:
    Tsun (2020), p. 306
    
    Parameters:
    x_bar (float): Rata-rata sampel atau proporsi sampel hasil observasi.
    mu0 (float): Nilai rata-rata atau proporsi di bawah asumsi hipotesis nol (H0).
    sigma (float): Deviasi standar populasi (atau standar eror yang diketahui).
    n (int): Ukuran sampel (banyaknya data).
    alternative (str): Arah pengujian ('two-sided', 'less', 'greater'). Default 'two-sided'.
    alpha (float): Tingkat signifikansi pengujian. Default 0.05.
    
    Returns:
    dict: Hasil pengujian berisi z_stat, p_value, decision, dan interpretation.
    """
    # 1. Hitung statistik uji Z
    z_stat = (x_bar - mu0) / (sigma / np.sqrt(n))
    
    # 2. Hitung p-value berdasarkan arah alternatif pengujian
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    elif alternative == 'greater':
        p_value = stats.norm.sf(z_stat)  # Menggunakan survival function untuk akurasi numerik
    else:
        raise ValueError("Argumen alternative harus berupa 'two-sided', 'less', atau 'greater'.")
        
    # 3. Menentukan keputusan penarikan kesimpulan statistik
    if p_value < alpha:
        decision = "Reject H0"
        interpretation = (f"Dengan nilai p-value = {p_value:.4f} < alpha ({alpha}), "
                          f"terdapat bukti statistik yang kuat untuk menolak H0. Perubahan atau perbedaan "
                          f"pada metrik repositori GitHub ini bersifat signifikan secara nyata.")
    else:
        decision = "Fail to reject H0"
        interpretation = (f"Dengan nilai p-value = {p_value:.4f} >= alpha ({alpha}), "
                          f"kita gagal menolak H0. Tidak terdapat cukup bukti statistik untuk menyatakan bahwa "
                          f"metrik repositori GitHub mengalami perubahan yang signifikan secara nyata.")
        
    return {
        "z_stat": z_stat,
        "p_value": p_value,
        "decision": decision,
        "interpretation": interpretation
    }

def z_test_two_sample(x_bar1, x_bar2, sigma1, sigma2, n1, n2, alternative='two-sided', alpha=0.05):
    """
    Melakukan uji Z dua sampel independen (two-sample Z-test).
    
    Formula:
    Z = (x_bar1 - x_bar2) / sqrt((sigma1^2 / n1) + (sigma2^2 / n2))
    
    Referensi:
    Tsun (2020), p. 309
    
    Parameters:
    x_bar1 (float): Rata-rata atau proporsi dari sampel kelompok pertama.
    x_bar2 (float): Rata-rata atau proporsi dari sampel kelompok kedua.
    sigma1 (float): Deviasi standar atau standar eror kelompok pertama.
    sigma2 (float): Deviasi standar atau standar eror kelompok kedua.
    n1 (int): Ukuran sampel kelompok pertama.
    n2 (int): Ukuran sampel kelompok kedua.
    alternative (str): Arah pengujian ('two-sided', 'less', 'greater'). Default 'two-sided'.
    alpha (float): Tingkat signifikansi pengujian. Default 0.05.
    
    Returns:
    dict: Hasil pengujian berisi z_stat, p_value, decision, dan interpretation.
    """
    # 1. Hitung statistik uji Z dua sampel
    denominator = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    z_stat = (x_bar1 - x_bar2) / denominator
    
    # 2. Hitung p-value berdasarkan arah alternatif pengujian
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    elif alternative == 'greater':
        p_value = stats.norm.sf(z_stat)
    else:
        raise ValueError("Argumen alternative harus berupa 'two-sided', 'less', atau 'greater'.")
        
    # 3. Menentukan keputusan penarikan kesimpulan statistik
    if p_value < alpha:
        decision = "Reject H0"
        interpretation = (f"Dengan nilai p-value = {p_value:.4f} < alpha ({alpha}), "
                          f"terdapat bukti statistik yang kuat untuk menolak H0. Perbandingan antara kedua "
                          f"kelompok sampel di repositori menunjukkan perbedaan yang signifikan secara nyata.")
    else:
        decision = "Fail to reject H0"
        interpretation = (f"Dengan nilai p-value = {p_value:.4f} >= alpha ({alpha}), "
                          f"kita gagal menolak H0. Tidak terdapat cukup bukti statistik untuk menyatakan adanya "
                          f"perbedaan bermakna antara kedua kelompok sampel yang diteliti.")
        
    return {
        "z_stat": z_stat,
        "p_value": p_value,
        "decision": decision,
        "interpretation": interpretation
    }