""" Consigna
Escribir un programa que pida N notas (de 1 a 10) y genere un análisis completo del curso.
Requisitos
• Pedir al usuario CUÁNTAS notas va a cargar (validar que sea positivo)
• Pedir las N notas, validando que cada una esté entre 1 y 10 (si no, pedir de nuevo)
• Guardar las notas en una lista
• Mostrar el análisis usando funciones:
◦ promedio(notas) — devuelve el promedio
◦ mas_alta(notas) y mas_baja(notas) — SIN usar max() ni min()
◦ contar_aprobados(notas) — devuelve cuántos aprobaron (≥6)
◦ distribucion(notas) — devuelve un texto que cuente cuántas notas hay en cada 
rango: [1-3], [4-5], [6-7], [8-10]

Ejemplo de ejecución
¿Cuántas notas vas a cargar? 5
Nota 1: 8
Nota 2: 6
Nota 3: 4
Nota 4: 10
Nota 5: 7
=== ANÁLISIS ===
Notas: [8, 6, 4, 10, 7]
Promedio: 7.00
Más alta: 10
Más baja: 4
Aprobados: 4 de 5 (80%)
Distribución: 0 reprobados graves, 1 reprobado, 2 regulares, 2 excelentes

Pistas
• Para mas_alta sin max(): inicializar variable mayor = notas[0], después for nota in notas:
if nota > mayor: mayor = nota
• Para distribución usar 4 contadores y un for con if-elif-else"""

while True:
    try:
        cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: "))
        break
    except ValueError:
        print("\nERROR: Debe ingresar un número válido.\n")
        print("Intente de nuevo\n")
notas = []

while cantidad_notas <= 0:
    cantidad_notas = int(input("¿La cantidad debe ser positiva. Ingrese cantidad de notas: "))

for n in range(cantidad_notas):
    while True:
        try:
            nota = int(input(f"Ingrese la nota {n + 1}: "))
            break
        except ValueError:
            print("\nDebe ingresar un número válido\n")
                
    while nota < 1 or nota > 10:
        nota = int(input(f"\nLa nota debe estar entre 1 y 10. Ingrese nuevamente la nota {n + 1}: "))
    notas.append(nota)


def promedio_notas(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def mas_alta(notas):
    mayor = notas[0]
    for n in notas:
        if n > mayor:
            mayor = n
    return mayor

def mas_baja(notas):
    menor = notas[0]
    for n in notas:
        if n < menor:
            menor = n
    return menor

def contar_aprobados(notas):
    aprobados = 0
    for n in notas:
        if n >= 6:
            aprobados += 1
    return aprobados


def distribución_notas(notas):
    reprobados_graves = 0
    reprobados = 0
    regulares = 0
    excelentes = 0

    for n in notas:
        if 1 <= n <= 3:
            reprobados_graves += 1
        elif n < 6:
            reprobados += 1
        elif n < 8:
            regulares += 1
        else:
            excelentes += 1
    texto_resultado = f"{reprobados_graves} reprobados graves, {reprobados} reprobados, {regulares} regulares, {excelentes} excelentes"
    return texto_resultado


def análisis_notas(notas):
    print("\n===ANÁLISIS===")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio_notas(notas):.2f}")
    print(f"Más alta: {mas_alta(notas)}")
    print(f"Más baja: {mas_baja(notas)}")
    total = len(notas)
    aprobados = contar_aprobados(notas)
    porcentaje = (aprobados / total) * 100
    print(f"Aprobados: {aprobados} de {total} ({porcentaje:.0f}%)")
    print(f"Distribución: {distribución_notas(notas)}\n")

análisis_notas(notas)

