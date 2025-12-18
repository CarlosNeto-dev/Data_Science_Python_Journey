"""This archive talks about my ninth exercise of numpy library!"""
import numpy as np

# Criando dois arrays 1D...
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Fazendo Operações Aritméticas Básicas...
ADDITION = A + B
print(ADDITION)
print("--------------")

SUBTRACTION = A - B
print(SUBTRACTION)
print("--------------")

MULTIPLICATION = A * B
print(MULTIPLICATION)
print("--------------")

DIVISION = A / B
print(DIVISION)
print("--------------")

EXPONENTIATION = A ** B
print(EXPONENTIATION)
print("--------------")

# Por que isso é mais rápido do que um loop comum no Python?

# Os dados são armazenadas de forma contígua e linear na memória;
# Não há a necessidade de checar o tipo de cada elemento no array;
# É feita de elemento para elemento.
