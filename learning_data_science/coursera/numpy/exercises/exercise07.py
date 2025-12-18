"""This archive talks about my seventh exercise of numpy library!"""
import numpy as np

# Criando o primeiro array 1D...
A = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
])
CHANGING_ARRAY_A = A[5:] = 0
print(A) # Retorna-se uma "view"

# Criando o segundo array 1D...
B = np.arange(0, 6)
FANCY_INDEXING = B[[1, 0, 4, 2]]
COPYING_VALUES = FANCY_INDEXING[:] = 0
print(B) # Retorna-se uma "copy"
