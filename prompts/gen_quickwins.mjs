import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI(); // requiere OPENAI_API_KEY en el entorno

const SECTOR = "Consultoría de operaciones y logística";
const template = `Rol: Consultor de crecimiento para ${SECTOR}.
Objetivo: Encontrar 3 quick wins que generen ingresos en 7–14 días.
Restricciones: Presupuesto mínimo, canales orgánicos primero, claridad táctica.
Formato de salida:
1) Quick win #1 — pasos, estimación de impacto (€), esfuerzo (bajo/medio/alto), riesgo.
2) Quick win #2 — ...
3) Quick win #3 — ...
Cierre: 1 CTA accionable para hoy.`;

const resp = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [
    { role: "system", content: "Eres un consultor de crecimiento ultra pragmático. Responde en español, formato claro y accionable." },
    { role: "user", content: template }
  ]
});

const today = new Date().toISOString().slice(0,10);
// Para no pisar el archivo de Python, generamos uno con sufijo _js
const outPath = `prompts/quickwins_js_${today}.md`;
fs.mkdirSync("prompts", { recursive: true });
fs.writeFileSync(outPath, resp.choices[0].message.content, "utf8");
console.log("Guardado en:", outPath);
