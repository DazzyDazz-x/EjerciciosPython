
from flask import Flask
app= Flask(__name__)

@app.route("/")
def homepage():
    return "Home page Deisy. <a href= '/nose'> Click aqui </a> para ir a nose "

@app.route("/nose")
def agur():
    return "<h1>AGUR</h1> <a href= '/'> Click aqui </a> para ir a Home Page  "


if "__name__" == '_main_':
    app.run()