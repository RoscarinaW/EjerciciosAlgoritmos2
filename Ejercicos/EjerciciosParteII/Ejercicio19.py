#programa para compra con descuento de 15% para compras inferiores a $20000 y del 35% para compras mayores o igual a $20000

print("---CAJA REGISTRADORA---")
print("--VENTA DE RESTAURANTE--")

NombreProducto1 = input("Ingrese el Nombre del primer Producto: ")
ValorProducto1 = float(input("Ingrese el Valor del Producto: "))
CantidadUnitarias = int(input("Ingrese la cantidad Unitaria: "))

SubValor = ValorProducto1 * CantidadUnitarias
Descuentoinferior = SubValor * 0.15
TotalDescuentoInfe = SubValor - Descuentoinferior
DescuentoMayor = SubValor * 0.35
TotalDescuentosuper = SubValor - DescuentoMayor


if SubValor < 20000:
    print("<<>>"*5)
    print("Factura de Venta")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(NombreProducto1))
    print("Cantidad: {}".format(ValorProducto1))
    print("Valor unitario: {}".format(CantidadUnitarias))
    print(f"sub Total: {SubValor}")
    print("Descuento del 15%: {}".format(Descuentoinferior))
    print("Total a pagar: {}".format(TotalDescuentoInfe))
    print("____Gracias por su Compra____")

elif SubValor >= 20000:
    print("<<>>"*5)
    print("Factura de Venta")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(NombreProducto1))
    print("Cantidad: {}".format(ValorProducto1))
    print("Valor unitario: {}".format(CantidadUnitarias))
    print(f"sub Total: {SubValor}")
    print("Descuento del 35%: {}".format(DescuentoMayor))
    print("Total a pagar: {}".format(TotalDescuentosuper))
    print("____Gracias por su Compra____")