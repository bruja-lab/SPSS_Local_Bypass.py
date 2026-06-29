import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. The Raw Data (All 40 students' completed classes)
data = [1, 6, 3, 3, 3, 4, 4, 5, 2, 3, 
        3, 1, 6, 4, 3, 4, 4, 0, 4, 10, 
        3, 3, 2, 7, 6, 4, 4, 1, 5, 3, 
        3, 4, 5, 4, 7, 4, 3, 2, 3, 4]

df = pd.DataFrame(data, columns=['Classes_Completed'])

# 2. Calculate Frequencies and Percentages
freq_table = df['Classes_Completed'].value_counts().sort_index().reset_index()
freq_table.columns = ['Classes Completed', 'Frequency']
freq_table['Valid Percent (%)'] = (freq_table['Frequency'] / len(df) * 100).round(1)

print("--- FREQUENCY TABLE ---")
print(freq_table.to_string(index=False))

# 3. Calculate Descriptive Statistics
mean_val = df['Classes_Completed'].mean()
median_val = df['Classes_Completed'].median()
# Mode can return multiple values, we take the first one
mode_val = df['Classes_Completed'].mode()[0] 
range_val = df['Classes_Completed'].max() - df['Classes_Completed'].min()
variance_val = df['Classes_Completed'].var() # pandas defaults to sample variance (n-1)
std_dev_val = df['Classes_Completed'].std()

print("\n--- DESCRIPTIVE STATISTICS ---")
print(f"Total N: {len(df)}")
print(f"Mean (M): {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Mode: {mode_val}")
print(f"Range: {range_val}")
print(f"Sample Variance (s²): {variance_val:.2f}")
print(f"Sample Standard Deviation (s): {std_dev_val:.2f}")

# 4. Generate the Histogram (Best graph for Ratio/Quantitative Data)
plt.figure(figsize=(10, 6))

# Using bins aligned to our discrete values (0 through 10)
bins = np.arange(-0.5, 11.5, 1)
plt.hist(df['Classes_Completed'], bins=bins, color='seagreen', edgecolor='black', alpha=0.8)

plt.title('Classes Completed Prior to Behavioral Statistics (N=40)', fontsize=14, fontweight='bold')
plt.xlabel('Number of Classes', fontsize=12)
plt.ylabel('Frequency (Number of Students)', fontsize=12)
plt.xticks(range(0, 11))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the chart
plt.show()
