# Cronograma completo – 6 semanas

**Nota:** Cada día incluye *Objetivo*, *Pasos*, *Quick win*, *Mini-quiz*, *Checklist* y *Mini-proyecto*. 
Elige Python o JavaScript según prefieras (ambos ejemplos incluidos cuando aplica).

---
## Semana 1 — Setup, Git/GitHub, Prompting y GPTs

### Día 1 — Entorno + “hello, model”
**Objetivo:** Tener API key, entorno listo y primer script.
**Pasos (Windows/PowerShell):**
1. Crear API key (OpenAI) y guardarla como variable de entorno:
   ```powershell
   setx OPENAI_API_KEY "TU_CLAVE_AQUI"
   ```
2. Instalar Git, Node LTS y Python 3.11+ (ver README en scripts).
3. Crear carpeta de trabajo:
   ```powershell
   mkdir C:\ai-lab && cd C:\ai-lab
   git init
   ```
4. **Python** (opcional):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install --upgrade pip openai
   ```
   Ejecuta `python ..\scripts\python\hello.py`
5. **JavaScript** (opcional):
   ```powershell
   mkdir hello-js && cd hello-js
   npm init -y
   npm install openai
   node ..\..\scripts\javascript\hello.mjs
   ```
**Quick win:** ver una respuesta del modelo en consola.  
**Mini-quiz:** 4 preguntas básicas de setup (usa plantilla en /docs/plantillas/MiniQuiz_Template.md).  
**Checklist:** variable OPENAI_API_KEY creada; Python o Node funcionando; Git configurado.  
**Mini-proyecto:** *Pitch Generator* simple (ver plantilla en README scripts).

### Día 2 — GitHub + repositorio remoto
**Objetivo:** Subir tu primer repo.
**Pasos:**
```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
git add . && git commit -m "init"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/ai-lab.git
git push -u origin main
```
**Quick win:** repo online.  
**Mini-quiz:** comandos clave (`add`, `commit`, `push`, `pull`).  
**Mini-proyecto:** añade `pitches/` y sube tu primer pitch.

### Día 3 — Prompting para negocio
**Objetivo:** Crear prompts que produzcan valor.
**Pasos:** Usa `/docs/plantillas/Prompting_Business_Template.md` con tu sector.
**Quick win:** 3 quick wins con impacto y esfuerzo estimado.
**Mini-quiz:** estructura de prompt (rol, objetivo, restricciones, entregable).  
**Mini-proyecto:** guarda mejores prompts en `prompts/` y súbelos al repo.

### Día 4 — Crear un GPT (UI) con instrucciones y conocimiento
**Objetivo:** Tener tu coach interno dentro de ChatGPT.
**Pasos:** ver `/docs/Guia_Crear_Proyecto_y_GPT_en_ChatGPT.md`
**Quick win:** GPT responde siguiendo tus reglas y usando tu Knowledge.  
**Mini-quiz:** diferencia entre instrucciones, conocimiento y capacidades.  
**Mini-proyecto:** Añade un *Action* simple (si procede) o prueba Code Interpreter.

### Día 5 — Connectors
**Objetivo:** Conectar Google Drive/GitHub (según permisos).
**Quick win:** el GPT encuentra y resume un archivo de tu Drive o repo.  
**Mini-proyecto:** flujo “subo archivo → resumen ejecutivo + tareas”.

### Día 6 — Actions básicas
**Objetivo:** Llamar una API pública (ej. Open-Meteo) desde tu GPT.
**Quick win:** “Dame el tiempo de hoy en Madrid y genera un plan corto.”  
**Mini-proyecto:** action que crea un *issue* en tu repo GitHub.

### Día 7 — Repaso semanal
**Objetivo:** Consolidar aprendizaje.
**Quick win:** checklist completa + quiz semanal.
**Mini-proyecto:** “Asistente de Founder” dentro del GPT (plantilla en docs).

---
## Semana 2 — Assistants API (Code Interpreter, File Search, Tool Calling)

### Día 8 — Estructura Assistants (Assistant / Thread / Run)
**Objetivo:** Crear un assistant desde código (Python/JS).  
**Quick win:** responder a un mensaje con un assistant.  
**Mini-proyecto:** CLI mínima que crea hilos y guarda transcripciones.

### Día 9 — Code Interpreter
**Objetivo:** Análisis de CSV con gráficos.
**Quick win:** subir `ventas.csv` y obtener 3 insights + 1 gráfico.  
**Mini-proyecto:** plantilla de informe semanal automatizado.

### Día 10 — File Search
**Objetivo:** Q&A sobre PDF/MD locales (vector store gestionada).
**Quick win:** responder con citas de un PDF cargado.  
**Mini-proyecto:** “Buscador de políticas internas” (carpeta /docs_internos).

### Día 11 — Tool/Function Calling
**Objetivo:** Definir funciones externas y dejar que el modelo decida llamarlas.
**Quick win:** función `get_weather(city)` + resumen con recomendación.  
**Mini-proyecto:** pipeline: pregunta → busca doc → llama función → compone email.

### Día 12 — Eventos, streaming, reintentos
**Objetivo:** Manejar estados y flujos robustos.
**Quick win:** ver logs de eventos de un run.  
**Mini-proyecto:** wrapper con reintentos exponenciales.

### Día 13 — Seguridad y costes
**Objetivo:** Cuidar claves y límites.
**Quick win:** límite de coste mensual y alertas; `.env` y secretos bien guardados.  
**Mini-proyecto:** script que imprime coste estimado por ejecución.

### Día 14 — Proyecto semanal
**Objetivo:** “Analista Operativo”
**Entregable:** subes Excel, el agente limpia datos con Code Interpreter, usa File Search
para contexto y llama una función para enviar informe por email (simular).

---
## Semana 3 — Audio (STT/TTS) + Integraciones

### Día 15 — STT (transcripción)
**Objetivo:** transcribir un `nota.wav`.
**Quick win:** texto limpio con tiempos clave.  
**Mini-proyecto:** “Reunión → resumen en Markdown”.

### Día 16 — TTS (síntesis)
**Objetivo:** generar `pitch.mp3` a partir de un texto.
**Quick win:** voz natural con 20–30s de guion.  
**Mini-proyecto:** “Audio pitch diario” con tus quick wins.

### Día 17 — Grabadora-resumidora
**Objetivo:** pipeline local: grabar → transcribir → resumir → guardar MD.
**Quick win:** archivo `resumen_2025-08-10.md` en /notas.  
**Mini-proyecto:** añadir tags y acciones (crear tarea).

### Día 18 — Notion API
**Objetivo:** guardar resúmenes en Notion.
**Quick win:** crear página por cada resumen.  
**Mini-proyecto:** base de conocimiento personal.

### Día 19 — Gmail / Zapier
**Objetivo:** enviar correo con adjuntos desde el agente o lanzar Zaps.
**Quick win:** enviar a tu email el resumen del día.  
**Mini-proyecto:** “dicta y dispara” (voz → texto → acción).

### Día 20 — Proyecto semanal
**Objetivo:** “Minuto CEO”
**Entregable:** dictas 1 min → resumen + tareas a Notion + TTS para compartir.

---
## Semana 4 — Realtime (voz) + Producto

### Día 21 — Realtime WebRTC (demo navegador)
**Objetivo:** conversación de voz básica con el modelo.  
**Quick win:** hablar y recibir respuesta en tiempo real.

### Día 22 — Realtime WebSocket (Node server + cliente web)
**Objetivo:** backend simple que intermedia tokens y audio.  
**Quick win:** demo compartible en LAN.

### Día 23 — Multimodal y barge-in
**Objetivo:** combinar herramientas y permitir interrupciones.  
**Quick win:** interrumpir al agente con una nueva instrucción.

### Día 24 — UX de voz y latencia
**Objetivo:** mejorar tiempos y sensación de naturalidad.
**Quick win:** push-to-talk + respuesta parcial.

### Día 25 — Empaquetado “producto”
**Objetivo:** landing mínima, captación de emails, demo.
**Quick win:** formulario + email de bienvenida.

### Día 26–27 — Proyecto final (elige vertical)
**Objetivo:** “Agente de Prospección” o “Agente de Soporte”.  
**Quick win:** script de evaluación interna (casos ejemplo).

### Día 28 — Cierre
**Objetivo:** métricas y plan de escalar.
**Quick win:** One-pager con costes, riesgos y próximos pasos.
