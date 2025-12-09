#Ejercicio 44 Notas, promedio, Mayor y aprobacion.

print("--- Análisis de Calificaciones ---")

NOTA_APROBACION = 40.0

while True:
    try:
        N = int(input("¿Cuántas calificaciones va a ingresar? (N): "))
        if N >= 1:
            break
        else:
            print("Debe ingresar al menos una calificación.")
    except ValueError:
        print("Entrada no válida.")

contador = 0
suma_notas = 0
nota_mayor = 0.0 

while contador < N:
    try:
        nota = float(input(f"Introduce la calificación {contador + 1} de {N} (0 a 100): "))
        
        if nota < 0 or nota > 100:
            print("Calificación fuera del rango (0-100). Inténtelo de nuevo.")
            continue 
        
        suma_notas += nota
        
        if nota > nota_mayor:
            nota_mayor = nota
            
        contador += 1
        
    except ValueError:
        print("Entrada no válida. Introduce un número.")

nota_promedio = suma_notas / N

print("\n--- Resultados y Decisión ---")
print(f"a) Nota promedio: {nota_promedio:.2f}")
print(f"b) Nota mayor: {nota_mayor:.2f}")

print("c) Estado de la Materia:")
if nota_promedio >= NOTA_APROBACION:
    print(f"  El estudiante APRUEBA la materia (Promedio >= {NOTA_APROBACION:.2f})")
else:
    print(f"  El estudiante NO APRUENA la materia (Promedio < {NOTA_APROBACION:.2f})")