# Raw — Scaffold práctica P2-A: Átomos y Koopmans
# Origen: chat de scaffold + brief content_briefs.md (Chat 3)
# Fecha: 2026-10-23

Proyecto: M_QUIFIS2 — materiales docentes para "Química Física II: Prácticas de Ordenador"
(asignatura de grado, UPV/EHU). Jupyter Book colaborativo en español.
Directorio de trabajo: /home/javi/ORGANIZED/PHD/M_QUIFIS2
Rama git activa: practice/part2-spectroscopy

━━━ REGLAS INVIOLABLES ━━━
1. El texto final publicado lo escribe un humano. Claude compila, formatea y estructura
   — NUNCA genera prosa final. Todo bloque de texto nuevo va dentro de un admonition
   MyST marcado [TEXTO HUMANO].
2. Todo el contenido para estudiantes en castellano.
3. Contenido nuevo propuesto por Claude se marca [PROPUESTA] — requiere aceptación
   humana explícita antes de incluirse.
4. Pedagogía primero: química antes que informática. Los pasos de GaussView son
   el medio, no el fin.
5. Los alumnos son novatos absolutos. Usar GaussView como interfaz gráfica exclusiva
   — NO escriben inputs a mano ni usan terminal.

━━━ TAREA DE ESTE CHAT ━━━
Escribir el scaffold de la página: content/atomos-koopmans.md
El archivo ya existe como stub vacío. Sobreescribirlo con la estructura completa
siguiendo el brief y la plantilla.

━━━ BRIEF DE CONTENIDO (Chat 3 de content_briefs.md) ━━━
Objetivo: calcular IE de átomos del 1er y 2º período via Koopmans; comparar con
experimento; visualizar orbitales en GaussView.

Secciones obligatorias:
- Introducción
- Fundamento teórico
- Procedimiento (4–5 pasos)
- Tabla de resultados (el alumno la rellena)
- Visualización de orbitales
- Preguntas

Ecuación central: IE ≈ −ε_HOMO  (LaTeX: $\text{IE} \approx -\varepsilon_{\text{HOMO}}$)
Conversión de unidades: 1 Ha = 27.2114 eV

Multiplicidades por átomo:
H→2, He→1, Li→2, Be→1, B→2, C→3, N→4, O→3, F→2, Ne→1

IE experimentales de referencia (eV):
H=13.60, He=24.59, Li=5.39, Be=9.32, B=8.30, C=11.26, N=14.53, O=13.62, F=17.42, Ne=21.56

Pasos del procedimiento (del brief):
1. Abrir GaussView, dibujar el átomo
   - Truco: átomo = molécula de 1 átomo
2. Gaussian Calculation Setup
   - Job Type: Energy
   - Method: HF / STO-3G (o 3-21G para mejor resultado)
   - Multiplicidad: según tabla
   - Additional Keywords: pop=full (ver todos los orbitales)
3. Lanzar y verificar terminación
4. Results → Summary → leer ε_HOMO (en Hartrees)
   - Alternativamente: abrir .log, buscar "Alpha occ. eigenvalues"
5. Convertir a eV y comparar con tabla experimental

━━━ REGLAS DE FORMATO ━━━
Admonitions estándar:
  :::{note} [TEXTO HUMANO] :::       ← secciones a escribir por humano
  :::{warning} ... :::               ← advertencias operativas
  :::{tip} ... :::                   ← consejos de GaussView
  [PROPUESTA: ...] dentro de {note}  ← sugerencias de Claude

━━━ RESULTADO ━━━
Archivo content/atomos-koopmans.md escrito con:
- Estructura MyST completa buildable con jupyter-book
- Tabla con IE experimentales precargadas, columnas para datos del alumno
- Ecuaciones LaTeX
- Todo texto narrativo marcado [TEXTO HUMANO] o [PROPUESTA]
- Tabla de multiplicidades completa
- Fragmento de .log de ejemplo para leer ε_HOMO

━━━ ESTADO TRAS EL CHAT ━━━
- content/atomos-koopmans.md: ESCRITO ✓
- Texto narrativo en secciones: pendiente de autor humano
- IE experimentales: precargadas en tabla (fuente: content_briefs.md)
- [CONFIRMAR con laboratorio]: nombres exactos de archivos, carpeta de trabajo,
  versión de Gaussian disponible (¿16?), base STO-3G vs 3-21G preferida
- [CONFIRMAR]: disponibilidad de Results → Summary en la versión del laboratorio
  (algunos labs solo tienen Results → MOs)
