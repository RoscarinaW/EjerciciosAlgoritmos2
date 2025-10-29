#Programa para determinar si una persona es mayor de edad
print("Calcualdora de Mayoría edad")

fechaNacimiento = int(input("Ingresa fecha de Nacimiento: "))
fechaActual = int(input("Ingresa fecha Actual: "))

edad = fechaActual - fechaNacimiento 

if edad >= 18:
    print(f"Tienes {edad} años. --ERES MAYOR DE EDAD--")
else: 
    print(f"Tienes {edad} años. --ERES MENOR DE EDAD--")
