# Higher order function: una función dentro de otra función (HOF
"""
Normalmente solemos usar parámetros y argumentos como sinónimos, y en la práctica podemos inferir lo que esto significa según el contexto. Pero en un entorno profesional, deberíamos tener muy claro que los parámetro son las reglas o instrucciones que definimos dentro de la función, mientras los argumentos son los datos que le pasamos a la función para que los “reemplace” y ejecute la función.

Algo así como en matemáticas básicas, cuando definimos y = x^2 + x + 3, la derecha de la ecuación serían los parámetros, mientras que los argumentos, serían los valores que le asignamos a la x, bien sea para encontrar las coordenadas de un punto (una iteración), o para trazar la gráfica completa (multiples iteraciones)…

**Parámetros: **Reglas Internas de la Función.
**Argumentos: **Datos Externos que le Pasamos a la Función para que Pueda Hacer sus Cálculos.
"""
def increment(x):
    return x + 1


def high_order_function(x, funcion):
    return x + funcion(x)

# llamado de la HOF:
print(high_order_function(2, increment)) # 5

# uso de HOF con lambdas
increment_v2 = lambda x : x + 1

high_order_function_v2 = lambda x, funcion: x + funcion(x)

print(high_order_function_v2(2, increment_v2)) # 5



