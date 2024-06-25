import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/'

def response(x, y, z):
    try:
        # Faz a solicitação POST à API
        resp = requests.post(f"{API_URL}/predict", json={"text": [x, y, z]})
        resp.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = resp.json()
        resultado = data["resultado"]

        # Exibe o resultado com formatação adequada
        st.success(f"Previsão da Quantidade de venda: {resultado}")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}")
    except ValueError:
        st.error("Erro ao processar a resposta da API")

st.title('Previsor de Vendas')
x = st.text_input('Digite o Número do Mês')
y = st.text_input('Digite o Id da Loja')
z = st.text_input('Digite o Id do Item')

if st.button('Predict'):
    response(x, y, z)



