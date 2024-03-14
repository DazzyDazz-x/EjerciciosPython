
"""lenguajes= ["Python", "Javascript", "Java", "React", "Swift"]
#crear una lista con lenguajes de longitud de 5 o menos
#esto es list comprehension
lista_nueva=  [l for l in lenguajes if len(l)<=5]
print(lista_nueva)

#otra forma, filter funciona practicamente como map
x= filter(lambda x:len(x)<=5, lenguajes)
print(list(x))
print(lista_nueva)"""

usuarios= [{"nombre":"Jon", "edad": 25}, 
           {"nombre": "isabel", "edad": 60}, 
           {"nombre": "Kary", "edad": 45}]

#crear una lista de diccionarios con usuarios de mas de 40
users= filter(lambda x: x["edad"]>=40, usuarios)
print(list(users))

#entre 1000 y 2000
ventas=[('2021-05-31', 1500), ('2021-04-31', 1200), ('2021-03-31', 800), ('2021-02-28', 8000)]

milydosm=filter(lambda x: x[1]>1000 and x[1]<2000, ventas)
print(list(milydosm))




