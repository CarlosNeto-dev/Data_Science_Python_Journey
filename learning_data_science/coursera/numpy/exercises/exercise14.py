"""This archive talks about my fourteen exercise of numpy library!"""
import numpy as np

# Criando um array 1D aleatório...
A = np.random.rand(12, )

# Fazendo reshape()...
print(A.reshape(3, 4))
print("----------------------------------------------------")
print(A.reshape(2, 2, 3))

# Para fazer um reshape, é necessário ser compatível segundo a regra.
# Ou seja, é necessário ter a mesma composição distribuídos entre si.
