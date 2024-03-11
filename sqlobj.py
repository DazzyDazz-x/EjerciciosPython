from dataclasses import dataclass, astuple
import sqlite3

""" conn = sqlite3.connect('pelis.db')
conn.execute("CREATE TABLE Empleados2 (id integer, nombre text, salario)")
conn.close() """

@dataclass
class Empleado:
    id: int
    name: str
    salario: float

conn = sqlite3.connect('pelis.db')    
cursor = conn.cursor()
nombre= input("Cual es tu nombre: ")
salario= input("Cual es tu salario: ")
e= Empleado(5, nombre, salario)

cursor.execute("INSERT INTO empleados3 (id, nombre, salario) VALUES (?,?, ?);", astuple(e))
conn.close()


