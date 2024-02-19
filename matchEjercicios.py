#MATCH (switch)
""" lenguaje= input("Cual es tu lenguaje de programacion favorito (python, java o javascript) ?: ")
match lenguaje:
    case "python":
        print("Ami me gusta python tambien")

    case "java" | "javascript": 
            print("bueno, bastante complicado...")
        
    case _:
        print(f"No tengo conocimiento  de este  {lenguaje}")     """


#Ejercicio de coche
coche= input("Obedece ala siguiente instruccion: encender, correr o apagar: ")
match coche:
    case "encender":
        print("estoy encendido")

    case "correr": 
        print("estoy en marcha")
        
    case "apagar":
        print(f"Estoy apagado")       

    case _:
        print("No te he entendido")    