#Ejercicio 40, programa que sume los numero primos naturales

print("<<--Suma de los Numero primos Naturales-->>")
while True:
    try:
        N = int(input("Introduce el numero límite (N) para la suma (ej: si es 5, la suma sera 1+2+3+4+5):  "))
        if N >= 1: 
            break
        else:
            print("N debe ser un número natural (entero positivo)")
    except ValueError:
        print("Entrada no válida, ingrese un numero entero")

suma = 0
contador = 1

while contador <= N:
    suma += contador
    contador += 1

print(f"\n<<<---RESULTADO--->>>")
print(f"La suma de los primeros {N} números naturales es: {suma} ")