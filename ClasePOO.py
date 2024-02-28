# Ejercicio pagina 80
"""class Bebida:
    def __init__(self, volumen:int, liquido=str, cantidad=float):
        #self.volumen= volumen
        self.liquido= liquido
        self.cantidad= cantidad

    def llenar(self):
        print(f"Estas bebiendo  {self.liquido} de {self.cantidad} ml ")

#Programa
beb=input("Que bebida quieres cafe o te?: ")  
medida= input("De que medida lo quieres 250 o 150 ml? ") 

TuEleccion= Bebida(0, beb, medida)
TuEleccion.llenar() """


#Pedir a 3 usuarios que bebida quiere tomar, guardarlos en una lista, mostrar todas las bebidas y beberlas
class Bebida:
    def __init__(self, flavor):
        self.flavor= flavor
    def beber(self):   
        print(f"Has pedido de beber {self.flavor}") 


#Programa
listBeverages=[]        

"""for i in range(3)
    beverage= input("Que bebida deseas tomar??? :  ")
    listBeverages[beverage]
    with open("listaBebidas.txt", "a") as f:
            descripcion=  "-" + listBeverages + "-"
            f.write( descripcion +"\n") """

for i in range(3):
    tipo= input("Que quieres tomar?: ") 
    bebida= Bebida(tipo)
    listBeverages.append(bebida)
    bebida.beber()
    with open("listaBebidas.txt", "a") as f:
        descripcion=  "-" + tipo + "-"
        f.write( descripcion + "\n")

with open("listaBebidas.txt", "r") as f: 
    #leer todos los datos y mostrarlos
   print(f.readlines())            





#la del maistro 2da parte
"""         t= input("que quieres tomar")
            c=input("cuanto vas a beber ahora(0 a 100)?")
            bebida= Bebida(t, c, 120)
            listBeverages.append(bebida) 
             
              
            for bebida in listBeverages:
                print(bebida.tipo)
                print(bebida.cantidad)   """
