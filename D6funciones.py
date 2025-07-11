def es_primo(p):
    if p <= 1:
       #print("No es primo")
       return False     #Verificar que el número dado sea mayor a 1

    for i in range(2, p):  #Obtenemos los números naturales hasta el p dado.
        if p % i == 0:  #Verificamos que el p no sea divisible entre algun natural menor.
           # print("No es primo")
            return False 
    #print("Es primo")
    return True
   

def cantidad_primos(lista):
  cantidad = 0             
  for i in lista:
    if es_primo(i) == True:       #si la función es_primo da True
      cantidad += 1               #Se le suma 1 a la cantidad
  return cantidad
    

