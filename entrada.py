#funtion imput-> retorna string

num_a=int (input("ingresa un numero"))
num_b=int(input("ingresa un numero"))

print(num_a + num_b)

name=input("ingresa tu nombre: ")
age=int(input("Ingresa tu edad: "))
city=input("Ingresa tu ciudad/pueblo: ")

#sting format

"""
Hola, soy nombre, tengo age años y vivo en city

"""
greeting="Hola, soy {}, tengo {} años y vivo en {}"


print(greeting.format(name, age, city))

greeting_2=f"Hola, soy {name}, tengo {age} años y vivo en {city}"

print(greeting_2)