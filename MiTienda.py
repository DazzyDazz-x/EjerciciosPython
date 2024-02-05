compra= ["manzanas", "zumos", "leche", "chaqueta", "tacos", "laptop", "ferrari", "diamantes"]
precio=[3, 5,  1.5, 15, 10, 750 ,  10000000 , 100000]
opciones= int(input("Introduce 1: para ver todos los productos, 2:para hacer una compra y 3: para borrar un producto:  "))


if opciones== 1:
    print (compra)

elif opciones== 2: 
    j=0
    for i in compra:
      
       print("Producto: " + i,  ", Precio: " )
       print( precio[j])
       j=j+1
       
    ProdElegido= input("Que producto deseas comprar (escribelo tal como se muestra en la lista)?: ")

    j=0
    for i in compra:
        if ProdElegido == i:
            Billete= float(input("De cuanto es tu billete?: ")) 
            Cambio= Billete-precio[j] 
            print(f"Tu cambio es de: {Cambio} euros")
        j=j+1

  



elif opciones== 3:
    j=0
    print(compra)
    ProdBorrado= input("Que Producto quieres borrar de la lista?: ")
    for i in compra:
         if ProdBorrado== i:
             compra.remove(compra[j])
             print(compra)
         j+=1
         
