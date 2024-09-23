from collections import Counter
from itertools import chain
"""magina que tienes una tienda que vende diferentes tipos de artículos. 
El inventario de la tienda se almacena en una lista bidimensional donde cada fila representa una categoría de productos, 
y cada elemento dentro de esa fila representa un producto.
Cada categoría puede tener productos repetidos, lo que significa que algunos productos se venden más que otros.
Tu tarea es crear una función que cuente cuántas veces aparece cada producto en el inventario,
 y luego muestre los productos más vendidos, es decir, aquellos que se repiten más veces.

Instrucciones:
Usa chain para aplanar el inventario (la lista 2D).
Usa Counter para contar cuántas veces aparece cada producto.
Retorna los 3 productos más vendidos."""

inventory = [
    ['apple', 'orange'],
    ['banana', 'orange']]
# Salida:
# [('apple', 6), ('banana', 5), ('orange', 3)]

def inventario(inventario):
    contadorProductos = Counter(chain(*inventario))
    return "No hay suficientes productos" if len(contadorProductos) < 3 else contadorProductos.most_common(3)

print(inventario(inventory))