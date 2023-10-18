class Facade:
    pass
facade1=Facade()
facade_1_type=type(facade1)
print(facade_1_type)
class Grade:
    minimun_passing=65
class Rules:
    def washing_brushes(self):
        return "esta es la prueba"
#Ejercicio 1
class Circle:
    pi=3.14
    def area(self,radius):
        return Circle.pi*radius**2
circle=Circle()
area_piazza=circle.area(12/2)
table_area=circle.area(36/2)
room_area=circle.area(11460/2)
print(area_piazza)
print(table_area)
print(room_area)
#Ejercicio 2
class Circle2:
    pi=3.14
    def __init__(self,diameter):
        print('Nuevo circulo con diametro: {}'.format (diameter))
teaching_table2=Circle2(10)
#Ejercicio 3
class Circle3:
    pi=3.14
    def __init__(self,diameter):
        print('Nuevo circulo con diametro "Ejercicio 3": {d}'.format (d=diameter))
        self.radius =diameter/2
    def circunference(self):
        return 2*self.pi*self.radius
media_pizza=Circle3(12)
teaching_table=Circle3(36)
round_room=Circle3(11460)
print(media_pizza.circunference())
print(teaching_table.circunference())
print(round_room.circunference())
