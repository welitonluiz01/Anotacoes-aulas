import numpy as np
import matplotlib.pyplot as plt

pesos = [60.2, 73.5, 64.0, 68.1, 87.0, 75.4, 70.0, 76.8, 81.2, 58.9, 69.7, 92.5, 78.6, 66.3, 71.8, 79.5, 63.7, 72.5, 83.0, 76.1]
alturas = [1.65, 1.75, 1.68, 1.72, 1.90, 1.80, 1.77, 1.82, 1.87, 1.60, 1.74, 2.00, 1.78, 1.67, 1.73, 1.83, 1.62, 1.76, 1.90, 1.79]

corr_coef = np.corrcoef(pesos, alturas)[0, 1]

plt.scatter(pesos, alturas)
plt.xlabel('Peso (kg)')
plt.ylabel('Altura (m)')
plt.title(f'Correlação: {corr_coef:.2f}')
plt.show()

goupby = ['peso', 'altura']
print(goupby)
