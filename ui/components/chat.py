"""
Componente chat para Santos Pegasus AI.

Sistema de chat modular inspirado en ChatGPT/Claude.
"""

from typing import Dict, List
import streamlit as st
from .icons import Icons, AppIcons


def render_chat(messages: List[Dict], feedback: Dict):
    """
    Renderiza todo el historial del chat.
    
    Args:
        messages: Lista de mensajes del chat
        feedback: Diccionario con feedback de usuarios
    """
    if not messages:
        render_empty_state()
        return
    
    for index, message in enumerate(messages):
        render_message(message, index, feedback)


def render_empty_state():
    """Renderiza el estado vacío del chat."""
    st.markdown(
        f"""
        <div style="text-align:center; padding:5rem 1rem; opacity:.85;">
            <h2>{AppIcons.LOGO} Santos Pegasus AI</h2>
            <p style="font-size:18px;">
                Pregunta cualquier cosa sobre la documentación
                de Santos Pegasus Soluciones.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_message(message: Dict, index: int, feedback: Dict):
    """
    Renderiza un mensaje individual del chat.
    
    Args:
        message: Diccionario con el mensaje
        index: Índice del mensaje
        feedback: Diccionario con feedback
    """
    role = message["role"]
    avatar = Icons.USER if role == "user" else AppIcons.LOGO
    
    with st.chat_message(role, avatar=avatar):
        st.markdown(message["content"])
        
        if role == "assistant":
            render_sources(message)
            render_feedback(index, feedback)


def render_sources(message: Dict):
    """
    Renderiza las fuentes del mensaje.
    
    Args:
        message: Diccionario con el mensaje
    """
    sources = message.get("sources", [])
    
    if not sources:
        return
    
    with st.expander(
        f"{AppIcons.DOCUMENT} Documentos utilizados ({len(sources)})",
        expanded=False,
    ):
        for source in sources:
            st.markdown(f"- {source}")


def render_feedback(index: int, feedback: Dict):
    """
    Renderiza los botones de feedback.
    
    Args:
        index: Índice del mensaje
        feedback: Diccionario con feedback
    """
    if index in feedback:
        value = feedback[index]
        
        if value == "like":
            st.success("Gracias por tu feedback 👍")
        else:
            st.warning("Gracias por tu feedback 👎")
        
        return
    
    col1, col2, col3 = st.columns([1, 1, 8])
    
    with col1:
        if st.button(
            Icons.THUMBS_UP,
            key=f"like_{index}",
            help="Respuesta útil",
        ):
            feedback[index] = "like"
            st.rerun()
    
    with col2:
        if st.button(
            Icons.THUMBS_DOWN,
            key=f"dislike_{index}",
            help="Respuesta incorrecta",
        ):
            feedback[index] = "dislike"
            st.rerun()


def render_typing():
    """Renderiza indicador de typing."""
    with st.chat_message("assistant", avatar=AppIcons.LOGO):
        with st.spinner("Pensando..."):
            pass


def add_user_message(text: str):
    """
    Agrega un mensaje del usuario al historial.
    
    Args:
        text: Texto del mensaje
    """
    st.session_state.messages.append({
        "role": "user",
        "content": text,
    })


def add_assistant_message(answer: str, sources=None):
    """
    Agrega un mensaje del asistente al historial.
    
    Args:
        answer: Respuesta del asistente
        sources: Lista de fuentes (opcional)
    """
    if sources is None:
        sources = []
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
    })


def clear_chat():
    """Limpia el historial de chat."""
    st.session_state.messages = []
    st.session_state.feedback = {}


def chat_input():
    """
    Renderiza el input de chat.
    
    Returns:
        Texto ingresado por el usuario
    """
    return st.chat_input("Escribe tu pregunta...")
