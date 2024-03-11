#Lista de Compra

""" frutas= ["MANZANA", "pera", "NARANJA", "uva", "MELON"]

nuevas_frutas=[]

for fruta in frutas:
    if fruta.isupper():
        nuevas_frutas.append(fruta)

print(nuevas_frutas)     """    

#Esto es igual que lo de arriba
frutas= ["MANZANA", "pera", "NARANJA", "uva", "MELON"]
nuevas_frutas= [fruta for fruta in frutas if fruta.isupper()]
print(nuevas_frutas)

#Ejercicios Pagina 36 
numeros = [3, 54, -12, 4, -67, 99, -120]
lista_positivas=[num for num in numeros if num >= 0 ]
print(lista_positiva)

#no probado
​​numbers = [2, 6, 7, 3, 4, 8]
todos=["Par" if i%2==0 else "Impar" for i in numeros]
print("todos")