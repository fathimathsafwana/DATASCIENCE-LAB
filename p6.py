import numpy as np

r1=int(input("enter rows for Matrix A:"))
c1=int(input("enter columns for Matrix A:"))
print(f"Enter {r1} rows(numbers separated by spaces):")

A=np.array([[float(x)for x in input(f"row{i+1}:").split()]for i in range(r1)])
r2=int(input("enter rows for Matrix B:"))
c2=int(input("enter columns for Matrix B:"))

print(f"Enter {r2} columns(numbers separated by spaces):")
B=np.array([[float(x)for x in input(f"column{i+1}:").split()] for i in range(r2)])
print(f"\nMatrix A:\n{A}\n\nMatrix B:\n{B}\n")

if A.shape==B.shape:
    print(f"Addition(A+B):\n{A+B}\n")
else:
    print("Addition not possible(Dimension must match).\n")
if c1==r2:
    print(f"multiplication (A@B):\n{A@B}")
else:
    print(f"multiplication not possible(columns of A must equal Rows of B)")