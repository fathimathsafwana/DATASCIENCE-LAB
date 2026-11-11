import pandas as pd

data={
    'name':['ali','sara','anu','ramu'],
    'age':[21,15,24,27],
    'marks':[85,90,78,88],
    'city':['Kochi','Malappuram','Kochi','Kochi']
}

df=pd.DataFrame(data)

print("Original DataFrame")
print(df)

print("\nStudents with marks greater than 80:")
print(df[df['marks']>80])

print("\nStudents aged 24 or above:")
print(df[df['age']>=24])

print("\nStudents from Kochi with marks > 80:")
print(df[(df['city']=='Kochi') & (df['marks']>80)])

print("\nName and Marks of students with marks > 80:")
print(df.loc[df['marks']>80,['name','marks']])
