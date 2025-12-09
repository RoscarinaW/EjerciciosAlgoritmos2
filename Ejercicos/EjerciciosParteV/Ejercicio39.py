#Ejercicio 39 Potencia (Base y exponente)

print("<<<---Calculo de potencia--->>>")

while True:
    try:
        base = int(input("Ingrese el valor de la base (Numer entero): "))
        break
    except ValueError:
        print("Entreda no valida, solo numero entero.")
while True:
    try:
        exponente = int(input("Ingrese el valor del exponente (Numer entero): "))
        if exponente >= 0:
            break
        else:
            print("El exponente debe ser un numero entero no negativo")
    except ValueError:
        print("Entreda no valida, solo numero entero.")

resultado = 1
contador = 0

while contador < exponente:
    resultado *= base
    contador += 1

print(f"\n<<<---RESULTADO--->>>")
print(f"La potencia de {base} elevado a {exponente} es: {resultado}")