#Ejemplos en pizarron
""" paises={"Australia": "Canberra", "España": "Madrid"} #un elemento y su valor despues de dos puntos
print(paises["Australia"]) #get()

paises.update({"España":123})
print(paises)

paises.update({"Mexico":"Cd Mexico"}) #agrega ala lista otro elemento mas
print(paises)

paises.pop("España") # para borrar
print(paises)

for k, v, in paises.items():
    print(k,v)

for v in paises.values():
    print(v)    

for k in paises.keys():
    print(k)     

user1= {"email": "blabla", "nombre": "che"} 
user2= {"email": "blabla2", "nombre": "deisy"} 

users=[user1, user2]

for i in users:
    print(type(i))
    print(i["nombre"])
 """

#Ejemplos del libro
#Ejercicio 1.a:Usar un diccionario para gestionar las características de un coche. 
#Por ejemplo, modelo, color, …Practicar añadir una característica, borrar, conseguir, ….
""" 
coche= {"Modelo": "Mazda", "Color": "Rojo", "Puertas":"4", "Motor": "V6"}
print(coche)
coche.update({"Transmision": "Automatica"}) #añadir caracteristica
print(coche)

coche.pop("Puertas")
print(coche) #borrar caracteristica

print(coche["Modelo"]) #conseguir una caracteristica en especifico
for k, v, in coche.items():
    print(k,v) """


#Ejercicio 1.b: Colocar dos diccionarios de coches en un array (lista), para tener una estructura 
#que pueda guardar varios tipos de coches.
""" coche1= {"Modelo": "Mazda", "Color": "Rojo", "Puertas":"4", "Motor": "V4"}
coche2= {"Modelo": "Challenger", "Color": "Negro", "Puertas":"2", "Motor": "V6"}
Miscoches=[coche1, coche2]

for i in Miscoches:
    print(f"El coche de modelo  {i["Modelo"]} es color: {i["Color"]} ")
 """



#Ejercicio 2: Preguntar a 3 usuarios por su nombre, y la comida que más les gusta. 
#Guardar su nombre y comida en un diccionario.

""" for i in range(3):

    nombre=input("Dime tu nombre: ")
    comida= input("Dime tu comida favorita: ")
    usuario={nombre:comida}
    print(f"Para {nombre} su comida favorita es {comida} ")    
    for k, v in usuario.items():
        print(k, v)
 """

usuario={}

for i in range(3):
    nombre=input("Dime tu nombre: ")
    comida= input("Dime tu comida favorita: ")
    usuario.update({"nombre":"comida"})
    print(f"Para {nombre} su comida favorita es {comida} ")        