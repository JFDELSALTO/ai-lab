from openai import OpenAI
import os, datetime, pathlib

# Ajusta tu sector aquí
SECTOR = "Consultoría de operaciones y logística"

client = OpenAI()  # usa OPENAI_API_KEY del entorno

template = f"""Rol: Consultor de crecimiento para {SECTOR}.
Objetivo: Encontrar 3 quick wins que generen ingresos en 7–14 días.
Restricciones: Presupuesto mínimo, canales orgánicos primero, claridad táctica.
Formato de salida:
1) Quick win #1 — pasos, estimación de impacto (€), esfuerzo (bajo/medio/alto), riesgo.
2) Quick win #2 — ...
3) Quick win #3 — ...
Cierre: 1 CTA accionable para hoy.
"""

messages = [
    {"role": "system", "content": "Eres un consultor de crecimiento ultra pragmático. Responde en español, formato claro y accionable."},
    {"role": "user", "content": template}
]

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

today = datetime.date.today().isoformat()
out_path = pathlib.Path("prompts") / f"quickwins_{today}.md"
out_path.write_text(resp.choices[0].message.content, encoding="utf-8")

print("Guardado en:", out_path)
if hasattr(resp, "usage") and resp.usage:
    print("Tokens usados:", resp.usage.total_tokens)

