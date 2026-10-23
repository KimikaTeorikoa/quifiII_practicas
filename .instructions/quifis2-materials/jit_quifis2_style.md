# JIT Guide: quifis2 — Style and Page Anatomy
**Load this guide at the start of any dispatch session for M_QUIFIS2.**

## Page anatomy (every practice)
1. **Introducción** — chemical motivation, human-written
2. **Objetivos** — numbered learning goals, human-written
3. **Fundamento teórico** — equations and key concepts, human-written; Claude formats LaTeX
4. **Instrucciones paso a paso** — numbered steps for Gaussian/GaussView/Python, human-written; Claude formats code blocks
5. **Resultados y análisis** — guided questions for data interpretation, human-written
6. **Preguntas** — mandatory student questions, human-written
7. **Observaciones** *(optional)* — caveats and common errors, human-written

## Markers
- `[TEXTO HUMANO]` — placeholder where human must write
- `[PROPUESTA]` — content proposed by Claude, needs human approval
- `[EXT]` — blocked on external dependency

## Flujo de trabajo del estudiante — GaussView primero

**Los estudiantes usan GaussView como interfaz gráfica exclusiva.** No escriben archivos `.gjf` a mano, no lanzan comandos Bash, no usan terminal (salvo quizá para abrir GaussView).

Flujo típico:
1. Abrir GaussView → dibujar/importar la molécula con el editor gráfico
2. `Calculate → Gaussian Calculation Setup` → seleccionar método y base en desplegables
3. Añadir keywords adicionales (opt, freq, td, scrf) en el campo de ruta si no hay desplegable
4. Clic en `Submit` → GaussView genera el `.gjf` y lanza el cálculo automáticamente
5. Cuando termina, abrir el `.log` desde GaussView → `Results → ...` para visualizar

**Consecuencias para los scaffolds:**
- Las instrucciones deben describir acciones de GUI: "En el menú...", "Selecciona en el desplegable...", "Haz clic en..."
- NO escribir bloques de input Gaussian para que el alumno los copie — esos van en las notas internas/JIT, no en las páginas de práctica
- Los bloques de código en las páginas de práctica son solo para mostrar fragmentos del `.log` que el alumno debe localizar e interpretar
- Capturas de pantalla de GaussView serían ideales (marcar con `[FIGURA: captura GaussView X]`)

## Style rules
- Language: Spanish throughout all student-facing content
- Tone: claro, directo, pedagógico — como explicar a un estudiante listo que nunca ha usado computación científica
- Instrucciones: siempre en forma de pasos de GUI ("Abre...", "Selecciona...", "Haz clic en...")
- Code blocks: solo para mostrar fragmentos del .log que el alumno debe leer e interpretar
- Tables: para resultados numéricos extraídos del .log (R, E, frecuencias, IE...)
- No walls of text: párrafos cortos, listas numeradas, pasos concretos
- Chemistry first: siempre explicar el *porqué* antes del *cómo*

## File format
- Prefer `.md` pages for text-heavy sections
- Use `.ipynb` only when interactive Python is genuinely needed for analysis
- Jupyter Book config: match Part 1 structure (TBD when URL available, EXT-04)

## Gaussian conventions (⚠️ ACTUALIZADO desde logs reales — difiere del manual antiguo)
- **Versión: Gaussian 16 (g16)** — el manual dice g03, pero los logs de referencia confirman g16
- Input files: **`.gjf`** extension (el manual dice `.com` — usar `.gjf`)
- Output files: `.log` extension
- Run command: `g16 filename.gjf` (confirmar con T003 la sintaxis exacta del lab)
- Success check: última línea del .log = `Normal termination of Gaussian 16 at [fecha].`
- Visualization: MOLDEN (`molden filename.log`) o GaussView
- Guía completa de keywords, output patterns y ejemplos: `jit_quifis2_gaussian.md`

## Patrones de escritura observados en el manual de referencia
- Secciones numeradas con títulos breves (Capítulo N: título)
- Comandos en fuente monoespaciada, siempre con contexto de uso ("Ejecuta el programa con…")
- Tablas para resultados numéricos (Z, IE_exp, IE_calc, % error)
- Figuras referenciadas como "Figura N" con pie de figura explicativo
- Preguntas numeradas al final de cada capítulo, formuladas para reflexión (no mecánicas)
- Ejercicios de los slides combinan tabla de resultados + visualización de orbitales
- La introducción siempre motiva el porqué antes del cómo
