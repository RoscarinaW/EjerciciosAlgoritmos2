#Ejercicio 42 Potencias elevadas cubo cuarta y quinta

print("Potencia de N Número (Cubo, Cuarta y Quinta)")

while True:
    try:
        N = int(input("¿De cuántos números deseas calcular las potencias? (N):"))
        if N >= 1:
            break
        else:
            print("Dede ingresar N mayor o igual a 1")
    except ValueError:
        print("Entrada no válida, ingrese un numero entero")
contador = 0

print("\n Calculos de potencias ")
while contador < N:
    try: 
        num = float(input(f"Ingrese el numero {contador + 1}: "))

        cubo = num ** 3
        cuarto = num ** 4
        quinta = num ** 5

        print(f" El Número ingresado es {num}: ")
        print(f"    - Cubo (potencia de 3): {cubo:.2f}")
        print(f"    - Cuarta potencia (potencia de 4): {cuarto:.2f}")
        print(f"    - Quinta potencia (potencia de 5): {quinta:.2f}")

        contador += 1
    except ValueError:
        print("Entrada no válida, ingrese un numero")
print("\n <<<---Fin del calculo--->>>")