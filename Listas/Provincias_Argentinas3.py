#Crear una lista con nombres de provincias argentinas
provincias_argentinas = ["Buenos Aires", "Cordoba", "Tierra del Fuego", "Santa Fe", "Mendoza", "Tucuman", "Salta"]
# Imprimir los elementos desde el segundo hasta el cuarto (inclusive). Para esto, utilizamos la técnica de "slicing" (rebanado) de listas.
# El slicing se define como [inicio:fin], donde 'inicio' es el índice del primer elemento a incluir (inclusive)
#  y 'fin' es el índice del primer elemento a excluir (exclusive).
# El segundo elemento tiene índice 1.
# El quinto elemento tiene índice 4 (para que el cuarto sea incluido).
print(provincias_argentinas[1:4])