#Creacion de paginas web, pero de forma local en tu ordenador

import streamlit as st
import pandas as pd
st.title("Primer proyecto de Deisy!!!")
st.write("Guapa!")
st.markdown("## *BYe*")

animales=("dog", "cat", "bird")

name=st.text_input('Introducir el nombre de un animal: ')
if name in animales:
    st.write(f'El animal es: ', name)



def aplicarEdad(x):
    return x*10

edad= st.number_input('Que edad tienes?: ')

if st.button("Click me"):
    st.write(f"tu edad es: {aplicarEdad(edad)} ")
  
df=pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv")  
st.dataframe(df)