items = [{
    "product": "shirt",
    "price": 24.78,
}, {
    "product": "t-shirt",
    "price": 30.78
}, {
    "product": "pants",
    "price": 100
}]

# obtenemos los precios
prices = list(map(lambda item: item.get("price"), items))

print(prices)


# agregamos un elemento a items
def add_taxes(item):
    item = item.copy(
    )  # hacemos una copia del item para que en el llamado de map() no se modifique el arreglo original
    item["taxes"] = item.get("price") * .19
    return item


new_items = list(map(add_taxes, items))
print((items))
print((new_items))
