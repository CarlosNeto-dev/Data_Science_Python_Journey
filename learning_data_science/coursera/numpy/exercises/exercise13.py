"""This archive talks about my thirteen exercise of numpy library!"""
import numpy as np

# Criando dois arrays aleatórios...

A = np.random.rand(2, 3, 4)
B = np.random.rand(2, 4, 5)

# Verificando os shapes dos Arrays "A" e "B"...

print(A.shape)
print("------------------")
print(B.shape)
print("------------------")

# São compatíveis, pois:
# O número de colunas de A igualam o número de linhas de B.
# O eixo anterior dos Arrays "A" e "B" são compatíveis via broadcasting.

# Fazendo Dot Product de A @ B...

print(A @ B)