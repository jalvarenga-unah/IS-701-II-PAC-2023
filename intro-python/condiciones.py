
# operadores de comparacion
# ==, !=, <, >, <=, >=

#operadores logicos
# and, or, not
 
edad = 18

# print('Esto es antes de la condición')

# if edad > 18:
#     print("Es mayor de edad")
#     print("Esto es dentro de la condición")
#     if edad < 21:
#         print("Si es mayor de 18, pero menor que 21")
#     else:
#         print("cumple con las restricciones de edad")
# else:
#     print("Es menor de edad")
#     print("Esto es dentro de la condición del else")


# print('Esto es despues de la condición y fuera de ella')


# a un valor entre 1 - 12
mes = 2

#listas
mesesCon31 = [1, 3, 5, 7, 8, 10, 12]
anioBisiesto = True

if mes >= 1 and mes <= 12:

    if mes in mesesCon31:
        print("El mes tiene 31 días")
    else:
        if mes == 2:
            if anioBisiesto:
                print("El mes tiene 29 días")
            else:
                print("El mes tiene 28 días")
        else:
            print("El mes tiene 30 días")

else:
    print("el mes no es válido");