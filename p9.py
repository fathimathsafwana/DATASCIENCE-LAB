import matplotlib.pyplot as plt
rollnumber=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks=[22,87,5,43,56,73,55,54,11,20,61,5,79,31,27]
plt.figure(figsize=[9,5])
plt.scatter(rollnumber,marks,color="violet",s=60,edgecolor="black",label="students")
plt.title("students marks VS roll number")
plt.xlabel("roll number")
plt.ylabel("marks obtained")
plt.grid(True,linestyle="--",alpha=0.3)
plt.legend()
plt.show()
