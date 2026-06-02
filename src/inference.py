import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, beta

# Menambahkan path folder utama agar folder src terbaca
sys.path.append("../") 

# Import fungsi yang sudah dibuat di src/inference.py
from src.inference import ci_bernoulli, credible_interval