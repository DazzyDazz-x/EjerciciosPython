import sqlite3

print("Programa DB de Pelis")

conn= sqlite3.connect('pelis.db')


while True:
    accion= int(input("Que quieres hacer:  1. Select, 2. Insert, 3. Update, 4. Delete, 5. Close, 6. SELECT Query ?:  "))

    if accion== 1:
        # mostrar todas las pelis
        sSQL= "SELECT * FROM Peliculas"
        cur= conn.cursor()
        cur.execute(sSQL)
        filas = cur.fetchall() #muestra todas las filas y con fetchone muestra solo 1
        for fila in filas:
            print(fila)
      
    elif accion == 2:
        nombre= input("Cual es el nombre: ")
        duracion = input("Cual es la duracion: ")
        cur = conn.cursor()
        sSQL= "INSERT INTO Peliculas (nombre, duracion) VALUES (?, ?)"
        cur.execute(sSQL, (nombre, duracion))
        conn.commit()
        print("Tu transaccion ha funcionado correctamente")


    elif accion == 3: #UPDATE
        id = input("Que numero quieres actualizar? ")
        duracion = input("Que duracion tiene? ")
        cur= conn.cursor()
        sSQL="UPDATE peliculas SET duracion = ?  WHERE id = ?"
        cur.execute(sSQL, (duracion, id))
        conn.commit()

    elif accion == 4: #DELETE
        id = input("Que numero quieres borrar? ")
      
        cur= conn.cursor()
        sSQL="DELETE  FROM Peliculas  WHERE id = " + id
        cur.execute(sSQL,)
        conn.commit()


    elif accion == 5:
        print("cerrando") 
        conn.close()
        break
   

    elif accion == 6:
        nombre= input("Que pelis buscas?")
        nombre= nombre + "%"
        #sSQL= f"SELECT *FROM Peliculas WHERE nombre LIKE ?"    
        cursor= conn.cursor()
        cursor.execute(sSQL, (nombre,))
        filas= cursor.fetchall()
        for fila in filas:
            print(fila)

    else: 
        pass
              