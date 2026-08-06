# Se pide la edad al usuario en años. Se devuelve la cantidad de días, 
# horas y minutos que vivió, considerando un año como 365 días.
# Extra: se muestran lo segundos vividos y el total de latidos del corazón (aprox 70 por minuto)

edad = int(input("¿Cuántos años tenés? "))

dias = edad * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
latidos = minutos * 70

print()
print(f"En {edad} años aproximadamente viviste:\n")
print(f"Días: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")
print(f"Latidos: {latidos}")
