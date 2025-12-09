#Ejercicio 37 Multiples de 5 hasta 100

print("Multiplos de 5 hasata el 100")

limite = 100
print(f"---Multiplos de 5: ---")

multiplo_de_5 = []

for numero in range(5, limite + 1, 5):
    multiplo_de_5.append(str(numero))

print(", ".join(multiplo_de_5))