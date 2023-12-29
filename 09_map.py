# usaremos map() para aplicar una función a cada elemento de una lista.

numbers = [1, 2, 3, 4]
numbers_v2 = [number * 2 for number in numbers]
print(numbers_v2)

# ahora haremos lo mismo pero usando map()
numbers_v3 = list(map(lambda number: number * 2, numbers))
print(numbers_v3)


naturales = [1, 2, 3, 4, 5]
primos = [2, 3, 5, 7]

mix = list(map(lambda x, y: x+y, naturales, primos))
print(mix) # la salida  será: [3, 5, 8, 11] ya que lo que hace map es tomar cada itema de ambas listas y sumarlos dejando el size del arreglo más pequeño que en este caso es 3 (primos[])
