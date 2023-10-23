
class Circle:
    pi=3.14
    def __init__(self,diameter):
        print('Nuevo circulo con diametro "Ejercicio 1": {d}'.format (d=diameter))
        self.radius =diameter/2
    def circunference(self):
        return print ('Perimetro del circulo:', 2*self.pi*self.radius)
    def area(self):
        return print('area del Circulo:', 2*self.pi*(self.radius)**2)
media_pizza=Circle(12)
teaching_table=Circle(36)
round_room=Circle(11460)
print(media_pizza.circunference())
print(teaching_table.circunference())
print(round_room.circunference())
print(media_pizza.area())
print(teaching_table.area())
print(round_room.area())
#Cuadrado
class Cuadrado:
    def __init__(self,lado):
        print('Nuevo cuadrado de lado "Ejercicio 2": {l}'.format (l=lado))
        self.lado=lado
    def area(self):
        self.area=self.lado*self.lado
        return print('Area del cuadrado: ', self.area)
    def perimetro(self):
        return print('Perimetro del Cuadrado: ', 4*self.lado)
Camilo=Cuadrado(12)
Mauricio=Cuadrado(36)
Ferley=Cuadrado(11460)
print(Camilo.area())
print(Mauricio.area())
print(Ferley.area())
print(Camilo.perimetro())
print(Mauricio.perimetro())
print(Ferley.perimetro())
#Ejercicio 3
from math import sqrt
class Triangulo:
    def __init__(self,lado1, lado2, lado3):
        print('Nuevo Triangulo de lados: {l1}, {l2}, {l3}'.format(l1=lado1, l2=lado2,l3=lado3))
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def area(self):
        S=(self.lado1+self.lado2+self.lado3)/2
        self.area= sqrt(S*(S-self.lado1)*(S-self.lado2)*(S-self.lado3))
        return print('Area del triangulo: ', self.area, S)
    def perimetro(self):
        self.perimetro=self.lado1+self.lado2+self.lado3
        return print('Perimetro del triangulo: ', self.perimetro)

Piramide=Triangulo(4,2,3)
Triangulo1=Triangulo(7,10,12)
print(Piramide.area())
print(Triangulo1.area())
print(Piramide.perimetro())
print(Triangulo1.perimetro())
#Ejercicio 4(triangulo rectangulo)
class Triangulo2:
    def __init__(self,base,altura):
        print('Nuevo Triangulo de base y altura: {b}, {a}'.format(b=base, a=altura))
        self.base=base
        self.altura=altura
    def area(self):
        S=(self.lado1+self.lado2+self.lado3)/2
        self.area= sqrt(S*(S-self.lado1)*(S-self.lado2)*(S-self.lado3))
        return print('Area del triangulo: ', self.area, S)
    def perimetro(self):
        self.perimetro=self.lado1+self.lado2+self.lado3
        return print('Perimetro del triangulo: ', self.perimetro)
#Ejercicio 5
class Rectangulo:
    def __init__(self, largo, ancho):
        print('Nuevo rectangulo de base: {l}'.format (l=largo), 'y ancho: {a}'.format(a=ancho))
        self.largo=largo
        self.ancho=ancho
    def area(self):
        self.area=self.largo*self.ancho
        return print('Area del rectangulo: ', self.area)
    def perimetro(self):
        self.perimetro=2*self.largo+2*self.ancho
        return print('Perimetro del rectangulo: ', self.perimetro)
Rodrigo=Rectangulo(3,2)
Nicolas=Rectangulo(15,20)
print(Rodrigo.area())
print(Nicolas.area())
print(Rodrigo.perimetro())
print(Nicolas.perimetro())