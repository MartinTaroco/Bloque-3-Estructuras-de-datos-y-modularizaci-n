#Crea una función recursiva que invierta las palabras en una oración sin utilizar funciones incorporadas de Python para invertir cadenas o listas.


lista_vacia=[]  #Lista donde voy a invertir el texto  (afuera porque sino se reinicia cada vez que la función se llama a si misma)
def inversor(texto):
 
  lista_texto = texto.split()       #Separo el texto que me da en partes
  
  if len(lista_texto) > 0:                 #Verifico si el texto que me da existe, sino PARO LA RECURSION
    ultimo = lista_texto.pop()             #Elimino y obtengo la ultima palabra
    
    lista_vacia.append(ultimo)             #La agrego al inicio de la lista inversa
    
    nuevo_texto =" ".join(lista_texto)     #Agarro lo que sobro del texto original (sin la ultima palabra ahora)
  
    inversor(nuevo_texto)                    #Lo mando a la función otra vez, para que le saque la ultima palabra y lo agregue a la lista inversa
  

    return " ".join(lista_vacia)                 #Al final me devuelve la unión de la lista vacio (el texto al reves)


resultado = inversor ("hola como estas")


print(resultado)