#Ejercicio 38

notasTotales = 15
notaMinima = 4.0
sumaNotas = 0 

print(f"Promedio de {notasTotales} notas y aprobación")

for i in range(1, notasTotales + 1):
    while True:
        try:
            nota = float(input(f"Introduce la nota {i} (0.0 a 5.0): "))
            if nota >= 0.0 and nota <= 5.0:
                break
            else:
                print("Por favor, introduce una nota válida (generalmente entre 0.0 y 5.0).")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
    sumaNotas += nota
promedio = sumaNotas / notasTotales

print("<<<---Resultado de estudiante de Programación De Software--->>>")
print(f"Suma total de notas: {sumaNotas:.2f}")
print(f"Promedio de notas: {promedio:.2f}")

if promedio >= notaMinima:
    print(f"¡Felicidades! Gana la materia. Su promedio ({promedio:.2f}) es mayor o igual a {notaMinima}.")
else:
    print(f"No gana la materia. Su promedio ({promedio:.2f}) es menor a {notaMinima}.")