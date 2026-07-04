import requests
import time
from typing import Dict, List, Optional

API_URL = "http://127.0.0.1:8000/ask"


class APIClient:
    """Cliente para comunicarse con la API FastAPI"""
    
    def __init__(self, base_url: str = API_URL):
        self.base_url = base_url
    
    def ask_question(self, question: str, timeout: int = 120) -> Dict:
        """
        Envía una pregunta al endpoint /ask
        
        Args:
            question: La pregunta a realizar
            timeout: Tiempo máximo de espera en segundos
            
        Returns:
            Dict con la respuesta de la API
        """
        start_time = time.time()
        
        try:
            response = requests.post(
                self.base_url,
                json={"question": question},
                timeout=timeout
            )
            response.raise_for_status()
            
            data = response.json()
            elapsed_time = time.time() - start_time
            
            return {
                "success": True,
                "answer": data.get("answer", "Sin respuesta."),
                "sources": data.get("sources", []),
                "question": data.get("question", question),
                "elapsed_time": elapsed_time
            }
            
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "answer": "Error: Tiempo de espera agotado. El servidor tardó demasiado en responder.",
                "sources": [],
                "question": question,
                "elapsed_time": time.time() - start_time
            }
            
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "answer": "Error: No se pudo conectar con el servidor. Asegúrate de que uvicorn esté corriendo.",
                "sources": [],
                "question": question,
                "elapsed_time": time.time() - start_time
            }
            
        except Exception as e:
            return {
                "success": False,
                "answer": f"Error: {str(e)}",
                "sources": [],
                "question": question,
                "elapsed_time": time.time() - start_time
            }


class MetricsTracker:
    """Rastrea métricas de uso de la aplicación"""
    
    def __init__(self):
        self.total_questions = 0
        self.total_documents = 0
        self.response_times = []
    
    def add_question(self, response_time: float, num_sources: int):
        """Registra una pregunta con sus métricas"""
        self.total_questions += 1
        self.total_documents = max(self.total_documents, num_sources)
        self.response_times.append(response_time)
    
    def get_average_time(self) -> float:
        """Calcula el tiempo promedio de respuesta"""
        if not self.response_times:
            return 0.0
        return sum(self.response_times) / len(self.response_times)
    
    def get_stats(self) -> Dict:
        """Retorna todas las estadísticas"""
        return {
            "total_questions": self.total_questions,
            "total_documents": self.total_documents,
            "average_time": self.get_average_time()
        }
    
    def reset(self):
        """Reinicia las métricas"""
        self.total_questions = 0
        self.total_documents = 0
        self.response_times = []
