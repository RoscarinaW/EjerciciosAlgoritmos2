#programa para calcular la edad promedio de un grupo de 15 estudiantes

TotalEstudiante = 15
sumaEdades = 0

print(f"Calculadora de promedio de edad para un grupo de {TotalEstudiante} estudiantes")

for i in range(1, TotalEstudiante + 1):
    while True:
        try:
            edad = int(input(f"Introduce la edad del estudiante {i}: "))
            if edad >= 1:
                break
            else:
                print("La edad debe ser un número positivo.")
        except ValueError:
            print("Entrada no valida, introduce un numero entero.")
    sumaEdades += edad

edadPromedio = float(sumaEdades) / TotalEstudiante

print("\n<<<<RESULTADOS>>>>")
print(f"Total de las edades sumadas: {sumaEdades}")
print(f"Edad promerdio del grupo de estudiantes: {edadPromedio:.2f} años")