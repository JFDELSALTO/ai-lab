from openai import OpenAI
import datetime, pathlib

# Usa la variable de entorno OPENAI_API_KEY (no pongas la clave en el código)
client = OpenAI()

SECTOR = "Consultoría de operaciones y logística"
prompt = f"""Rol: Consultor de crecimiento para {SECTOR}.
Objetivo: Encontrar 3 quick wins que generen ingresos en 7–14 días.
Restricciones: Presupuesto mínimo, canales orgánicos primero, claridad táctica.
Formato de salida:
1) Quick win #1 — pasos, estimación de impacto (€), esfuerzo (bajo/medio/alto), riesgo.
2) Quick win #2 — ...
3) Quick win #3 — ...
Cierre: 1 CTA accionable para hoy.
"""

resp = client.chat.completions.create(
    model="gpt-4o-mini",   # modelo económico (coste bajo)
    temperature=0.3,       # respuestas más consistentes
    max_tokens=500,        # CAP de salida => CAP de coste
    messages=[
        {"role": "system", "content": "Eres un consultor de crecimiento práctico y directo."},
        {"role": "user", "content": prompt}
    ]
)

out = pathlib.Path("prompts") / f"demo_{datetime.date.today().isoformat()}.md"
out.write_text(resp.choices[0].message.content, encoding="utf-8")
print("Guardado en:", out)
if hasattr(resp, "usage") and resp.usage:
    print("Tokens usados:", resp.usage.total_tokens)
