"""
Módulo de estilos para Santos Pegasus AI.

Exporta todos los submódulos del sistema de estilos.
"""

from .theme import (
    get_theme_config,
    get_css_variables,
    get_streamlit_theme_config,
)
from .css import (
    get_base_css,
    get_sidebar_css,
    get_hero_css,
    get_dashboard_css,
    get_chat_css,
    get_buttons_css,
    get_metrics_css,
    get_footer_css,
    get_scrollbar_css,
    get_utilities_css,
    get_responsive_css,
    get_complete_css,
)
from .animations import (
    get_animations_css,
    get_background_animations,
    get_animation_classes,
    get_transition_classes,
    get_hover_effects,
    get_loading_states,
    get_responsive_animations,
)

__all__ = [
    # Theme
    "get_theme_config",
    "get_css_variables",
    "get_streamlit_theme_config",
    # CSS
    "get_base_css",
    "get_sidebar_css",
    "get_hero_css",
    "get_dashboard_css",
    "get_chat_css",
    "get_buttons_css",
    "get_metrics_css",
    "get_footer_css",
    "get_scrollbar_css",
    "get_utilities_css",
    "get_responsive_css",
    "get_complete_css",
    # Animations
    "get_animations_css",
    "get_background_animations",
    "get_animation_classes",
    "get_transition_classes",
    "get_hover_effects",
    "get_loading_states",
    "get_responsive_animations",
]
