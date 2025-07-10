#Desafio 4 - Batalla Naval
import numpy as np


# Crear una matriz de ceros
B = np.zeros((5, 5))
print("\nB =\n", B)


fila =int( np.random.randint(0, 5) )  #número aleatorio entero
columna =int( np.random.randint(0, 5) )  #número aleatorio entero

print (fila, columna)
B[fila,columna] = 1            #Se asigna a una posición aleatoria un 1

#Se repite el proceso dos veces
fila =int( np.random.randint(0, 5) )
columna =int( np.random.randint(0, 5) )
print (fila, columna)
B[fila,columna] = 1

fila =int( np.random.randint(0, 5) )
columna =int( np.random.randint(0, 5) )


print (fila, columna)
B[fila,columna] = 1

#Anterirormente se genero una matriz de 5x5 compuesto de 0, y a tres posiciones aleatorias se les asigno un 1.
print("\nB =\n", B)


def jugar(x,y):       #Se crea la función para jugar, condicional que verifica si las coordenadas pasadas por el jugador corresponden o no a un 1.
  
  if B[x,y] == 1:
    print("Hundiste un barco!")
  else:
    print("Le erraste")
    

intentos = 5    #número de intentos del jugador.

while intentos > 0:                    
  f = int(input("Dime una fila: "))
  c = int(input("Dime una columna: ") )
  jugar(f,c)          #Se juega con las coordendas que el jugador paso anteriormente
  intentos -= 1
  
