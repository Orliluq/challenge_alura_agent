"""
Santos Pegasus AI - Aplicación principal Streamlit.

Interfaz moderna y modular para asistente RAG con Gemini 2.5 Flash.
"""

import streamlit as st
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ui.utils import APIClient, MetricsTracker
from ui.components import (
    render_header,
    render_sidebar,
    render_chat,
    chat_input,
    add_user_message,
    add_assistant_message,
    clear_chat as clear_chat_component,
    render_empty_dashboard,
    render_footer,
    render_floating_actions,
    AppIcons,
)
from ui.styles import apply_custom_styles
from ui.export import download_markdown, download_pdf


# ============================================
# CONFIGURACIÓN
# ============================================

st.set_page_config(
    page_title="Santos Pegasus AI | Asistente RAG",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================
# INICIALIZACIÓN DE ESTADO
# ============================================

def initialize_session_state():
    """Inicializa el estado de la aplicación."""
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "dark"
    
    if "is_mobile" not in st.session_state:
        st.session_state.is_mobile = _detect_mobile()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "feedback" not in st.session_state:
        st.session_state.feedback = {}
    
    if "api_client" not in st.session_state:
        st.session_state.api_client = APIClient()
    
    if "metrics_tracker" not in st.session_state:
        st.session_state.metrics_tracker = MetricsTracker()


def _detect_mobile():
    """Detecta si el usuario está en un dispositivo móvil."""
    try:
        return st.session_state.get("client_width", 1200) < 768
    except Exception:
        return False


# ============================================
# CALLBACKS
# ============================================

def clear_chat():
    """Limpia el historial de chat."""
    st.session_state.messages = []
    st.session_state.feedback = {}
    st.session_state.metrics_tracker.reset()
    st.rerun()


def export_chat_markdown():
    """Exporta el chat a Markdown."""
    if st.session_state.messages:
        download_markdown(st.session_state.messages)
    else:
        st.warning("No hay mensajes para exportar")


def export_chat_pdf():
    """Exporta el chat a PDF (formato impresión)."""
    if st.session_state.messages:
        download_pdf(st.session_state.messages)
    else:
        st.warning("No hay mensajes para exportar")


# ============================================
# PROCESAMIENTO DE PREGUNTAS
# ============================================

def process_question(question: str):
    """
    Procesa una pregunta del usuario.
    
    Args:
        question: Pregunta del usuario
    """
    # Agregar mensaje del usuario
    add_user_message(question)
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(question)
    
    # Generar respuesta del asistente
    with st.chat_message("assistant"):
        with st.spinner(f"Consultando documentos con Gemini 2.5 Flash..."):
            response = st.session_state.api_client.ask_question(question)
            
            answer = response.get("answer", "Sin respuesta.")
            sources = response.get("sources", [])
            elapsed_time = response.get("elapsed_time", 0)
            
            # Actualizar métricas
            st.session_state.metrics_tracker.add_question(elapsed_time, len(sources))
        
        # Mostrar respuesta
        st.markdown(answer)
        
        # Mostrar fuentes si existen
        if sources:
            with st.expander(f"{AppIcons.DOCUMENT} Documentos utilizados"):
                for source in sources:
                    st.write("•", source)
            
            st.caption(f"{AppIcons.TIME} Tiempo de respuesta: {elapsed_time:.2f}s")
    
    # Agregar respuesta al historial
    add_assistant_message(answer, sources)
    
    # Rerun para actualizar la UI
    st.rerun()


# ============================================
# APLICACIÓN PRINCIPAL
# ============================================

def main():
    """Función principal de la aplicación."""
    # Inicializar estado
    initialize_session_state()
    
    # Aplicar estilos
    apply_custom_styles()
    
    # Renderizar header
    render_header()
    
    # Renderizar sidebar
    metrics = st.session_state.metrics_tracker.get_stats()
    render_sidebar(
        metrics=metrics,
        on_clear_chat=clear_chat,
        on_export_markdown=export_chat_markdown,
        on_export_pdf=export_chat_pdf
    )
    
    # Renderizar dashboard vacío si no hay mensajes
    if not st.session_state.messages:
        render_empty_dashboard(metrics)
    
    # Renderizar historial de chat
    render_chat(
        st.session_state.messages,
        st.session_state.feedback,
    )
    
    # Input de usuario
    question = chat_input()
    
    if question:
        process_question(question)
    
    # Footer
    render_floating_actions(
        on_clear_chat=clear_chat,
        on_export=export_chat_markdown,
    )
    
    st.markdown(
        f"""
        <div class="footer-card">
            <strong>Santos Pegasus AI Assistant</strong> | 
            Powered by Gemini 2.5 Flash + RAG | 
            Construido con FastAPI + Streamlit | 
            Desarrollado por Orli Dun
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    render_footer()


if __name__ == "__main__":
    main()
