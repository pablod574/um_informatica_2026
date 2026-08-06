#ejercicio 3: Pidiendo al usuario la base y altura de un rectángulo, se devuelve el área y perímetro del mismo.

base = float(input("Ingrese el valor de la base del rectángulo (metros): "))
altura = float(input("Ingrese el valor de la altura del rectángulo (metros): "))

area = base * altura
perimetro = 2 * (base + altura)

print()
print(f"Base del rectángulo: {base:.2f} mts.")
print(f"Altura del rectángulo: {altura:.2f} mts.\n")
print(f"El Área es: {area:.2f} m2.")
print(f"El Perímetro es: {perimetro:.2f} m2.")
