# Creando un diccionario dentro de un diccionario e imprimo
diccionario = {"subdiccionario": {"a": 30, "b": False},
                   "lista1": [10, 20, 30]}
print(diccionario)
# Imprimo solo el objeto almacenado en b
print(diccionario["subdiccionario"]["b"])
# Imprimo solo el objeto almacenado en la posicion 1
print(diccionario["lista1"][1])
# Para explorar el diccionario utilizo la palabra reservada keys()
print(diccionario.keys())
# Para saber los valores que conteniene el diccionario y subdiccionario uso la palabra reservada values()
print(diccionario.values())