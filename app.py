import streamlit as st

st.title("Aula 1 - Calculadora Simples")

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


st.title("Aula 2 - Verificador de Idade")

idade = st.number_input("Digite a idade", min_value=0, step=1)

if idade == 0:
    st.write("Encerrado.")
elif idade >= 18:
    st.write("Adulto")
elif idade >= 12:
    st.write("Adolescente")
else:
    st.write("Criança")

st.title("Aula 3 - Números Pares e Ímpares de 1 a 20")

pares = [n for n in range(1, 21) if n % 2 == 0]
impares = [n for n in range(1, 21) if n % 2 != 0]

st.subheader("Números Pares:")
for numero in pares:
    st.write(numero)

st.subheader("Números Ímpares:")
for numero in impares:
    st.write(numero)

st.title("Aula 4 - Calculadora com Funções")

a = st.number_input("Digite o primeiro número", value=0, key="num1")
b = st.number_input("Digite o segundo número", value=0, key="num2")

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y if y != 0 else "Divisão por zero"

st.write("Soma:", soma(a, b))
st.write("Subtração:", subtracao(a, b))
st.write("Multiplicação:", multiplicacao(a, b))
st.write("Divisão:", divisao(a, b))

st.title("Aula 5 - Agenda de Contatos")

# Dicionário inicial de contatos
agenda = {"Lucas": "lucas@email.com", "Maria": "maria@email.com"}

# Mostrar contatos
st.subheader("Contatos existentes:")
for nome, email in agenda.items():
    st.write(f"{nome}: {email}")

# Adicionar novo contato
st.subheader("Adicionar novo contato")
novo_nome = st.text_input("Nome", key="novo_nome")
novo_email = st.text_input("Email", key="novo_email")

if st.button("Adicionar contato", key="botao_adicionar"):
    agenda[novo_nome] = novo_email
    st.success(f"Contato {novo_nome} adicionado!")
