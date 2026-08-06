"""Consigna
Implementar 4 funciones que generan diferentes patrones visuales en la consola usando bucles
anidados (un for adentro de otro).
Funciones a implementar
1) tabla_multiplicar(n) — Imprime la tabla del n del 1 al 10:
tabla_multiplicar(5)
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
2) tabla_completa(n) — Imprime una tabla NxN con los productos:
tabla_completa(3)
  1   2   3
  2   4   6
  3   6   9
3) triangulo(altura) — Imprime un triángulo de asteriscos:
triangulo(4)
*
**
***
****
4) triangulo_invertido(altura) — Como el anterior pero al revés:
triangulo_invertido(4)
****
***
**
*
Pistas
• Un bucle anidado es un for adentro de otro for. El de afuera maneja las filas, el de 
adentro maneja las columnas
• Para el triángulo: la fila i tiene i asteriscos
• Usar print("*", end="") para imprimir sin salto de línea, y print() solo para terminar la 
línea
"""

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

tabla_multiplicar(3)

def tabla_completa(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i * j:3}", end = "")
        print()

tabla_completa(3)

def triangulo(altura):
    for i in range(1, altura + 1):
        print("*" * i)

triangulo(4)

def triangulo_invertido(altura):
    for i in range(altura):
        print("*" * (altura - i))

triangulo_invertido(4)