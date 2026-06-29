import pandas as pd

# 1. Create a list of the 5 responses
data = ['Mac', 'Mac', 'Mac', 'Mac', 'PC']

# 2. Convert to a pandas Series (a one-dimensional array)
responses = pd.Series(data, name='ComputerPreference')

# 3. Calculate frequency counts
frequency = responses.value_counts()

# 4. Calculate percentages
percentage = responses.value_counts(normalize=True) * 100

# 5. Combine into a results table
results = pd.DataFrame({'Frequency': frequency, 'Percentage': percentage})

# Display the results
print("--- Frequency Distribution ---")
print(results)
