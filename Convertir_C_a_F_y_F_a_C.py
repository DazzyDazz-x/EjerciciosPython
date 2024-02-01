#ESTE PROGRAMA SIRVE PARA LA CONVERSION DE GRADOS CENTIGRADOS A FARENHEIT Y VICEVERSA

#Convertir grados Centigrados a Farenheit
C= int(input("Introduce los grados centigrados: "))
F= (C*1.8) + 32
print(f"Los grados Farenheit son: {F}")

#Convertir grados Farenheit a Centigrados
F= int(input("Introduce los grados Farenheit: "))
C= (F-32)/1.8
print(f"Los grados Centigrados son: {C}")