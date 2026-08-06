#ejercicio 1: Se pide al usuario un valor en km y otro en millas. Se realiza la conversión de km a millas y viceversa

MILLAS_A_KM = 1.60934

valor_en_km = float(input("Ingrese el valor en Km: "))

print(f"{valor_en_km:.2f} km equivalen a {valor_en_km / MILLAS_A_KM:.2f} millas.")

valor_en_millas = float(input("Ingrese el valor en millas: "))

print(f"{valor_en_millas:.2f} millas equivalen a {valor_en_millas * MILLAS_A_KM:.2f} km.")
