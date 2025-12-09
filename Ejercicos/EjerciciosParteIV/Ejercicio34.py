#Ejercicio34   ESTATURA PROMEDIO Y CALIFICAR

totalEstudiantes = 18
sumaEstaturas = 0

print(f"<<<---Estatura promedio de {totalEstudiantes} estudiantes--->>>")
for i in range(1,totalEstudiantes + 1):
    while True:
        try:
            estatura = float(input(f"Introduce la estatura en 'cm' del estudiante {i}: "))
            if estatura > 0:
                break
            else:
                print("La estatura debe ser un numero positivo")
        except ValueError:
            print("Entrada no valida, introduce un numero positivo")

    sumaEstaturas += estatura
estaturaPromedio = sumaEstaturas / totalEstudiantes

print("\n <<<RESULTADO>>>")
print(f"Estatura promero del grupo: {estaturaPromedio:.2f} cm")

if estaturaPromedio < 140:
    print("a) “Estudiantes muy bajos”")
elif estaturaPromedio >= 140 and estaturaPromedio <= 170:
    print("b) “Estudiantes de estatura normal”")
else:
    print("c) “Estudiantes muy altos”")