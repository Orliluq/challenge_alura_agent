from typing import Dict


def get_base_css() -> str:
  
    return """
    /* ============================================
       FUENTES - Fira Code
       ============================================ */
    
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap');
    
    /* ============================================
       BASE Y RESET
       ============================================ */
    
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    body {
        font-family: var(--font-primary);
        font-size: var(--font-size-base);
        line-height: 1.6;
        color: var(--text-main);
        background: var(--bg-main);
    }
    
    .stApp {
        background: var(--bg-main);
        color: var(--text-main);
        color: var(--text-main);
        position: relative;
        overflow-x: hidden;
        min-height: 100vh;
    }

    /* Header de Streamlit */
    .stAppHeader {
        background: var(--bg-main) !important;
        border-bottom: 1px solid var(--border) !important;
    }
 
    .stDecoration {
        background: var(--bg-main) !important;
    }

    /* Chat input de Streamlit */
    .stChatInput {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
    }
 
    .stChatInput textarea {
        background: transparent !important;
        color: var(--text-main) !important;
    }
 
    .stChatInput button {
        background: var(--primary) !important;
        color: white !important;
    }
    
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    h1, h2, h3, h4, h5, h6,
    p, label, div, span {
        color: var(--text-main) !important;
    }
"""


def get_sidebar_css() -> str:

    return """
    /* ============================================
       SIDEBAR
       ============================================ */
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--bg-sidebar), var(--bg-card));
        border-right: 1px solid var(--border);
        backdrop-filter: blur(var(--glass-blur));
    }
    
    .sidebar-hero {
        padding: 0.9rem;
        margin-bottom: 0.8rem;
        border-radius: 18px;
        background: var(--gradient-hero);
        border: 1px solid var(--glass-border);
    }
    
    .sidebar-hero h3 {
        margin: 0 0 0.2rem 0;
        font-size: 1rem;
        font-weight: 700;
    }
    
    .sidebar-hero p {
        margin: 0;
        color: var(--text-muted) !important;
        font-size: 0.9rem;
    }
    
    .theme-switch {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.45rem 0.7rem;
        border-radius: 999px;
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        margin-bottom: 0.9rem;
        font-size: 0.9rem;
    }
"""


def get_hero_css() -> str:

    return """
    /* ============================================
       HERO / HEADER
       ============================================ */
    
    .hero-shell {
        margin: 0 0 1.2rem 0;
        padding: 1.2rem 1.3rem;
        border: 1px solid var(--border);
        border-radius: 24px;
        background: var(--gradient-hero);
        box-shadow: 0 18px 45px var(--shadow);
        backdrop-filter: blur(var(--glass-blur));
        position: relative;
        overflow: hidden;
        isolation: isolate;
    }
    
    .hero-shell::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(
            110deg,
            transparent 20%,
            rgba(255, 255, 255, 0.18) 50%,
            transparent 80%
        );
        transform: translateX(-120%);
        animation: shimmer 5.2s ease-in-out infinite;
        z-index: -1;
    }
    
    .hero-top {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        flex-wrap: wrap;
    }
    
    .hero-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 48px;
        height: 48px;
        border-radius: 16px;
        background: var(--gradient-primary);
        box-shadow: 0 10px 25px rgba(255, 107, 53, 0.35);
    }
    
    .hero-shell h1 {
        margin: 0 0 0.25rem 0;
        font-size: clamp(1.5rem, 2vw, 2.2rem);
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    
    .hero-shell p {
        margin: 0;
        color: var(--text-muted) !important;
        font-size: 0.98rem;
        line-height: 1.55;
    }
    
    .hero-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 0.9rem;
    }
    
    .hero-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 0.5rem 0.75rem;
        border-radius: 999px;
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        font-size: 0.84rem;
        color: var(--text-main) !important;
        transition: all 0.3s ease;
    }
    
    .hero-pill:hover {
        background: var(--bg-card);
        transform: translateY(-2px);
    }

"""


def get_dashboard_css() -> str:

    return """
    /* ============================================
       DASHBOARD Y CARDS
       ============================================ */
    
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.8rem;
        margin: 0 0 1rem 0;
    }
    
    .dashboard-card {
        padding: 0.95rem 1rem;
        border-radius: 18px;
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        box-shadow: 0 12px 30px var(--shadow);
        backdrop-filter: blur(var(--glass-blur));
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }
    
    .dashboard-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 16px 36px var(--shadow);
    }
    
    .dashboard-card h4 {
        margin: 0 0 0.25rem 0;
        font-size: 0.95rem;
        color: var(--text-main) !important;
        font-weight: 700;
    }
    
    .dashboard-card p {
        margin: 0;
        font-size: 0.86rem;
        color: var(--text-muted) !important;
        line-height: 1.45;
    }
    
    .dashboard-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 48px;
        height: 48px;
        border-radius: 12px;
        font-size: 1.5rem;
    }
    
    .dashboard-title {
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.25rem;
    }
    
    .dashboard-value {
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }
    
    .dashboard-subtitle {
        font-size: 0.85rem;
        color: var(--text-muted) !important;
    }
    
    .status-chip {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 0.75rem;
        border-radius: 999px;
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
    }
    
    .status-emoji {
        font-size: 1.2rem;
    }
    
    .status-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--text-muted) !important;
    }
    
    .status-value {
        font-size: 0.9rem;
        font-weight: 700;
    }
"""


def get_chat_css() -> str:

    return """
    /* ============================================
       CHAT
       ============================================ */
    
    .stChatMessage {
        background: linear-gradient(135deg, var(--glass-bg), rgba(255, 255, 255, 0.04));
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 0.95rem 1rem;
        margin: 0.7rem 0;
        box-shadow: 0 16px 38px var(--shadow);
        backdrop-filter: blur(var(--glass-blur));
        animation: bounceIn 0.45s ease both;
    }
    
    [data-testid="stChatMessage"] [data-testid="chatAvatar"] {
        background: var(--gradient-primary);
        border: none;
    }
    
    .stChatInput {
        border: 1px solid var(--border);
        border-radius: 16px;
        background: var(--glass-bg);
        box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.04);
    }
    
    .stChatInput textarea {
        color: var(--text-main) !important;
    }
    
    .streamlit-expanderHeader {
        border-radius: 12px;
        border: 1px solid var(--border);
        background: var(--glass-bg);
    }
"""


def get_buttons_css() -> str:

    return """
    /* ============================================
       BOTONES
       ============================================ */
    
    .stButton > button,
    .stButton button,
    .stButton > button:hover,
    .stButton > button:focus,
    .stButton > button:active {
        border: none !important;
        border-radius: 999px !important;
        background: var(--gradient-primary) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        padding: 0.65rem 1rem !important;
        transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease !important;
        box-shadow: 0 10px 24px rgba(255, 107, 53, 0.28) !important;
    }
    
    .stButton > button:hover,
    .stButton button:hover,
    .stButton > button:focus,
    .stButton button:focus {
        transform: translateY(-2px) !important;
        background: linear-gradient(135deg, #ff8a53, #ff3d71) !important;
        box-shadow: 0 16px 34px rgba(255, 77, 124, 0.32) !important;
        color: #ffffff !important;
    }
    
    .stButton > button:active,
    .stButton button:active {
        transform: translateY(0) !important;
        box-shadow: 0 8px 20px rgba(255, 77, 124, 0.22) !important;
    }
    
    .stButton > button[disabled],
    .stButton button[disabled] {
        opacity: 0.72 !important;
        cursor: not-allowed !important;
    }
"""


def get_metrics_css() -> str:
 
    return """
    /* ============================================
       MÉTRICAS
       ============================================ */
    
    [data-testid="stMetricValue"] {
        color: var(--secondary) !important;
        font-size: 1.8rem;
        font-weight: 800;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: 0.85rem;
    }
"""


def get_footer_css() -> str:
   
    return """
    /* ============================================
       FOOTER
       ============================================ */
    
    .footer-card {
        margin-top: 1.3rem;
        padding: 0.8rem 1rem;
        text-align: center;
        border-radius: 16px;
        background: var(--glass-bg);
        border: 1px solid var(--border);
        color: var(--text-muted) !important;
        font-size: 0.9rem;
        box-shadow: 0 10px 24px var(--shadow);
    }
    
    .floating-actions {
        position: fixed;
        right: 1.2rem;
        bottom: 1.2rem;
        display: flex;
        flex-direction: row;
        gap: 0.6rem;
        z-index: 999;
    }
    
    .floating-actions button {
        border-radius: 999px !important;
        width: 40px !important;
        height: 40px !important;
        box-shadow: 0 10px 26px rgba(255, 107, 53, 0.28) !important;
    }
"""


def get_scrollbar_css() -> str:

    return """
    /* ============================================
       SCROLLBARS
       ============================================ */
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.04);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--gradient-primary);
        border-radius: 999px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #ff8a53, #ff3d71);
    }
"""


def get_utilities_css() -> str:
 
    return """
    /* ============================================
       UTILIDADES
       ============================================ */
    
    hr {
        border-color: var(--border);
    }
    
    .welcome-card {
        padding: 2rem;
        border-radius: 20px;
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        margin-bottom: 1.5rem;
    }
    
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(var(--glass-blur));
        border: 1px solid var(--glass-border);
        border-radius: 16px;
    }
    
    .gradient-border {
        position: relative;
        background: var(--glass-bg);
        border-radius: 16px;
    }
    
    .gradient-border::before {
        content: "";
        position: absolute;
        inset: -2px;
        background: var(--gradient-primary);
        border-radius: 18px;
        z-index: -1;
    }
"""


def get_responsive_css() -> str:

    return """
    /* ============================================
       RESPONSIVE
       ============================================ */
    
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 0.9rem;
            padding-right: 0.9rem;
        }
        
        .hero-shell {
            padding: 1rem;
            border-radius: 18px;
        }
        
        .hero-shell h1 {
            font-size: 1.35rem;
        }
        
        .stChatMessage {
            padding: 0.8rem;
            margin: 0.45rem 0;
        }
        
        [data-testid="stMetricValue"] {
            font-size: 1.45rem !important;
        }
        
        .dashboard-grid {
            grid-template-columns: 1fr;
        }
        
        .floating-actions {
            right: 0.8rem;
            bottom: 0.8rem;
        }
        
        .hero-pills {
            gap: 0.4rem;
        }
        
        .hero-pill {
            font-size: 0.76rem;
            padding: 0.4rem 0.6rem;
        }
    }
    
    @media (max-width: 480px) {
        .hero-shell h1 {
            font-size: 1.2rem;
        }
        
        .dashboard-card {
            padding: 0.8rem;
        }
        
        .stChatMessage {
            padding: 0.7rem;
            border-radius: 16px;
        }
    }

    @media (max-width: 640px) {
        .floating-actions {
            flex-direction: column;
        }
    }
"""


def get_complete_css(theme: Dict[str, str]) -> str:
  
    from .theme import get_css_variables
    from .animations import (
        get_animations_css,
        get_background_animations,
        get_animation_classes,
        get_transition_classes,
        get_hover_effects,
        get_loading_states,
        get_responsive_animations
    )
    
    css_parts = [
        "<style>",
        get_css_variables(theme),
        get_base_css(),
        get_background_animations(),
        get_sidebar_css(),
        get_hero_css(),
        get_dashboard_css(),
        get_chat_css(),
        get_buttons_css(),
        get_metrics_css(),
        get_footer_css(),
        get_scrollbar_css(),
        get_utilities_css(),
        get_animations_css(),
        get_animation_classes(),
        get_transition_classes(),
        get_hover_effects(),
        get_loading_states(),
        get_responsive_css(),
        get_responsive_animations(),
        "</style>"
    ]
    
    return "\n".join(css_parts)