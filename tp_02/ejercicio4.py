"""Consigna

Pedir un párrafo de texto al usuario y devolver varias estadísticas y transformaciones.

Requisitos
• Cantidad total de palabras
• Cantidad de vocales (a, e, i, o, u, incluyendo mayúsculas y con acento: áéíóú)
• Palabra más larga del texto
• Palabra más corta del texto
• El texto con TODAS las vocales reemplazadas por *
• El texto con las palabras en orden inverso (la última primero, la primera última)

Ejemplo de ejecución
Ingresá un texto: Aprender Python es muy divertido

Palabras: 5
Vocales: 11
Más larga: divertido
Más corta: es
Sin vocales: Apr*nd*r Pyth*n *s m*y d*v*rt*d*
Orden inverso: divertido muy es Python Aprender

Pistas
• texto.split() divide por espacios y devuelve una lista de palabras
• Para reemplazar vocales: usar replace() varias veces, o un for que recorra el texto y 
arme uno nuevo carácter por carácter
• Para invertir el orden: lista[::-1] (slicing con paso -1) o usar reversed()
• Para juntar de nuevo en string: " ".join(lista_palabras)
"""
texto = input("Ingresá un texto: ")
texto_limpio = texto.lower().strip()
texto_lista = texto_limpio.split()
texto_original_lista = texto.split()


total_palabras = len(texto_lista)


VOCALES = "aeiouáéíóúAEIOUÁÉÍÓÚ"

def cantidad_vocales(texto_a_analizar):
    total_vocales = 0
    for letra in texto_a_analizar:
        if letra in VOCALES:
            total_vocales += 1
    return total_vocales


def más_larga(palabras):
    palabra_mayor = palabras[0]
    for p in palabras:
        if len(p) > len(palabra_mayor):
            palabra_mayor = p
    return palabra_mayor


def más_corta(palabras):
    palabra_menor = palabras[0]
    for p in palabras:
        if len(p) < len(palabra_menor):
            palabra_menor = p
    return palabra_menor


def reemplaza_vocales(palabra):
    sin_vocales = ""
    for letra in palabra:
        if letra in VOCALES:
            sin_vocales += "*"
        else:
            sin_vocales += letra
    return sin_vocales


def invertir_texto(texto):
    invertido = texto[::-1]
    texto_unido = " ".join(invertido)
    return texto_unido    

print()
print(f"Palabras: {total_palabras}")
print(f"Vocales: {cantidad_vocales(texto)}")
print(f"Más larga: {más_larga(texto_original_lista)}")
print(f"Más corta: {más_corta(texto_original_lista)}")
print(f"Sin vocales: {reemplaza_vocales(texto)}")
print(f"Orden inverso: {invertir_texto(texto_original_lista)}")



