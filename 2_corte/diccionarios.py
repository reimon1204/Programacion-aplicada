sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
# ejemplo numero 2 diccionarios
translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
#Diccionario con listas:
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"],"Matematicas":"Ferley","Notas bajas":[1,2,1.5,2,0.5]}
print(students_in_classes)
#Diccionario no valido(palabra clave, lista)
#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#Declarar diccionario vacio
my_dictionary={}
my_dictionary["Gafas"]=5
my_dictionary["Zapatos"]=10
print(my_dictionary)
#Actualizar diccionario
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
#Actualizar palabra clave
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
oscar_winners["Animated Feature"] = "No te metas con sojan"
print(oscar_winners)
#Agregar una lista previamente realizada
bebidas=["Coca cola","Speed Max","Fanta","Jugo hit"]
gas=[85,42,21,0]
zipped_bebidas=zip(bebidas,gas)
bebidas_con_gas={key:value for key, value in zipped_bebidas}
print(bebidas_con_gas)