# Estilos CSS para Streamlit - Tema Oscuro Santos Pegasus

STYLES = """
<style>
    /* Colores principales - Identidad Santos Pegasus */
    :root {
        --primary-color: #7B61FF;
        --secondary-color: #A855F7;
        --accent-color: #00D9B6;
        --bg-dark: #0F1419;
        --bg-card: #1A1F26;
        --text-primary: #E0E0E0;
        --text-secondary: #B0B0B0;
        --border-color: #2D3748;
    }
    
    /* Fondo principal */
    .stApp {
        background-color: var(--bg-dark);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: var(--bg-card);
        border-right: 1px solid var(--border-color);
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: var(--text-primary) !important;
        font-weight: 600;
    }
    
    /* Chat messages */
    .stChatMessage {
        background-color: var(--bg-card);
        border-radius: 12px;
        padding: 16px;
        margin: 8px 0;
    }
    
    /* User message */
    [data-testid="stChatMessage"] [data-testid="chatAvatar"] {
        background-color: var(--primary-color);
    }
    
    /* Assistant message */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: #252B36;
    }
    
    /* Input field */
    .stChatInput {
        background-color: var(--bg-card);
        border: 1px solid var(--border-color);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(
        135deg,
        #7B61FF,
        #A855F7
    );
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 500;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background-color: var(--secondary-color);
        transform: translateY(-1px);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 8px;
    }
    
    /* Metrics cards */
    [data-testid="stMetricValue"] {
        color: var(--accent-color);
        font-size: 2rem;
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary);
        font-size: 0.9rem;
    }
    
    /* Divider */
    hr {
        border-color: var(--border-color);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--border-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary-color);
    }
    
    /* ============================================
       RESPONSIVE DESIGN - MEDIA QUERIES
       ============================================ */
    
    /* Mobile (375px - 767px) */
    @media (max-width: 767px) {
        /* Sidebar colapsada en móvil */
        [data-testid="stSidebar"] {
            width: 100% !important;
            max-width: 100% !important;
        }
        
        /* Ajustar métricas para móvil */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.8rem !important;
        }
        
        /* Chat messages más compactos */
        .stChatMessage {
            padding: 12px !important;
            margin: 4px 0 !important;
        }
        
        /* Botones más pequeños */
        .stButton > button {
            padding: 6px 12px !important;
            font-size: 0.9rem !important;
        }
        
        /* Títulos más pequeños */
        h1 {
            font-size: 1.5rem !important;
        }
        
        h2 {
            font-size: 1.2rem !important;
        }
        
        h3 {
            font-size: 1rem !important;
        }
        
        /* Input field */
        .stChatInput {
            font-size: 0.9rem !important;
        }
        
        /* Expander header */
        .streamlit-expanderHeader {
            font-size: 0.9rem !important;
        }
    }
    
    /* Tablet (768px - 1023px) */
    @media (min-width: 768px) and (max-width: 1023px) {
        /* Sidebar más estrecha */
        [data-testid="stSidebar"] {
            width: 280px !important;
        }
        
        /* Métricas ajustadas */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
        }
        
        /* Chat messages */
        .stChatMessage {
            padding: 14px !important;
        }
    }
    
    /* Desktop (1024px+) */
    @media (min-width: 1024px) {
        /* Sidebar completa */
        [data-testid="stSidebar"] {
            width: 350px !important;
        }
        
        /* Chat messages con más espacio */
        .stChatMessage {
            padding: 16px !important;
            max-width: 800px;
        }
    }
    
    /* Large Desktop (1440px+) */
    @media (min-width: 1440px) {
        .stChatMessage {
            max-width: 900px;
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2.5rem !important;
        }
    }
    
    /* Orientación landscape en móvil */
    @media (max-width: 767px) and (orientation: landscape) {
        [data-testid="stSidebar"] {
            height: auto !important;
            max-height: 40vh !important;
        }
    }
    
    /* High DPI displays */
    @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
        /* Mejorar renderizado de texto */
        h1, h2, h3, p {
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
    }
    
    /* Dark mode preference */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-dark: #0F1419;
            --bg-card: #1A1F26;
        }
    }
    
    /* Reduced motion preference */
    @media (prefers-reduced-motion: reduce) {
        .stButton > button {
            transition: none !important;
        }
        
        .stChatMessage {
            transition: none !important;
        }
    }
</style>
"""


def apply_custom_styles():
    """Aplica los estilos personalizados a la aplicación"""
    import streamlit as st
    st.markdown(STYLES, unsafe_allow_html=True)


def get_custom_theme():
    """Retorna la configuración del tema personalizado"""
    return {
        "primaryColor": "#7B61FF",
        "backgroundColor": "#0F1419",
        "secondaryBackgroundColor": "#1A1F26",
        "textColor": "#E0E0E0",
        "font": "sans serif"
    }
