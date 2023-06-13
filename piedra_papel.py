# Eleccion aleatoria Maq
import random

#Fuction randint(min-max)
rand_int=random.randint(1, 3)
if rand_int==1:
    choice_maq='piedra'
elif rand_int==2:
    choice_maq='papel'
else:
    choice_maq='tijeras'

#Eleccion de usuario
choice_text='''
Escribe una de las opciones:
piedra
papel
tijeras
'''
choice_user=input(choice_text)

#Imprecion de Opciones
print("Usuario eligio ->", choice_user)
print("Maquina eligio ->", choice_maq)

#Ganador!
if choice_maq==choice_user:
    print("Empate")
else:
    if choice_maq=='piedra' and choice_user=='papel':
        print("Gana Don chingon")
    elif choice_maq=='piedra' and choice_user=='tijeras':
        print("Gana la PC")
    elif choice_maq=='papel' and choice_user=='tijeras':
        print("Gana Don chingon")
    elif choice_maq=='papel' and choice_user=='piedra':
        print("Gana la PC")
    elif choice_maq=='tijeras' and choice_user=='piedra':
        print("Gana Don chingon")
    else:
        print('Gana la PC')
