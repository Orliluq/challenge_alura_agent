import time
from transformers import pipeline

print("Cargando modelo...")

inicio = time.time()

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=20,
    do_sample=False
)

print(f"Modelo cargado en {time.time()-inicio:.2f} segundos")

print("Generando...")

inicio = time.time()

respuesta = pipe("Hola")

print(f"Generado en {time.time()-inicio:.2f} segundos")

print(respuesta)
import time
from transformers import pipeline

print("Cargando modelo...")

inicio = time.time()

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=20,
    do_sample=False
)

print(f"Modelo cargado en {time.time()-inicio:.2f} segundos")

print("Generando...")

inicio = time.time()

respuesta = pipe("Hola")

print(f"Generado en {time.time()-inicio:.2f} segundos")

print(respuesta)