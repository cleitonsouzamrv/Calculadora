import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Questionário Sim ou Não")

# Lista de perguntas
perguntas = [
    "Você gosta de programar?",
    "Você já trabalhou com Python?",
    "Você gosta de aprendizado de máquina?"
]

# Armazenar respostas
respostas = {}

# Criar botões para cada pergunta
for pergunta in perguntas:
    resposta = st.radio(pergunta, ('Sim', 'Não'))
    respostas[pergunta] = resposta

# Exibir respostas
if st.button("Enviar Respostas"):
    st.write("Suas Respostas:")
    for pergunta, resposta in respostas.items():
        st.write(f"{pergunta} : **{resposta}**")