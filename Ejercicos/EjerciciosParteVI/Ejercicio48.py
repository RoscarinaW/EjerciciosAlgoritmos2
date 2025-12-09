#Ejercicio 48, Calculadora 
def calculadora_basica():
    
    num1 = 0
    num2 = 0
    
    print("-<<<-- Ejercicio 48: Menú de Calculadora (Simulación do-while) --->>>")
    
    while True:
        print("\n<<<--- MENÚ DE OPERACIONES --->>>")
        print("1. Ingresar 2 números")
        print("2. Realizar la suma")
        print("3. Realizar la resta")
        print("4. Realizar la multiplicación")
        print("5. Realizar la división")
        print("6. Salir del programa")
        
        try:
            opcion = input("Seleccione una opción (1-6): ")
            opcion_int = int(opcion)
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
            continue

        if opcion_int == 1:
            try:
                num1 = float(input("  > Ingrese el primer número: "))
                num2 = float(input("  > Ingrese el segundo número: "))
                print(f"   Números ingresados: {num1} y {num2}")
            except ValueError:
                print("   Error: Ingrese números válidos.")

        elif opcion_int == 2:
            print(f"  > Suma: {num1} + {num2} = {num1 + num2:.2f}")

        elif opcion_int == 3:
            print(f"  > Resta: {num1} - {num2} = {num1 - num2:.2f}")

        elif opcion_int == 4:
            print(f"  > Multiplicación: {num1} * {num2} = {num1 * num2:.2f}")

        elif opcion_int == 5:
            if num2 != 0:
                print(f"  > División: {num1} / {num2} = {num1 / num2:.2f}")
            else:
                print(" Error: No se puede dividir por cero.")
        
        elif opcion_int == 6:
        
            print("\n¡Hasta pronto! Saliendo del programa...")
            break 
            
        else:
            print("Opción fuera de rango. Seleccione un número del 1 al 6.")

calculadora_basica()