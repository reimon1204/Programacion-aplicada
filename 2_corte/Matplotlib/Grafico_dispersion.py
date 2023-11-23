import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear un gráfico de dispersión
plt.scatter(x, y, color='red', marker='o')

# Etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Dispersión')

# Mostrar el gráfico
plt.show()
