"""
Componente header para Santos Pegasus AI.

Header principal inspirado en ChatGPT/Claude/Linear.
Sin CSS inline, usando el sistema de estilos centralizado.
"""

import streamlit as st
from .icons import AppIcons, Icons


def render_header():
    """
    Header principal de la aplicación.
    Inspirado en ChatGPT / Claude / Linear.
    """
    st.markdown(
        f"""
        <div class="hero-shell">
            <div class="hero-top">
                <div class="hero-badge">{AppIcons.LOGO}</div>
                <div>
                    <h1>Santos Pegasus AI Assistant</h1>
                    <p>Asistente inteligente basado en Gemini 2.5 Flash + RAG para explorar la documentación oficial de Santos Pegasus Soluciones.</p>
                </div>
            </div>
            <div class="hero-pills">
                <span class="hero-pill">{AppIcons.RAG} Respuestas vivas</span>
                <span class="hero-pill">{AppIcons.DOCUMENT} Fuentes contextuales</span>
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
    Header compacto para vistas móviles.
    """
    st.markdown(
        f"""
        <div class="hero-shell">
            <div class="hero-top">
                <div class="hero-badge">{AppIcons.LOGO}</div>
                <div>
                    <h1>Santos Pegasus AI</h1>
                    <p>Consulta documentos con una experiencia más viva, rápida y visual.</p>
                </div>
            </div>
            <div class="hero-pills">
                <span class="hero-pill">{AppIcons.RAG} RAG</span>
                <span class="hero-pill">{AppIcons.DOCUMENT} Docs</span>
                <span class="hero-pill">{Icons.CHART} Métricas</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
