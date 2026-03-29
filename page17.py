import matplotlib.pyplot as plt

regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
vendas = [1500, 2500, 1800, 3000, 2700]


plt.bar(regioes, vendas, color="#D00808")
plt.title( 'Vendas por Região')
plt.xlabel('Regiões')
plt.ylabel('Vendas')

plt.show()
