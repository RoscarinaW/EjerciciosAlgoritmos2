#Programa para determinar cual es mayor entre 2 numeros cualquiera ingresado por el usuario.
print("---PROGRAMA PARA DETERMINAR EL MAYOR NUMERO ---")
A = float(input("Ingrese el primer numero: "))
B = float(input("Ingrese el segundo numero: "))

if A > B:
    print(f"\n El numero {A} es mayor que {B} ")
else:
    print(f"\n El numero {A} es menor que {B}")