
class Funciones:

    #constructor
    def __init__(self, num1, num2):
        #declaración de atributos
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def areaTriangulo(self, base, altura = 1):
        return (base * altura) / 2
    
    def sumaNumeros(self, *numeros):
        return sum(numeros)
    
    def mascota(self, **args):
        return 'Mi mascota es un ' + args['tipo'] + ' y se llama ' + args['nombre']

    # def mascota(self, tipo, nombre):
        # return 'Mi mascota es un ' + tipo + ' y se llama ' + nombre



instancia = Funciones(1,2)
# print('Suma:', instancia.suma())
# print('Area de un trinagulo',instancia.areaTriangulo(3,0))
print(instancia.sumaNumeros(1,2,3,4,5,6,7,8,9,10))
# print(instancia.mascota( 'Apolo', 'perro', 'Apolito'))
print(instancia.mascota( nombre = 'Apolo', tipo = 'perro'))