#Desafío 1:
#Investiga y utiliza al menos tres funciones del módulo string que puedan ser útiles para mejorar nuestro procesador de texto.


import string
import random

texto = "esto es una frase"
resultado = string.capwords(texto)    #Cambia cada palabra para que inicie en mayuscuka

print (resultado)



resultado_2 = string.ascii_lowercase   #Obtener todas las letras del abecedario
resultado_3 = string.digits   #Obtener los digitos del 0 al 9
resultado_4 = string.punctuation  #Obtener todos los signos de puntuación

#Lo anterior es util para generar contraseñas. Por ejemplo

letras = []
digitos = []
puntuacion = []
for i in resultado_2:
  letras.append(i)
  
for i in resultado_3:
  digitos.append(i)
  
for i in resultado_4:
  puntuacion.append(i)
  
print(letras)
print(digitos)
print(puntuacion)

lista_unica = letras + digitos + puntuacion  #Concatenamos las listas

random.shuffle(lista_unica)   #La desordenamos
print(lista_unica)

pre_pasword = lista_unica[0:8]   #Slixing para tomar una porcion de la lista de 8 caracteres
print(pre_pasword)

pasword="".join(pre_pasword)   #Unimos con un join.
print(pasword)