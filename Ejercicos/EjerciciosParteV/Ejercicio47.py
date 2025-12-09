#Ejercicio 47 Estaruras mayor de un grupo de N estudiantes.

print("<<<---Mayor estarura del grupo--->>>")

while True:
    try:
        N = int(input("¿Cuántos estudiantes conforman el grupo? (N): "))
        if N >= 1:
            break
        else:
            print("Debe haber al menos un estudiante.")
    except ValueError:
        print("Entrada no válida.")

contador = 0
estatura_mayor = 0.0 

while contador < N:
    try:
        estatura = float(input(f"Introduce la estatura (en cm) del estudiante {contador + 1}: "))
        
        if estatura <= 0:
            print("La estatura debe ser positiva. Inténtelo de nuevo.")
            continue
            
        if estatura > estatura_mayor:
            estatura_mayor = estatura
            
        contador += 1
        
    except ValueError:
        print("Entrada no válida. Introduce un número.")

print("\n--- Resultado ---")
print(f"Total de estudiantes evaluados: {N}")
print(f"La MAYOR estatura registrada fue: {estatura_mayor:.2f} cm")