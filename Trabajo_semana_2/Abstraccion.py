from abc import ABC, abstractmethod
#Codigo para operaciones basicas
class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a, b):
        pass

class Suma(Operacion):
    def ejecutar(self, a, b):
        return a + b

class Resta(Operacion):
    def ejecutar(self, a, b):
        return a - b

# Uso de las clases
operaciones = [Suma(), Resta()]
for operacion in operaciones:
    print(operacion.ejecutar(10, 3))
