#Desafío 3:
#Construye una función que tome dos listas y devuelva True si tienen al menos un elemento en común, de lo contrario, que devuelva False.

def verificador(lista1, lista2):
  positivos = []   #Lista para guardar 1(coincidencia) y 0(no coincidencia)
  for i in lista1:    
    if i in lista2:     #Se verifica si algun elemento de la primera esta en la segunda
      positivos.append(1)   #De estarlo agrega un 1 a la lista de positivos
    else:
     positivos.append(0)   #De no estarlo agrega un 0 a la lista de positivos
  
  if 1 in positivos:  #Para finalizar se verifica si la lista de  positivos tiene algún 1 para devolver o no un True 
    return True
  else:
    return False
     
resultado = verificador([1, 2, 3, 5, 6],[9, 90, 0])

print(resultado)