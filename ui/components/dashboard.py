import streamlit as st
from typing import Dict
from .icons import AppIcons
from .metrics import render_app_metrics, render_system_status


def render_dashboard(metrics: Dict):
    """
    Dashboard principal con métricas.
    
    Args:
        metrics: Diccionario con métricas de la aplicación
    """
    st.markdown("## 📊 Panel")
    render_app_metrics(metrics)
    st.markdown("")
    render_system_status()


def render_welcome():
    """
    Card de bienvenida para el estado vacío.
    """
    st.markdown(
        f"""
        <div class="welcome-card">
            <h2>👋 Bienvenido/a</h2>
            <p>Escribe tu pregunta y te ayudaré a encontrar la información que necesitas.</p>
            <p>Puedes consultar:</p>
            <ul>
                <li>📄 Procesos</li>
                <li>📚 Manuales</li>
                <li>⚙️ Procedimientos</li>
                <li>💼 Servicios</li>
                <li>🔍 Información técnica</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_dashboard(metrics: Dict):
    """
    Dashboard cuando no hay mensajes en el chat.
    
    Args:
        metrics: Diccionario con métricas
    """
    render_welcome()
    st.markdown("")
    render_dashboard(metrics)
