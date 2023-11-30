import streamlit as st

st.title("Hello")


num1 = st.number_input("Digite o primeiro número: ")
num2 = st.number_input("Digite o segundo número: ") 

if st.button("Calcular"):
    resultado1 = num1 + num2
    st.text(f' a soma entre eles é: {resultado1}')
    resultado2 = num1 - num2
    st.text(f' a subtração entre eles é: {resultado2}')
    resultado3 = num1 *  num2
    st.text(f' a multiplicação entre eles é : {resultado3}')
    resultado4 = num1  / num2
    st.text(f' a divisão entre eles: {resultado4}')
    st.title( Obrigado)        














