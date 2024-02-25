#Square

""" def square (x): 
    return x*x """

"""main"""
""" num= int(input("Dame un numero para calcular su cuadrado: "))
print(f"El cuadrado es : ", square(num))
 """

#Calculo del Area
""" def area(x, y):
    return x*y """

"""main"""
""" largo=int(input("Dame el largo: "))
ancho=int(input("Dame el ancho: "))
print(f"el resultado es: ", area(largo,ancho), "mts cuadrados")
 """
#Hamburgueseria
""" def comida (eleccion):
    comida= {"pizza":10, "hamburguesa": 15, "pintxo": 2 }
    IVA= 0.13
    comidas= comida[eleccion]
    total= comida*(1+IVA)
    return total
    
#main
orden= input("Que vas a pedir para comer, hamburguesa, pizza o pintxo?: ") """

def comida (eleccion):
    comida1= {"pizza":10, "hamburguesa": 15, "pintxo": 2 }
    IVA= 0.13
    comidas= comida1[eleccion]
    total= comidas*(1+IVA)
    return total
    
"""main"""
eleccion= input("Que vas a pedir para comer, hamburguesa, pizza o pintxo?: ")

print(f"El precio con iva es: ",str(comida(eleccion)))




"""
#Crear una función para mostrar la diferencia entre dos números enteros.
def diff (x,y):
    z= x-y
    return z

x= int(input("Dime un numero: "))
y= int(input("Dime otro numero: "))
print("La diferencia entre los dos numeros es: "+ str(abs(diff(x,y))))

#Crear una función para comprobar si la primera letra de un string es mayúscula. Por ejemplo, “Google” devuelve True 
#pero “google” devuelve False.

def mayus(text:str)->bool: 
    if text[0].isupper():
        return True
    else: 
        return False
    
texto=input("Introduce una palabra y te dire si la primer letra es mayuscula o no: ")
print("La palabra tiene primer letra mayuscula?: " + str(mayus(texto)))"""