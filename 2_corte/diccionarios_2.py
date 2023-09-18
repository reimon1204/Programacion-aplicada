diccionario={"Nombre":"Ferley","Apellido":"Raigoso"}.get("Nombre")#Devuelve unicamente el valor de la palabra clave seleccionado.
#Si en la funcion get() la palabra clave no esta presente en el diccionario, se arrojara un valor vacio:none
print(diccionario)
#Actualizar un diccionario a partir de otro diccionario
dict_1={"Color":"Green","Forma":"Cuadrado"}
dict_2={"Color":"Red","Numero":"46"}
print("Antes: ", dict_1)
dict_1.update(dict_2)
print("Despues: ",dict_1)#Si tienen palabras clave en comun, el diccionario 2 sobreescribe su valor en el diccionario 1
#Imprimir las palabras calve dentro de un diccionario
new_dict={"A":"Ardilla","B":"Ballena","C":"Caracol"}
print(new_dict.keys())
print(new_dict.items())