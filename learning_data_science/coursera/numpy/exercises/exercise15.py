"""This archive talks about my fifteen exercise of numpy library!"""
import numpy as np

# Importando informações do arquivo CSV

DATA = np.genfromtxt("exercise_archive", delimiter=",", skip_header=1)
print(DATA)

# Papel das funcionalidades do "genfromtxt":

# delimiter -⇾ É responsável por buscar o separador de cada frase, se for errado, retorna nan.
# skip_header -⇾ Ele pula uma determinada linha do arquivo.

# Por que retornou "nan"?

# É retornado "nan" três vezes. Pois não é possível converter valores não numéricos
# O numpy não é ideal para isso, é melhor usar o PANDAS nesses casos.
