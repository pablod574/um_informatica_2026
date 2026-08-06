# Se pide al ususario una cantidad de segundos y se devuelve cuántas horas, minutos y segundos representa.

total_segundos = int(input("Ingrese segundos (entero): "))
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = (total_segundos % 3600) % 60

print(total_segundos, f"segundos equivalen a : \n{horas} horas, {minutos} minutos y {segundos} segundos.")