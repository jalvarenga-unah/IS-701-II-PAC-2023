mascota = {
    "nombre": "Apolo",
    "raza": "Terrier",
    "edad": 2
}

copia_mascota = mascota.copy()

# print('Antes de modificar', mascota)

mascota['nombre'] = 'Polar'
mascota['apodo'] = 'Polarcin'

# print('Después de modificar', mascota)
# print('Copia', copia_mascota)
# print(mascota.keys()) # Llaves
# print(mascota['nombre'])
# print(mascota.get('raza'))


# Eliminar elementos
del mascota['edad'] # Elimina el elemento enviado por parámetro
# print(mascota)
mascota.pop('apodo') # Elimina el elemento enviado por parámetro

mascota.popitem() # Elimina el último elemento
mascota.clear() # Elimina todos los elementos
print(mascota)

heroe = dict(nombre='Batman', edad=30, ciudad='Gotham')
print('Antes del cambio', heroe)
heroe.update({'nombre': 'Robin', 'edad': 20, 'ciudad': 'Gotham'})
print('Después del cambio', heroe)