"""Consigna

Crear un mini-sistema para gestionar los libros de una biblioteca. El sistema funciona con un 
menú en bucle, donde el usuario elige opciones hasta salir.

Datos
Cada libro se representa como una lista: [titulo, autor, año, prestado]. Por ejemplo: ["El Aleph", 
"Borges", 1949, False].
Todos los libros se guardan en una lista global llamada biblioteca.

Menú
=== BIBLIOTECA ===
1. Agregar libro
2. Listar todos los libros
3. Buscar libro por título
4. Prestar libro (cambia prestado a True)
5. Devolver libro (cambia prestado a False)
6. Listar solo disponibles
7. Listar solo prestados
8. Estadísticas (cuántos hay, cuántos prestados)
9. Salir

Elegir opción: 

Funciones obligatorias
• mostrar_menu() — imprime el menú
• agregar_libro(biblioteca, titulo, autor, año) — agrega un libro nuevo (prestado=False)
• listar_libros(biblioteca) — imprime todos los libros
• buscar_libro(biblioteca, texto) — devuelve los libros cuyo título CONTIENE el texto 
(ignorar mayúsculas)
• prestar(biblioteca, titulo) — marca el libro como prestado (devuelve True si tuvo éxito, 
False si no se encontró o ya estaba prestado)
• devolver(biblioteca, titulo) — marca como devuelto
• estadisticas(biblioteca) — imprime cantidades

Requisitos extra
• Al arrancar, cargar 5 libros de ejemplo precargados
• El programa debe seguir funcionando hasta que el usuario elija "Salir"
• Validar que las opciones del menú estén entre 1 y 9
• Si el usuario quiere prestar un libro que no existe, mostrar mensaje claro"""

MENU ="""===BIBLIOTECA===
1. Agregar libro
2. Listar todos los libros
3. Buscar libro por título
4. Prestar libro (cambia prestado a True)
5. Devolver libro (cambia prestado a False)
6. Listar solo disponibles
7. Listar solo prestados
8. Estadísticas (cuántos hay, cuántos prestados)
9. Salir"""

biblioteca = [["El Aleph", "Borges", 1949, False], ["Cien años de soledad", "García Márquez", 1967, False], ["1984", "Orwell", 1949, False], ["El principito", "Saint-Exupéry", 1943, False], ["Rayuela", "Cortázar", 1963, False]]



def mostrar_menu():
    print(MENU)



def agregar_libro(biblioteca, titulo, autor, año):
    nuevo_libro = [titulo, autor, año, False]
    biblioteca.append(nuevo_libro)


def listar_libros(biblioteca):
    print("\nListado de libros\n")
    for libro in biblioteca:
        estado = "Prestado" if libro[3] else "Disponible"
        print(f"Título: {libro[0]} | Autor: {libro[1]} | Año: {libro[2]} | Estado: {estado}")


def buscar_libro(biblioteca, texto):
    resultados = []
    texto_buscar = texto.lower()
    for libro in biblioteca:
        titulo_libro = libro[0].lower()
        if texto_buscar in titulo_libro:
            resultados.append(libro)
    return resultados


def prestar(biblioteca, titulo):
    for libro in biblioteca:
        if libro[0].lower() == titulo.lower():
            if libro[3]:
                return False
            else:
                libro[3] = True
                return True
    return False

def devolver(biblioteca, titulo):
    for libro in biblioteca:
        if libro[0].lower() == titulo.lower():
            if libro[3]:
                libro[3] = False
                return True
            else:
                return False
    return False

def estadisticas(biblioteca):
    total_libros = len(biblioteca)
    total_prestados = 0
    for libro in biblioteca:
        if libro[3] == True:
            total_prestados += 1
    print("\n--- ESTADÍSTICAS ---")
    print(f"Cantidad total de libros: {total_libros}")
    print(f"Cantidad de libros prestados: {total_prestados}")
    print(f"Cantidad de libros disponibles: {total_libros - total_prestados}")


while True:
    mostrar_menu()
    opcion = input("\nElegir opción: ")
    
    if opcion == "1":
        print("\n--- AGREGAR NUEVO LIBRO ---")
        tit = input("Ingrese el título: ")
        aut = input("Ingrese el autor: ")
        # Validamos que el año sea un número entero
        try:
            anio = int(input("Ingrese el año de publicación: "))
            agregar_libro(biblioteca, tit, aut, anio)
            print(f"¡El libro '{tit}' se agregó correctamente!")
        except ValueError:
            print("Error: El año debe ser un número entero. No se guardó el libro.")
            
    elif opcion == "2":
        listar_libros(biblioteca)
        
    elif opcion == "3":
        print("\n--- BUSCAR LIBRO ---")
        busqueda = input("Ingresa el título o parte de él a buscar: ")
        libros_encontrados = buscar_libro(biblioteca, busqueda)
        
        if not libros_encontrados:
            print("No se encontraron libros con ese término.")
        else:
            print(f"\nLibros encontrados ({len(libros_encontrados)}):")
            for libro in libros_encontrados:
                estado = "Prestado" if libro[3] else "Disponible"
                print(f"- Título: {libro[0]} | Autor: {libro[1]} | Año: {libro[2]} [{estado}]")
                
    elif opcion == "4":
        print("\n--- PRESTAR LIBRO ---")
        tit_prestar = input("Ingrese el título del libro a prestar: ")
        exito = prestar(biblioteca, tit_prestar)
        
        if exito:
            print(f"¡Éxito! El libro '{tit_prestar}' ha sido prestado.")
        else:
            print("Error: El libro no existe o ya se encuentra prestado.")
            
    elif opcion == "5":
        print("\n--- DEVOLVER LIBRO ---")
        tit_devolver = input("Ingrese el título del libro a devolver: ")
        exito = devolver(biblioteca, tit_devolver)
        
        if exito:
            print(f"¡Éxito! El libro '{tit_devolver}' ha sido devuelto a la biblioteca.")
        else:
            print("Error: El libro no existe o no estaba registrado como prestado.")
            
    elif opcion == "6":
        print("\n--- LIBROS DISPONIBLES ---")
        # Filtramos directamente aquí las sublistas donde prestado (índice 3) es False
        disponibles = [libro for libro in biblioteca if not libro[3]]
        if not disponibles:
            print("No hay libros disponibles en este momento.")
        else:
            for libro in disponibles:
                print(f"- {libro[0]} de {libro[1]} ({libro[2]})")
                
    elif opcion == "7":
        print("\n--- LIBROS PRESTADOS ---")
        # Filtramos directamente aquí las sublistas donde prestado (índice 3) es True
        prestados = [libro for libro in biblioteca if libro[3]]
        if not prestados:
            print("No hay libros prestados actualmente.")
        else:
            for libro in prestados:
                print(f"- {libro[0]} de {libro[1]} ({libro[2]})")
                
    elif opcion == "8":
        estadisticas(biblioteca)
        
    elif opcion == "9":
        print("\nSaliendo del sistema de biblioteca. ¡Hasta luego!")
        break
        
    else:
        print("\n[!] Opción inválida. Por favor, selecciona un número del 1 al 9.")
