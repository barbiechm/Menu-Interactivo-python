# importamos la función selector_de_precios desde datos.py
from datos import selector_de_precios

# Función para calcular el total de un pedido dado una lista de productos
def calcular_total(pedido):
    subtotal = 0.0
    errores = []
    for categoria, productos in pedido.items():
        for producto in productos:
            precio = selector_de_precios(categoria, producto)
            if isinstance(precio, (int, float)):
                subtotal += precio
            else:
                errores.append({'categoria': categoria, 'producto': producto, 'mensaje': precio})
    # IVA 16% y servicio 10%
    IVA = 0.16
    SERVICIO = 0.10
    total = subtotal * (1 + IVA + SERVICIO)
    if errores:
        for e in errores:
            print(f"Producto '{e['producto']}' no encontrado en la categoría '{e['categoria']}': {e['mensaje']}")
    return total