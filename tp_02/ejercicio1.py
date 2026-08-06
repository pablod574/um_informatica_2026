"""Consigna

Crear un programa que convierta temperaturas entre Celsius, Fahrenheit y Kelvin. Debe usar 
funciones para cada conversión.

Requisitos

• Definir las funciones: celsius_a_fahrenheit(c), fahrenheit_a_celsius(f), 
celsius_a_kelvin(c), kelvin_a_celsius(k)
• Cada función recibe un número y devuelve el resultado convertido (NO usar print 
adentro)
• El programa principal: pedir al usuario una temperatura, la unidad de origen y la unidad 
de destino, y mostrar el resultado
• Si origen y destino son la misma unidad, avisar y no hacer nada

Fórmulas
F = C * 9/5 + 32
C = (F - 32) * 5/9
K = C + 273.15"""


def celsius_a_fahrenheit(c):
    fahrenheit = c * 9/5 + 32
    return fahrenheit

def fahrenheit_a_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius

def celsius_a_kelvin(c):
    kelvin = c + 273.15
    return kelvin

def kelvin_a_celsius(k):
    celsius = k - 273.15
    return celsius

while True:
    try:
        temperatura = float(input("Ingrese una temperatura: "))
        break
    except ValueError:
        print("\nERROR: debe ingresar un número válido.\n")
        print("Intente nuevamente...\n")


def pedir_unidades():
    unidad_origen = input("Ingrese la unidad de origen (c/f/k): ").lower()
    unidad_destino = input("Ingrese la unidad de destino (c/f/k): ").lower()
    return unidad_origen, unidad_destino


while True:
    unidad_origen, unidad_destino = pedir_unidades()

    if unidad_origen not in ["c", "f", "k"] or unidad_destino not in ["c", "f", "k"]:
        print("\nERROR: las unidades de medida deben ser 'c', 'f' o 'k'.\n")
        print("Intente nuevamente...\n")
    elif unidad_origen == unidad_destino:
        print("\nERROR: Las unidades de origen y destino no pueden ser iguales.\n")            
        print("Intente nuevamente...\n")

    else:
        break


def convertir(temperatura, unidad_origen, unidad_destino):
    if unidad_origen == "f":
        temperatura = fahrenheit_a_celsius(temperatura)
    elif unidad_origen == "k":
        temperatura = kelvin_a_celsius(temperatura)

    if unidad_destino == "f":
        return celsius_a_fahrenheit(temperatura)
    elif unidad_destino == "k":
        return celsius_a_kelvin(temperatura)
    else:
        return temperatura
        
resultado = convertir(temperatura, unidad_origen, unidad_destino)

print(f"\n{temperatura:.2f} {unidad_origen.upper()}° equivalen a {resultado:.2f} {unidad_destino.upper()}°\n")
