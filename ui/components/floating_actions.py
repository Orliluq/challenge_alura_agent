import streamlit as st
from typing import Callable, List, Tuple
from .icons import AppIcons


def render_floating_actions(
    on_clear_chat: Callable = None,
    on_export: Callable = None,
    actions: List[Tuple[str, Callable, str]] = None,
):
    """
    Renderiza botones de acción flotantes.
    
    Args:
        on_clear_chat: Callback para limpiar chat
        on_export: Callback para exportar
        actions: Lista de tuplas (icono, callback, tooltip)
    """
    if actions is None:
        actions = [
            (AppIcons.NEW_CHAT, on_clear_chat, "Limpiar conversación"),
            (AppIcons.EXPORT_MD, on_export, "Exportar conversación"),
        ]
    
    st.markdown('<div class="floating-actions">', unsafe_allow_html=True)
    
    for icon, callback, tooltip in actions:
        if callback is None:
            continue
        
        if st.button(
            icon,
            key=f"float_{icon}",
            help=tooltip,
            use_container_width=True,
        ):
            callback()
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_quick_action_button(
    icon: str,
    callback: Callable,
    tooltip: str,
    key: str = None,
):
    """
    Renderiza un botón de acción rápida individual.
    
    Args:
        icon: Icono del botón
        callback: Función a ejecutar
        tooltip: Texto de ayuda
        key: Clave única para el botón
    """
    if key is None:
        key = f"quick_action_{icon}"
    
    if st.button(
        icon,
        key=key,
        help=tooltip,
        use_container_width=True,
    ):
        callback()


def render_action_menu(
    actions: List[Tuple[str, Callable, str]],
    label: str = "Acciones rápidas",
):
    """
    Renderiza un menú de acciones.
    
    Args:
        actions: Lista de tuplas (icono, callback, tooltip)
        label: Etiqueta del menú
    """
    with st.expander(label):
        for icon, callback, tooltip in actions:
            if st.button(
                f"{icon} {tooltip}",
                key=f"menu_{icon}",
                use_container_width=True,
            ):
                callback()
