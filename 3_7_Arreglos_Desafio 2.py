#Como encargado de la biblioteca, necesitas organizar los libros de acuerdo con sus códigos de identificación en orden decreciente, sin modificar la lista original. Se recomienda usar la función sorted(). ¿Por qué es importante no modificar la lista original? ¿Por qué no puedo usar el método sort sobre la lista original?

codigo_libros = [1234, 4356, 23254, 22121, 55454, 32, 54435, 23242]


ordenado = sorted(codigo_libros, reverse=True)

print(codigo_libros)                    
print(ordenado)
print(codigo_libros)

#Sorted crea una copia de la lista y esta copia es ordenada, sort se aplica a la lista (codigo_libros.sort()) y enseguida la modifica. Modicar una lista puede no ser bueno por si se quiere usar la lista original por algún motivo.