import streamlit as st

st.title("Calculadora Simples")

# Entrada dos números
a = st.number_input("Digite o primeiro número", value=0)
b = st.number_input("Digite o segundo número", value=0)

# Operações
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b if b != 0 else "Divisão por zero"

# Resultados
st.write("Soma:", soma)
st.write("Subtração:", subtracao)
st.write("Multiplicação:", multiplicacao)
st.write("Divisão:", divisao)
