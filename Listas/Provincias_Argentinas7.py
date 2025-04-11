#Crear una lista con nombres de provincias argentinas
provincias_argentinas = ["Buenos Aires", "Cordoba", "Tierra del Fuego", "Santa Fe", "Mendoza", "Tucuman", "Salta"]
# La nueva provincia que queremos agregar
nueva_provincia = "Neuquén"
# La posición donde queremos insertar la nueva provincia (índice 3, ya que la indexación comienza en 0)
posicion = 3
# Utilizar el método insert() para agregar la provincia en la posición deseada
provincias_argentinas.insert(posicion, nueva_provincia)
# Imprimir la lista actualizada
print(provincias_argentinas)