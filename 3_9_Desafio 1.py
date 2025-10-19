#Crea una función recursiva que calcule el máximo común divisor (MCD) de dos números. El MCD de dos números es el número más grande que puede dividir ambos números sin dejar un residuo. Por ejemplo, el MCD de 8 y 12 es 4.


def MCD(a,b):
  print(a, b)
  if a % b > 0:
    resto = a % b
    return MCD(b, resto)
  else:
    return b



resultado = MCD(156,120)


print(resultado)