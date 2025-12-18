"""This archive talks about my sixth exercise about numpy library!"""
import numpy as np

# Criando um array 2D...
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Usando Boolean Mask e Slicing:

# Slicing
CHANGING_VALUE = A[1, :] = 0
print(A) # Retorna-se uma "view" do Array "A".
print("-------------")

# Boolean Mask
CHANGING_VALUE2 = A[A > 50]
COPYING_VALUES = CHANGING_VALUE2[:] = -1
print(A) # Retorna-se uma "copy" do Array "A"
