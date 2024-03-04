#Ejercicio pag. 85

#Herencia múltiple

class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad

    def mostrar(self):
        print(self.calle)
        print(self.ciudad)

class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email= email

    def mostrar(self):
        print(self.nombre + ' ' + self.email)

# Agregar funcionalidad para usar la herencia múltiple
class Contacto(Direccion, Persona):
    def __init__(self,calle, ciudad, nombre, email, activo):
        Direccion.__init__(self, calle, ciudad)
        Persona.__init__(self, nombre, email)
        self.activo=activo

    def mostrar(self):
        Direccion.mostrar(self)
        Persona.mostrar(self)
        print(self.activo)


Deisy= Contacto("elosegi", "Lazkao", "deisy", "fagta@ka.com", True)
Deisy.mostrar


#no esta funcionando, revisar, te debe arrojar los datos en la pantalla


