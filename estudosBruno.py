import streamlit as st

st.title('Bem Vindo ao streamlit')
st.markdown("vamos realizar seu cadastro abaixo:")

nome = st.text_input("digite seu nome:")

if nome: 
    st.markdown(f"seu nome foi cadastrado {nome}!") 
    data = st.date_input("agora digite sua data de nascimento:")