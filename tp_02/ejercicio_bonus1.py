"""Consigna
Implementar el juego del ahorcado en versión consola.

Cómo funciona
• Hay una lista de palabras predefinida (al menos 10 palabras)
• El programa elige una palabra (la pueden hardcodear o usar random.choice)
• Se muestra la palabra con guiones bajos en lugar de las letras no adivinadas: "_ _ _ _ 
_"
• El usuario va ingresando letras de a una. Si la letra está, se revela en sus posiciones
• Tiene 6 intentos fallidos. Cada letra incorrecta resta un intento
• Si adivina la palabra antes de gastar los 6 intentos: GANÓ
• Si gasta los 6 sin adivinar: PERDIÓ (mostrar la palabra correcta)

Bonus del bonus
• Dibujar el ahorcado en cada estado (estado 0, estado 1, ... estado 6)
• Mostrar las letras ya intentada"""

import random


palabras = ["almohada", "cochera", "reluciente", "estuche", "cancionero", "estaciones", "coleccionista", "estudiantes", "profesores", "universitario"]

elección_programa = random.choice(palabras)

vidas_máximas = 6


def crear_progreso(palabra):
    progreso = []
    for letra in palabra:
       progreso.append("_")
    return progreso

def dibujar_ahorcado(errores):
    estados = [
        """
           +---+

           |   |
               |
               |
               |
               |
         =========
        """,
        """
           +---+

           |   |
           O   |
               |
               |
               |
         =========
        """,
        """
           +---+

           |   |
           O   |

           |   |
               |
               |
         =========
        """,
        """
           +---+

           |   |
           O   |
          /|   |
               |
               |
         =========
        """,
        """
           +---+

           |   |
           O   |
          /|\  |
               |
               |
         =========
        """,
        """
           +---+

           |   |
           O   |
          /|\  |
          /    |
               |
         =========
        """,
        """
           +---+

           |   |
           O   |
          /|\  |
          / \  |
               |
         =========
        """
    ]
    
    print(estados[errores])


def mostrar_tablero(progreso, intentadas, vidas_restantes, errores):
    dibujar_ahorcado(errores)
    print(f"Palabra: {" ".join(progreso)}")
    print(f"Letras intentadas: {", ".join(intentadas)}")
    print(f"Intentos restantes: {vidas_restantes}")


def jugar_ahorcado():
    palabra_secreta = elección_programa
    progreso = crear_progreso(palabra_secreta)
    intentadas = []
    errores = 0

    print("Bienvenido al juego!!")

    while errores < vidas_máximas and "_" in progreso:
        vidas_restantes = vidas_máximas - errores
        mostrar_tablero(progreso, intentadas, vidas_restantes, errores)
        letra = input("\nIngresa una letra: ").lower()
        
        if letra in intentadas:
            print(f"Ya intentaste la letra '{letra}'. Prueba con otra.")
            continue
        intentadas.append(letra)

        if letra in palabra_secreta:
            print(f"\nLa letra '{letra}' sí está!")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    progreso[i] = letra
        else:
            print(f"\nLa letra '{letra}' no está.")
            errores += 1
    dibujar_ahorcado(errores)
    if "_" not in progreso:
        print(f"Ganaste!! Adivinaste la palabra: {palabra_secreta}.")
    else:
        print(f"Perdiste. Te quedaste sin intentos. La palabra era: {palabra_secreta}")

jugar_ahorcado()
