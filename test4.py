#Valores mutables e inmutables
""" 
x= 4.65

x=6.5
y=1.32
print(type(x)) #para saber el tipo de dato
print(id(x)) #ubicacion de donde esta guardado en la memoria
print(id(y)) # "" """

""" z= 6
print(type(z))
print(id(z)) """

""" 
x=["hoLA", 4,5]
print(type(x))
print(id(x))

x[0]= "Agur"
print(id(x))  # Es mutable """

"""Ejercicio 1
inflacion=3.465
print(type(inflacion)) #Muestra el tipo de dato que es float en este caso
print(id(inflacion)) #muestras su ubicacion en la memoria
inflacion=9 #asignas otro valor ala variable inflacion
print(id(inflacion)) #muestras su  unicacion en la memoria, que es en este caso otra, lo que significa que es inmutable"""

""" #Ejercicio 2
a=5
b=4.32
c=10

x=[a,b,c]
suma= 0

for i in x:
    if isinstance (i, int):
        suma += i  #suma=suma+i
print(suma)         """


# Bucle while
""" i=0
while i < 10:
    print("hola" + str(i))
    i+= 1
print("end")     """
   


""" x= input("introducir un valor,   q   para quit")
while x != "q":
    print("hola")
    x= input("Introducir un valor,    q   para quit") """

""" x=0
while x< 10:
    if x== 5:
        print("x is 5")
    print(x)
    x=x+1 """

""" 
x=0
while x< 10:
    x=x+1
    if x== 5:
        print("x is 5")
        continue
    print(x)
    """

""" 
x=0
while x< 10:
    x=x+1
    if x== 5:
        print("x is 5")
        break
    print(x) """


""" x=0
while x< 10:
    x=x+1
    if x== 5:
        print("x is 5")
        continue
    print(x)
else:
    print("else") """
   
""" x=12
while x< 10:
    x=x+1
    if x== 5:
        print("x is 5")
        continue
    print(x)
else:
    print("else")   """ 

x=1
while x< 10:
    x=x+1
    if x== 5:
        print("x is 5")
        continue
    print(x)
else:
    print("else")  