# Se pide el peso y la altura. Se devuelve el índice de masa corporal (IMC).

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

categoria = (
    (imc < 18.5) * "Bajo peso" +
    ((imc >= 18.5) and (imc < 25)) * "Peso normal" +
    ((imc >= 25) and (imc < 30)) * "Sobrepeso" +
    (imc >= 30) * "Obesidad"
)

print()
print(f"IMC: {imc:.2f}")
print(f"Categoría: {categoria}")