# Programa de temperaturas
print("Programa de promedio de temperaturas")
print("___"*3)

temperatura1 = float(input("Ingrese la temperatura del Día 1: "))
temperatura2 = float(input("Ingrese la temperatura del Día 2: "))
temperatura3 = float(input("Ingrese la temperatura del Día 3: "))
temperatura4 = float(input("Ingrese la temperatura del Día 4: "))
temperatura5 = float(input("Ingrese la temperatura del Día 5: "))

totalTemperaturas = temperatura1 + temperatura2 + temperatura3 + temperatura4 + temperatura5
resto = totalTemperaturas / 5

if resto > 35: 
    print("La temperatura promedio es de {}".format(resto))
    print("“Que semana tan calurosa”")
elif resto >= 15 and resto <= 35:
    print("La temperatura promedio es de {}".format(resto))
    print("“Que clima tan delicioso”")
elif resto < 15:
    print("La temperatura promedio es de {}".format(resto))
    print("“Que semana tan fría”")