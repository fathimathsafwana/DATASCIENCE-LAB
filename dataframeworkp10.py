import pandas as pd

# Create a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 22, 21, 23, 20],
    'Marks': [85, 90, 78, 88, 95],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Display basic information
print("\nBasic Information:")
print(df.info())
