import time
inicio = time.time()
a=int(input("Ingrese la cota inferior del rango de datos: "))
b=int(input("Ingrese la cota superior del rango de datos: "))
def numero_primo(a,b):
    for i in range(a,b+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
              
        if conta == 2:
            print(f'{i} es un primo')
        
fin = time.time()
numero_primo(a,b)