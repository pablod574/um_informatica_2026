# Se pide al usuario el radio de un círculo. Se devuelve al área y perímetro del círculo.

radio = float(input("Ingrese el radio del círculo (metros): "))

pi = 3.14159

area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print()
print(f"Para un círculo de radio {radio:.2f} mts.:\n")
print(f"Área: {area:.2f} m2.")
print(f"Perímetro: {perimetro:.2f} mts.")

