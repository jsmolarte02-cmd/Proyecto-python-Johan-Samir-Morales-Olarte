def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


inventario = [
    ["A001", "Teclado", 5, 10],
    ["A002", "Mouse", 15, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "Cable HDMI", 20, 15],
    ["A005", "Memoria USB", 2, 12]
]


print("LISTA DE PEDIDOS")
print("----------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo, "| Artículo:", nombre, "| Cantidad a pedir:", cantidad_pedir)