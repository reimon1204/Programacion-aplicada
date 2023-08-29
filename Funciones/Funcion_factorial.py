def funcion_factorial(a):
    while True:
        #Condicional while
            fact=1
        #Ciclo for, para que recorra desde el numero 1 hasta la variable valor+1
            for i in range (1, a + 1):
                fact=fact*i
            return fact
def evaluar_num(a):
    if a>0:
        funcion_factorial(a)
        print("El numero factorial de",a ,"Es: ",funcion_factorial(a))
    else:
        print("Por favor, ingrese un numero entero positivo")
a=int(input("Ingrese el numero para calcular su factorial(debe ser entero): "))
print("Valor ingresado: ",a)
evaluar_num(a)