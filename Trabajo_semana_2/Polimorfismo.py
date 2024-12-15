#Codigo para saludando con diferentes mensajes
class Persona:
    def saludar(self):
        return "Hola, soy una persona."

class Estudiante(Persona):
    def saludar(self):
        return "Hola, soy un estudiante."

class Profesor(Persona):
    def saludar(self):
        return "Hola, soy un profesor."

# Uso polimórfico
personas = [Persona(), Estudiante(), Profesor()]
for persona in personas:
    print(persona.saludar())
