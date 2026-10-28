# Reglas de edición — Armonización Parte 2 con Parte 1
# Versión: 1.0.0 | 2026-10-28
# Cargar junto al JIT de estilo en cada sesión de edición.

---

## A. Reglas globales de tono y registro

### A1 — Primera persona del plural (ALTA prioridad)
Sustituir el impersonal sistemático por primera persona del plural.

| Forma a eliminar | Forma de Parte 1 |
|---|---|
| "se selecciona", "se abre", "se accede" | "seleccionamos", "abrimos", "accedemos" |
| "se emplea", "se utiliza" | "empleamos", "usamos" |
| "se construye", "se obtiene" | "construimos", "obtenemos" |
| "puede observarse" | "podemos observar" |

Excepción: los pasos numerados del **Procedimiento** pueden mezclar ambas formas si el imperativo ("pulsa", "abre") suena más natural y directo.

### A2 — Primera frase de las introducciones
No abrir con una frase-resumen que lo enumera todo. Parte 1 abre simple y directo:
> ✗ "La química computacional requiere transformar geometrías moleculares tridimensionales en coordenadas e instrucciones numéricas procesables por algoritmos de estructura electrónica."
> ✓ "Para hacer un cálculo en Gaussian, primero hay que decirle al programa cómo está dispuesta la molécula en el espacio."

### A3 — Ritmo de oraciones
Alternar frases cortas (< 15 palabras, sujeto-verbo-objeto) con frases más largas bien hiladas. Nunca tres oraciones seguidas de la misma longitud.

### A4 — Léxico prohibido (§10.2 del JIT de estilo)
Ver tabla completa en `jit_quifis2_style.md §10.2`. Más frecuentes en Parte 2:
- "excelente equilibrio" → describir con datos concretos
- "condicionan" como verbo vago → especificar qué determina qué
- Frases de apertura de párrafo del tipo "Cabe destacar que" → eliminar

---

## B. Reglas globales de formato

### B1 — Separadores `---`
Eliminar los separadores `---` entre subsecciones dentro de un mismo archivo.
Parte 1 no los usa en ningún momento. Excepción admitida: un único `---` al final del cuerpo principal, antes de "Bibliografía" y "Para ir más lejos".

### B2 — Sintaxis de admonition
Usar **exclusivamente** la forma `:::` de MyST. Prohibida la forma con triple backtick para admonitions.

Forma correcta:
```
:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: descripción]
:::
```

Forma incorrecta (a corregir):
```
```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: descripción]
```
```

### B3 — Emoji del dropdown "Para ir más lejos"
Usar siempre `🚀` como icono. Si el dropdown tiene otro emoji, cambiarlo.

---

## C. Reglas globales de contenido

### C1 — Notas de scaffold → convertir a [TEXTO HUMANO]
Cualquier párrafo que sea una instrucción de autor ("Párrafo corto. Explicación cualitativa...") debe convertirse al placeholder normalizado:
```
:::{note}
[TEXTO HUMANO: descripción breve de qué debe contener este párrafo]
:::
```
No inventar ni redactar el contenido: solo normalizar el placeholder.

### C2 — Comentarios de "VERSIÓN ESQUEMÁTICA" → eliminar
Eliminar el bloque de comentario HTML al inicio de atomos-koopmans.md, modos-normales.md y espectroscopia-uv.md. No es texto del libro.

---

## D. Anti-sesgos LLM (instrucción de prompt obligatoria)

Incluir siempre en el prompt de edición de cada archivo:

> "Mejora la redacción aplicando las reglas del archivo `reglas_edicion.md` sin omitir datos, secciones, ejemplos ni bloques de código existentes. Si modificas la estructura, mantén la densidad de información original. No modifiques rutas de archivo, URLs ni sintaxis de enlaces ya presentes. No resumas secciones ya redactadas."

---

## E. Orden de edición recomendado (por lotes temáticos)

### Lote 0 — Mecánico (sin tocar prosa)
Archivos: atomos-koopmans.md, modos-normales.md, espectroscopia-uv.md
Cambios: solo C2 (eliminar banner) y B2 (corregir sintaxis admonition)

### Lote 1 — Intros conceptuales
Orden: intro-gaussview → intro-born-oppenheimer → intro-energias → intro-hartree-fock → intro-mas-alla-hf → intro-bases
Cambios por archivo: A1 + A2 + A3 + A4 + B1

### Lote 2 — Prácticas con prosa completa
Orden: moleculas-pes → atomos-koopmans
Cambios: A1 + A3 + B1 + ajustes puntuales

### Lote 3 — Prácticas con scaffold parcial
Orden: modos-normales → espectroscopia-uv
Cambios: A1 + B1 + C1 (normalizar placeholders)

### Lote 4 — Índice
Archivo: index.md
Cambios: reescribir en tono introductorio, no de catálogo

---

---

## G. Normas añadidas en Fase 1 (globales)

- **Sin emojis. Nunca.** En títulos de sección, dropdowns, admonitions ni en ningún texto del libro.
- **Admonitions en español.** Usar `:::{admonition} Advertencia\n:class: warning` y `:::{admonition} Atención\n:class: danger` en lugar de los tipos ingleses directos `:::{warning}` y `:::{danger}`.
- **Título global de Parte 2:** "Introducción a la química computacional con Gaussian" (aplicado en index.md).
- **index.md reducido:** sin párrafo descriptivo formal, sin sección "Estructura de la Sección", sin bloques temáticos. Solo título + 2-3 frases de orientación.

---

## F. Directivas locales por archivo (añadir aquí al ir procesando)

*(Rellenar durante Fase 1 y Fase 2 a medida que el autor da instrucciones específicas)*

| Archivo | Directiva específica | Fase |
|---|---|---|
| — | — | — |
