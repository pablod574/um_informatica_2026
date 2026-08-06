#ejercicio 2: Se pide al usuario temperatura en °C y en °F. Se realiza la conversión de °C a °F y viceversa.

valor_en_celsius = float(input("Ingrese el valor en Celsius: "))

fahrenheit = (valor_en_celsius * 9 / 5) + 32

print(f"{valor_en_celsius} °C equivalen a {fahrenheit:.2f} °F.")

valor_en_fahrenheit = float(input("Ingrese el valor en Fahrenheit: "))

celsius = (valor_en_fahrenheit - 32) * 5 / 9

print(f"{valor_en_fahrenheit} °F equivalen a {celsius:.2f} °C.")
