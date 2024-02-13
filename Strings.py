""" s= "Deisy esta en el curso de Python de la academia Nazaret"

print(s.upper())
print(s.capitalize())
print(s.islower())
print(s.swapcase())
print(s.istitle())
print(s.isprintable())
print(s.find("D"))
 """
#Quitar los espacios, las comas y los numeros y dejar como una frase normal
""" s= "    ,122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  " 
s =s.strip()
listaString= s.split(",")
listaDePalabras=[]
for i in listaString:
    if not i.isnumeric():
        listaDePalabras.append(i)
#print(listaDePalabras)
resultado= " ".join(listaDePalabras)
print(resultado) """

#Usando replace(), cambiar el texto para que sea correcto. Además, usar el nombre 
#original de “Python” en lugar de Píton.

texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
t= texto.replace("Pitón", "Python", )
t1=t.replace("automación", "IA")
t2=t1.replace("Bill Gates en 1960", "Guido Van Rossum en 1989")
t3=t2.replace("difícil", "fácil")
print(t3)