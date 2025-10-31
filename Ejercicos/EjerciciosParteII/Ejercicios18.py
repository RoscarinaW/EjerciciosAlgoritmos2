#Programa para registrar compras
print("---CAJA REGISTRADORA---")
print("--VENTA DE CAMAS--")

nomProducto = input("Agregue el nombre el producto: ")
valorProducto = float(input("Ingrese el valor: "))
cantidad = float(input("Ingrese la cantidad de las unidades: "))

subTotal = valorProducto * cantidad
descuento = subTotal * 0.20
total = subTotal - descuento


if 1000000 <= subTotal:
    print("<<>>"*5)
    print("Factura de Venta")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(nomProducto))
    print("Cantidad: {}".format(cantidad))
    print("Valor unitario: {}".format(valorProducto))
    print(f"sub Total: {subTotal}")
    print("Total a pagar: {}".format(total))

elif 1000000 > subTotal:
    print("<<>>"*5)
    print("Factura de Venta")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(nomProducto))
    print("Cantidad: {}".format(cantidad))
    print("Valor unitario: {}".format(valorProducto))
    print(f"sub Total: {subTotal}")
    print("Total a pagar: {}".format(subTotal))


