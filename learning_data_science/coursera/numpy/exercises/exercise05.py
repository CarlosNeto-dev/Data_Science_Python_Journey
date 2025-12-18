"""This archive talks about my fifth exercise of numpy library!"""
import numpy as np

# Criando um array 2D...
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Usando Fatiamento (Slicing) e Indexação (Indexing):

FOUNDING_VALUE_50 = A[1, 1]
print(FOUNDING_VALUE_50)
print("--------------")

FIRST_ROW = A[0, :]
print(FIRST_ROW)
print("--------------")

LAST_COLUMN = A[:, -1]
print(LAST_COLUMN)
print("--------------")

SUBMATRIX = A[:2, 1:3]
print(SUBMATRIX)
