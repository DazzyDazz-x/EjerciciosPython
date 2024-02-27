import streamlit as st

import streamlit as st
from datetime import datetime  #porque asi te aparecen mas opciones para usar


st.title("Servicio Tecnico 2")

#with st.form("my form", clear_on_submit=True):
nom= st.text_input("## *Nombre*: ")
pro= st.text_area("## *Describe tu problema tecnico:* ")
    
if st.button("Guardar Informe"):
            
    with open("InformeProbTecnico.txt", "a") as f:
        descripcion= nom + "-" + pro + "-" + str( datetime.now()) #.strftimr("%yy%M%d")
        f.write( descripcion +"\n")

if st.button("Mostrar Informe"):
    with open("InformeProbTecnico.txt", "r") as f: 
    #leer todos los datos y mostrarlos
        st.write(f.readlines())

if "counter" not in st.session_state:
    st.session_state.counter=0

if st.button("Contar"):
    st.session_state.counter +=1
st.write(f"{st.session_state.counter} veces que pinchamos")    

st.write(eval("10+10==21"))
st.write("Instrucciones: usar st.write() para imprimir :v:")


codigo= st.text_area('Introducir codigo')

if codigo:
    exec(codigo)
