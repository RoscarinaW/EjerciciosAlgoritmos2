import sys

def seleccionar_coctel(cocteles):

    print("\n--- <<< Menú de Cócteles Disponibles >>> ---")
    for codigo, nombre in cocteles.items():
        print(f"[{codigo}] {nombre}")
    print("------------------------------------------")

    while True:
        seleccion = input("Ingresa el número del cóctel que deseas preparar: ")
        if seleccion in cocteles:
            return seleccion
        else:
            print("Opción no válida. Por favor, ingresa el número de la lista.")

def obtener_cantidad_cocteles():
    while True:
        try:
            cantidad = int(input("¿Cuántos cócteles deseas preparar? "))
            if cantidad > 0:
                return cantidad
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def mostrar_receta_calculada(nombre_coctel, receta_base, cantidad):
    """Calcula y muestra la receta con las cantidades ajustadas."""
    print(f"\n==============================================")
    print(f"  ¡Tu Receta para {cantidad} {nombre_coctel}, está Lista!")
    print(f"==============================================")

    print(f"\nCoctel Base: {nombre_coctel} (Receta para 1 persona):")
    for ingrediente, cantidad_base in receta_base.items():
        print(f"- {ingrediente}: {cantidad_base}")

    print(f"\n Ingredientes Totales para {cantidad} cóctel(es):")
    print("<<>><<>>"*5)

    for ingrediente, cantidad_base in receta_base.items():
        try:
            valor_numerico = float(''.join(filter(str.isdigit or str.isspace or (lambda c: c == '.'), cantidad_base)))
            unidad = ''.join(filter(str.isalpha or str.isspace, cantidad_base)).strip()
            
            cantidad_total = valor_numerico * cantidad
            
            if cantidad_total == int(cantidad_total):
                cantidad_formateada = int(cantidad_total)
            else:
                cantidad_formateada = round(cantidad_total, 2)
            
            print(f"- **{ingrediente}:** {cantidad_formateada} {unidad}")
        except ValueError:
            print(f"- **{ingrediente}:** {cantidad_base} (mantener esta cantidad)")

    print("\n¡Salud!\n")
    print("By: Oscarina y Luisa")


COCTELES = {
    '1': 'Mojito',
    '2': 'Margarita',
    '3': 'Gin Tonic',
    '4': 'Old Fashioned'
}

RECETAS = {
    'Mojito': {
        'Ron Blanco': '60 ml',
        'Zumo de Lima': '30 ml',
        'Azúcar': '2 cucharaditas',
        'Hojas de Menta': '10 hojas',
        'Agua con Gas': 'Relleno (top up)',
        'Hielo': 'Al gusto'
    },
    'Margarita': {
        'Tequila': '45 ml',
        'Cointreau (o Triple Sec)': '30 ml',
        'Zumo de Lima': '30 ml',
        'Sal': 'Para el borde del vaso',
        'Hielo': 'Al gusto'
    },
    'Gin Tonic': {
        'Ginebra': '60 ml',
        'Tónica': '120 ml',
        'Rodaja de Lima o Limón': '1 rodaja',
        'Hielo': 'Al gusto'
    },
    'Old Fashioned': {
        'Whisky (Bourbon o Rye)': '60 ml',
        'Terrón de Azúcar': '1 terrón',
        'Angostura Bitters': '3 dashes',
        'Rodaja de Naranja': '1 rodaja',
        'Hielo': '1 cubo grande'
    }
}

def main():
    print("  ¡Bienvenido al Asistente de Recetas de Cócteles!  ")
    
    codigo_seleccionado = seleccionar_coctel(COCTELES)
    nombre_coctel = COCTELES[codigo_seleccionado]
    receta_base = RECETAS[nombre_coctel]

    print(f"\n--- Receta Base de {nombre_coctel} (1 Cóctel) ---")
    for ingrediente, cantidad in receta_base.items():
        print(f"- {ingrediente}: {cantidad}")
    print("-------------------------------------------------")
    
    cantidad_a_preparar = obtener_cantidad_cocteles()

    mostrar_receta_calculada(nombre_coctel, receta_base, cantidad_a_preparar)


if __name__ == "__main__":
    main()