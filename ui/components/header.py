import streamlit as st
from .icons import AppIcons, Icons


def render_header():

    st.markdown(
        f"""
        <div class="hero-shell">
            <div class="hero-top">
                <div class="hero-badge">{AppIcons.LOGO}</div>
                <div>
                    <h1>Santos Pegasus AI Agent</h1>
                    <p>Asistente inteligente basado en Gemini 2.5 Flash + RAG para explorar la documentación oficial de Santos Pegasus Soluciones.</p>
                </div>
            </div>
            <div class="hero-pills">
                <span class="hero-pill">{AppIcons.RAG} Respuestas precisas</span>
                <span class="hero-pill">{AppIcons.DOCUMENTS} Fuentes contextuales</span>
                <span class="hero-pill">{Icons.CHART} Panel interactivo</span>
                <span class="hero-pill">{Icons.INFO} Solo documentación indexada</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("### 👋 ¿En qué puedo ayudarte hoy?")
    st.caption("Haz preguntas sobre la documentación indexada de Santos Pegasus Soluciones.")


def render_compact_header():
    """
    Header para móviles.
    """
    st.markdown(
        f"""
        <div class="hero-shell">
            <div class="hero-top">
                <div class="hero-badge">{AppIcons.LOGO}</div>
                <div>
                    <h1>Santos Pegasus AI</h1>
                    <p>Consulta documentos de manera rápida y precisa.</p>
                </div>
            </div>
            <div class="hero-pills">
                <span class="hero-pill">{AppIcons.RAG} RAG</span>
                <span class="hero-pill">{AppIcons.DOCUMENTS} Docs</span>
                <span class="hero-pill">{Icons.CHART} Métricas</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
