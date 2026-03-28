# Pedindo os números ao usuário (separados por espaço)
entrada = input("Digite uma lista de números separados por espaço: ")

# Transformando a string de entrada em uma lista de números inteiros
numeros = [int(n) for n in entrada.split()]

# Calculando a soma apenas dos ímpares
soma_impares = 0
for n in numeros:
    if n % 2 != 0:
        soma_impares += n

print(f"A lista digitada foi: {numeros}")
print(f"A soma dos números ímpares é: {soma_impares}")

import random

# Criando uma lista com 10 números aleatórios entre 1 e 100
# O 'range(10)' define que queremos 10 itens na lista
lista_aleatoria = [random.randint(1, 100) for _ in range(10)]

print(f"Lista gerada: {lista_aleatoria}")

# Encontrando o maior e o menor
maior = max(lista_aleatoria)
menor = min(lista_aleatoria)

print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")
