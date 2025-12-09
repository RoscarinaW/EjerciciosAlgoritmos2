#Ejercico 46 Caja registradora

print("<<<___CAJA REGISTRADORA___>>>")

while True: 
    try:
        N = int(input("¿Cuántos productos se van a registrar?: "))
        if N >= 1:
            break
        else:
            print("Ingresa al menos un producto.")
    except ValueError:
        print("Entrada no valida")

contadorProductos = 0
valorTotal = 0.0

while contadorProductos < N:
    try:
        precio = float(input(f"Ingresa el precio del producto {contadorProductos + 1}: "))

        if precio < 0: 
            print("El precio no puede ser negativo, Inténtelo de nuevo")
            continue
        valorTotal += precio
        contadorProductos += 1
    except ValueError:
        print("Entrada no válida. Introduce un número.")

print("\n<<<---Resumen de la Compra--->>>")
print(f"Total de productos registrados: {N}")
print(f"VALOR TOTAL A PAGAR: ${valorTotal:,.2f}")