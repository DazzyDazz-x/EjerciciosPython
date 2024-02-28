class Guitarra:
    def __init__(self,marca, cuerdas) : #definicion de los atributos(marca, cuerdas) atraves del constructor _init_
        self.marca= marca #atributos
        self.cuerdas= cuerdas #atributo
        self._precio= 100 #el guion bajo significa que debe ser privado
       
    def tocar(self): #Metodo
        print(f"Soy {self.marca} y brrn, brnnnn, brrrrnnnn") #para acceder a los atributos se debe poner el self

        
#Main programa- instanciar/ usar la clase
        
nombre= input("Cual es el nombre de la guitarra? ")
guit1= Guitarra(nombre, 6)
print(guit1.marca) #atributo
print(guit1.cuerdas) #atributo
guit1.tocar() #metodo
#print(guit1._precio) # esto es lo que no se debe de hacer

"""bajo= Guitarra("Bajo sencillo", 4)
bajo.cuerdas=5
print(bajo.cuerdas)"""










