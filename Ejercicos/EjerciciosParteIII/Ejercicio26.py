#26. Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú:
# 1. Determinar si es positivo o negativo 
# 2.Determinar si es par o impar
#El programa debe realizar las operaciones que el usuario seleccione del menú

print("____Ejercicio 26____")

def determiner_signo(numero):
    if numero > 0:
        print(f"El numero {numero} es positivo.")
    elif numero < 0:
        print(f"El numero {numero} es negativo.")
    else:
        print(f"El numero {numero} es cero.")


def determinar_par_impar(numero):
    if int(numero) % 2 == 0:
        print(f"El nuemro {int(numero)} es par.")
    else:
        print(f"El nuermo {int(numero)} es impar.")


def menu_numerico():
    print("\n ____Menú numérico____")

    try:
        numero = float(input("Ingrese un numero: "))
        print("Caso 1. Determinar si el numero es positivo o negatico")
        print("Caso 2. Determinar si el numero es ppar o impar")
        opcion = input("Seleccione la opcion (1 or 2): ")
        
    except ValueError:
        print("Error, ingrese un valor numeroco valido.")
        return
   
    
    
    casos = {
        '1': determiner_signo,
        '2': determinar_par_impar
    }

    accion = casos.get(opcion)
    
    if accion:
        accion(numero)
    else:
        print("la opcion no es validad, vuelva a intentallo")
    
menu_numerico()