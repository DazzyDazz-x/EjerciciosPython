""" #for i in range(20):
#    print("Hola" + str(i))
 #   print("next")

    
for a in range(100, 0, 5 ):
    print(f"{a}") 

   
x = [1, 2, 3 ]
result = print(type(x))   

x = (1, 2, 3 )
result = print(type(x))    


x = {1, 2, 3 }
result = print(type(x))   

x = range (6)
result = print(type(x))    

for i in range(20):
    print("Hola" + str(i))
    print("next")           

x = frozenset([1, 4, 5])
type(x)                   

x = {4, 5, 6, "hola"}
print(type(x))
print(x)
x.add("agur")
print(x)

y=frozenset({4,5,6, "hola"})
print(y)                         

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.union(b))            

a = set()
a.add(10)
print(a)
a.add("hola")
print(a)                    

developers = {"maria", "pedro"}
empleados = {"maria", "pedro", "jhon", "henry"}
gym = {"jhon", "maria", "henry"}

y = empleados.difference(developers, gym)
print(y)
x = gym.intersection(developers)
print(x)                                    

x= 23444.4567
print (f"${x:.2f}")         

valores = range(100)
for x in valores:
    print(x)            

empresa = "Nazaret Zentroa"
"Zentroa" in empresa                

number ="hola"
try:
    float(number)
except ValueError as e:
    print("hubo un error")
    print(e)                

compra = ["manzana","platanos", "kiwi"]
compra.append("mango")
compra.remove("manzana")
print(compra)

for i in compra:
    if i =="platanos":
        print("fruta es " + i)
    else:
        print("no es platano")    

compra = ["platanos","manzanas", "leche"]
compra.append(["huevos", "patatas"])

print(compra)                       

compra = ["platanos","manzanas", "leche"]
compra.append("galletas")
compra.append("zumo")                       

compra = ["platanos","manzanas", "leche", "galletas", "zumo"]

print(compra[3] , compra[4])                 

compra = ["platanos","manzanas", "leche", "galletas", "zumo"]
compra.remove("zumo")
compra.append("zumo de naranja") 
compra.pop(4)
print(compra)                           """

compra = ["platanos","manzanas", "leche", "galletas", "zumo"]
compra.insert(2, "limones")

print(compra)

print(compra.sort())












