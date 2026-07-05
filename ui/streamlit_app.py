import streamlit as st
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ui.utils import APIClient, MetricsTracker
from ui.components import (
    render_sidebar,
    render_chat_message,
    render_header,
    render_loading_spinner,
)
from ui.styles import (
    apply_custom_styles,
    get_custom_theme,
)
from ui.export import (
    download_markdown,
    download_pdf,
)

# ============================================
# CONFIGURACIÓN
# ============================================

st.set_page_config(
    page_title="Santos Pegasus AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar tema personalizado
theme = get_custom_theme()
st.config.set_option("theme.base", "dark")
st.config.set_option("theme.primaryColor", theme["primaryColor"])

# Aplicar estilos CSS
apply_custom_styles()

# ============================================
# ESTADO DE LA APLICACIÓN
# ============================================

# Detectar dispositivo móvil
def detect_mobile():
    """Detecta si el usuario está en un dispositivo móvil"""
    try:
        import streamlit as st
        width = st.session_state.get('sidebar_state', 'expanded')
        # Streamlit no tiene detección directa, usamos ancho de ventana
        return st.session_state.get('client_width', 1200) < 768
    except:
        return False

# Inicializar detección móvil
if 'is_mobile' not in st.session_state:
    st.session_state.is_mobile = detect_mobile()

# Inicializar estado de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Inicializar estado de feedback
if "feedback" not in st.session_state:
    st.session_state.feedback = {}

# Inicializar cliente API
if "api_client" not in st.session_state:
    st.session_state.api_client = APIClient()

# Inicializar tracker de métricas
if "metrics_tracker" not in st.session_state:
    st.session_state.metrics_tracker = MetricsTracker()

# ============================================
# CALLBACKS
# ============================================

def clear_chat():
    """Limpia el historial de chat"""
    st.session_state.messages = []
    st.session_state.feedback = {}
    st.session_state.metrics_tracker.reset()
    st.rerun()


def export_chat_markdown():
    """Exporta el chat a Markdown"""
    if st.session_state.messages:
        download_markdown(st.session_state.messages)
    else:
        st.warning("No hay mensajes para exportar")


def export_chat_pdf():
    """Exporta el chat a PDF (formato impresión)"""
    if st.session_state.messages:
        download_pdf(st.session_state.messages)
    else:
        st.warning("No hay mensajes para exportar")


# ============================================
# INTERFAZ PRINCIPAL
# ============================================

# Renderizar header
render_header()

# Renderizar sidebar con métricas
metrics = st.session_state.metrics_tracker.get_stats()
render_sidebar(
    metrics=metrics,
    on_clear_chat=clear_chat,
    on_export_markdown=export_chat_markdown,
    on_export_pdf=export_chat_pdf
)

# ============================================
# HISTORIAL DE CHAT
# ============================================

for i, message in enumerate(st.session_state.messages):
    render_chat_message(message, i, st.session_state.feedback)

# ============================================
# INPUT DE USUARIO
# ============================================

question = st.chat_input("💬 Escribe tu pregunta sobre Santos Pegasus Soluciones...")

if question:
    # Agregar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(question)
    
    # Generar respuesta del asistente
    with st.chat_message("assistant"):
        with st.spinner("🧠 Consultando documentos con Gemini 2.5 Flash..."):
            # Llamar a la API
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
            with st.expander("📚 Documentos utilizados"):
                for source in sources:
                    st.write("•", source)
            
            # Mostrar tiempo de respuesta
            st.caption(f"⏱️ Tiempo de respuesta: {elapsed_time:.2f}s")
    
    # Agregar respuesta al historial
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })
    
    # Rerun para actualizar la UI
    st.rerun()

# ============================================
# FOOTER
# ============================================

st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8rem;'>
    <strong>Santos Pegasus AI Assistant</strong> | 
    Powered by Gemini 2.5 Flash + RAG | 
    🚀 Construido con FastAPI + Streamlit | Desarrollado por Orli Dun 
</div>
""", unsafe_allow_html=True)
