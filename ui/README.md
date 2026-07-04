# 🤖 Santos Pegasus AI - Interfaz Streamlit

Interfaz de usuario profesional para el asistente de IA basado en Gemini 2.5 Flash + RAG.

## 📁 Estructura de Archivos

```
ui/
├── streamlit_app.py      # Aplicación principal de Streamlit
├── components.py         # Componentes reutilizables de UI
├── styles.py            # Estilos CSS personalizados (tema oscuro)
├── export.py            # Funciones de exportación (Markdown/PDF)
├── utils.py             # Cliente API y tracker de métricas
└── __init__.py          # Paquete Python
```

## 🚀 Instalación

```bash
# Instalar dependencias
pip install streamlit requests

# O desde requirements.txt
pip install -r requirements.txt
```

## ▶️ Ejecutar la Aplicación

```bash
# Asegúrate de que el servidor FastAPI esté corriendo
uvicorn app.api:app --reload

# En otra terminal, ejecutar Streamlit
streamlit run ui/streamlit_app.py
```

## ✨ Características

### 💬 Chat Interactivo
- Interfaz tipo ChatGPT con `st.chat_message()`
- Historial de conversación persistente
- Feedback con botones 👍/👎

### 🎨 Tema Oscuro Profesional
- Identidad visual de Santos Pegasus
- Colores personalizados (#1E88E5, #1565C0, #42A5F5)
- Diseño responsive y moderno

### 📊 Barra Lateral con Métricas
- **Preguntas totales** - Contador de consultas
- **Documentos usados** - Número de fuentes consultadas
- **Tiempo medio** - Promedio de tiempo de respuesta

### 📚 Citas Enriquecidas
- Documentos fuente utilizados
- Metadatos de documentos (página, sección)
- Tiempo de respuesta por consulta

### 💾 Exportación
- **Markdown** - Exportar chat a formato .md
- **PDF** - Exportar formato para impresión
- **Portapapeles** - Copiar contenido directamente

### 🧩 Componentes Reutilizables
- `render_sidebar()` - Barra lateral con métricas
- `render_chat_message()` - Mensajes con feedback
- `render_header()` - Header personalizado
- `render_loading_spinner()` - Spinner de carga

## 🔧 Configuración

### API URL
Por defecto, la aplicación se conecta a `http://127.0.0.1:8000/ask`.

Para cambiar la URL, modifica `API_URL` en `ui/utils.py`:

```python
API_URL = "http://tu-api-url:8000/ask"
```

### Tema Personalizado
Los colores del tema se pueden modificar en `ui/styles.py`:

```python
:root {
    --primary-color: #1E88E5;
    --secondary-color: #1565C0;
    --accent-color: #42A5F5;
    --bg-dark: #0F1419;
    --bg-card: #1A1F26;
}
```

## 📦 Componentes

### APIClient (`utils.py`)
Cliente para comunicarse con la API FastAPI:
- Manejo de errores (timeout, conexión)
- Tiempo de respuesta tracking
- Parsing de respuestas

### MetricsTracker (`utils.py`)
Rastrea métricas de uso:
- Total de preguntas
- Documentos consultados
- Tiempo promedio de respuesta

### Export Functions (`export.py`)
Funciones de exportación:
- `export_to_markdown()` - Formato Markdown
- `export_to_pdf()` - Formato para impresión
- `download_markdown()` - Botón de descarga
- `download_pdf()` - Botón de descarga PDF

## 🎯 Uso

1. **Iniciar el servidor FastAPI:**
   ```bash
   uvicorn app.api:app --reload
   ```

2. **Iniciar Streamlit:**
   ```bash
   streamlit run ui/streamlit_app.py
   ```

3. **Abrir el navegador:**
   La aplicación se abrirá automáticamente en `http://localhost:8501`

4. **Hacer preguntas:**
   Escribe tu pregunta en el campo de chat y presiona Enter

5. **Ver resultados:**
   - Respuesta del asistente
   - Fuentes utilizadas
   - Tiempo de respuesta
   - Opciones de feedback

## 🛠️ Personalización

### Agregar Nuevas Métricas
En `ui/utils.py`, agrega métricas adicionales a `MetricsTracker`:

```python
class MetricsTracker:
    def __init__(self):
        self.total_questions = 0
        self.new_metric = 0  # Tu nueva métrica
```

### Modificar Estilos
Edita `ui/styles.py` para personalizar colores y diseño:

```python
STYLES = """
<style>
    /* Tu CSS personalizado */
</style>
"""
```

### Agregar Nuevas Exportaciones
En `ui/export.py`, agrega nuevas funciones de exportación:

```python
def export_to_json(messages: List[Dict]) -> str:
    # Tu lógica de exportación
    pass
```

## 📱 Responsive Design

La interfaz es completamente responsive y funciona en:
- Desktop (1920x1080+)
- Laptop (1366x768+)
- Tablet (768x1024+)
- Mobile (375x667+)

## 🔒 Seguridad

- Las llamadas a la API se hacen desde el cliente
- No se almacenan datos sensibles en el cliente
- Timeout configurado para evitar bloqueos

## 🐛 Troubleshooting

**Error de conexión con la API:**
- Asegúrate de que uvicorn esté corriendo
- Verifica que la URL en `utils.py` sea correcta
- Revisa el firewall/antivirus

**Estilos no se aplican:**
- Limpia el caché del navegador
- Verifica que `apply_custom_styles()` se llame en `streamlit_app.py`

**Exportación no funciona:**
- Verifica permisos de escritura
- Asegúrate de que haya mensajes para exportar
