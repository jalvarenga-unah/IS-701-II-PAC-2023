colores = [ 'rojo', 'morado',  'verde', 'azul' , 'morado' ]

# copiar una lista
copiaColores = colores.copy()

# agregar un nuevo valor al final
colores.append( 'amarillo' )

# insertar un nuevo valor en la posicion enviada como parametro
colores.insert( 10, 'naranja' )

# elimina la primera coincidencia del valor enviado como parametro
colores.remove( 'verde' )

# obtener la posicion de un valor
print(colores.index( 'morado' ))


#eliminar el ultimo valor
colores.pop()

# eliminar el valor en la posicion enviada como parametro
colores.pop( 1 )

# eliminar todos los valores
# colores.clear()

# ordenar la lista
colores.sort()

# invertir el orden de la lista
colores.reverse()

# tuplas
coloresTupla = ( 'rojo', 'morado',  'verde', 'azul' , 'morado');

print( len( colores ) )
print('El morado aparece ',colores.count( 'morado' ))
print(colores)
print(copiaColores)

for color in colores:
    print(color)