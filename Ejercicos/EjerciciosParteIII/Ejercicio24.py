#programa que permita determinar si una letra es o no vocal

print("Ejercicio de Vocal o No Vocal")

def es_vocal_o_no_es(letra):
    letra = letra.lower()
    vocales = "aeiouáéíóú"

    if letra in vocales:
        print("La letra '{}' es una VOCAL.".format(letra))
        return True
    else: 
        print("La Letra '{}' NO es un VOCAL.".format(letra))
        return False

vocal = input("ingrese una letra: ")
es_vocal_o_no_es(vocal)
