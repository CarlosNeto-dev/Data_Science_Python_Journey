"""This archive talks about my tenth exercise about numpy library!"""
import numpy as np

# Criando arrays...
A = np.ones((3, 3))
B = np.array([1, 2, 3])

# Fazendo Broadcasting...

# Verificando se é compatível os shapes dos arrays "A" e "B":
print(A.shape)
print(B.shape) # Durante o cálculo, o numpy irá extender o shape para (1, 3), sendo compatível.
print("--------------")

print(A + B) # Não dá erro, pois os valores lidos da direita para a esquerda são iguais.
