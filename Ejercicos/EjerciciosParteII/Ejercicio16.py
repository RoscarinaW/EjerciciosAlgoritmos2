#Operaciones: si los numero son iguales restarlos y si los numero son diferentes sumarlos.

print("<<>>"*3)
print("Programa para operaciones (A = B: REsta y A=/ B Sumar)")
print("<<>>"*3)

A = float(input("Ingrese el primer numero: "))
B = float(input("Ingrese el segundo numero: "))

Suma = A + B
Resta = A - B

if A == B:
    print(f"\nEl primer numero {A} es igual a {B}")
    print("Entonces los numero se restan: {}".format(Resta))
elif A != B:
    print(f"\nEl primer numero {A} es diferente a {B}")
    print("Entonces los numero se suman: {}".format(Suma))