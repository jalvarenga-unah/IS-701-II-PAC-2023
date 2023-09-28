# entrada = input('Ingrese un valor')

#print(entrada)
import random as rand

palabras = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

rand. shuffle(palabras) # Mezcla los elementos de la lista alterando el orden en la lista original
# index = rand.randint(0, len(palabras) - 1) 
# palabra_random = palabras[index]
palabra_random = rand.choice(palabras)
intentos = 3

while intentos > 0:
    buscar = input('ingrese una palabra: ')
    if buscar == palabra_random:
        print('Felicidades crack!! adivinaste, la palabra era: ', palabra_random)
        break
    else:
        intentos -= 1
        print('Lo siento, te quedan ', intentos, ' intentos')
