#Crear una lista con nombres de provincias argentinas
provincias_argentinas = ["Buenos Aires", "Cordoba", "Tierra del Fuego", "Santa Fe", "Mendoza", "Tucuman", "Salta"]
# Provincia que ya existe en la lista
provincia_existente = "Córdoba"

# Provincia que no existe en la lista
provincia_nueva = "Chubut"
# Agregar la provincia existente a la lista
# Intentar agregar un elemento que ya existe duplicará el elemento en la lista.
provincias_argentinas.append(provincia_existente)
print(f"Lista después de intentar agregar '{provincia_existente}': {provincias_argentinas}")

# Agregar la provincia nueva a la lista
provincias_argentinas.append(provincia_nueva)
print(f"Lista después de agregar '{provincia_nueva}': {provincias_argentinas}")