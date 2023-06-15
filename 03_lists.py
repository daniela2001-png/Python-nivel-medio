numbers = []
for number in range(1, 11):
    numbers.append(number * 2)
print(numbers)

numbers_v2 = [number * 2 for number in range(1, 11)]
print(numbers_v2)

# structure of a comprehension list with one condition:
# [element for element in iterable if condition]
numeros_pares = [number for number in range(0, 21) if number % 2 == 0]
print(numeros_pares)

numeros_pares = [number*2 for number in range(0, 21) if number % 2 == 0]
print(numeros_pares)
# la anterior representación  en forma de un ciclo normal, se veria como sigue:
numbers = []
for number in range(0, 21):
    if number % 2 == 0:
        numbers.append(number * 2)
print(numbers)


