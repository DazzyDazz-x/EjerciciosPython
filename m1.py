productos=["raqueta", "balon", "guantes", "pelota"]

#crear una funcion para convertir la primera en mayuscula

"""prodMay=[]

def convertir_may(s):
    return s.capitalize()

#2. aplicarla a todos los elementos de la lista
for p in productos:
    print(convertir_may(p))

newp=[convertir_may(p) for p in productos]
print(newp) """
   

   #otra forma
"""
captext= lambda x:x.capitalize()
print(captext("raqueta"))"""


#ahora con map


"""def convertir_may(s):
    return s.capitalize()

print(list(map(convertir_may, productos))) """

"""def convertir_may(s):
    return s.capitalize()
print(list(map(lambda x:x.capitalize(), productos)))   """

#ejercicio 1: sumar 2 a cada elemento de la lista [4,5,6]= [6,7,8]
listnum=[4,5,6]

print(list(map(lambda x: x+2, listnum)))

# ó,  es lo mismo que arriba
def s2(x):
    return  x+2
print(list(map(s2,listnum)))
    


#ejercicio 2: import math para aprovechar de la funcion math.sqrt
import math 
x= tuple(map(math.sqrt, listnum))
print(x)

#ejercicio 3: teniendo 3 listas de numeros, multiplicar cada numero
x=[4,5,6]
y=[6,3,1]
z=[8,1,2]

lambda a, b, c: a*b*c

print(tuple(map(lambda a, b, c: a*b*c, x,y,z)))