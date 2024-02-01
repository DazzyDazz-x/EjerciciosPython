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