#Aqui solo se define la funcion
""" def mensaje():
    print("Hola Jose")
    print("Adios")

# Main: aqui ya se ejecuta la funcion
for i in range(5):    
    mensaje()     """
""" 
def mensaje(sNombre):
    print("Hola" + sNombre)
    print("Adios")

# Main: argumento
for i in range(5):    
    mensaje("Mary")   

# o
x= input("cual es tu nombre: ")         
mensaje(x) """


""" 
#EJERCICIO 1


def mensaje(sNombre, sApellido, iEdad):
    print("Hola" + sNombre + sApellido+ str(iEdad))
    print("Adios")

# Main: argumento

x= input("cual es tu nombre?: ")  
y= input("cual es tu apellido?: ")       
z= int(input("Cual es tu edad?: "))
mensaje(x, y, int(z)) """

#EJERCICIO 2
def suma(x, y):
    return x + y

def resta(x, y):   
    return x - y

def mult(x, y):
    return  x * y

def div(x, y):
    return x / y

#Main
operacion= input("Que operacion quieres realizar: suma, resta, mult o div?:  ")
x= int(input("Introduce el primer numero: "))
y= int(input("Introduce el segundo numero: "))

match operacion:
    
    case "suma":
        print(suma(x,y))
   
    case "resta":

        print(resta(x,y))
        
    case "mult":     
        print(mult(x,y))

    case "div":    
         print(div(x,y))

