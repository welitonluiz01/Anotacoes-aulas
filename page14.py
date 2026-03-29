import matplotlib.pyplot as plt

x = 'Janeiro 2025'
x2 = 'Fevereiro 2025'


y = 'Janeiro 2026'
y2 = 'Fevereiro 2026'



x = [10, 24, 18, 46, 65]
x2 = [28, 35, 10, 33, 45]

y = [12, 14, 36, 28, 35]
y2 = [2, 10, 34, 20, 30]

# Criando o gráfico de linhas 

#plt.style.use('ggplot')
#plt.plot(x, color = '#E1F000',label='Janeiro 2025', ls ='--', marker='o', markerfacecolor="#2ED404", markersize=8)
#plt.plot(x2, color = '#00F04C', label='Janeiro 2026', ls = '-', marker='v', markerfacecolor="#F000F0", markersize=8)
#plt.plot(y, color = '#F000F0', label='Fevereiro 2025', ls = '--', marker='s', markerfacecolor="#E1F000", markersize=8)
#plt.plot(y2, color = '#2ED404', label='Fevereiro 2026', ls = '-', marker='D', markerfacecolor="#00F04C", markersize=8)

#plt.xlabel('Quantidade')
#plt.ylabel('Tempo')
#plt.title('Comparação entre Anos', fontdict={'fontsize': 16, 'fontweight': 'bold', 'color': "#0A7935"})
#plt.legend()

#plt.show()

figura =  plt.figure(figsize= (10,5))
figura.suptitle('Comparativo')

figura.add_subplot(131)
plt.plot(x, color = '#E1F000',label='Janeiro 2025', ls ='--', marker='o', markerfacecolor="#2ED404", markersize=8)
plt.title('2025')
plt.legend()

figura.add_subplot(132)
plt.plot(y, color = "#0004F0",label='Janeiro 2026', ls ='--', marker='>', markerfacecolor="#2ED404", markersize=8)
plt.title('2026')
plt.legend()


plt.show()
