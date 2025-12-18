"""This archive talks about my eighth exercise of numpy library!"""
import numpy as np

# Criando um array 1D...
A = np.array([10, 15, 20, 25, 30, 35])

# Usando Indexing...
ODD_VALUES = A[A % 2 == 0]
print(A) # Retornou uma "copy"
print("----------------")

FILTERED_VALUES = A[A > 25]
MASK = FILTERED_VALUES[:] = 100
print(A) # Retornou uma "copy"
print("----------------")

CHOOSED_NUMBERS = A[[0, 2, 4]]
print(A) # Retornou uma "copy"
