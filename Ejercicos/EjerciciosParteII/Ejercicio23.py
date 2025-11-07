#Programa para determinar si un deportista es aceptado o no en un equipo deportivo.

print("Programa de ingreso al equipo")

nombre = input("Ingrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
fechaNacimiento = int(input("Ingrese el año de nacimiente del estudiante: "))
fechaActual = int(input("Ingrese el año actual: "))

promedio = (nota1 + nota2 + nota3) / 3
edad = fechaActual - fechaNacimiento

if promedio >= 3.0:
    print("El estudiante {}".format(nombre))
    print("Edad del estudiante: {}".format(edad))
    print("Nota #1: {}".format(nota1))
    print("Nota #2: {}".format(nota2))
    print("Nota #3: {}".format(nota3))
    print(f"El estudiante {nombre} obtuvo un promedio: {promedio}")
    print("Obtuvo nota APROBATORIA y entra al equipo")
    print("<<>>"*3)
    print("<<<FELICIDADES>>>")
    print("<<>>"*3)
else:
    print("El estudiante {}".format(nombre))
    print("Edad del estudiante: {}".format(edad))
    print("Nota #1: {}".format(nota1))
    print("Nota #2: {}".format(nota2))
    print("Nota #3: {}".format(nota3))
    print(f"El estudiante {nombre} obtuvo un promedio: {promedio}")
    print("Obtuvo nota REPROBATORIA y NO entra al equipo")
    print("<<>>"*3)
    print("<<<SUERTE PARA LA PROXIMA>>>")
    print("<<>>"*3)