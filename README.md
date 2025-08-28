# 📊 Agente LLM de Economía

Este proyecto implementa un **Agente LLM especializado en economía** utilizando **LangChain** y **Groq**, desplegado en una aplicación web con **Streamlit**.

## 🚀 Funcionalidades
- Explicación de conceptos económicos y financieros.
- Análisis de tendencias de mercado.
- Simulación de escenarios económicos.

## 🛠️ Tecnologías
- [Streamlit](https://streamlit.io/) para la interfaz web.
- [LangChain](https://www.langchain.com/) para la orquestación del modelo LLM.
- [Groq](https://groq.com/) como proveedor de modelos gratuitos.

## 📦 Instalación y uso
```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/econ-llm-agent.git
cd econ-llm-agent

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tu GROQ_API_KEY

# Ejecutar la aplicación
streamlit run app.py
```

## 📁 Estructura del proyecto
```
econ-llm-agent/
│── app.py              # Aplicación principal de Streamlit
│── requirements.txt    # Dependencias
│── .env.example        # Variables de entorno de ejemplo
│── README.md           # Documentación
│── .gitignore          # Archivos ignorados por git
```

## 📜 Licencia
MIT License.
