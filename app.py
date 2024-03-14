import sqlite3
from flask import Flask, render_template, request, url_for, redirect

app= Flask(__name__)

@app.route("/")
def homepage():
    return "Home page Deisy. <a href= '/nose'> Click aqui </a> para ir a nose "

@app.route("/nose")
def agur():
    return "<h1>AGUR</h1> <a href= '/'> Click aqui </a> para ir a Home Page  "

@app.route("/dashboard/<string:username>")
def dashboard(username):
    return f"Ya estas dentro {username}!"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")    
    else: #POST
        username = request.form["username"]
        password = request.form["password"]

        if username == username and password=="password":
            return redirect(url_for("dashboard", username= username))
        else:
            return "No puedes entrar. Contraseña o usuario incorrecto"


        return f"submit resultados con POST {username} y {password}"
    


@app.route("/peliculas", methods=['GET'])    
def Peliculas():
    #abrir conexion a database
    conn= sqlite3.connect('pelis.db')

   
   
   
    #select todas las pelis
    sSQL= "SELECT * FROM Peliculas"
    cur= conn.cursor()
    cur.execute(sSQL)
    rows= cur.fetchall()
   
    """for row in rows:
        print(row)"""
    #cerrar conexion
    conn.close()

@app.route("/addpelicula", methods=['GET', 'POST'])
def addpelicula():
    if request.method=="GET":
        return render_template("addpelicula.html")    
    else: #POST
        nombre = request.form["nombre"]
        duracion = request.form["duracion"]

         #abre conexion
        conn= sqlite3.connect('pelis.db')
        cur= conn.cursor()
        sSQL= "INSERT INTO Peliculas (nombre, duracion) VALUES (?,?)"      
        cur.execute(sSQL, (nombre, duracion))
        conn.commit()
        conn.close()
        return redirect(url_for("peliculas"))
      


     
    



    return render_template("Peliculas.html", rows= rows)

if "__name__" == '_main_':
    app.run()
