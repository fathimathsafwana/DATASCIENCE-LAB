import matplotlib.pyplot as plt
marks={22,45,67,89,34,56,23,12,45,67,78,67,45,34,89,100}
bins=range(0,101,10)
plt.figure(figsize=[9,5])
plt.hist(marks,bins=bins,edgecolor='black',color='lightpink')
plt.title("Distribution of students marks")
plt.xlabel("Marks intervals")
plt.ylabel("Number of students")
plt.xticks(bins)
plt.yticks(range(0,5,1))
plt.grid(axis='y',alpha=0.75)
plt.show()
