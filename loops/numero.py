import random
from matplotlib import pyplot as plt # para poder correr el codigo, es necesario instalar o tener en el computador la extension de la libreria matplotlib

# Add your code below:
numbers_a = range(1, 13)
numbers_b = [random.randint(1, 1000) for i in range(12)]
plt.plot(numbers_a, numbers_b)
plt.show()
