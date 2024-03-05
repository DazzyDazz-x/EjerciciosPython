#Ejercicio pag 87
#RETO:  Sistema para calcular las nóminas

class empleado():
    def __init__(self, name, salario, languaje):
        self.name= name
        self.salario= salario
        self.languaje= languaje
      

    def Calcular_Salario(self):
        return self.salario*1.1

class posicion():
    def __init__(self, programador, analista, scrum_master):
        self.programador= programador
        self.analista= analista
        self.scrum_master= scrum_master
       
class Sistema_Nominas(empleado, posicion):
    #parametro- una lista de clase Empleado
    def calcular_nominas(self, empleados):
        print('Calculando nominas')
        print('')
        for empleado in empleados:
            print(f'Nomina para: {self.name} - {self.languaje}')
            print(f'- $ : {self.Calcular_Salario}')
            print('')

#Ejecutar el metodo para calcular los salarios

deisy=("deisy", 50000, "python")
maria= ("maria", 25000,"java")
karlos= ("karlos",20000,  "c++")

empleados=[]
empleados.append(deisy)
empleados.append(maria)
empleados.append(karlos)

nominas= Sistema_Nominas()
nominas.calcular_nominas(empleados)       