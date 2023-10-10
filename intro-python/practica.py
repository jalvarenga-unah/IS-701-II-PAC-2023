
class ContarCadena:
    def __init__(self, cadena, tipo = 1):
        self.cadena = cadena
        self.tipo = tipo

    #enumarar cuantas veces aparece una letra en una cadena
    def contarLetras(self):
        letras = {}
        for letra in self.cadena:
            if letra == " ":
                continue

            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1
        return letras
    

    #enumarar cuantas veces aparece una palabra en una cadena
    def contarPalabras(self):
        palabras = {}
        for palabra in self.cadena.split():
            if palabra in palabras:
                palabras[palabra] += 1
            else:
                palabras[palabra] = 1
        return palabras
    
    def contar(self):
        if self.tipo == 1:
            return self.contarLetras()
        else:
            return self.contarPalabras()
        
cadena = "Hola mundo mas texto"
contador = ContarCadena(cadena,1)

print(contador.contar())
