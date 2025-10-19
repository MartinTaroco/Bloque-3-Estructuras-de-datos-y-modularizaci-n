#Desafio 2

import random
import string

def contraseña(l):                    #Longitud de la contrasela es l
     numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]            #Lista cion los digitos
     letras = list(string.ascii_lowercase)               #Lista con letras en minusculas
     letrasM = list(string.ascii_uppercase)               #Lista con letras mayusuclas
      
     pre_password = numeros + letras + letrasM          #Uno las tres listas en una pre-password
     random.shuffle(pre_password)                           # Las desordeno
     password = random.sample(pre_password, l)              #Hago una PRE-LISTA con una selección de L elementos de la pre password
     final_password = "".join(str(e) for e in password)      #Uno todo en un string, convirtiendo a string todos los elementos de la lista ultima
     return final_password
         
   
   
resultado = contraseña (8)     #Contraseña de 10 caracteres

print(resultado)