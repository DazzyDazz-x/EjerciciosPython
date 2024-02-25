#EJERCICIOS PAGINA 56

"""En una estructura de diccionarios de empresas, mantienes información sobre los números de empleados. Por ejemplo, Apple tiene 25,000 empleados, Google tiene 19,500, …
 Crear una función que devuelva el número de empleados según quiera el usuario. 
 Extender este mismo ejemplo para usuarios y contraseñas. Si la contraseña es correcta, devolver True;"""

""" def empleados(empresa):
    dicc={"Apple":25000, "Google": 19500, "CAF":10000}
    numempleados=dicc[empresa]
    return numempleados

entrada=input("Nombra una empresa: ")
print(f"Su numero de empleados es: ", empleados(entrada))

#Ejemplos Fallidos!!
def passok(passw)->bool:
    dicc1={"us1":"passw1", "us2":"passw2"}
    lista=[dicc1]

    passuser=dicc1[passw]
    if passuser != :
        pass
        return True
    else:
        return False

entrada=input("Cual es el usuario: ")
entrada2=input("Cual es la contraseña: ")
print(f"Su contraseña es: ", passok(entrada2))


for v in dicc1.values():
    print(v)

 """

"""u1="us1"
u2="us2"
p1="pass1"
p2="pass2"

ent1=input("Introduce tu usuario: ")
ent2=input("Introduce tu passw: ")

if ent1== u1:
    if ent2== p1:
        print("Tu passw es:", True)
    else:
         print("Tu passw es:", False)   
if ent1== u2:         
    if ent2== p2:
        print("Tu passw es:" ,True)
    else:
         print("Tu passw es:", False) """ 


"""u1="us1"
u2="us2"
p1="pass1"
p2="pass2" 
    if ent1== u1:
        if ent2== p1:
            return   True
        else:
            return False  
    if ent1== u2:         
        if ent2== p2:
            return   True 
        else:
            return False
           
            
ent1=input("Introduce tu usuario: ")
ent2=input("Introduce tu passw: ")

print(f"Tu passw es:", dicc(ent1, ent2))
              """

def dicc(ent1, ent2)->bool:

    dicc1={"us1":"passw1", "us2":"passw2"}
    passuser=dicc1[ent1]
    if ent2==passuser:
        return True
    else:
        return False


ent1=input("Introduce tu usuario: ")
ent2=input("Introduce tu passw: ")

print(f"Tu passw es:", dicc(ent1, ent2))

