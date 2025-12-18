"""This archive talks about my third exercise of numpy library!"""
import numpy as np

# Criando os seguintes arrays:
ARRAY_ONE = np.arange(0, 21, 2)
ARRAY_TWO = np.linspace(0, 1, 5)
ARRAY_THREE = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
ARRAY_FOUR = np.array([[7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7, 7]])

# Verificando os arrays:

# ARRAY_ONE:
print(ARRAY_ONE.ndim)
print(ARRAY_ONE.shape)
print(ARRAY_ONE.dtype)
print("--------------")

#ARRAY_TWO:
print(ARRAY_TWO.ndim)
print(ARRAY_TWO.shape)
print(ARRAY_TWO.dtype)
print("--------------")

#ARRAY_THREE:
print(ARRAY_THREE.ndim)
print(ARRAY_THREE.shape)
print(ARRAY_THREE.dtype)
print("--------------")

#ARRAY_FOUR:
print(ARRAY_FOUR.ndim)
print(ARRAY_FOUR.shape)
print(ARRAY_FOUR.dtype)
print("--------------")

# Mostrando os arrays:

# ARRAY_ONE:
print(ARRAY_ONE)
print("-------------------------")

# ARRAY_TWO:
print(ARRAY_TWO)
print("-------------------------")

# ARRAY_THREE:
print(ARRAY_THREE)
print("-------------------------")

# ARRAY_FOUR:
print(ARRAY_FOUR)
print("-------------------------")
