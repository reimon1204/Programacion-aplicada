import matplotlib.pyplot as plt

# Datos
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]

# Crear un gráfico de barras
plt.bar(categories, values, color='blue')

# Etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Mostrar el gráfico
plt.show()
