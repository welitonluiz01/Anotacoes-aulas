# Array Numpy (NP) - biblioteca instalada para trabalhar com arrays de forma mais eficiente e rápida do que os
# arrays tradicionais do Python.

import numpy as np

arr2 = np.array([1, 2, 3, 4])
print(arr2)
print(arr2[1])

# NP.arrange() - função para criar um array com um intervalo de números

arr = np.arange(0,100,1,'int')
print(arr)


# Reshape () - função para mudar a forma de um array sem alterar seus dados
arr = np.reshape(arr, (10,10))
print(arr)

# Indexação de matrizes - acessar elementos específicos de um array multidimensional
arr[8,5]
print(arr[8,5])


# Operações sobre matrizes - realizar operações matemáticas em arrays de forma eficiente
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
matriz_soma = matriz1 + matriz2
print(matriz_soma)

matriz_subtracao = matriz1 - matriz2
print(matriz_subtracao)

# NP.SUM - função para calcular a soma de todos os elementos de um array ou a soma ao longo de um eixo específico
arr = np.sum(matriz_soma)
print(arr)

#np.zeros() - função para criar um array preenchido com zeros
arr0 = np.zeros((5,5), dtype='int')
print(arr0)

arr1 = np.ones((5,5), dtype='int')
print(arr1)

# np.eye() - função para criar uma matriz identidade, que é uma matriz quadrada com 1s na diagonal
# principal e 0s em todas as outras posições

arr= np.eye(5,5,0, dtype='int')
print(arr)

# np.random.rand() - função para criar um array com números aleatórios entre 0 e 1
arr = np.random.rand (3,3)
print(arr)


# np.append() - função para adicionar elementos a um array existente
num = np.array(5)
print(num)
num = np.append(num,0.3)
print(num)

#np.diagonal() - função para extrair a diagonal de um array ou criar uma matriz diagonal a partir de um array
arr = np.array([1, 2, 3, 5, 8, 13, 21])
diff = np.diff(arr)
print(diff)


# np.vstack() - função para empilhar arrays verticalmente (um em cima do outro)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_vstack = np.vstack((arr1, arr2))
print(arr_vstack)

# np.column_stack() - função para empilhar arrays horizontalmente (um ao lado do outro)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_column_stack = np.column_stack((arr1, arr2))
print(arr_column_stack)


