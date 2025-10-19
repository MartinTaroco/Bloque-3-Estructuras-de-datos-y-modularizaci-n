#Desafío 4: El Mono que cuenta manzana

#Imagina que tenemos un mono que intenta contar manzanas. Sin embargo, nuestro mono es un poco distraído y olvida cuántos manzanas ha contado cada vez que empieza a contar de nuevo. Cada vez que termina una secuencia de conteo, se olvida de los manzanas contados antes y vuelve a empezar, sumando todos desde el principio. Implementa una función recursiva que simule cómo el mono cuenta manzanas.

#Reglas:
#El mono puede contar un manzana a la vez.
#Cada vez que el mono termina de contar una pila de manzanas, tiene que volver a contar desde cero, pero sigue acumulando el total.
#Por ejemplo:
#Si el mono tiene 5 manzanas en la pila, contará uno por uno, luego olvida y vuelve a empezar, acumulando la suma.



def contando_pila(cantidad):
    if cantidad == 0:
      return 0                       #Caso base, sino no funciona nada
    if cantidad > 0: 
      return cantidad + contando_pila(cantidad-1)
      
      
resultado = contando_pila(5)

def contando_manzanas(pilas):     #Aca le pasamos una lista con la cantidad de manzanas en cada íla [5 , 3]
  suma = 0
  for i in pilas:
    suma += contando_pila(i)                  #usamos la función creada anteriormente para obtener la suma de cada ila
  return suma

resultado_final = contando_manzanas([5,3])


print(resultado_final)