import pandas as pd
import matplotlib.pyplot as plt

# 1. The Raw Data (All 30 students exactly as they appear in the problem)
raw_data = [
    "Psychology", "Sociology", "Sociology", "Psychology", "Psychology", 
    "Psychology", "Psychology", "Psychology", "Psychology", "History", 
    "Communications", "Sociology", "Other", "Other", "Business", 
    "Sociology", "Psychology", "Psychology", "Psychology", "History", 
    "Political Science", "Sociology", "Psychology", "Psychology", "Psychology", 
    "Psychology", "Sociology", "Anthropology", "Other", "Psychology"
]

df = pd.DataFrame(raw_data, columns=['Major_Label'])

# 2. The Coding Map (Assigning numbers to the qualitative categories)
coding_map = {
    "Psychology": 1,
    "Sociology": 2,
    "History": 3,
    "Communications": 4,
    "Business": 5,
    "Political Science": 6,
    "Anthropology": 7,
    "Other": 8
}

# 3. Apply the Code to the Data
df['Numeric_Code'] = df['Major_Label'].map(coding_map)

# 4. Show the Full Coded Dataset (Using .to_string() to prevent truncation)
print("--- FULL CODED DATA VIEW ---")
print(df[['Numeric_Code', 'Major_Label']].to_string())

# 5. Calculate SPSS-style Frequencies & Percentages
# Grouping by both the numeric code and the label for a clean table
freq_table = df.groupby(['Numeric_Code', 'Major_Label']).size().reset_index(name='Frequency')
freq_table['Valid Percent (%)'] = (freq_table['Frequency'] / len(df) * 100).round(1)

print("\n\n--- SPSS FREQUENCY TABLE ---")
print(freq_table.to_string(index=False))
print(f"\nTotal N: {len(df)}")

# 6. Generate the Frequency Bar Chart
plt.figure(figsize=(10, 6))

# Ensure the bars display in the numerical order of our codes (1 through 8)
plot_data = df.groupby('Major_Label').size().reindex(list(coding_map.keys()))
plot_data.plot(kind='bar', color='mediumpurple', edgecolor='black')

plt.title('Statistics Student Majors Survey (N=30)', fontsize=14, fontweight='bold')
plt.xlabel('Declared Major (Coded 1-8)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the chart
plt.show()
