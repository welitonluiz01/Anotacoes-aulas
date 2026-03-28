# Criar lista aleatoria com 10 numeros entre 1 e 100,
# e mostrar o maior e o menor numero da lista

import random

lista_numeros = []
for i in range(10):
    lista_numeros.append(random.randint(1, 100))

print("Lista de números:", lista_numeros)

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
