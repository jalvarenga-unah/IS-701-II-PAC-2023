


class Heroe:

    # nombre = "Flash"
    # poder = "Super velocidad"


    def __init__(self, nombre = '', poder = ''):
        self.nombre = nombre
        self.poder = poder

    def getInfo(self):
        return f"Soy {self.nombre} y mi poder es {self.poder}"
    


heroe1 = Heroe( poder= "Dinero", nombre= "Batman") 

def realizarSuma( a, b, self = ''):
    return a + b

print(realizarSuma(b = 1, a = 2))
# print(heroe1.getInfo())