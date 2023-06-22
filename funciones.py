#funciones en python
#def name:funcion(params):
#   Codigo
#   return

#funcion sin parametros y sin retorno
def saludos():
    print("Hola a todos")

saludos()

#funciones con un parametro
def get_age_in_future(age):
    print(f"en tres años tendras {age+3} años")

get_age_in_future(39)

#funciones con dos parametros sin retorno
def suma(numa, numb):
    print(f"{numa}+{numb}={numa+numb}")

suma(12, 35)

#funciones con parametros opcionales
def get_heroes(h1= "Ironman", h2= "Spiderman"):
    print([h1, h2])

get_heroes()
get_heroes("Batman")
get_heroes("Batman", "Superman")
get_heroes(h2="Batman", h1="Superman")

#funciones con retorno
def title(texto):
    return texto.title()

text_changed=title("H0la a TOdos")
print(text_changed)