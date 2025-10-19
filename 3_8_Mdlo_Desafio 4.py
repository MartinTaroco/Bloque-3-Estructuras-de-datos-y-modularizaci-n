#Utiliza el módulo collections para analizar un texto y generar estadísticas avanzadas, como las 10 palabras más comunes y su frecuencia. Extiende esto creando un gráfico de barras con matplotlib para visualizar la frecuencia de las palabras.


import collections
import matplotlib.pyplot as plt


def frecuencia_palabras(texto):
  formateado = texto.lower()
  lista_texto = formateado.split()
  frecuencia = collections.Counter(lista_texto)      #Devuelve un diccionario.
  return frecuencia



resultado = frecuencia_palabras("HOLA como estas hola yo estas bien y vos como andas?")

palabras = []
cantidad = []

for clave, valor in resultado.items():                     #El metodo items transforma el dict en un una lista de tuplos (clave,valor)
  palabras.append(clave)
  cantidad.append(valor)
  
plt.bar(palabras,cantidad)
plt.ylabel("Frecuencia")
plt.xlabel("Palabras")
plt.show()