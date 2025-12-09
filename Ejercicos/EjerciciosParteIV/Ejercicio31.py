#Programa que permita determinar cuantos estudiantes son mayores de edad de un grupo de 20-


TOTAL_ESTUDIANTES = 20
EDAD_MAYORIA = 18

mayores_de_edad = 0

print(f"--- Estudianres mayores de edad en un grupo de {TOTAL_ESTUDIANTES} ---")

for i in range(1, TOTAL_ESTUDIANTES + 1):
    while True:
        try:
            edad = int(input(f"Introduce la edad del estudiante {i}: "))
            if edad >= 1 and edad <= 120:
                break
            else:
                print("Por favor, introduce una edad válida (entre 1 y 120).")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
   
    if edad >= EDAD_MAYORIA:
        mayores_de_edad += 1

print("\n--- Resultado ---")
print(f"Total de estudiantes evaluados: {TOTAL_ESTUDIANTES}")
print(f"Cantidad de estudiantes mayores de edad: {mayores_de_edad}")
print(f"Cantidad de estudiantes menores de edad: {TOTAL_ESTUDIANTES - mayores_de_edad}")