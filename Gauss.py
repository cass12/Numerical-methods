import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n, omega):
    U = A-(D+L)
    #rewrite x=-(D+L)^-1*(U*x)+(D+L)^-1*b as (D+L)^-1*(b-(U*x))
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))

        print(x)
    return x

'''___MAIN___'''

A = np.array([[10.0, -1.0, 2.0,0.0], [-1.0, 11.0,-1.0, 3.0], [2.0, -1.0, 10.0, -1.0], [0.0, 3.0, -1.0, 8.0]])
b = [6.0, 25.0, -11.0, 15.0]
x = [1, 1, 1,1]
n = 10

print("\n\ninit"),
print(x)
print("")
x = gauss(A, b, x, n)
print("\nSol "),
print(x)
print("Act "),
print (solve(A, b))
print("\n")
