import streamlit as st
from datetime import datetime


APP_NAME = "Santos Pegasus AI Agent"
VERSION = "v2.0.0"


def render_footer():
    """
    Footer principal de la aplicación.
    """

    current_year = datetime.now().year

    st.markdown("---")

    # _, col2, _ = st.columns([3, 2, 3])

    with st.container():
        st.caption(
            f"© {current_year} **{APP_NAME}** Desarrollado con ❤️ por **Orli Dun**"
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
        f"© {current_year} Desarrollado con ❤️ por **Orli Dun**"
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

