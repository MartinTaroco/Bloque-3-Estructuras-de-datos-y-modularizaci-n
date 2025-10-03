#Desafio 2

import numpy as np

A = np.array([[1,0,1], [4,-1, 4], [5,6,7]])

inversaA = np.linalg.inv(A)

print(A)
print("-"*20)
print(inversaA)
print("-"*20)
print(A@inversaA)
