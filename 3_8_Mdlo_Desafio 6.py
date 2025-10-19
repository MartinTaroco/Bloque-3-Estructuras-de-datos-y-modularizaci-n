#Calculadora de Fechas Objetivo: Escribir un programa en Python que permita calcular la diferencia entre dos fechas, utilizando el módulo datetime.



from datetime import date

# Fecha 1
fecha1 = date(2025, 9, 28)      #Transforme los datos a una fecha
print(fecha1)
# Fecha 2
fecha2 = date(2024, 9, 28)      #Transforme los datos a una fecha
print(fecha2)
# Diferencia
diferencia = fecha2 - fecha1              #Python sabe que esta restando dos fechas.
print(diferencia)           
print(diferencia.days)   #Obtenemos solo los dias 