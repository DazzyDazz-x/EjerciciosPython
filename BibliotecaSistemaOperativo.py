#para que independientemente del sistema operativo que trabajes, funcione python practicamente igual
import os
"""print(os.getcwd) #te dice donde estas en un directorio
print(os.listdir())

os.chdir("..") #subo en el directorio
print(os.getcwd())   """
""" os.chdir("Python")#cambia al directorio Python
print(os.getcwd())
print(os.listdir()) """

""" 
os.mkdir("dir1") #Crear un nuevo directorio
with open("file1.txt", "w") as f:  #para escribir, si quieres agregar algo mas usa 'a' en lugar del append
    f.write("hola") """

#print(os.getcwd)
#os.chdir("..")

#os.rmdir("dir1") #para borrar directorio
#os.mkdir("dir1") #Crear un nuevo directorio


""" print(os.getcwd)
d1="dir1"
d2="dir2"
d3="dir3"
f="abc.txt"

s=os.path.join(d1,d2,d3,f) #concatena todo en una linea separados por barra invertida
print(s)
#os.mkdir(s) """



""" 
#print(os.getcwd)
os.chdir("..")
print(os.getcwd())

 """
#os.mkdir("dir1")
#os.chdir("dir1")
#print(os.getcwd()) #imprime el directorio en donde nos encontramos


#EJERCICIO EN CLASE: PREGUNTAR NOMBRE DE DIRECTORIO Y CREARLO, PONERME EN EL, Y CREAR DOS ARCHIVOS DE TEXTO Y LISTARLOS
dirX=input("Que nombre de directorio quieres crear?: ")
if os.path.exists(dirX):
    print("El archivo ya existe, debes cambiar de nombre")
else:
    os.mkdir(dirX)

os.chdir(dirX)
print(os.getcwd())
with open("a.txt", "w") as f:
    f.write("hola")
with open("b.txt", "w") as f:
    f.write("hola") 
#esto un poco mas avanzado que lo demas
""" t_archivos= ("a_txt, "b.txt")
    for file in t_archivos:
        with open(file, "w") as f:
            f.write("")"""           

print(os.listdir())

for f in os.listdir():
    print(os.path.splitext(f)) #muestra el nombre y la extension del archivo, se podria hacer x,y=os.path.splitext(f) para que te de el key y la clave
    print(f)
