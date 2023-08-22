#Uso del ciclo while
while True:
    valor=int(input("Ingrese un numero de valor entero positivo: ")) 
    print("Valor: ", valor)
    a = isinstance(valor, int)
    #Condicional if
    if a==True and valor>0:
    #Indica que se cumpla la condicion de que a se mantenga en estado verdadero y que valor sea estricatamente mayor a 0
       fact=1
       #Ciclo for, para que recorra desde el numero 1 hasta la variable valor+1
       for i in range (1, valor + 1):
           fact=fact*i
           print(f'el factorial de {valor} es: ', fact)
       #si a esta es estado falso o la varible valor es menor a 0, se establece otra ruta procedimental
    else:
        print("Por favor, ingrese un numero entero positivo")