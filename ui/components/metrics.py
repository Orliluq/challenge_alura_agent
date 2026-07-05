"""
Componente de métricas para Santos Pegasus AI.

Cards y visualizaciones de métricas de forma modular.
"""

import streamlit as st
from typing import Dict, List, Tuple
from .icons import AppIcons, Icons


def render_metric_card(
    icon: str,
    title: str,
    value: str,
    subtitle: str = None,
    color: str = None,
):
    """
    Renderiza una card de métrica individual.
    
    Args:
        icon: Icono de la métrica
        title: Título de la métrica
        value: Valor a mostrar
        subtitle: Subtítulo opcional
        color: Color del icono (opcional)
    """
    if color is None:
        color = "var(--primary)"
    
    st.markdown(
        f"""
        <div class="dashboard-card hover-lift">
            <div class="dashboard-icon" style="background: {color};">
                {icon}
            </div>
            <div class="dashboard-title">{title}</div>
            <div class="dashboard-value">{value}</div>
            {f'<div class="dashboard-subtitle">{subtitle}</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics_grid(
    metrics: List[Tuple[str, str, str, str, str]],
    columns: int = 3,
):
    """
    Renderiza una grilla de métricas.
    
    Args:
        metrics: Lista de tuplas (icono, título, valor, subtítulo, color)
        columns: Número de columnas
    """
    cols = st.columns(columns)
    
    for i, (icon, title, value, subtitle, color) in enumerate(metrics):
        with cols[i % columns]:
            render_metric_card(icon, title, value, subtitle, color)


def render_app_metrics(metrics: Dict):
    """
    Renderiza las métricas específicas de la aplicación.
    
    Args:
        metrics: Diccionario con métricas (total_questions, total_documents, average_time)
    """
    total_questions = metrics.get("total_questions", 0)
    total_documents = metrics.get("total_documents", 0)
    average_time = metrics.get("average_time", 0)
    
    app_metrics = [
        (AppIcons.QUESTIONS, "Preguntas", str(total_questions), "Consultas realizadas", "#3b82f6"),
        (AppIcons.DOCUMENTS, "Documentos", str(total_documents), "Fuentes utilizadas", "#22c55e"),
        (AppIcons.TIME, "Tiempo", f"{average_time:.2f}s", "Respuesta promedio", "#f59e0b"),
    ]
    
    render_metrics_grid(app_metrics, columns=3)


def render_status_chip(
    icon: str,
    title: str,
    value: str,
    status: str = "active",
):
    """
    Renderiza un chip de estado.
    
    Args:
        icon: Icono del estado
        title: Título del estado
        value: Valor del estado
        status: Estado (active, inactive, warning, error)
    """
    status_colors = {
        "active": "#22c55e",
        "inactive": "#64748b",
        "warning": "#f59e0b",
        "error": "#ef4444",
    }
    
    color = status_colors.get(status, "#22c55e")
    
    st.markdown(
        f"""
        <div class="status-chip">
            <div class="status-emoji">{icon}</div>
            <div>
                <div class="status-title">{title}</div>
                <div class="status-value" style="color: {color};">{value}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_system_status():
    """
    Renderiza el estado del sistema.
    """
    st.markdown("### 🚀 Sistema")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        render_status_chip(AppIcons.API, "API", "Conectada", "active")
    
    with c2:
        render_status_chip(AppIcons.MODEL, "Modelo", "Gemini 2.5 Flash", "active")
    
    with c3:
        render_status_chip(AppIcons.VECTOR_DB, "Base vectorial", "FAISS", "active")
    
    with c4:
        render_status_chip(AppIcons.BACKEND, "Backend", "FastAPI", "active")


def render_sidebar_metrics(metrics: Dict, is_mobile: bool = False):
    """
    Renderiza métricas en el sidebar.
    
    Args:
        metrics: Diccionario con métricas
        is_mobile: Si es vista móvil
    """
    st.markdown("### 📊 Estadísticas")
    
    if is_mobile:
        st.metric("Preguntas", metrics.get("total_questions", 0))
        st.metric("Documentos", metrics.get("total_documents", 0))
        st.metric("Tiempo medio", f"{metrics.get('average_time', 0):.2f} s")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Preguntas", metrics.get("total_questions", 0))
        
        with col2:
            st.metric("Documentos", metrics.get("total_documents", 0))
        
        st.metric("Tiempo medio", f"{metrics.get('average_time', 0):.2f} s")
