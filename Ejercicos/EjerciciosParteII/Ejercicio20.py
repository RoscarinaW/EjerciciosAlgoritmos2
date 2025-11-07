#Programa para determinar si un número es par o impar 
print("Programa para determinar si un numero Entero es par o impar")
print("<<>>"*2)

numero = int(input("Ingrese un numero entero: "))
resto = numero % 2

if resto == 0:
    print("El numero ingresado es un numero PAR")
else:
    print("El numero ingresado es un numero IMPAR")