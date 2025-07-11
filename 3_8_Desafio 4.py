#Desafío 4: Algoritmo MCD
#El Máximo Común Divisor (MCD) es un concepto matemático que ha sido estudiado desde tiempos antiguos. Atribuido a Euclides, el algoritmo para determinarlo es elegante y eficiente. Tu tarea es implementar una función que calcule el MCD de dos números utilizando el algoritmo de Euclides.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
  
resultado = mcd(15,9)

print(resultado)