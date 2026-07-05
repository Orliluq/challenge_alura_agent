"""
Sistema de temas centralizado para Santos Pegasus AI.

Implementa temas light/dark con identidad visual consistente:
- 💜 Creatividad
- 💙 Tecnología  
- 🧡 Energía
- 💛 Cercanía
- 💚 Innovación
"""

from typing import Dict


def get_theme_config(mode: str = "dark") -> Dict[str, str]:
    """
    Retorna la configuración completa del tema.
    
    Args:
        mode: "dark" o "light"
        
    Returns:
        Diccionario con todas las variables CSS del tema
    """
    if mode == "light":
        return _get_light_theme()
    
    return _get_dark_theme()


def _get_light_theme() -> Dict[str, str]:
    """Tema claro con identidad vibrante."""
    return {
        # Colores principales
        "primary": "#ff6b35",
        "secondary": "#ffb703",
        "accent": "#ff3d71",
        "accent_2": "#22c55e",
        "accent_3": "#3b82f6",
        
        # Fondos
        "bg_main": "#fff8ef",
        "bg_card": "rgba(255, 255, 255, 0.92)",
        "bg_sidebar": "rgba(255, 255, 255, 0.96)",
        
        # Texto
        "text_main": "#111827",
        "text_muted": "#475569",
        
        # Bordes y sombras
        "border": "rgba(15, 23, 42, 0.12)",
        "shadow": "rgba(15, 23, 42, 0.16)",
        
        # Tipografía
        "font_primary": "'Fira Code', 'JetBrains Mono', 'IBM Plex Mono', monospace",
        "font_size_base": "16px",
        
        # Gradientes
        "gradient_primary": "linear-gradient(135deg, #ff6b35, #ffb703)",
        "gradient_accent": "linear-gradient(135deg, #ff3d71, #3b82f6)",
        "gradient_hero": "linear-gradient(135deg, rgba(255, 107, 53, 0.15), rgba(59, 130, 246, 0.12), rgba(255, 183, 3, 0.12))",
        
        # Glassmorphism
        "glass_bg": "rgba(255, 255, 255, 0.7)",
        "glass_blur": "20px",
        "glass_border": "rgba(255, 255, 255, 0.3)",
    }


def _get_dark_theme() -> Dict[str, str]:
    """Tema oscuro con identidad vibrante."""
    return {
        # Colores principales
        "primary": "#ff6b35",
        "secondary": "#ffb703",
        "accent": "#ff3d71",
        "accent_2": "#22c55e",
        "accent_3": "#3b82f6",
        
        # Fondos
        "bg_main": "#07111f",
        "bg_card": "rgba(17, 24, 39, 0.86)",
        "bg_sidebar": "rgba(15, 23, 42, 0.94)",
        
        # Texto
        "text_main": "#f8fafc",
        "text_muted": "#cbd5e1",
        
        # Bordes y sombras
        "border": "rgba(255, 255, 255, 0.14)",
        "shadow": "rgba(15, 23, 42, 0.35)",
        
        # Tipografía
        "font_primary": "'Fira Code', 'JetBrains Mono', 'IBM Plex Mono', monospace",
        "font_size_base": "16px",
        
        # Gradientes
        "gradient_primary": "linear-gradient(135deg, #ff6b35, #ffb703)",
        "gradient_accent": "linear-gradient(135deg, #ff3d71, #3b82f6)",
        "gradient_hero": "linear-gradient(135deg, rgba(255, 107, 53, 0.22), rgba(59, 130, 246, 0.16), rgba(255, 183, 3, 0.16))",
        
        # Glassmorphism
        "glass_bg": "rgba(17, 24, 39, 0.7)",
        "glass_blur": "18px",
        "glass_border": "rgba(255, 255, 255, 0.12)",
    }


def get_css_variables(theme: Dict[str, str]) -> str:
    """
    Genera las variables CSS desde la configuración del tema.
    
    Args:
        theme: Configuración del tema
        
    Returns:
        String con las variables CSS formateadas
    """
    return f"""
    :root {{
        --primary: {theme['primary']};
        --secondary: {theme['secondary']};
        --accent: {theme['accent']};
        --accent-2: {theme['accent_2']};
        --accent-3: {theme['accent_3']};
        --bg-main: {theme['bg_main']};
        --bg-card: {theme['bg_card']};
        --bg-sidebar: {theme['bg_sidebar']};
        --text-main: {theme['text_main']};
        --text-muted: {theme['text_muted']};
        --border: {theme['border']};
        --shadow: {theme['shadow']};
        --font-primary: {theme['font_primary']};
        --font-size-base: {theme['font_size_base']};
        --gradient-primary: {theme['gradient_primary']};
        --gradient-accent: {theme['gradient_accent']};
        --gradient-hero: {theme['gradient_hero']};
        --glass-bg: {theme['glass_bg']};
        --glass-blur: {theme['glass_blur']};
        --glass-border: {theme['glass_border']};
    }}
"""


def get_streamlit_theme_config(mode: str = "dark") -> Dict[str, str]:
    """
    Retorna configuración compatible con Streamlit theme config.
    
    Args:
        mode: "dark" o "light"
        
    Returns:
        Diccionario con configuración de tema de Streamlit
    """
    theme = get_theme_config(mode)
    
    return {
        "primaryColor": theme["primary"],
        "secondaryColor": theme["secondary"],
        "accentColor": theme["accent"],
        "accentColor2": theme["accent_2"],
        "accentColor3": theme["accent_3"],
        "backgroundColor": theme["bg_main"],
        "secondaryBackgroundColor": theme["bg_card"],
        "textColor": theme["text_main"],
        "textMuted": theme["text_muted"],
        "borderColor": theme["border"],
        "shadowColor": theme["shadow"],
        "font": theme["font_primary"],
    }
