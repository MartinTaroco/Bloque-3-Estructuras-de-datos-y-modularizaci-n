from D6funciones import es_primo, cantidad_primos

numero = int(input("Dame un número natural= "))

resultado = es_primo(numero)

if resultado:
  print(f"{numero} es primo")
else:
  print(f"{numero} no es primo")
  

lista_de_candidatos = []

while True:
  candidato = int(input("Dame un número para la lista, si colocas 0 se corta: "))
  
  if candidato == 0:
    break
  
  lista_de_candidatos.append(candidato)


print(f"Tu lista {lista_de_candidatos} tiene {cantidad_primos(lista_de_candidatos)} primos")