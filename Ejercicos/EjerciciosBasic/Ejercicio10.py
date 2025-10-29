#Programa que permita determinar el salario a pagar a un empleado teniendo
#como entradas el salario diario y el número de días trabajados. 
#Tenga en cuenta que al empleado se le debe descontar el 10% por
#concepto de pensión y 15% por concepto de salud

print("Calculadora de Salario")

nombre = input("Ingrese el nombre del trabajador ")
valorporDia = float(input("Ingrese el valor del salario por día "))
dias = int(input("Ingrese la cantidad de dia laborado "))
sunTotal = valorporDia * dias

pension = valorporDia * 0.10
salud = valorporDia * 0.15
Total =  sunTotal - pension - salud

print(f"\nDETALLA DE SALARIO")
print("---"*20)
print(f"--- Calculo de salario para: {nombre}---")
print(f"Valor de pago por día: {valorporDia}")
print(f"Cantidad de días laborados: ")
print(f"Valor SubTotal: {sunTotal}")
print(f"Valor a pagar de pensión {pension}")
print(f"Valor a pagar de salud {salud}")
print("---"*20)
print(f"Total de salario: {Total}")