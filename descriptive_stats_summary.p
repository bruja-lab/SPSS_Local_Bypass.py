import pandas as pd

# 1. Put your 5 numbers here
my_data = [10, 25, 5, 50, 15]

# 2. Create the DataFrame
df = pd.DataFrame(my_data, columns=['TextsPerDay'])

# 3. Calculate the stats
print("--- Data Table ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
