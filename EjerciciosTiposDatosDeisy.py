
#EJERCICIOS DE TIPOS DE DATOS
#Range
""" for _ in range(100):
    print(f"Numero {_} ") """

""" x=45.674
y= int(x)
print(y) """

""" loggedIn = False
print(int(loggedIn)) """

""" #intersection
a= {10, 20, 30, 40}
b= {30, 40, 50, 60}
print(a.intersection(b)) """

""" #difference
a= {10, 20, 30, 40}
b= {30, 40, 50, 60}
print(a.difference(b)) """

""" #simetric difference
a= {10, 20, 30, 40}
b= {30, 40, 50, 60}
print(a.symmetric_difference(b)) """

""" #Set & frozenset
x=input("Que valor quieres en tu set?: ")

s = set()

s.add(x)

#print(s)

y= 5

s.add(y)

print(s)
#5y= frozenset(s) """
 

"""  ####
print(f"{0.1:.18f}") """

""" #redondea el valor
x=23.4567
print(f"{x:.2f}") """

""" valores = range(100)
for x in valores:
    print(x) """

"""s= "Python es genial!"
"Python" in s """

""" s= "Python es mi favorito"
s[3] """

""" 
empresa= "Nazaret Zentroa"
print("Zentroa" in empresa) """
""" 
compra= ["manzanas", "platanos", "kiwis"]
print(compra[2])
print(len(compra))
compra.append("mango") #agrega mango
print(compra)
print(len(compra))
compra.remove("manzanas")
print(compra)
print(len(compra))
compra.append("manzanas")
print(compra)
for i in compra:
    print("Fruta es: " + i)

for i in compra:
    if i == "platanos":
       print("Fruta es: " + i)   
    else: 
       print("No son platanos") 

print("END")

compra.sort()
print(compra) """

compra= ["manzanas", "zumos", "leche", "chaqueta", "tacos", "laptop", "ferrari", "diamantes"]
precio=[3, 5,  1.5, 15, 10, 750 ,  10000000 , 100000]
opciones= int(input("Introduce 1: para ver todos los productos, 2:para hacer una compra y 3: para borrar un producto:  "))


if opciones== 1:
    print (compra)

elif opciones== 2: 
    #print (compra[0] + precio[0], compra[1]+precio[1], compra[2] +precio[2],  compra[3] +precio[3],  compra[4] + precio[4],  compra[5] +precio[5],  compra[6] +precio[6] )  
    j=0
    for i in compra:
      
       print("Producto: " + i,  ", Precio: " )
       print( precio[j])
       j=j+1
       
    ProdElegido= input("Que producto deseas comprar (escribelo tal como se muestra en la lista)?: ")
 
    if ProdElegido in compra:
        Billete= int(input("De cuanto es tu billete?: ")) 
        if compra == compra[i]:
            Cambio= Billete-precio[0] 
           
    print(f"Tu cambio es de: {Cambio} euros") 
 
    #if compra[0]==True:

elif opciones== 3:
    ProdBorrado= int(input("Que Producto quieres borrar de la lista: 1: Manzanas, 2: Zumos o 3: Leche?: "))
    if ProdBorrado== 1:
        compra.remove("manzanas")
        print(compra)
    elif ProdBorrado == 2:
        compra.remove("zumos")    
        print(compra)
    elif ProdBorrado == 3:
        compra.remove("leche")    
        print(compra)    