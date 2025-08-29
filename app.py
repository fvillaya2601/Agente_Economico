import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os

# Configuración
st.set_page_config(page_title="Agente Económico", page_icon="📈", layout="wide")
st.title("📊 Chat de Economía")

# API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.warning("⚠️ No se encontró la clave de API de Groq. Configura GROQ_API_KEY en tu entorno.")

# Inicializar modelo
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)

# Prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "Eres un experto en economía y finanzas. Responde de forma clara y útil solo preguntas especificas de temas de economía y finanzas. Restringe respuestas sobre otros temas."),
    ("user", "{question}")
])

# Entrada del usuario
question = st.text_area("Escribe tu consulta sobre economía:", placeholder="Ejemplo: Que es el PIB.")

if st.button("Analizar"):
    if question.strip():
        chain = template | llm
        response = chain.invoke({"question": question})
        st.subheader("💡 Respuesta:")
        st.write(response.content)
    else:
        st.warning("Por favor escribe una consulta una consulta de Economía.")
