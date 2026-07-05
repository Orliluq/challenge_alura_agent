"""
Sistema de iconos para Santos Pegasus AI.

Utiliza emojis nativos para máxima compatibilidad con Streamlit.
Sin SVG incrustados, sin dependencias externas.
"""

from typing import Dict


class Icons:
    """
    Clase centralizada para todos los iconos de la aplicación.
    
    Usa emojis nativos para:
    - Máxima compatibilidad con Streamlit
    - Sin dependencias externas
    - Rendimiento óptimo
    - Consistencia visual
    """
    
    # ============================================
    # ICONOS PRINCIPALES
    # ============================================
    
    APP = "🤖"
    SPARKLES = "✨"
    ROBOT = "🤖"
    BRAIN = "🧠"
    AI = "🤖"
    
    # ============================================
    # DOCUMENTOS Y ARCHIVOS
    # ============================================
    
    DOCUMENT = "📄"
    FILE = "📁"
    FOLDER = "📂"
    BOOK = "📚"
    PAGE = "📝"
    CLIPBOARD = "📋"
    
    # ============================================
    # ACCIONES
    # ============================================
    
    SEND = "📤"
    DOWNLOAD = "⬇️"
    UPLOAD = "⬆️"
    TRASH = "🗑️"
    COPY = "📋"
    PASTE = "📌"
    EDIT = "✏️"
    SAVE = "💾"
    SHARE = "🔗"
    
    # ============================================
    # NAVEGACIÓN
    # ============================================
    
    HOME = "🏠"
    MENU = "☰"
    SETTINGS = "⚙️"
    SEARCH = "🔍"
    FILTER = "🔎"
    BACK = "⬅️"
    FORWARD = "➡️"
    
    # ============================================
    # ESTADO Y FEEDBACK
    # ============================================
    
    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ℹ️"
    QUESTION = "❓"
    LOADING = "⏳"
    
    THUMBS_UP = "👍"
    THUMBS_DOWN = "👎"
    HEART = "❤️"
    STAR = "⭐"
    FIRE = "🔥"
    
    # ============================================
    # TEMA Y APARIENCIA
    # ============================================
    
    SUN = "☀️"
    MOON = "🌙"
    PALETTE = "🎨"
    EYE = "👁️"
    
    # ============================================
    # TECNOLOGÍA
    # ============================================
    
    CODE = "💻"
    TERMINAL = "⌨️"
    DATABASE = "🗄️"
    SERVER = "🖥️"
    CLOUD = "☁️"
    WIFI = "📶"
    BOLT = "⚡"
    GEAR = "⚙️"
    CHIP = "💾"
    
    # ============================================
    # MÉTRICAS Y DATOS
    # ============================================
    
    CHART = "📊"
    GRAPH = "📈"
    TREND = "📉"
    ANALYTICS = "📊"
    STATISTICS = "📊"
    
    # ============================================
    # COMUNICACIÓN
    # ============================================
    
    MESSAGE = "💬"
    CHAT = "💬"
    EMAIL = "📧"
    NOTIFICATION = "🔔"
    BELL = "🔔"
    
    # ============================================
    # USUARIO
    # ============================================
    
    USER = "👤"
    USERS = "👥"
    PROFILE = "👤"
    ACCOUNT = "👤"
    LOGIN = "🔑"
    LOGOUT = "🚪"
    
    # ============================================
    # SISTEMA
    # ============================================
    
    POWER = "🔌"
    REFRESH = "🔄"
    SYNC = "🔄"
    UPDATE = "🆕"
    VERSION = "🏷️"
    
    # ============================================
    # SEGURIDAD
    # ============================================
    
    LOCK = "🔒"
    UNLOCK = "🔓"
    SHIELD = "🛡️"
    KEY = "🔑"
    
    # ============================================
    # TIEMPO
    # ============================================
    
    CLOCK = "🕐"
    TIMER = "⏱️"
    CALENDAR = "📅"
    SCHEDULE = "📅"
    
    # ============================================
    # UBICACIÓN
    # ============================================
    
    LOCATION = "📍"
    MAP = "🗺️"
    PIN = "📍"
    
    # ============================================
    # HERRAMIENTAS
    # ============================================
    
    TOOLS = "🛠️"
    WRENCH = "🔧"
    HAMMER = "🔨"
    SCREWDRIVER = "🪛"
    
    # ============================================
    # MÁS
    # ============================================
    
    PLUS = "➕"
    MINUS = "➖"
    CLOSE = "✖️"
    CHECK = "✔️"
    CROSS = "❌"
    DOTS = "⋯"
    MORE = "⋯"
    
    EXTERNAL = "↗️"
    LINK = "🔗"
    NEW_TAB = "🔗"


def get_icon(name: str) -> str:
    """
    Retorna un icono por su nombre.
    
    Args:
        name: Nombre del icono (ej: "APP", "DOCUMENT", "SUCCESS")
        
    Returns:
        Emoji correspondiente al icono solicitado
    """
    return getattr(Icons, name.upper(), Icons.APP)


def get_status_icon(status: str) -> str:
    """
    Retorna un icono basado en el estado.
    
    Args:
        status: Estado ("success", "error", "warning", "info", "loading")
        
    Returns:
        Emoji correspondiente al estado
    """
    status_icons = {
        "success": Icons.SUCCESS,
        "error": Icons.ERROR,
        "warning": Icons.WARNING,
        "info": Icons.INFO,
        "loading": Icons.LOADING,
    }
    
    return status_icons.get(status.lower(), Icons.INFO)


def get_theme_icon(theme: str) -> str:
    """
    Retorna el icono del tema.
    
    Args:
        theme: "dark" o "light"
        
    Returns:
        Icono del tema (sol o luna)
    """
    return Icons.SUN if theme == "light" else Icons.MOON


# ============================================
# ICONOS ESPECÍFICOS DE LA APLICACIÓN
# ============================================

class AppIcons:
    """
    Iconos específicos para Santos Pegasus AI.
    """
    
    # Branding
    LOGO = "🤖"
    BRAND = "🦄"
    
    # Features
    RAG = "✨"
    GEMINI = "🧠"
    FASTAPI = "⚡"
    FAISS = "📚"
    STREAMLIT = "💬"
    
    # Actions
    NEW_CHAT = "🧹"
    EXPORT_MD = "📄"
    EXPORT_PDF = "📑"
    CLEAR = "🗑️"
    
    # Metrics
    QUESTIONS = "💬"
    DOCUMENTS = "📚"
    TIME = "⏱️"
    
    # System
    API = "🟢"
    MODEL = "🤖"
    VECTOR_DB = "📚"
    BACKEND = "⚡"
