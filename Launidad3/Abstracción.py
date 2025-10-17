from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
bicicleta1 = Bicicleta("Trek", "MTB", "2025", "Azul")
#Otras instancias
auto2 = Auto("Toyota", "Camry", 2020, "Blanco")
moto2 = Moto("Yamaha", "MT", 2025, "Gris")
camion2 = Camion("Volvo", "FM", 2022, "Negro")
bicicleta2 = Bicicleta("Trek", "AXS", "2021", "Morado")

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(bicicleta1)
print(auto2)
print(moto2)
print(camion2)
print(bicicleta2)