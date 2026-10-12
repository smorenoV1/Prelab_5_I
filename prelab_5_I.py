# ==========================================
# Ejercicio 1: Pedido de Impresión
# Asignatura: Programación I
# ==========================================

# Constantes y variables iniciales
paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]
PRECIO_PAGINA = 2

# Variables acumuladoras y contadoras
total_paginas = 0
paquetes_aceptados = 0


def calcular_subtotal(total_paginas, precio_pagina):
    """
    Calcula el subtotal multiplicando el total de páginas acumuladas
    por el precio de cada página.
    """
    return total_paginas * precio_pagina


# Recorrido de los paquetes según los requisitos técnicos
for indice in range(len(paquetes)):
    nombre_paquete = paquetes[indice]
    entrada = input(f"Ingrese la cantidad de páginas para '{nombre_paquete}': ")

    # Conversión y manejo de errores
    try:
        paginas = int(entrada)
    except ValueError:
        print(f"Error: '{entrada}' no es un número entero válido. Se omite este paquete.\n")
        continue

    # Validación de rango (1 a 50 páginas inclusive)
    if paginas < 1 or paginas > 50:
        print(f"Error: La cantidad de páginas debe estar entre 1 y 50. Se omite este paquete.\n")
        continue

    # Si pasa las validaciones, se procesa el paquete
    total_paginas += paginas
    paquetes_aceptados += 1
    print(f"-> Paquete '{nombre_paquete}' aceptado con {paginas} páginas.\n")

# Reporte Final
print("=" * 40)
print("           RESUMEN DEL PEDIDO           ")
print("=" * 40)

if paquetes_aceptados == 0:
    print("No se generó un pedido.")
    subtotal = 0
    descuento = 0
    total = 0
else:
    subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)
    
    # Regla de descuento: mayor a 100 páginas otorga 10% de descuento
    if total_paginas > 100:
        descuento = subtotal * 0.10
    else:
        descuento = 0.0

    total = subtotal - descuento

print(f"Paquetes aceptados : {paquetes_aceptados}")
print(f"Total de páginas   : {total_paginas}")
print(f"Subtotal           : {subtotal}")
print(f"Descuento          : {descuento}")
print(f"Total a pagar      : {total}")
print("=" * 40)