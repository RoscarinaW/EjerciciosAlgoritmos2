#Programa para determinar el promedio de tres notas de una materia de un estudiante, que imprima, nombre, materia, notas, y si aprobo.

print("---Programa para promediar---")

NomMateria = input("Ingrese el nombre de la materia: ")
NombreEstudiante = input("Ingrese el nombre del estudiante: ")
CodigoEstudiante = int(input("Ingrese el codigo del estudiante: "))

NotaA = float(input("Ingrese la primera nota: "))
NotaB = float(input("Ingrese la segunda nota: "))
NotaC = float(input("Ingrese la tercera nota: "))

promedio = (NotaA + NotaB + NotaC) / 3

if promedio >= 4.0:
    print("La Materia: {}".format(NomMateria))
    print("Codigo del estudiantes: {} ".format(CodigoEstudiante))
    print(f"Notas acumuladas: {NotaA}, {NotaB} y {NotaC}")
    print("El promedio total es {}".format(promedio))
    print(f"\nLa materia {NomMateria} dio un promedio aprobatorio")
    print("----FELICIDADES----")
elif promedio <= 3.9:
    print("La Materia: {}".format(NomMateria))
    print("Codigo del estudiantes: {} ".format(CodigoEstudiante))
    print(f"Notas acumuladas: {NotaA}, {NotaB} y {NotaC}")
    print("El promedio total es {}".format(promedio))
    print(f"\nLa materia {NomMateria} dio un promedio No aprobatorio")
    print("----Buena suerte----")