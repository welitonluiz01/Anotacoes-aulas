numeros = input("Digite uma sequência de números separados por vírgula: ")
numeros_lista = numeros.split(",")
soma = 0

for numero in numeros_lista:
    if int(numero) % 2 == 1:
        soma += int(numero)
        print('A soma de todos os números ímpares na lista é:', soma)
        