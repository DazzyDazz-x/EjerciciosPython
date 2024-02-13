#Conversacion acerca del clima

clima=input("Que tal esta el clima hoy?: ")
climas= ["bueno", "malo", "regular"]

while clima not in climas:
    s="Pista: bueno, malo o regular"
    print(s)
    clima=input("Que tal esta el clima hoy?: ")    

P2=input("Hace calor o frio?: ")

if  "calor" in P2:
    P3=input("Levas gafas de sol?: ")

elif "frio" in P2:
    P4= input("Llevas chaqueta?: ")   

P5=int(input("Cuantos grados hace?: "))

while P5>-5:
    if P5>=-5 and P5<=10:
        print("Vaya, si que hace frio!")
    if P5>=11 and P5<=25:  
        print("Bueno, ni tan mal, podria ser peor, no llores!") 
    if P5>=26 and P5<=35:   
        print("Clima tropical, suertudo!")
    if P5>35:
        print("Rayos, estas en el infierno o que?!!!")   



