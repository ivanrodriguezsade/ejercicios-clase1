#Crear una lista con nombres de provincias argentinas
provincias_argentinas = ["Buenos Aires", "Cordoba", "Tierra del Fuego", "Santa Fe", "Mendoza", "Tucuman", "Salta"]
# Otra lista de provincias que queremos agregar
otras_provincias = ["Chaco", "Formosa", "Corrientes"]
# Utilizar el método extend() para agregar los elementos de la segunda lista a la primera
provincias_argentinas.extend(otras_provincias)
# Imprimir la lista extendida
print(provincias_argentinas)