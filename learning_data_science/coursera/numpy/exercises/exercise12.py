"""This archive talks about my twelfth exercise of numpy library!"""
import numpy as np

# Criando dois arrays...
A = np.array([
    [1, 2, 3],
    [4, 5, 6]])
B = np.array([1, 0, 1])

# Verificando os shapes dos Arrays "A" e "B"...

print(A.shape)
print("------------------")
print(B.shape) # Durante o cálculo, o numpy entenderá (1, 3), sendo compatível.
print("------------------")

# Fazendo Dot Product de A @ B...

print(A @ B)

# Isso funcionou, pois o número de colunas de A igualam o número de linhas de B.
# Se fizéssemos B @ A, daria errado. Pois não seria compatível segundo a regra.
