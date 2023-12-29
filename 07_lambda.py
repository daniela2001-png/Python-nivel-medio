def increment(x):
    return x + 1


result = increment(2)
print(result)

# Usamos la funcion anónima  lambda para hacer lo que ya hace increment()

increment_v2 = lambda x: x + 1
print(increment_v2(2)) # 3

full_name = lambda first_name, last_name: f"full_name -> {first_name} {last_name}."
print(full_name("Juan", "Perez")) # full_name -> Juan Perez.
