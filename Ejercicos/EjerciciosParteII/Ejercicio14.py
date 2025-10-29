#Programa para distribucion de refrigerio para ni;os de 6to grado a jardin. 
print("___ Programa para distribución de refrigerios determinado por la SECRETARIA DE EDUCACIÓN___")


Grado = int(input("Por favor, ingrese el grado del estudiante (ej: 4,6,7,10): "))
Nombre = input("Ingrese el nombre del estudiante: ")

if Grado <= 6:
    print(f"\nEl estudiante {Nombre} 'SI' requiere refrigerio por disposición de la Secretaria de Educación")
    print("Es de grado {}.".format(Grado))
elif Grado >= 7:
    print(f"\nEl estudiante {Nombre} 'NO' requiere refrigrio. es de grado {Grado}")