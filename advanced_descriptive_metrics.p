import pandas as pd
import numpy as np
from scipy import stats

# 1. Enter your 5 text message data points here
data = [10, 25, 5, 50, 15]
df = pd.DataFrame(data, columns=['Texts_Per_Day'])

# 2. Calculate the required statistics
desc = df['Texts_Per_Day'].describe()
mode = stats.mode(df['Texts_Per_Day'], keepdims=True)
variance = df['Texts_Per_Day'].var()
data_range = df['Texts_Per_Day'].max() - df['Texts_Per_Day'].min()

# 3. Print the results clearly
print("--- Descriptive Statistics ---")
print(f"Mean: {desc['mean']}")
print(f"Median: {desc['50%']}")
print(f"Mode: {mode.mode[0]}")
print(f"Standard Deviation: {desc['std']}")
print(f"Variance: {variance}")
print(f"Range: {data_range}")
