#Programa para determinar si un deportista es aceptado o no en un equipo deportivo.
print("Programa de ingreso al equipo")

nombre = input("Ingrese el nombre del estudiante: ")
fechaNacimiento = int(input("Ingrese el año de nacimiente del estudiante: "))
fechaActual = int(input("Ingrese el año actual: "))
estarura = float(input("Ingrese la estarura actual del estudiante: "))
peso = float(input("Ingrese el peso actual del estudiante: "))

edad = fechaActual - fechaNacimiento

if edad <= 18 and estarura <= 1.80 and peso <= 80:
    print("El estudiante {}".format(nombre))
    print("Edad del estudiante: {}".format(edad))
    print("La estatura actual del estudiantes es: {}".format(estarura))
    print("El peso actual del estudiante es: {}".format(peso))
    print("Obtuvo todas las condiciones APROBATORIA y entra al equipo")
    print("<<>>"*3)
    print("<<<FELICIDADES>>>")
    print("<<>>"*3)
else:
    print("El estudiante {}".format(nombre))
    print("Edad del estudiante: {}".format(edad))
    print("La estatura actual del estudiantes es: {}".format(estarura))
    print("El peso actual del estudiante es: {}".format(peso))
    print("No cumple con todas las condiciones, el estudiante NO ENTRA AL EQUIPO")
    print("<<>>"*3)
    print("<<<Buena sueter>>>")
    print("<<>>"*3)