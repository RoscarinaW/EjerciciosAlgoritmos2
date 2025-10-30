#Programa para determinar la mitad de un numero ingresado por el usuiario es mayor o menor que 100
print("---Programa para determinar la mitad de un numero ingresado por el usuario es MAYOR o MENOR de 100---")
print("---"*10)
a = float(input("Ingrese un numero: "))
Division = a / 2

if Division > 100:
    print(f"La mitad de {a} es {Division}")
    print("---"*10)
    print("El {} es mayor de 100. ".format(Division))
elif Division < 100:
    print(f"La mitad de {a} es {Division}")
    print("---"*10)
    print("El {} es menor de 100.".format(Division))