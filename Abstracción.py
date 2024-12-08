# Clase para un círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio**2

# Clase para un rectángulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Usar las clases y mostrar resultados
circulo = Circulo(5)  # Radio 5
rectangulo = Rectangulo(4, 6)  # Ancho 4, Alto 6

print("Área del círculo:", circulo.calcular_area())
print("Área del rectángulo:", rectangulo.calcular_area())
