#Ejercicio 41 Listado de N numero y determinar el numero mayor y el numero menor

print("<<<---Número Mayor y Menor de N Números--->>>")

while True:
    try:
        N = int(input("¿Cuántos números va a ingresar? (N):"))
        if N >= 1:
            break
        else:
            print("iDebe ingresar al menos un número.")
    except ValueError:
        print("Entrada no válida, ingrese un numero entero")

contador = 1
numeroMayor = None
nuemroMenor = None

while contador <= N:
    try:
        num = float(input(f"Introducce el numero {contador}: "))
        if contador == 1:
            numeroMayor = num
            nuemroMenor = num
        else:
            if num > numeroMayor:
                numeroMayor = num
            if num < nuemroMenor:
                nuemroMenor = num
        contador += 1
    except ValueError:
        print("Entrada no válida, ingrese un numero")

print(f"\n<<<---RESULTADO--->>>")
print("De los {N} números ingresados: ")
print(f"El numero mayor es: {numeroMayor}")
print(f"El numero nemor es: {nuemroMenor}")