""" #Imprimir de 1 al 9
i=1
while i < 10:
    print(i)
    i=+ 1
 """

#Imprimir los valores desde 50 hasta 100.
""" i=50
while i <= 100:
    print(i)
    i+= 1 """

#Desde 5, imprimir los valores 5 a 20, pero excluye 12.
""" i= 5
while i<=20:
    if i>=5 and i<12: 
        print(i)
    elif i>12:   
        print(i)
    i+= 1 
 """

#Preguntar al usuario por números hasta que el usuario introduzca “q” para quit.  Sumar los valores y imprimir el resultado final. 

""" Numero= input("Introduce el numero que quieras. Para terminar presiona 'q' :  ")

suma= 0
while Numero != 'q':
    suma = suma + int(Numero)
    Numero= input("Quieres continuar?,  Si: Introduce un numero. No: Introduce  'q' :  ")
print(suma) """


total = 0
while total < 100:
    num = int(input("Enter a number: "))
    total = total + num
print("Tthe total is", total)    