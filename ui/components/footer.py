import streamlit as st
from datetime import datetime


APP_NAME = "Santos Pegasus AI"
VERSION = "v2.0.0"


def render_footer():
    """
    Footer principal de la aplicación.
    """

    current_year = datetime.now().year

    st.markdown("---")

    col1, col2, col3 = st.columns([2, 3, 2])

    with col1:
        st.caption(f"🤖 **{APP_NAME}**")

    with col2:
        st.caption(
            "⚡ Gemini 2.5 Flash • FastAPI • FAISS • Streamlit"
        )

    with col3:
        st.caption(f"© {current_year}")

    st.caption(
        f"""
Versión **{VERSION}**

Desarrollado con ❤️ por **Orli Dun**
"""
    )


# =====================================================
# FOOTER MINIMAL
# =====================================================

def render_minimal_footer():
    """
    Footer compacto para pantallas pequeñas.
    """

    st.markdown("---")

    st.caption(
        "🤖 Santos Pegasus AI • Gemini 2.5 Flash • FastAPI • FAISS"
    )


# =====================================================
# FOOTER STATUS
# =====================================================

def render_status_bar():

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🟢 API")

    with c2:
        st.success("📚 FAISS")

    with c3:
        st.success("🤖 Gemini")

