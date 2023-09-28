inicio =2
fin = 10
rango = range(inicio, fin)

cadena = "Hola mundo"
numeros = [1,2,3,4,5,6,7,8,9,10]

print(cadena[3])

#ciclo FOR
for item in numeros:
    if item % 2 == 0:
        continue

    if item == 5:
        break
    print(item)

# cliclo WHILE
control = 0

while control < 10 :
    print('vlaor de control', control)
    control += 1

#ciclo do while
while True: #ciclo infinito (la expresión siempre es verdadera)
    print('valor de control', control)
    control += 1
    if control > 10:
        break