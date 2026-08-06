#Pidiendo al usuario las coordenadas x e y de dos puntos, se devuelve la distancia entre los mismos.

coordenada_x1 = int(input("Ingrese el x de la coordenada 1: "))
coordenada_y1 = int(input("Ingrese el y de la coordenada 1: "))

coordenada_x2 = int(input("Ingrese el x de la coordenada 2: "))
coordenada_y2 = int(input("Ingrese el y de la coordenada 2: "))

distancia = int(((coordenada_x2 - coordenada_x1) **2 + (coordenada_y2 - coordenada_y1) ** 2) ** 0.5)

print()
print(f"Punto 1\n x1: {coordenada_x1}\n y1: {coordenada_y1}\n")
print(f"Punto 2\n x2: {coordenada_x2}\n y2: {coordenada_y2}\n")
print(f"La distancia entre ({coordenada_x1}, {coordenada_y1}) y ({coordenada_x2}, {coordenada_y2}) = ", distancia)

