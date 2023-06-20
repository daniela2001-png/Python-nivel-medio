"""
Nota: Dentro de una función puede haber variables, las cuales se llaman variables locales. Estas variables locales, se identifican porque están escritas dentro de la definición de la función; y únicamente funcionan mientras que la función sea llamada o utilizada. Si vas a llamar a una variable local por fuera de la función, no servirá.
Y existen variables globales, que son las que están escritas fuera de una función. Estas variables si funcionan al ser llamadas sin la función, porque no están determinadas dentro de la función.
"""
# declaramos nuestra variable global
nombre = "daniela"


def cambiar_nombre():
    # nombre =  nombre + "yeinmy" # UnboundLocalError !!!
    global nombre
    nombre = nombre + "yeinmy"  # manera correcta de cambiar el valor de una variable global (aunque se considera mala practica!)
    return nombre


print(nombre)
nombre = cambiar_nombre()
print(nombre)

# Una variable local tiene un scope compartido no solo con la funcion donde se defina sino tambien dentro de la funciones que existan concatenadas dentro de esa función, por ejemplo:


def funcion_principal():
    edad = 21

    def funcion_secundaria():
        print(edad)

    funcion_secundaria()


funcion_principal()

# docs: https://www.w3schools.com/python/python_scope.asp