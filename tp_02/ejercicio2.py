"""Consigna

Escribir un programa que pida una contraseña al usuario y le diga si es SEGURA o no, dando 
feedback específico sobre qué le falta.

Requisitos — la contraseña es segura si cumple TODAS estas condiciones

• Tiene al menos 8 caracteres
• Contiene al menos una letra MAYÚSCULA
• Contiene al menos una letra minúscula
• Contiene al menos un dígito (0-9)
• Contiene al menos un carácter especial (de esta lista: !@#$%&*?)

Ejemplo de ejecución

Ingresá una contraseña: hola123

Contraseña INSEGURA. Le falta:
- Al menos 8 caracteres
- Al menos una letra mayúscula
- Al menos un carácter especial"""

def validar_password(pwd):
    tiene_mínimo_caracteres = len(pwd) >= 8
    caracteres_especiales = "!@#$%&*?"
    
    tiene_mayúscula = False
    tiene_minúscula = False
    tiene_dígito = False
    tiene_especial = False

    for c in pwd:
        if c.isupper():
            tiene_mayúscula = True
        elif c.islower():
            tiene_minúscula = True
        elif c.isdigit():
            tiene_dígito = True
        elif c in caracteres_especiales:
            tiene_especial = True
    problemas = []   
    if not tiene_mínimo_caracteres:
        problemas.append("-Al menos 8 caracteres")
    if not tiene_mayúscula:
        problemas.append("-Al menos una mayúscula")
    if not tiene_minúscula:
        problemas.append("-Al menos una minúscula")
    if not tiene_dígito:
        problemas.append("-Al menos un dígito (0-9)")
    if not tiene_especial:
        problemas.append(f"-Al menos un caracter especial ({caracteres_especiales})")
    if not problemas:
        print("\nContraseña segura")
    else:
        print("\nContraseña INSEGURA. Le falta:")
        print("\n".join(problemas))

contraseña = input("Ingrese una contraseña: ")
validar_password(contraseña)



