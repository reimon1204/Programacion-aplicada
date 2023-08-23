lista=["Rojo","Azul", "Amarillo","Naranja","Violeta","Verde"]
print(lista)
print(type(lista))
print(lista[2])

print("My lista tiene una cantidad de", len(lista), "elementos")
print(lista[0:3])
print(lista[:2])

lista.append("Blanco")
lista.insert(3,"Negro")
print(lista)

lista.extend(['Marron', 'Gris'])  
print(lista)
lista.remove("Marron")
print(lista)
lista.insert(8,"Marron")
print(lista.pop)
size=len(lista)

lista_nueva=lista*3
print("Lista nueva:", lista_nueva)

print("Sort:")
print()
my_listaSort = lista.sort()
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("ordenar lista: ")
my_NumList.sort()
print(my_NumList)


#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)