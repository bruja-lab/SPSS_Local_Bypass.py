import pandas as pd
import numpy as np
from scipy import stats

# 1. Enter your 9 sample scores data points here
data = [3, 6, 7, 3, 9, 8, 3, 7, 5]
df = pd.DataFrame(data, columns=['Sample_Scores'])

# 2. Calculate the required statistics
desc = df['Sample_Scores'].describe()
mode = stats.mode(df['Sample_Scores'], keepdims=True)
variance = df['Sample_Scores'].var()
data_range = df['Sample_Scores'].max() - df['Sample_Scores'].min()

# 3. Print the results clearly
print("--- Descriptive Statistics ---")
print(f"Mean: {desc['mean']}")
print(f"Median: {desc['50%']}")
print(f"Mode: {mode.mode[0]}")
print(f"Standard Deviation: {desc['std']}")
print(f"Variance: {variance}")
print(f"Range: {data_range}")
