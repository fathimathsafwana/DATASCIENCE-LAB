import pandas as pd
data={
    'name':['ali','sara','anu','ramu'],
    'age':[21,15,24,27],
    'marks':[85,90,78,88]
}
df=pd.DataFrame(data)
print("original DataFrame")
print(df)
print("\nStudents with marks>80:")
print(df[df['marks']>80])
print("\nSelected data using .loc:")
print(df.loc[0:2,['name','marks']])
