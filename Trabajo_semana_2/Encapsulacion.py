#Codigo para control de edad
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def mostrar_edad(self):
        return f"{self.__nombre} tiene {self.__edad} años."

    def modificar_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser positiva.")

# Uso de la clase
persona = Persona("Luis", 18)
print(persona.mostrar_edad())
persona.modificar_edad(25)
print(persona.mostrar_edad())
