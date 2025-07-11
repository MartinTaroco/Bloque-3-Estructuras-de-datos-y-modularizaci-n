#Desafío 2:
#Diseña una función que tome una cadena y devuelva la misma cadena, pero con el primer carácter de cada palabra en mayúsculas.


def formateo(texto):   #Toma la cadena de texto
  lista_palabras = texto.split()      #coloca cada palabra en una lista (teniendo en cuenta el espacio como separación)
  lista_palabras_formateadas = []      #Lista para colocar cada palabra con mayuscula al inicio para despues unir.
  for palabra in lista_palabras:       #Accedemos a cada palabra original
    palabra_formateada = palabra.capitalize()    #usamos el metodo capitalize para dejar la primera letra mayuscula
    lista_palabras_formateadas.append(palabra_formateada)    #Se agrega cada palabra a la lista de palabras formateadsas
    
  texto_formateado = " ".join(lista_palabras_formateadas)  #Se las une dejando un espacio en el medio.
  return (texto_formateado)


resultado = formateo ("Hola mundo como estas?")

print(resultado)