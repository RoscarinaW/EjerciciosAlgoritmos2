#Calculadora de Edad
print("Calculadora de Edad")
fechaNacimiento = int(input("Ingresa tu fecha de nacimiento: "))
fechaActual = int(input("Ingresa en año actual: "))
edad = fechaActual - fechaNacimiento

print(f"\nTu edad actual es {edad}")