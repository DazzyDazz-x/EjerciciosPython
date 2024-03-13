productos=["raqueta", "balon", "guantes", "pelota"]

#crear una funcion para convertir la primera en mayuscula

prodMay=[]

def convertir_may(s):
    return s.capitalize()

#2. aplicarla a todos los elementos de la lista
for p in productos:
    print(convertir_may(p))
   