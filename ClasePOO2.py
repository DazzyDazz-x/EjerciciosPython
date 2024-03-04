# HERENCIA 
class Madre:
   def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad=edad
   def cocinar(self):
        print("La madre le gusta cocinar")   

class Padre:
    def __init__(self, ojos): 
        self.ojos= ojos

    def cocinar(self):
        print("El padre le gusta cocinar")

class Hijo(Padre, Madre): 
    def __init__(self, nombre, edad, ojos, estudios): 
        Madre.__init__(self, nombre, edad)
        Padre.__init__(self,ojos)
        self.estudios= estudios
   

jon=Hijo("Jon", 32, "azules", "programacion")
jon.cocinar()
print(jon.nombre) 
print(jon.edad)
print(jon.ojos)
print(jon.estudios)
