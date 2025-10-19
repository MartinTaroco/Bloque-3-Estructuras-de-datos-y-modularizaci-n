inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

#Pregunta 1: ¿Cuántos tipos de productos hay en el inventario inicial?

variedad = len(inventario)

print(f"En la verdulera tenemos un total de {variedad} frutas y verduras diferentes ")

#Pregunta 2: ¿Qué producto está en la tercera posición del inventario?

print(f"En la tercera posición del inventario se encuentre la {inventario[2]}")

#Pregunta 3: ¿Cómo actualizarías el inventario después de la venta?

inventario.remove("bananas")

print(f"Inventario actualizado: {inventario}")

#Pregunta 4: ¿Cómo añadirías estos productos al inventario?
inventario.append("frutilla")
inventario.append("apio")
inventario.append("papas")

print(f"Inventario actualizado: {inventario}")

#Pregunta 5: ¿Cómo verificas si las "papas" están ahora en el inventario?

if "papas" in inventario:
  print("Tenemos papas!")
else: 
  print("No tenemos papas!")
  
#Pregunta 6: ¿Cómo decidirías qué producto sacar para hacer espacio para el "dragonfruit"?

#Hay varios factores a tener en cuenta, quizá si partimos de que la lista esta en orden de llegada de la fruta a la verudleria, sería logíco sacar los primeros elementos por un tema de caducidad.
inventario.remove("manzanas")
inventario.remove("zanahorias")
inventario.remove("espinacas")
inventario.append("dragonfruit")

print(f"Inventario actualizado: {inventario}")

#Pregunta 7: ¿Cómo ordenarías el inventario?

inventario.sort()
print(f"Inventario actualizado: {inventario}")

#Pregunta 8: ¿Cómo proporcionarías una copia del inventario al nuevo empleado, asegurándote de que si el empleado hace cambios en su copia, el inventario original no se vea afectado?

duplicado_inventario = inventario.copy()

print(f"El duplicado de inventario es: {duplicado_inventario}")

duplicado_inventario.append("sandias")

print(f"El duplicado de inventario modificado es : {duplicado_inventario}, lo cual no altera el inventario original: {inventario}")