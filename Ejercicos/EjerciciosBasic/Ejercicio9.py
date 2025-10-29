#Programa para calcular una comprea del mismo producto.
print("Caculadora de costo con IVA 16%")
productoNombre = input("Ingrese el nombre del producto: ")
producto = float(input("Ingrese el valor initario de producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados:  "))

sub_total = producto * cantidad
iva = sub_total * 0.16
total = iva + sub_total

print("\n--Factura--")
print("___DETALLE DE COMPRA___")
print("-" *  30)
print(f"Nombre del producto:{productoNombre}")
print(f"Valor Unitario: {producto}")
print(f"Subtotal: {sub_total:,.2f}")
print(f"Valor de IVA 16% {iva}")
print("-" *  30)
print(f"Total: {total}")