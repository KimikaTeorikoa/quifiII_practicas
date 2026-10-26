# JIT Guide: Estilo y Estructura — M_QUIFIS2
# Cargado por Claude al inicio de cada chat de scaffold de práctica.
# Versión: 1.1.0 | 2026-10-24

---

## 1. Perfil del alumno (INVARIANTE)

Los alumnos de esta asignatura son **novatos absolutos** en química computacional:
- No han usado Gaussian ni GaussView antes.
- No saben qué es un archivo `.gjf`, `.log`, ni un orbital.
- No usan el terminal. Nunca. GaussView es su único punto de contacto.
- Pueden copiar y pegar texto de un archivo `.log` a una tabla de Word/Excel.
- No saben programar. No se les pide ningún script.
- Su objetivo es desarrollar **intuición física**, no convertirse en usuarios expertos.

**Consecuencia directa para el scaffold:**
Cada paso del procedimiento debe decir EXACTAMENTE en qué menú hacer clic, con qué
nombre aparece la opción, y qué aspecto tiene la pantalla esperada. Nunca dar por
conocido un paso de interfaz.

---

## 2. Secciones obligatorias de cada práctica (en este orden)

Toda página de práctica DEBE contener estas secciones, en este orden:

```
1. Introducción
2. Objetivos
3. ¿Qué software vamos a usar?      ← solo en la primera práctica; resto → referencia breve
4. Conceptos clave                   ← intuición física; NO derivaciones matemáticas
5. Procedimiento                     ← numerado, paso a paso, menús explícitos
6. Resultados                        ← tablas con columnas pre-definidas, instrucciones de copia
7. Preguntas y pruebas               ← obligatorias; mezcla de comprensión e interpretación
8. Bibliografía                      ← al menos 2 referencias; estilo APA o equivalente
9. [Opcional] Para ir más lejos      ← solo si hay tiempo; no en el hilo principal
```

Ninguna sección puede eliminarse. Las secciones `[TEXTO HUMANO]` marcan dónde escribe
el autor humano; el scaffold proporciona la estructura y los placeholders.

---

## 3. Convenciones de escritura de menús GaussView

Siempre escribir las rutas de menú en negrita con `→`:

> **File → Save As...**
> **Calculate → Gaussian Calculation Setup**
> **Results → MOs**

Nunca escribir "ve a resultados" o "abre el menú de cálculo" — siempre el nombre exacto
que aparece en la interfaz.

---

## 4. Placeholders de captura de pantalla

Cuando se necesite una captura de pantalla que aún no existe, usar:

```
[CAPTURA: descripción de lo que debe verse — p. ej. "ventana Gaussian Calculation Setup
con pestaña Method abierta, mostrando HF/STO-3G seleccionado"]
```

Nunca omitir las capturas: dejar el placeholder es correcto; omitir la sección no lo es.
Las capturas son especialmente importantes en los pasos de GaussView que los alumnos
nunca han visto.

---

## 5. Bloque de intuición física (admonition `{note}` con título)

Para conceptos que los alumnos deben entender sin derivar, usar este patrón:

```markdown
:::{note} ¿Por qué las energías son negativas?
[TEXTO HUMANO: explicación en 3-4 frases, sin fórmulas, usando analogías.]
:::
```

Conceptos que DEBEN tener su bloque de intuición en la práctica correspondiente:

| Concepto | Práctica donde aparece |
|----------|----------------------|
| Energías negativas (sistemas ligados) | P2-A (primera vez) |
| HOMO y LUMO: qué son, para qué sirven | P2-A (primera vez) |
| Multiplicidad: qué es, cómo elegirla | P2-A (primera vez) |
| Superficie de energía potencial: paisaje | P2-B |
| Modos normales: por qué los átomos vibran | P2-C |
| Transiciones electrónicas y color | P2-D |

Una vez explicado en la primera práctica, las siguientes solo hacen referencia cruzada.

---

## 6. Cómo guardar y registrar resultados (sin scripting)

El procedimiento estándar de recogida de datos para esta asignatura es:

1. **Abrir el archivo `.log`** con el editor de texto del sistema (gedit, mousepad, etc.).
2. **Buscar la línea relevante** (indicada en cada práctica con el texto exacto a buscar).
3. **Copiar el número** y pegarlo en la tabla del guión (Word, LibreOffice Calc, o en papel).
4. **Nunca modificar el `.log`** — es de solo lectura.

Los alumnos NO extraen datos con scripts. Si la práctica requiere un gráfico, se indica
explícitamente qué columnas copiar y en qué herramienta representarlos (LibreOffice Calc,
o Python si ya lo conocen de la Parte 1).

---

## 7. Sección "Para ir más lejos" (Opcional)

Esta sección va al final, después de la bibliografía. Reglas:

- Es completamente opcional: el alumno que va bien de tiempo la hace; el resto no.
- NO es un requisito para la nota. Debe indicarse explícitamente.
- Contiene 1-2 actividades de extensión que amplían el concepto central sin alejarse de él.
- Ejemplos válidos:
  - Convergencia con el tamaño de la base (P2-A)
  - Calcular la PES para una segunda molécula y comparar (P2-B)
  - Añadir un modo de vibración de CO₂ que no aparece en IR y justificar (P2-C)
  - Calcular el espectro de una segunda cetona y comparar λ_max (P2-D)
- NO incluye derivaciones matemáticas avanzadas ni scripting nuevo.

---

## 8. Bibliografía

Cada práctica DEBE incluir una sección `## Bibliografía` al final (antes de "Para ir más
lejos"). Mínimo 2 referencias. Formato sugerido: APA o estilo RSC.

Siempre incluir:
- El manual de la asignatura si existe (referencia interna).
- La referencia del software Gaussian (cita oficial de Gaussian 16).
- Un artículo o libro de texto relevante al contenido de la práctica.

Cita estándar de Gaussian 16 (incluir en todas las prácticas):

> Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.

---

## 9. Componentes reutilizables — uso canónico

Todos los estilos están definidos en `_static/custom.css`.
Las substituciones de texto están en `_config.yml` bajo `myst_substitutions`.

### Bloques de contenido

| Componente | Sintaxis | Uso |
|------------|----------|-----|
| Texto humano pendiente | `:::{note}\n[TEXTO HUMANO: ...]\n:::` | Secciones narrativas sin redactar |
| Intuición física | `:::{admonition} 💡 Título\n:class: intuicion\n...\n:::` | Explicaciones conceptuales sin fórmulas |
| Captura de pantalla | `:::{admonition} 📸 Captura de pantalla\n:class: captura\n[CAPTURA: desc]\n:::` | Placeholder de screenshot |
| Advertencia operativa | `:::{warning}\n...\n:::` | Errores frecuentes, multiplicidad |
| Verificación crítica | `:::{danger}\n...\n:::` | Comprobación de terminación correcta |
| Consejo GaussView | `:::{tip}\n...\n:::` | Rutas de menú, atajos |
| Sección opcional | `::::{dropdown} 🚀 Para ir más lejos\n:color: success\n:icon: rocket\n...\n::::` | Siempre al final, tras bibliografía |

### Substituciones MyST (usar en lugar de texto fijo)

| Macro | Se expande a | Cuándo usar |
|-------|-------------|-------------|
| `{{gaussian_version}}` | "Gaussian 16, Revision A.03" | Al mencionar el software |
| `{{gaussian_cite}}` | Cita completa G16 | En bibliografía |
| `{{ha_to_ev}}` | "27.2114" | En fórmulas de conversión |
| `{{ha_to_kcal}}` | "627.509" | Si se necesita kcal/mol |
| `{{termination_ok}}` | `` `Normal termination of Gaussian 16` `` | En paso de verificación |
| `{{practicas_folder}}` | `` `/home/ikasle/Documentos/Practicas/` `` | Al indicar dónde guardar |
| `{{metodo_base}}` | "HF/STO-3G" | Al describir el método por defecto |

---

## 10. Reglas de escritura natural — anti-LLM-ese

Estas reglas se aplican a **todo texto generado** en este proyecto, sin excepción.

### 10.1 Puntuación y formato
- Prohibido el em-dash (—). Usa coma, punto o paréntesis.
- No abuses de negritas dentro de párrafos normales: reserva la negrita para rutas de menú (`**File → Save As...**`) y términos técnicos en su primera aparición.
- No organices en listas lo que puede fluir como prosa. Las listas son para pasos secuenciales o tablas comparativas, no para ideas que tienen conexión lógica entre sí.

### 10.2 Léxico prohibido
Nunca uses estas palabras ni sus equivalentes castellanos:

| Inglés | Español equivalente prohibido |
|--------|-------------------------------|
| crucial | crucial, fundamental, vital |
| delve | profundizar, adentrarse |
| tapestry / landscape | tapiz, panorama, ecosistema |
| resonate | resonar (en sentido metafórico) |
| pivotal | pivotal, determinante (genérico) |
| navigate | navegar (metafórico) |
| fostering | fomentar (como muletilla) |
| multifaceted | multifacético |
| testament | testimonio de |

Sustituye por verbos concretos y datos específicos.

### 10.3 Estructuras retóricas vacías — prohibidas
- **Aperturas con eco:** "Buena pregunta", "Ciertamente", "Por supuesto, estaré encantado de…", paráfrasis de la consulta en la primera frase.
- **Cierres moralizantes:** "En conclusión", "En resumen", reflexiones genéricas sobre el futuro o la importancia del tema.
- **Simetría mecánica:** Introducción → 3 puntos idénticos → Conclusión. Rompe la estructura si el contenido lo pide.

### 10.4 Ritmo y sintaxis
- Alterna oraciones cortas (sujeto-verbo-objeto) con oraciones complejas bien hiladas. Evita párrafos donde todas las oraciones tienen la misma longitud.
- Voz activa por defecto.
- Muestra con datos y ejemplos concretos antes de adjetivar. "La energía del HOMO es −0.498 Ha" es mejor que "la energía del HOMO tiene un valor relevante".

---

## 11. Lo que Claude NUNCA hace en los scaffolds

- Generar prosa narrativa final (todo va en `[TEXTO HUMANO]`).
- Inventar resultados numéricos no presentes en los logs de referencia.
- Introducir derivaciones matemáticas más allá de las ecuaciones centrales de cada práctica.
- Eliminar la sección "Para ir más lejos" aunque parezca redundante.
- Omitir la sección de Bibliografía.
- Usar el terminal o scripting como herramienta principal del alumno.
- Violar las reglas anti-LLM-ese de la sección 10 en ningún texto generado.
