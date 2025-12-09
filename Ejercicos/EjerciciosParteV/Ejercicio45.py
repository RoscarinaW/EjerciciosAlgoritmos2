#Ejercicio Calcular el factorial de un numero.

print("Calculo de factorial")

while True:
    try:
        N = int(input("Ingrese un numero positivo para calcular su factorial: "))
        if N >= 0:
            break
        else:
            print("El factorial solo se calcula para números enteros no negativos")
    except ValueError:
        print("solo ingrese un numero entero")

factorial = 1
contador = N

if N == 0:
    factorial = 1
else: 
    while contador > 0:
        factorial *= contador
        contador -= 1

print(f"\n<<<--- Resultado --->>>")
print(f"El factorial de {N} ({N}!) es: {factorial}")