import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os

# Configuración
st.set_page_config(page_title="Agente Económico", page_icon="📈", layout="wide")
st.title("📊 Agente LLM de Economía")

# API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.warning("⚠️ No se encontró la clave de API de Groq. Configura GROQ_API_KEY en tu entorno.")

# Inicializar modelo
llm = ChatGroq(model="mixtral-8x7b-32768", api_key=api_key)

# Prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "Eres un experto en economía y finanzas. Responde de forma clara y útil."),
    ("user", "{question}")
])

# Entrada del usuario
question = st.text_area("Escribe tu consulta económica:", placeholder="Ejemplo: Explica la inflación en términos simples.")

if st.button("Analizar"):
    if question.strip():
        chain = template | llm
        response = chain.invoke({"question": question})
        st.subheader("💡 Respuesta del agente:")
        st.write(response.content)
    else:
        st.warning("Por favor escribe una consulta.")