"""Consigna

Simular el sistema de descuentos de una tienda online. El cliente carga productos a un carrito y
al final se calcula el total con todos los descuentos aplicados.

Requisitos
• El programa pide repetidamente nombre y precio de cada producto hasta que el usuario
escriba 'fin' como nombre
• Guardar los productos en una lista (de listas: cada producto es [nombre, precio])
• Después calcular el TOTAL aplicando estas reglas de descuento:
◦ Si el total es > $50.000 → 15% de descuento
◦ Si el total es > $20.000 → 10% de descuento
◦ Si el total es > $10.000 → 5% de descuento
◦ Si tiene más de 5 productos distintos → $1000 extra de descuento
• Si el cliente es 'CLUB' (preguntar al inicio) → 5% adicional sobre el subtotal con 
descuentos
• Mostrar al final: lista de productos, subtotal, descuentos aplicados (uno por línea), y total
final

Funciones requeridas

• cargar_productos() → devuelve la lista de productos
• calcular_subtotal(productos) → suma los precios
• calcular_descuento(subtotal, cantidad_productos, es_club) → devuelve el monto de 
descuento total
• mostrar_resumen(productos, subtotal, descuento, total) → imprime todo formateado
"""

es_club = input("¿Es cliente 'CLUB'? (s/n) ").lower().strip() == "s"

def cargar_productos():
    lista_productos = []
    while True:
        nombre = input("Ingrese el nombre del producto o 'fin'para finalizar): ")
        if nombre.lower() == "fin":
            break

        precio = float(input("Ingrese el precio: "))
        producto = [nombre, precio]
        lista_productos.append(producto)
    return lista_productos

def calcular_subtotal(productos):
    return sum(prod[1] for prod in productos)

def calcular_descuento(subtotal, cantidad_productos, es_club):
    monto_descuento = 0
    if subtotal > 50000:
        monto_descuento += subtotal * 0.15
    elif subtotal > 20000:
        monto_descuento += subtotal * 0.1
    elif subtotal > 10000:
        monto_descuento += subtotal * 0.05
    
    if cantidad_productos > 5:
        monto_descuento += 1000
    
    if es_club:
        subtotal_con_descuentos = subtotal - monto_descuento
        monto_descuento += subtotal_con_descuentos *0.05

    return monto_descuento

def mostrar_resumen(productos, subtotal, descuento, total):
    print("\nRESUMEN DE COMPRA\n")
    print("Productos en el carrito\n")
    for prod in productos:
        print(f"- {prod[0]}: ${prod[1]:.2f}")
    print(f"\nSubtotal: ${subtotal:.2f}\n")
    print("Descuentos aplicados:")
    hubo_descuento = False
    if subtotal > 50000:
        print(f" * Descuento 15% por superar $50000: -${subtotal * 0.15:.2f}")
        hubo_descuento = True
    elif subtotal > 20000:
        print(f" * Descuento 10% por superar $20000: -${subtotal * 0.10:.2f}")
        hubo_descuento = True
    elif subtotal > 10000:
        print(f" * Descuento 5% por superar $10000: -${subtotal * 0.05:.2f}")
        hubo_descuento = True

    if len(productos) > 5:
        print(" * Descuento extra por más de 5 productos: -$1000.00")
        hubo_descuento = True
    if es_club:
        desc_previo = (subtotal * 0.15 if subtotal > 50000 else 
                       subtotal * 0.10 if subtotal > 20000 else 
                       subtotal * 0.05 if subtotal > 10000 else 0)
        if len(productos) > 5:
            desc_previo += 1000
        monto_club = (subtotal - desc_previo) * 0.05
        print(f" * Descuento 5% adicional Cliente CLUB: -${monto_club:.2f}")
        hubo_descuento = True
        
    if not hubo_descuento:
        print(" Ninguno")
    
    print(f"\nTOTAL FINAL: ${total:.2f}\n")


carrito = cargar_productos()

if carrito:
    subtotal_calculado = calcular_subtotal(carrito)
    cantidad = len(carrito)
    descuento_total = calcular_descuento(subtotal_calculado, cantidad, es_club)
    total_final = subtotal_calculado - descuento_total

    mostrar_resumen(carrito, subtotal_calculado, descuento_total, total_final)
else:
    print("\nNo se cargaron productos al carrito")



