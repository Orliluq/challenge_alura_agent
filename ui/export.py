from typing import List, Dict
from datetime import datetime
import streamlit as st
from io import BytesIO
from fpdf import FPDF


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


def export_to_pdf(messages: List[Dict]) -> bytes:
    """
    Exporta el historial de chat a formato PDF
    
    Args:
        messages: Lista de mensajes del chat
        
    Returns:
        Bytes del PDF generado
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Configurar fuente (usamos fuentes estándar de FPDF)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Santos Pegasus AI - Chat Export", 0, 1, "C")
    
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 8, f"Fecha: {timestamp}", 0, 1, "C")
    pdf.cell(0, 8, f"Total de mensajes: {len(messages)}", 0, 1, "C")
    pdf.ln(10)
    
    # Agregar mensajes
    for i, message in enumerate(messages, 1):
        role_name = "Usuario" if message["role"] == "user" else "Asistente"
        
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"{role_name} - Mensaje {i}", 0, 1)
        
        pdf.set_font("Arial", "", 10)
        # Dividir texto largo en múltiples líneas
        content = message['content']
        pdf.multi_cell(0, 7, content)
        
        if message["role"] == "assistant" and message.get("sources"):
            pdf.ln(5)
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 7, "Fuentes utilizadas:", 0, 1)
            pdf.set_font("Arial", "", 9)
            for source in message["sources"]:
                pdf.cell(0, 6, f"- {source}", 0, 1)
        
        pdf.ln(10)
    
    # Footer
    pdf.ln(10)
    pdf.set_font("Arial", "I", 8)
    pdf.cell(0, 5, "Exportado desde Santos Pegasus AI Agent", 0, 1, "C")
    pdf.cell(0, 5, f"Generado automaticamente el {timestamp}", 0, 1, "C")
    
    # Generar bytes
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    
    return pdf_bytes


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
        filename = f"santos_pegasus_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    pdf_bytes = export_to_pdf(messages)
    
    st.download_button(
        label="📥 Descargar PDF",
        data=pdf_bytes,
        file_name=filename,
        mime="application/pdf",
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
