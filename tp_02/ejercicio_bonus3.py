"""Consigna

Implementar el cifrado César: cada letra se desplaza N posiciones en el alfabeto. Por ejemplo, 
con desplazamiento 3, A→D, B→E, ..., Z→C.

Requisitos

• Función cifrar(texto, n) que devuelve el texto cifrado desplazado n posiciones
• Función descifrar(texto, n) que descifra (es equivalente a cifrar con -n)
• Solo cifrar letras del alfabeto inglés (a-z, A-Z). Los espacios, números y signos quedan 
igual
• Mantener mayúsculas como mayúsculas y minúsculas como minúsculas
• El desplazamiento debe funcionar para cualquier número (n=27 equivale a n=1 porque 
el alfabeto tiene 26 letras)

Ejemplo

cifrar("Hola Mundo", 3)      →  "Kroñ Pxqgr"  (en realidad, ignorando ñ → "Krod Pxqgr")
cifrar("abc XYZ", 3)         →  "def ABC"
descifrar("def ABC", 3)      →  "abc XYZ" 

Pistas

• Usar ord(letra) para obtener el código numérico ASCII de la letra
• Usar chr(numero) para volver de número a letra
• Para que A=0, B=1, etc.: codigo = ord(letra) - ord('A')
• Para el wrap-around usar módulo: nuevo_codigo = (codigo + n) % 26"""

def cifrar(texto, n):
    texto_cifrado = ""
    
    for letra in texto:
        if letra.isupper():
            codigo_base_0 = ord(letra) - ord('A')
            nuevo_codigo = (codigo_base_0 + n) % 26
            letra_cifrada = chr(nuevo_codigo + ord('A'))
            texto_cifrado += letra_cifrada
            
        elif letra.islower():
            codigo_base_0 = ord(letra) - ord('a')
            nuevo_codigo = (codigo_base_0 + n) % 26
            letra_cifrada = chr(nuevo_codigo + ord('a'))
            texto_cifrado += letra_cifrada
            
        else:
            texto_cifrado += letra
            
    return texto_cifrado

def descifrar(texto, n):
    return cifrar(texto, -n)

print("--- PROBANDO CIFRADO CÉSAR ---")

resultado1 = cifrar("abc XYZ", 3)
print(f"Cifrar 'abc XYZ' con 3: {resultado1}")

resultado2 = descifrar("def ABC", 3)
print(f"Descifrar 'def ABC' con 3: {resultado2}")

resultado3 = cifrar("Hola Mundo", 3)
print(f"Cifrar 'Hola Mundo' con 3: {resultado3}")

resultado4 = cifrar("Hola Mundo", 4)
print(f"Cifrar 'Hola Mundo' con 4: {resultado4}")