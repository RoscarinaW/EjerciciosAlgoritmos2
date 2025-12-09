#Ejercicio 43. Conteo de numero frecuente, solicitar ese numewro en inicio al usuario.

print("<<<---Conteo de frecuencia de un Número--->>>")

while True:
    try:
        numeroBuscar = float(input("Ingrese el Número que desea contar en la lista: "))
        break
    except ValueError:
        print("Entrada no valida")
    
while True:
    try:
        n = int(input(f"¿Cuántos números va a ingresar en total?: "))
        if n >= 1: 
            break
        else:
            print("N debe ser al menos 1")
    except ValueError:
        print("Entrada no válida")

contadorLista = 0
conteoFrecuencia = 0 

while contadorLista < n:
    try:
        numIngresado = float(input(f"Ingresa el numero {contadorLista + 1} de {n}: "))
        if numIngresado == numeroBuscar:
            conteoFrecuencia += 1
        contadorLista += 1
    except ValueError:
        print("Entrada no válida, ingrese un numero")

print("\n <<<---Resultado--->>>")
print(f"El numero {numeroBuscar} apareció {conteoFrecuencia} veces")
