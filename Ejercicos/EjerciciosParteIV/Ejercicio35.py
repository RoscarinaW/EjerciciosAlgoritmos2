#Ejercicio 35 multiplos de 3 hasta 99

print("<<<---Multiplois de 3 hasta 99--->>>")

Limite = 99
print("Multiplos de 3: ")
multiplos_de_3 = []

for numero in range(3, Limite + 1, 3):
    multiplos_de_3.append(str(numero))

print(",".join(multiplos_de_3))