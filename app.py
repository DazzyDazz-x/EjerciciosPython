
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
    

if "__name__" == '_main_':
    app.run()
