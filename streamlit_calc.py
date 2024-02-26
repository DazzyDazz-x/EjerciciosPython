import streamlit as st                          #falta terminar
st.markdown("# Calculadora")

def sum(x , y):
    z= x+y
    return z
def mult(x,y):
    z=x*y
    return z


num1= st.number_input("Introducir el primer numero", min_value=0, max_value=100)
num2= st.number_input("Introducir el segundo numero", min_value=0, max_value=100)

oper= st.radio("SEleccionar una operacion: ", ["Sumar", "Multiplicar"])

if st.button("Calcular"):
    st.markdown(f"# {sum, mult(num1, num2, oper)}")
    if oper[0]:
        st.write(f"La suma de tus numeros es: ", sum(num1, num2))
    elif oper[1]:
        st.write(f"La multiplicacion de tus numeros es: ", mult(num1, num2))


left_column, right_column= st.columns(2) # o puedes poner por ejemplo [1,4] para que salgan de diferente tamaño

with left_column:
    st.markdown("# Hola Deisy left")
    st.video("https://www.youtube.com/watch?v=35kwlY_RR08")
with right_column:
    st.markdown("# Hola Deisy right")
    st.video("https://www.youtube.com/watch?v=35kwlY_RR08")
  
add_slider= st.sidebar.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0), )
st.sidebar.text("Cual es tu nombre: ")

#name= st.chat_input("Cual es tu nombre: ")
#st.write(name)