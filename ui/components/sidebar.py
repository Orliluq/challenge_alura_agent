import streamlit as st
from typing import Callable, Dict
from .icons import AppIcons, Icons, get_theme_icon
from .metrics import render_sidebar_metrics


def render_sidebar(
    metrics: Dict,
    on_clear_chat: Callable,
    on_export_markdown: Callable,
    on_export_pdf: Callable,
):
    """
    Sidebar principal de la aplicación.
    
    """
    with st.sidebar:
        _render_logo_section()
        _render_theme_selector()
        st.divider()
        
        is_mobile = st.session_state.get("is_mobile", False)
        render_sidebar_metrics(metrics, is_mobile)
        
        st.divider()
        _render_actions(on_clear_chat, on_export_markdown, on_export_pdf)
        
        st.divider()
        _render_system_info()
        st.divider()
        _render_footer()


def _render_logo_section():
    """Renderiza la sección del logo."""
    st.markdown(
        f"""
        <div class="sidebar-hero">
            <h3>{AppIcons.LOGO} Santos Pegasus IA</h3>
            <p>Agente IA para consultar documentación.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_theme_selector():
    """Renderiza el selector de tema."""
    st.subheader(f"{Icons.PALETTE} Apariencia")
    
    current_theme = st.session_state.get("theme_mode", "dark")
    theme_icon = get_theme_icon(current_theme)
    
    is_light = st.toggle(
        f"{theme_icon}",
        value=current_theme == "light",
    )
    
    new_theme = "light" if is_light else "dark"
    
    if new_theme != current_theme:
        st.session_state.theme_mode = new_theme
        st.rerun()


def _render_actions(
    on_clear_chat: Callable,
    on_export_markdown: Callable,
    on_export_pdf: Callable,
):
    """Renderiza las acciones del sidebar."""
    st.subheader(f"{Icons.BOLT} Acciones")
    
    if st.button(
        f"{AppIcons.NEW_CHAT} Nueva conversación",
        use_container_width=True,
        type="primary",
    ):
        on_clear_chat()
    
    if st.button(
        f"{AppIcons.EXPORT_MD} Exportar Markdown",
        use_container_width=True,
    ):
        on_export_markdown()
    
    if st.button(
        f"{AppIcons.EXPORT_PDF} Exportar PDF",
        use_container_width=True,
    ):
        on_export_pdf()


def _render_system_info():
    """Renderiza la información del sistema."""
    st.subheader(f"{Icons.INFO} Información")
    
    st.markdown(
        f"""
        <div class="sidebar-hero">
            <p><strong>Santos Pegasus AI</strong></p>
            <p>Gemini 2.5 Flash + RAG + FAISS</p>
            <p>FastAPI + Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_footer():
    """Renderiza el footer del sidebar."""
    st.caption(
        f"""
        {Icons.VERSION} Versión 2.0
        
        """
    )
