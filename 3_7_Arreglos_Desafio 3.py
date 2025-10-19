#Eres un desarrollador creando una herramienta educativa que muestra los caracteres ASCII correspondientes a una lista de números. Se recomienda usar la función chr() para convertir los números en caracteres.


def conversor(lista):
  
  for i in lista:
    print(f"El número { i } tiene como caracter ASCII a {chr(i)} ")
    
    
    
    
conversor([45, 3, 5, 56])