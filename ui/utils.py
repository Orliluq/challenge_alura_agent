import os
import time
from typing import Dict

import requests

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/ask"
)


class APIClient:
    """Cliente para comunicarse con la API FastAPI."""

    def __init__(self, base_url: str = API_URL):
        self.base_url = base_url

    def ask_question(self, question: str, timeout: int = 120) -> Dict:
        """Envía una pregunta al endpoint /ask y devuelve la respuesta."""

        start_time = time.time()

        try:
            print("=" * 70)
            print("API URL:", self.base_url)
            print("Pregunta:", question)
            print("=" * 70)

            r = requests.post(
                self.base_url,
                json={"question": question},
                timeout=timeout
            )

            print("STATUS:", r.status_code)
            print("RESPUESTA:")
            print(r.text)
            print("=" * 70)

            r.raise_for_status()

            data = r.json()
            elapsed_time = time.time() - start_time

            return {
                "success": True,
                "question": data.get("question", question),
                "answer": data.get("answer", "Sin respuesta."),
                "sources": data.get("sources", []),
                "elapsed_time": elapsed_time
            }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "question": question,
                "answer": "⏱️ El servidor tardó demasiado en responder.",
                "sources": [],
                "elapsed_time": time.time() - start_time
            }

        except requests.exceptions.RequestException as e:
            print("ERROR REQUEST")
            print(e)

            if e.response is not None:
                print("STATUS:", e.response.status_code)
                print(e.response.text)

            return {
                "success": False,
                "question": question,
                "answer": f"Error del servidor:\n{e}",
                "sources": [],
                "elapsed_time": time.time() - start_time
            }

        except Exception as e:
            print("ERROR GENERAL")
            print(e)

            return {
                "success": False,
                "question": question,
                "answer": str(e),
                "sources": [],
                "elapsed_time": time.time() - start_time
            }


class MetricsTracker:
    """Rastrea métricas de uso de la aplicación."""

    def __init__(self):
        self.total_questions = 0
        self.total_documents = 0
        self.response_times = []

    def add_question(
        self,
        response_time: float,
        num_sources: int
    ):
        self.total_questions += 1
        self.total_documents += num_sources
        self.response_times.append(response_time)

    def get_average_time(self) -> float:

        if not self.response_times:
            return 0.0

        return sum(self.response_times) / len(self.response_times)

    def get_stats(self) -> Dict:

        return {
            "total_questions": self.total_questions,
            "total_documents": self.total_documents,
            "average_time": self.get_average_time()
        }

    def reset(self):

        self.total_questions = 0
        self.total_documents = 0
        self.response_times.clear()