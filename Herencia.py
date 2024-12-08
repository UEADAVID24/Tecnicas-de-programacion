class Automovil(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, capacidad, tipo_combustible):
        super().__init__(marca, modelo, velocidad_maxima, capacidad)
        self.tipo_combustible = tipo_combustible
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, capacidad, tipo):
        super().__init__(marca, modelo, velocidad_maxima, capacidad)
        self.tipo = tipo
