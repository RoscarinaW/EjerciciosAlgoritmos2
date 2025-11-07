#Programa que me permite realizar calculos para calcular distancia o tiempo o velocidad
print("Calculadora de__Distancia__Velocidad___Tiempo___")
def calculadora_distancia():
    try:
        v = float(input("Ingrese la velocidad: "))
        t = float(input("Ingrese el tiempo: "))
        x = v * t
        print(f"La distancia recorrida es de {x:.2f}.")
    except ValueError:
        print("Error, ingrese valores númericos válidos.")
def calculadora_tiempo():
    try:
        x = float(input("Ingrese la distancia: "))
        v = float(input("Ingrese la velocidad: "))
        if v==0:
            print("Error, la velocidad no puede ser cero para calcular el tiempo")
            return
        t = x / v
        print(f"El tiempo transcurrido es {t:.2f}.")
    except ValueError:
        print("Error, ingrese valores númericos válidos.")
def calculadora_velocidad():
    try: 
        t = float(input("Ingrese el tiempo: "))
        x = float(input("Ingrese la distancia: "))
        if t == 0:
            print(f"La tiempo no puede ser cero para calcular la velocidad")
            return
        v = x/t
        print(f"La velocidad recorrida es: {v:2f}")
    except ValueError:
        print("rror, ingrese valores númericos válidos.")
def programa_usuario():
    print("\n Calculadora ")
    print(" 1. Calcular distacia. ")
    print(" 2. Calulcar tiempo. ")
    print(" 3. Calular velocidas. ")

    opcion = input("Selecciona una opción (1, 2 o 3): ")

    casos = {
        '1': calculadora_distancia,
        '2': calculadora_tiempo,
        '3': calculadora_velocidad
    }

    accion = casos.get(opcion, lambda: print("Opcioón no es válidad, ingrese 1, 2 o 3"))

    accion()
programa_usuario ()