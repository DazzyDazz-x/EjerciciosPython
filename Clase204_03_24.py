#Ejercicio pag 87
#RETO:  Sistema para calcular las nóminas


class Sistema_Nominas:
    #parametro- una lista de clase Empleado
    def calcular_nominas(self, empleados):
        print('Calculando nominas')
        print('###################')
        for empleado in empleados:
            print(f'Nomina para: {empleado.name} - {empleado.lenguaje}')
            print(f'- $ : {empleado.calcular_nomina()}')
            print('')


class empleados():
    def __init__(self, nombre, salario=float, programador=str, analista=str, scrum_master=str):
        self.nombre= nombre
        self.salario= salario
        self.programador= programador
        self.analista= analista
        self.scrum_master= scrum_master

    def Calcular_Salario(self):
        print(f"Tu salario es: ", {self.salario*1.1})






empleados=[]

empleados.append(jon)
empleados.append(maria)
empleados.append(pepe)






#Ejecutar el metodo para calcular los salarios
nominas= Sistema_Nominas()
nominas.calcular_nominas(empleados)
        