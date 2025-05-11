# Creo un diccionario de telefonos
fonos = {"Ivan": 2901333333,
         "Silvina": 2901444444,
         "Leo": 2901222222}
print(fonos)
# Saco un contacto y agrego otro, se agrega al final
fonos["Kande"]= 2901555555
del(fonos["Silvina"])
print(fonos)
# Aca modifico el numero de telefono de 1 contacto. 
fonos["Kande"]= 2901666666
print(fonos)
