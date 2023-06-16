# las funciones nos permiten cumplir con uno de los principios mas conocidos como DRY (do not repeat yourself)
# parametro vs argumento: los parametros hacen parte de la firma de nuestra funcion mientras que los argumentos son los valores dados a cada parametro.


# definimos parametros de la función
def main(parametro1, parametro2):
    print(parametro1, parametro2)


# definimos argumentos de la función
main("1", "2")


# ejemplos:
def suma_con_rango(min, max):
    suma = 0
    for num in range(min, max):
        suma += num
    return suma


suma_1 = suma_con_rango(1, 4)
suma_2 = suma_con_rango(1, 2)
print(f"suma_1: {suma_1}, suma_2: {suma_2}")
