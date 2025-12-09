#Programa que permita determinar cuanro hombres y mujers hay en un curso de 25 estudiantes.

TotalEstudiantes = 25

hombres = 0 
mujeres = 0 
print(f"Conteo de sexo de los estudiantes en un curso de {TotalEstudiantes}")

for i in range(1, TotalEstudiantes + 1):
    while True:
        sexo = input(f"Intruducce el sexo del estudiante {i} ('M' o 'F'): ").strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print("Entrada no valida, por favor solo introduce 'M' para masculino y '' para femenino")
    if sexo == 'M':
        hombres += 1
    elif sexo == 'F':
        mujeres += 1

print("\n<<RESULTADO>>")
print(f"Total de estudiantes evaluados: {TotalEstudiantes}")
print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")