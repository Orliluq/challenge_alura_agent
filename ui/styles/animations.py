from typing import Dict


def get_animations_css() -> str:

    return """
    /* ============================================
       ANIMACIONES PRINCIPALES
       ============================================ */
    
    @keyframes drift {
        0% {
            transform: translate3d(0, 0, 0) scale(1);
        }
        100% {
            transform: translate3d(40px, 24px, 0) scale(1.08);
        }
    }
    
    @keyframes shimmer {
        0% {
            transform: translateX(-120%);
        }
        100% {
            transform: translateX(120%);
        }
    }
    
    @keyframes bounceIn {
        0% {
            transform: translateY(10px) scale(0.98);
            opacity: 0;
        }
        60% {
            transform: translateY(-4px) scale(1.01);
            opacity: 1;
        }
        100% {
            transform: translateY(0) scale(1);
            opacity: 1;
        }
    }
    
    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
    
    @keyframes slideUp {
        0% {
            transform: translateY(20px);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    @keyframes glow {
        0%, 100% {
            box-shadow: 0 0 20px rgba(255, 107, 53, 0.3);
        }
        50% {
            box-shadow: 0 0 30px rgba(255, 107, 53, 0.5);
        }
    }
    
    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
    
    @keyframes typewriter {
        0% {
            width: 0;
        }
        100% {
            width: 100%;
        }
    }
    
    @keyframes blink {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0;
        }
    }
"""


def get_background_animations() -> str:

    return """
    /* ============================================
       ANIMACIONES DE FONDO
       ============================================ */
    
    .stApp::before,
    .stApp::after {
        content: "";
        position: fixed;
        width: 280px;
        height: 280px;
        border-radius: 50%;
        z-index: 0;
        filter: blur(30px);
        opacity: 0.6;
        pointer-events: none;
        animation: drift 14s ease-in-out infinite alternate;
    }
    
    .stApp::before {
        top: -80px;
        left: -60px;
        background: rgba(255, 107, 53, 0.28);
    }
    
    .stApp::after {
        right: -70px;
        bottom: 40px;
        background: rgba(59, 130, 246, 0.24);
        animation-duration: 18s;
    }
"""


def get_animation_classes() -> str:

    return """
    /* ============================================
       CLASES DE ANIMACIÓN
       ============================================ */
    
    .animate-fade-in {
        animation: fadeIn 0.3s ease-out;
    }
    
    .animate-slide-up {
        animation: slideUp 0.4s ease-out;
    }
    
    .animate-bounce-in {
        animation: bounceIn 0.45s ease both;
    }
    
    .animate-pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    .animate-float {
        animation: float 3s ease-in-out infinite;
    }
    
    .animate-glow {
        animation: glow 2s ease-in-out infinite;
    }
    
    .animate-shimmer {
        position: relative;
        overflow: hidden;
    }
    
    .animate-shimmer::before {
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
    }
"""


def get_transition_classes() -> str:

    return """
    /* ============================================
       TRANSICIONES
       ============================================ */
    
    .transition-smooth {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .transition-fast {
        transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .transition-slow {
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .transition-transform {
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .transition-opacity {
        transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .transition-colors {
        transition: color 0.3s cubic-bezier(0.4, 0, 0.2, 1),
                    background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1),
                    border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .transition-shadow {
        transition: box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
"""


def get_hover_effects() -> str:

    return """
    /* ============================================
       EFECTOS HOVER
       ============================================ */
    
    .hover-lift {
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1),
                    box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .hover-lift:hover {
        transform: translateY(-3px);
        box-shadow: 0 16px 36px rgba(2, 6, 23, 0.24);
    }
    
    .hover-scale {
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .hover-scale:hover {
        transform: scale(1.02);
    }
    
    .hover-glow {
        transition: box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .hover-glow:hover {
        box-shadow: 0 0 30px rgba(255, 107, 53, 0.4);
    }
    
    .hover-brightness {
        transition: filter 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .hover-brightness:hover {
        filter: brightness(1.1);
    }
"""


def get_loading_states() -> str:

    return """
    /* ============================================
       ESTADOS DE CARGA
       ============================================ */
    
    .skeleton {
        background: linear-gradient(
            90deg,
            var(--bg-card) 0%,
            rgba(255, 255, 255, 0.1) 50%,
            var(--bg-card) 100%
        );
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite;
        border-radius: 8px;
    }
    
    .skeleton-text {
        height: 1em;
        margin-bottom: 0.5em;
    }
    
    .skeleton-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
    }
    
    .skeleton-card {
        height: 120px;
    }
    
    .loading-dots::after {
        content: "...";
        animation: blink 1s steps(4, end) infinite;
    }
"""


def get_responsive_animations() -> str:

    return """
    /* ============================================
       ANIMACIONES RESPONSIVAS
       ============================================ */
    
    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
        }
    }
    
    @media (max-width: 768px) {
        .animate-bounce-in {
            animation-duration: 0.3s;
        }
        
        .animate-slide-up {
            animation-duration: 0.3s;
        }
        
        .hover-lift:hover {
            transform: translateY(-2px);
        }
    }
"""
