class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.capacidad = capacidad

    def atributos(self):
        print(self.marca, self.modelo, ":", sep=" ")
        print("·Velocidad Máxima:", self.velocidad_maxima, "km/h")
        print("·Capacidad:", self.capacidad, "personas")

    def mover(self):
        print(f"El {self.marca} {self.modelo} se está moviendo.")

    def detener(self):
        print(f"El {self.marca} {self.modelo} se ha detenido.")
