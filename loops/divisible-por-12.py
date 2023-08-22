#Uso del ciclo for
for i in range(100, 301):
    if (i%12) != 0:
        continue
    print(i)
    #A partir del ciclo for, se recorren los numeros del 100 al 300, y con aydua del condicional if, se valida que numeros entre dicho rango, tienen residuo 0 al dividirlos por 12, dichos numeros que cumplen la condicion, son impresos por 
