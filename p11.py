import pandas as pd

data = {
    'Name': ['Asha', 'Ravi', 'Anu', 'Rahul'],
    'Age': [20, 22, 19, 21],
    'Marks': [80, 90, 75, 85]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Filter rows where Marks > 80
print("\nMarks greater than 80:")
print(df.loc[df['Marks'] > 80])

# Select Name and Marks columns
print("\nName and Marks:")
print(df.loc[:, ['Name', 'Marks']])

# Filter rows and select specific columns
print("\nStudents with Marks > 80:")
print(df.loc[df['Marks'] > 80, ['Name', 'Marks']])
