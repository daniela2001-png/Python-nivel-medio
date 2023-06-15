# dictionary comprehension structure:
# {key:value for var in iterable}

dict = {}
for i in range(1, 11):
    dict[i] = i * 2

dict_comp = {i: i * 2 for i in range(1, 11)}

import random
# creamos un diccionario a partir de una lista
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 5)

population_v2 = {country: random.randint(1, 50) for country in countries}

names = ['dani', 'andy', 'valen']
ages = [21, 27, 16]

users = {name: age for (name, age) in list(zip(names, ages))}

# estructura para un dict comprehensive con condicional:
# {key: value for var in iterable if condition}
filter_dic = {
    key: value
    for key, value in population_v2.items() if value >= 20
}

text = 'Hola, Soy Daniela!'
vowels = {
    vowel: vowel.upper()
    for vowel in text.replace(" ", "").replace(",", "").replace("!", "")
    if vowel in 'aeiou'
}
print(vowels)

# contamos la moda de cada vocal sobre un texto dado:
counter = {key: text.count(key) for key in text if key in 'aeiou'}
print(counter)
