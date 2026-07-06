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
*Exportado desde Santos Pegasus AI Agent*
*Generado automáticamente el {timestamp}*
"""
    
    return markdown


def export_to_pdf(messages: List[Dict]) -> str:

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

    markdown_content = export_to_markdown(messages)
    
    st.code(
        markdown_content,
        language="markdown",
        label="Contenido para copiar"
    )
    
    st.info("💡 Copia el contenido de arriba y pégalo donde necesites")


def format_source_with_metadata(source: str, metadata: Dict = None) -> str:

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
