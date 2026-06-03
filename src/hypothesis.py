import numpy as np
import scipy.stats as stats

def z_test_one_sample(x_bar, mu0, sigma, n, alternative='two-sided', alpha=0.05):
    """
    Performs a one-sample Z-test.
    Formula used: Z = (x_bar - mu0) / (sigma / sqrt(n)) per Tsun (2020), p. 306.
    """
    # 1. Hitung Z-statistic
    z_stat = (x_bar - mu0) / (sigma / np.sqrt(n))
    
    # 2. Hitung P-value berdasarkan arah pengujian
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
        
    # 3. Pengambilan Keputusan (Sesuai larangan ketat dosen: TIDAK BOLEH menulis 'accept H0')
    if p_value < alpha:
        decision = "Reject H0"
        interpretation = f"With a p-value of {p_value:.4f} < {alpha}, we have sufficient evidence to reject H0 at the {alpha} significance level."
    else:
        decision = "Fail to reject H0"
        interpretation = f"With a p-value of {p_value:.4f} >= {alpha}, we fail to reject H0 at the {alpha} significance level. There is insufficient evidence to support the alternative hypothesis."
        
    return {
        "z_stat": z_stat,
        "p_value": p_value,
        "decision": decision,
        "interpretation": interpretation
    }