#Calculadora de propinas

cuenta = int(input("Ingrese el monto de la cuenta: "))
porcentaje_propina = int(input("Ingrese el porcentaje de propina (%): "))
propina = cuenta * (porcentaje_propina / 100)
personas = int(input("Ingrese la cantidad de personas: "))
total = cuenta + propina
total_por_persona = total / personas

print()
print("El resumen de la cuenta es:\n")
print(f"Cuenta: $ {cuenta:.2f}")
print(f"Propina ({porcentaje_propina} %): $ {propina:.2f}")
print(f"Total: $ {total:.2f}")
print(f"Por persona: $ {total_por_persona:.2f}")

