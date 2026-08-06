"""Consigna

Procesar las notas de los alumnos del curso e imprimir un informe detallado.

Datos de entrada

Una lista de listas, donde cada elemento es [nombre, parcial1, parcial2, recuperatorio]. Si el 
alumno no rindió el recuperatorio, ese valor es None. Ejemplo:
alumnos = [
["Ana López", 8, 7, None],
["Pedro Gómez", 4, 6, 7],
["Lucía Pérez", 9, 9, None],
["Juan Díaz", 3, 5, 4],
]

Requisitos del informe

• Para cada alumno: promedio de parciales (usando el recuperatorio si lo tiene en lugar 
del parcial reprobado)
• Indicar estado: PROMOCIÓN (promedio ≥ 8), REGULAR (≥ 6), LIBRE (resto)
• Estadísticas finales: cantidad de cada categoría, promedio del curso, mejor y peor 
alumno
• Imprimir todo formateado en tabla (usar f-strings con ancho fijo, ej. f"{nombre:<20}")"""

alumnos = [
["Ana López", 8, 7, None],
["Pedro Gómez", 4, 6, 7],
["Lucía Pérez", 9, 9, None],
["Juan Díaz", 3, 5, 4],
]

def calcular_promedio_alumno(sublista_alumno):
    nombre = sublista_alumno[0]
    parcial1 = sublista_alumno[1]
    parcial2 = sublista_alumno[2]
    recuperatorio = sublista_alumno[3]

    if recuperatorio is not None:
        if parcial1 < parcial2:
            parcial1 = recuperatorio
        else:
            parcial2 = recuperatorio
    promedio = (parcial1 + parcial2) / 2
    return nombre, promedio


def generar_reporte_curso(lista_alumnos):
    cant_promocion = 0
    cant_regular = 0
    cant_libre =0
    suma_promedios_curso =0
    mejor_alumno = ""
    mejor_promedio = -1
    peor_alumno = ""
    peor_promedio = 11
    print(f"\n{'ALUMNO':<20} | {'PROMEDIO':<10} | {'ESTADO':<15}")

    for alumno in lista_alumnos:
        nombre, promedio = calcular_promedio_alumno(alumno)
        if promedio >=8:
            estado = "PROMOCIÓN"
            cant_promocion += 1
        elif promedio >= 6:
            estado = "REGULAR"
            cant_regular += 1
        else:
            estado = "LIBRE"
            cant_libre += 1
        
        suma_promedios_curso += promedio

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = nombre
        
        if promedio < peor_promedio:
            peor_promedio = promedio
            peor_alumno = nombre

        print(f"{nombre:<20} | {promedio:<10.2f} | {estado:<15}")

    total_alumnos = len(lista_alumnos)
    promedio_general_curso = suma_promedios_curso / total_alumnos if total_alumnos > 0 else 0

    print("\n----ESTADíSTICAS FINALES----\n")
    print(f"Cantidad promocionados: {cant_promocion}")
    print(f"Cantidad regulares: {cant_regular}")
    print(f"Cantidad libres: {cant_libre}")
    print(f"Promedio general curso: {promedio_general_curso:.2f}")
    print(f"Mejor alumno: {mejor_alumno}- Nota: {mejor_promedio:.2f}")
    print(f"Peor alumno: {peor_alumno}- Nota: {peor_promedio:.2f}\n")



generar_reporte_curso(alumnos)


