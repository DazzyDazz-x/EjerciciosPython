import streamlit as st
from datetime import datetime  #porque asi te aparecen mas opciones para usar



with st.form("my form", clear_on_submit=True):
    nom= st.text_input("## *Nombre*: ")
    pro= st.text_area("## *Describe tu problema tecnico:* ")

    if st.form_submit_button("Generar y Guardar Informe"):
        st.write( pro)
        with open("InformeProbTecnico.txt", "a") as f:
            descripcion= nom + "-" + pro + "-" + str( datetime.now()) #.strftimr("%yy%M%d")
            f.write( descripcion +"\n")