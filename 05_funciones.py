# las funciones nos permiten cumplir con uno de los principios mas conocidos como DRY (do not repeat yourself)
# parametro vs argumento: los parametros hacen parte de la firma de nuestra funcion mientras que los argumentos son los valores dados a cada parametro.


# definimos parametros de la función
def main(parametro1, parametro2):
    print(parametro1, parametro2)


# definimos argumentos de la función
#main("1", "2")


# ejemplos:
def suma_con_rango(min, max):
    suma = 0
    for num in range(min, max):
        suma += num
    return suma


suma_1 = suma_con_rango(1, 4)
suma_2 = suma_con_rango(1, 2)

#print(f"suma_1: {suma_1}, suma_2: {suma_2}")


# parametros por defecto
def area_rectangulo(altura=2, ancho=2):
    return f"el area del rectangulo en metros cuadrados es: {altura * ancho}"


rect_1 = area_rectangulo(2, 5)
#print(rect_1)
rect_2 = area_rectangulo(5, 3)
#print(rect_2)

# si no le pasamos ningun argumento tomará los valores de los parametros por defecto que en este caso es 2 para ambos argumentos:
rect_3 = area_rectangulo()
#print(rect_3)

# tambien podemos enviarle solo uno de los argumentos:
rect_4 = area_rectangulo(10)

#print(rect_4)


# como funcionan los multiples retornos ? cuando mandamos mas de un valor dentro de un return el resultado obtenido por defecto será una tupla.
def obtener_datos(nombre, edad, direccion):
    return nombre, edad, direccion


r = obtener_datos('daniela', 21, 'calle 123')
# accedemos a r como una tupla:
print(r[0], r[1], r[2])

nombre, edad, direccion = obtener_datos('andres', 51, 'calle 143')
print(nombre, edad, direccion)
