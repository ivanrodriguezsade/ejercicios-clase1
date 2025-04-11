#Crear una lista con nombres de provincias argentinas
provincias_argentinas = ["Buenos Aires", "Cordoba", "Tierra del Fuego", "Santa Fe", "Mendoza", "Tucuman", "Salta"]
# Elemento que queremos eliminar (por su valor)
provincia_a_eliminar = "Mendoza"
# Utilizar el método remove() para eliminar la primera ocurrencia del elemento
provincias_argentinas.remove(provincia_a_eliminar)
# Imprimir la lista después de la eliminación
print(provincias_argentinas)