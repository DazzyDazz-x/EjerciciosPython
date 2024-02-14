#Funcion factorial
""" x=int(input("Introducir un numero: "))
fact=1

while x>0:
    fact= fact*x
    x=x-1

print(fact)    """ 


### Otra forma
""" x=int(input("Introducir un numero: "))
fact=1
while x>0:
    fact= fact*x
    x=x-1
else:
    print(fact)   """  


#Con la funcional factorial
import math 
x=int(input("Introducir un numero: "))   
print(math.factorial(x))