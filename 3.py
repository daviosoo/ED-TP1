import math

class FiguraGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.__radio = radio

    def obtener_radio(self):
        return self.__radio

    def establecer_radio(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return math.pi * self.__radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def obtener_base(self):
        return self.__base

    def establecer_base(self, base):
        self.__base = base

    def obtener_altura(self):
        return self.__altura

    def establecer_altura(self, altura):
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)

# Instanciación de un círculo y un rectángulo
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

# Calcular área y perímetro de las figuras
print("Círculo:")
print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())
print()

print("Rectángulo:")
print("Área:", rectangulo.calcular_area())
print("Perímetro:", rectangulo.calcular_perimetro())
