#esafío 5: Palíndromo
#crea na función llamada es_palindromo que tome una una cadena y devuelva true si es palindromo o false si no lo es.

def es_palindromo(palabra):
  palabra.lower()
  lista_palabra = []
  
  for i in palabra:
    lista_palabra.append(i)  #Se agrega letra por letra   ["g", "a", "t", "o"]

  inversa = lista_palabra[::-1]  #Se crea una lista inverse a la anterior  ["o", "t", "a", "g"]
  
  if lista_palabra == inversa:   #Si es palindromo va a coincidar la lista con su inverso
    print(True) 
  else:
    print(False)
    

resultado = es_palindromo("gato")

print(resultado)

#Codigo mucho mas limpio
def es_palindromo(palabra):
    return list(palabra) == list(palabra[::-1])

print(es_palindromo("arenera"))  # True