#Square

def square (x): 
    return x*x

"""main"""
num= int(input("Dame un numero para calcular su cuadrado: "))
print(f"El cuadrado es : ", square(num))


#Calculo del Area
def area(x, y):
    return x*y

"""main"""
largo=int(input("Dame el largo: "))
ancho=int(input("Dame el ancho: "))
print(f"el resultado es: ", area(largo,ancho), "mts cuadrados")

#Hamburgueseria
def comida (eleccion):
    comida= {"pizza":10, "hamburguer": 15, "pintxo": 2 }
    IVA= 0.13
    comidas= comida[eleccion]
    total= comida*(1+IVA)
    return total
    
"""main"""
comida()