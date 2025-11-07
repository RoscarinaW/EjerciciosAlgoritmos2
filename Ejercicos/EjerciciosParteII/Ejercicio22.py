#Ejercicio 22, Programa que permita para un super con descuento a) 10000 y 20000 10%, b) 20001 y 50000 30% y c) compras > 50000 el 50%
print("---CAJA REGISTRADORA---")
print("--VENTA DE SUPER MARKET--")

NombreProducto = input("Ingrese el Nombre del Producto: ")
ValorProducto = float(input("Ingrese el Valor del Producto: "))
CantidadUnitarias = int(input("Ingrese la cantidad Unitaria: "))

SubValor = ValorProducto * CantidadUnitarias
Descuentoinferior = SubValor * 0.11
TotalDescuentoInfe = SubValor - Descuentoinferior
DescuentoMediano = SubValor * 0.30
TotalDescuentoMedi =SubValor - DescuentoMediano
DescuentoMayor = SubValor * 0.50
TotalDescuentosuper = SubValor - DescuentoMayor

if SubValor >= 10000 and SubValor <=20000:
    print("<<>>"*5)
    print("Factura de Venta")
    print("--SUPER MARKET LOS DESCUENTOS--")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(NombreProducto))
    print("Cantidad: {}".format(ValorProducto))
    print("Valor unitario: {}".format(CantidadUnitarias))
    print(f"sub Total: {SubValor}")
    print("Descuento del 10%: {}".format(Descuentoinferior))
    print("Total a pagar: {}".format(TotalDescuentoInfe))
    print("____Gracias por su Compra____")
elif SubValor >= 20001 and SubValor < 50000:
    print("<<>>"*5)
    print("Factura de Venta")
    print("--SUPER MARKET LOS DESCUENTOS--")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(NombreProducto))
    print("Cantidad: {}".format(ValorProducto))
    print("Valor unitario: {}".format(CantidadUnitarias))
    print(f"sub Total: {SubValor}")
    print("Descuento del 30%: {}".format(DescuentoMediano))
    print("Total a pagar: {}".format(TotalDescuentoMedi))
    print("____Gracias por su Compra____")
elif SubValor > 50000:
    print("<<>>"*5)
    print("Factura de Venta")
    print("--SUPER MARKET LOS DESCUENTOS--")
    print("<<>>"*5)
    print("Nombre del producto: {}".format(NombreProducto))
    print("Cantidad: {}".format(ValorProducto))
    print("Valor unitario: {}".format(CantidadUnitarias))
    print(f"sub Total: {SubValor}")
    print("Descuento del 50%: {}".format(DescuentoMayor))
    print("Total a pagar: {}".format(TotalDescuentosuper))
    print("____Gracias por su Compra____")

 
