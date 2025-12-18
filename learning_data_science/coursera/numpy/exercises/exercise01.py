"""This archive talks about my first exercise of numpy library!"""
import numpy as np

# Crie:
ARRAY_ONE = np.arange(0, 10) # Um array 1D com valores de 0 a 9.
ARRAY_TWO = np.ones((3, 3)) # Um array 2D com o shape (3, 3) preenchido por um
ARRAY_THREE = np.zeros((2, 2, 3)) # Um array 3D com o shape (2, 2, 3) preenchido com zeros

# Análise

# ARRAY_ONE:
print(ARRAY_ONE.ndim)
print(ARRAY_ONE.shape)
print(ARRAY_ONE.dtype)

# ARRAY_TWO:
print(ARRAY_TWO.ndim)
print(ARRAY_TWO.shape)
print(ARRAY_TWO.dtype)

# ARRAY_THREE:
print(ARRAY_THREE.ndim)
print(ARRAY_THREE.shape)
print(ARRAY_THREE.dtype)
