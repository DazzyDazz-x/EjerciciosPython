#if_name_=="_main_": Con esto tienes tu main de la funcion en otro lado

#Ejemplo de tipos de dato para devolver dentro de una funcion
""" def calcular_longitud(nombre:str)->int: #devuelve o int o list o str o list[int]
    print("mi funcion"+nombre)
    return 1 #"hola", [12,65,658]
 """

#Ejemplo con comentarios dentro de una funcion
#def calcular_longitud(nombre:str)->int: #devuelve o int o list o str o list[int]
""" Descripcion:Esta funcion es para ...
parametros: nombre:str de un usuariop
devolver: int  """

    #print("mi funcion"+nombre)
    #return 1 #"hola", [12,65,658] 

#Crear una función para comprobar la edad de un usuario antes de que entre en una web para adultos. 
#Si es menor a 18, devolver False.

""" def block(edad:int)->bool:
    if edad<18:
        return False
    else:
        return True
    
#Main
Enter=int(input("Cual es tu edad?: ")) 
print("La entrada a la pagina web es: "+ str(block(Enter)))  

#Crear una función para convertir kilómetros a millas.
def conv(km:float)->float:
    millas= km * 0.62137
    return millas
  
#Main
kilom=float(input("Dime los km: "))
print("Son:"+ str(conv(kilom))+ "millas")

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
print("La palabra tiene primer letra mayuscula?: " + str(mayus(texto)))


#Crear una función para saber si un número es par o impar. Usar el % módulo operando, que devuelve lo que sobra de 
#una división.(pregunta d entrevista)

def tiponum (x:int)->bool:
    if x % 2== 0:
        return True
        
    else:
        return False

num=int(input("Introduce un numero: "))
if tiponum(num)== True:
    print("es par")
else:
    print("es impar")    
 

#Con una lista, encuentra el número máximo y mínimo. (no funciona, terminarlo!!)
    
def maxNum(*args):
    return  max(*args)
def minNum(*args):
    return min(*args)

num= input("Introduce una lista(separado por comas): ")
print("el num maximo es: " + str(maxNum(num)) + " el num minimo es: "+ str(minNum(num))) 

#La del maestro
def minmax(lista):
    return min(lista), max(lista)

x, y= minmax(lista)
print(x,y)

#otra, no terminada
defminmax(*args):
    return min(args), max(args)

x, y    



 """


#En una línea de texto, encuentra la palabra más larga. Por ejemplo, “Me gustan los garbanzos” devuelve “garbanzos”.(no terminada, es la mia)
def texto(palMayor)->str:
    list= texto.split(",")
    for i in list:
        tamaño=len(i)
        palMayor=max(tamaño)
        return palMayor
   

#la del profe
texto="me gustan los garbanzos"  
def encontrarPalabra(texto):  
    palabras=texto.split()
    max_len= 0
    max_palabra= ""

    for palabra in palabras:
        if len(palabra)>max_len:
            max_len= len(palabra)
            max_palabra=palabra

    return max_len, max_palabra       

print(encontrarPalabra("texto"))             



