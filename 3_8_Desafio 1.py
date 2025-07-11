#Desafío 1:
#Crea una función que tome una lista de números y devuelva la suma y el promedio de esos números.

def suma_promedio(a,b):
     
  suma= a+b
  promedio = suma/2
  
  return suma, promedio

resultado = suma_promedio(2, 6)

print(f"La suma es igual a {resultado[0]} y su promedio igual a {resultado[1]}")

