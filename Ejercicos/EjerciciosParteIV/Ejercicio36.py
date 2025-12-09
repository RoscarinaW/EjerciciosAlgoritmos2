#Ejercicio 36, tabla de multiplicar.

print("<<<---Tabla de Multiplicar--->>>")

while True:
    try:
        numeroBase = int(input("Ingresa el numero de la tabla de multiplicar a consultar: "))
        break
    except ValueError:
        print("Ingrese solo un numero entrero")

limiteTabla = 10
print(f"\nLa tabla de Multiplicar del {numeroBase} hasta el {limiteTabla}: ")

for i in range(1, limiteTabla + 1):
    resultado = numeroBase * i
    print(f"{numeroBase} x {i} = {resultado}")