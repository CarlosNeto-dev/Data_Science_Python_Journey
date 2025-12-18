"""This archive talks about my eleventh exercise of numpy library!"""
import numpy as np

# Qual desses arrays são compatíveis para a realização de uma operação aritmética?

A = np.ones((4, 3))
B = np.array([1, 2, 3])
C = np.array([1, 2])

# Verificando os shapes de cada array...
print(A.shape)
print("----------")
print(B.shape)
print("----------")
print(C.shape)
print("----------")

# A única operação compatível seria A + B. Pois seguem a regra de compatibilidade.
print(A + B)
