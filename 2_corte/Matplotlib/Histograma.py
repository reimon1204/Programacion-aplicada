import matplotlib.pyplot as plt
import numpy as np

# Datos generados aleatoriamente
data = np.random.randn(1000)

# Crear un histograma
plt.hist(data, bins=30, color='green', alpha=0.7)

# Etiquetas y título
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el gráfico
plt.show()
