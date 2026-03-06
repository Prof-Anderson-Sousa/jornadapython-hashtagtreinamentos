# titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
    # mostrar a mensagem que o usuario enviou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="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")

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state ["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem...") # markdown

for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"]) # markdown

if texto_usuario:
    print(texto_usuario)
    st.chat_message("user").write(texto_usuario) # markdown
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)    
    # Nome
    # user
    # assistant

    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["lista_mensagens"], model="gpt-4o")
    print(resposta_ia)
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia) # markdown  
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

print(st.session_state["lista_mensagens"])