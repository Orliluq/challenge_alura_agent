from typing import List, Dict
from datetime import datetime
import streamlit as st


def export_to_markdown(messages: List[Dict]) -> str:
    """
    Exporta el historial de chat a formato Markdown
    
    Args:
        messages: Lista de mensajes del chat
        
    Returns:
        String con el contenido en formato Markdown
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown = f"""# 🤖 Santos Pegasus AI - Chat Export

**Fecha:** {timestamp}
**Total de mensajes:** {len(messages)}

---

"""
    
    for i, message in enumerate(messages, 1):
        role_emoji = "👤" if message["role"] == "user" else "🤖"
        role_name = "Usuario" if message["role"] == "user" else "Asistente"
        
        markdown += f"## {role_emoji} {role_name} - Mensaje {i}\n\n"
        markdown += f"{message['content']}\n\n"
        
        if message["role"] == "assistant" and message.get("sources"):
            markdown += "**Fuentes utilizadas:**\n\n"
            for source in message["sources"]:
                markdown += f"- {source}\n"
            markdown += "\n"
        
        markdown += "---\n\n"
    
    markdown += f"""
*Exportado desde Santos Pegasus AI Assistant*
*Generado automáticamente el {timestamp}*
"""
    
    return markdown


def export_to_pdf(messages: List[Dict]) -> str:
    """
    Exporta el historial de chat a formato PDF (como Markdown para imprimir)
    
    Args:
        messages: Lista de mensajes del chat
        
    Returns:
        String con el contenido formateado para PDF
    """
    # Para PDF, usamos el mismo formato Markdown pero con estilos adicionales
    markdown = export_to_markdown(messages)
    
    # Agregar estilos CSS para impresión
    pdf_styles = """
<style>
    @media print {
        body { font-family: Arial, sans-serif; }
        h1 { color: #1E88E5; }
        h2 { color: #1565C0; border-bottom: 1px solid #ccc; }
        code { background-color: #f5f5f5; padding: 2px 4px; }
        pre { background-color: #f5f5f5; padding: 10px; overflow-x: auto; }
    }
</style>
"""
    
    return pdf_styles + markdown


def download_markdown(messages: List[Dict], filename: str = None):
    """
    Genera un botón de descarga para el archivo Markdown
    
    Args:
        messages: Lista de mensajes del chat
        filename: Nombre del archivo (opcional)
    """
    if not filename:
        filename = f"santos_pegasus_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    markdown_content = export_to_markdown(messages)
    
    st.download_button(
        label="📥 Descargar Markdown",
        data=markdown_content,
        file_name=filename,
        mime="text/markdown",
        use_container_width=True
    )


def download_pdf(messages: List[Dict], filename: str = None):
    """
    Genera un botón de descarga para el archivo PDF (como Markdown)
    
    Nota: Para PDF real, se necesitaría una librería como weasyprint o reportlab
    Por ahora, exportamos como Markdown formateado para impresión
    
    Args:
        messages: Lista de mensajes del chat
        filename: Nombre del archivo (opcional)
    """
    if not filename:
        filename = f"santos_pegasus_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    pdf_content = export_to_pdf(messages)
    
    st.download_button(
        label="📥 Descargar para imprimir (PDF)",
        data=pdf_content,
        file_name=filename,
        mime="text/markdown",
        use_container_width=True
    )


def copy_to_clipboard(messages: List[Dict]):
    """
    Copia el contenido del chat al portapapeles
    
    Args:
        messages: Lista de mensajes del chat
    """
    markdown_content = export_to_markdown(messages)
    
    st.code(
        markdown_content,
        language="markdown",
        label="Contenido para copiar"
    )
    
    st.info("💡 Copia el contenido de arriba y pégalo donde necesites")


def format_source_with_metadata(source: str, metadata: Dict = None) -> str:
    """
    Formatea una fuente con metadatos adicionales
    
    Args:
        source: Nombre del documento fuente
        metadata: Metadatos adicionales (página, sección, etc.)
        
    Returns:
        String formateado con la información completa
    """
    if metadata:
        page = metadata.get("page", "")
        section = metadata.get("section", "")
        
        if page and section:
            return f"{source} - Página {page}, {section}"
        elif page:
            return f"{source} - Página {page}"
        elif section:
            return f"{source} - {section}"
    
    return source
