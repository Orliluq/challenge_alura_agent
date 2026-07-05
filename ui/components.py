import streamlit as st
from typing import List, Dict
import time

from .styles import apply_custom_styles
from .utils import APIClient, MetricsTracker
from .export import download_markdown


def render_sidebar(metrics: Dict, on_clear_chat: callable, on_export_markdown: callable, on_export_pdf: callable):
    """
    Renderiza la barra lateral con métricas y acciones
    
    Args:
        metrics: Diccionario con estadísticas
        on_clear_chat: Callback para limpiar chat
        on_export_markdown: Callback para exportar a Markdown
        on_export_pdf: Callback para exportar a PDF
    """
    with st.sidebar:
        st.markdown("### 📊 Estadísticas")
        st.divider()
        
        # Detectar dispositivo móvil
        is_mobile = st.session_state.get('is_mobile', False)
        
        # Métricas - layout responsive
        if is_mobile:
            # En móvil, mostrar métricas verticalmente
            st.metric(
                label="Preguntas",
                value=metrics.get("total_questions", 0)
            )
            st.metric(
                label="Documentos",
                value=metrics.get("total_documents", 0)
            )
            st.metric(
                label="Tiempo medio",
                value=f"{metrics.get('average_time', 0):.2f} s"
            )
        else:
            # En desktop/tablet, mostrar en grid
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    label="Preguntas",
                    value=metrics.get("total_questions", 0)
                )
            
            with col2:
                st.metric(
                    label="Documentos",
                    value=metrics.get("total_documents", 0)
                )
            
            st.metric(
                label="Tiempo medio",
                value=f"{metrics.get('average_time', 0):.2f} s"
            )
        
        st.divider()
        
        # Acciones - layout responsive
        st.markdown("### 🛠️ Acciones")
        
        if st.button("🗑️ Nueva conversación", use_container_width=True):
            on_clear_chat()
        
        if is_mobile:
            # En móvil, botones verticales
            if st.button("📥 Exportar Markdown", use_container_width=True):
                on_export_markdown()
            if st.button("📥 Exportar PDF", use_container_width=True):
                on_export_pdf()
        else:
            # En desktop/tablet, botones en grid
            col_md, col_pdf = st.columns(2)
            
            with col_md:
                if st.button("📥 Markdown", use_container_width=True):
                    on_export_markdown()
            
            with col_pdf:
                if st.button("📥 PDF", use_container_width=True):
                    on_export_pdf()
        
        st.divider()
        
        # Info - simplificado en móvil
        st.markdown("### ℹ️ Info")
        if is_mobile:
            st.markdown("""
            **Santos Pegasus AI**
            
            🤖 Gemini 2.5 Flash
            📚 RAG + FAISS
            ⚡ FastAPI + Streamlit
            """)
        else:
            st.markdown("""
            **Santos Pegasus AI**
            
            Asistente inteligente basado en:
            - 🤖 Gemini 2.5 Flash
            - 📚 RAG con FAISS
            - ⚡ FastAPI + Streamlit
            """)


def render_chat_message(message: Dict, index: int, feedback: Dict):
    """
    Renderiza un mensaje del chat con feedback
    
    Args:
        message: Diccionario con el mensaje
        index: Índice del mensaje
        feedback: Diccionario con feedback de usuarios
    """
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Mostrar fuentes si es asistente
        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("📚 Documentos utilizados"):
                for source in message["sources"]:
                    st.write("•", source)
        
        # Botones de feedback para asistente
        if message["role"] == "assistant":
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("👍", key=f"up_{index}"):
                    feedback[index] = "👍"
                    st.rerun()
            
            with col2:
                if st.button("👎", key=f"down_{index}"):
                    feedback[index] = "👎"
                    st.rerun()
            
            if index in feedback:
                st.caption(f"Feedback: {feedback[index]}")


def render_header():
    """Renderiza el header de la aplicación"""
    # Detectar dispositivo móvil
    is_mobile = st.session_state.get('is_mobile', False)
    
    if is_mobile:
        # Header simplificado para móvil
        st.title("🤖 Santos Pegasus AI")
        
        st.markdown("""
        Asistente basado en **Gemini 2.5 Flash + RAG** para consultar la documentación de **Santos Pegasus Soluciones**.
        
        **Temas:**
        - 🏗️ Arquitectura
        - ⚙️ Backend
        - 🎨 Frontend
        - 🚨 Incidentes
        - 👨‍💻 Onboarding
        """)
    else:
        # Header completo para desktop/tablet
        st.title("🤖 Santos Pegasus AI Assistant")
        
        st.markdown("""
        Asistente inteligente basado en **Gemini 2.5 Flash + RAG** para consultar la documentación oficial de
        **Santos Pegasus Soluciones**.
        
        Puedes hacer preguntas sobre:
        
        - 🏗️ Arquitectura de Microservicios
        - ⚙️ Ingeniería Backend  
        - 🎨 Ingeniería Frontend
        - 🚨 Incidentes y Post Mortems
        - 👨‍💻 Onboarding de nuevos desarrolladores
        
        ⚠️ Este asistente responde únicamente utilizando la documentación indexada.
        """)
    
    st.divider()


def render_loading_spinner():
    """Renderiza un spinner de carga personalizado"""
    with st.spinner("🧠 Consultando documentos..."):
        time.sleep(0.1)  # Pequeña pausa para que el spinner se muestre


def render_error_message(error: str):
    """Renderiza un mensaje de error"""
    st.error(f"❌ {error}")


def render_success_message(message: str):
    """Renderiza un mensaje de éxito"""
    st.success(f"✅ {message}")
