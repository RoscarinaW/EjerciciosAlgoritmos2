#Ejercicio 27 Muestra de menu con las siguentes opciones:
# opcion 1 Pasa o no la materia? 
# opcion 2. Es mayor o menor de edad? 
#Caso 2: Solicitar 3 notas y determinar si el promedio es mayor a 3.0, en ese caso el estudiante pasa.
#Caso 3: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.

notaMinima = 3.0
mayorEdad = 18
print("___Escuela Santa Ana___")
nombre_studiante = input("Ingrese el nombre del estudiante: ")

def pasa_o_no_materia():
    print("OPCIÓN #1: Pasa o no pasa la materia")
    try:
        nota1 = float(input("Ingrese la primere nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        promedio = (nota1 + nota2 + nota3) / 3

        print(f"\nEl estudiante {nombre_studiante} tiene un promedio de {promedio}")

        if promedio >= notaMinima:
            print("Obtiene una nota aprobatoria")
            print("<<Felicidades>>")
        else:
            print("Lo sentimos, no alcanza el promedio aprobatorio")
            print("Buena suerte la proxima")
    except ValueError:
        print("Error!!! Ingrese valores numericos validos para las notas")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")

def edad_mayor_o_menor():
    print("OPCIÓN #2: Es mayor o menor de edad")
    try:
        fecha_nacimiento = int(input("Ingresa el año nacimiento: "))
        fecha_actual = int(input("Ingrese el año actual: "))
        edad = fecha_actual - fecha_nacimiento

        print(f"La eddad del {nombre_studiante} es de {edad}")

        if edad >= mayorEdad:
            print(f"El estudiante {nombre_studiante} es mayor de edad")
        else:
            print(f"El estudiante {nombre_studiante} es menor de edad")
    except ValueError:
        print("Erroor!!! Ingrese valores numericos validos")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")

def menu_ejercicio():
    print("<><><><><>"*2)
    print("Menú de elección")
    print("<><><><><>"*2)
    print(f"1. El estudiante {nombre_studiante} Pasa o no la materia.")
    print(f"2. El estudiante {nombre_studiante} Es mayor de edad")
    print("3. SALIR")
    print("<><><><><>"*2)
    while True:
        opcion = input("Seleccione una opcion (1, 2 o 3 para salir): ")

        casos = {
            '1': pasa_o_no_materia,
            '2':edad_mayor_o_menor
        }

        if opcion == '3':
            print("Gracias por preferirnos, Hasta pronto!!!!!!!")
            break
        accion = casos.get(opcion)

        if accion:
            accion()
        else:
            print("Error!! lq opcion no es correcta")
menu_ejercicio()