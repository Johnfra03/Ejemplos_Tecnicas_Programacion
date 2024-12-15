#Codigo para las formas basicas
class Forma:
    def area(self):
        return 0

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Uso de las clases
formas = [Cuadrado(4), Rectangulo(3, 6)]
for forma in formas:
    print(forma.area())
