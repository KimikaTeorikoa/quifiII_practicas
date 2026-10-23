# Content Briefs — Páginas Parte 2

> Documento interno. Un brief por página → input principal de cada chat de scaffold.
> Cada sección describe QUÉ debe contener (no el texto final — eso es [TEXTO HUMANO]).
> Notas [PROPUESTA] requieren aceptación humana.

---

## Chat 1 — `intro.md` (actualizar sección existente)

**Objetivo del chat:** añadir un párrafo al final de la intro existente que presente la Parte 2.

### Qué añadir
- 1 párrafo: transición de "modelos sencillos con Python" a "software de química computacional real"
- Mencionar GaussView + Gaussian como herramientas
- Listar las 4 prácticas con una frase cada una
- NO reescribir lo que ya existe — solo añadir al final de la sección "Bienvenida"

---

## Chat 2 — `gaussview-intro.md` *(página nueva, la más importante)*

**Objetivo:** que el alumno pueda abrir GaussView, dibujar cualquier molécula sencilla y lanzar un cálculo antes de llegar a las prácticas.

### Secciones

**¿Qué es GaussView? ¿Qué es Gaussian?**
- GaussView = interfaz gráfica; Gaussian = motor de cálculo. Son programas distintos.
- Analogía simple: GaussView es el volante, Gaussian es el motor.
- [PROPUESTA: figura esquema GaussView→Gaussian→.log]

**Abrir GaussView**
- Cómo arrancarlo desde el escritorio / terminal del laboratorio
- Descripción de la ventana principal: barra de herramientas, vista 3D, panel de resultados
- [FIGURA: captura pantalla GaussView anotada — zonas principales]

**Dibujar una molécula**
- Usar el editor de fragmentos: seleccionar átomo en tabla periódica, hacer clic para añadir
- Añadir enlaces: tipos de enlace, ajuste automático de geometría
- Limpiar la geometría inicial: Edit → Clean
- Consejo: para moléculas conocidas, usar `File → Fetch` con el nombre o SMILES [CONFIRMAR disponibilidad]
- [FIGURA: captura pantalla construcción molécula sencilla, p.ej. CO]

**Configurar el cálculo**
- Calculate → Gaussian Calculation Setup
- Pestaña Job Type: Energy / Optimization / Frequency / ...
- Pestaña Method: método (HF, B3LYP) y base (STO-3G, 3-21G, 6-311G)
- Pestaña Title: nombre descriptivo del cálculo
- Pestaña Additional Keywords: para keywords avanzados (scrf, td, pop=full...)
- Cómo ver el input que se va a generar (botón Preview / Edit)
- [FIGURA: captura Gaussian Calculation Setup con zonas anotadas]

**Lanzar el cálculo**
- Botón Submit → GaussView genera el .gjf y llama a Gaussian
- Cómo saber que está corriendo: indicador en la barra de estado
- Cuánto tarda aproximadamente (referencia: H₂ = segundos; acetona = minutos)
- [TEXTO HUMANO: instrucciones específicas del laboratorio — carpeta de trabajo, etc.]

**Verificar que el cálculo terminó bien**
- Cómo abrir el .log desde GaussView
- Qué buscar: la última línea debe decir "Normal termination of Gaussian 16"
- Si no aparece: el cálculo falló — qué hacer (avisar al profesor, no reintentar sin entender el error)
- [PROPUESTA: bloque de código mostrando la línea de terminación correcta]

**Ver los resultados en GaussView**
- Results → Optimization: geometría optimizada animada
- Results → Vibrations: modos normales animados
- Results → MOs: orbitales moleculares (HOMO, LUMO, ...)
- Results → Summary: resumen de propiedades calculadas
- [FIGURA: captura Results → MOs con HOMO de una molécula]

**Errores frecuentes**
- Lista breve: multiplicidad incorrecta, falta línea en blanco final, cálculo de frecuencias sin optimizar primero

---

## Chat 3 — `atomos-koopmans.md`

**Objetivo:** calcular la energía de ionización de átomos del primer y segundo período usando Koopmans; comparar con experimento; visualizar orbitales.

### Secciones

**Introducción**
- [TEXTO HUMANO]: ¿por qué nos interesa la IE? Contexto de la tabla periódica y tendencias periódicas.

**Fundamento teórico**
- El método Hartree-Fock: campo medio, un electrón en el campo de todos los demás
- Concepto de orbital atómico y energía orbital ε
- Teorema de Koopmans: IE ≈ −ε_HOMO
  - Ecuación en LaTeX: $\text{IE} \approx -\varepsilon_{\text{HOMO}}$
- Limitaciones: correlación electrónica, reorganización orbital
- Unidades: Hartree → eV (×27.2114)

**Procedimiento**
- Paso 1: Abrir GaussView, dibujar el átomo (p.ej. H, Li, C, Ne...)
  - Truco: átomo = molécula de 1 átomo; dibujar solo ese átomo
- Paso 2: Gaussian Calculation Setup
  - Job Type: Energy
  - Method: HF / STO-3G (o 3-21G para mejor resultado)
  - Multiplicidad: [TEXTO HUMANO — tabla de multiplicidades por átomo]
  - Additional Keywords: `pop=full` para ver todos los orbitales
- Paso 3: Lanzar y verificar terminación
- Paso 4: Results → Summary → leer ε_HOMO (en Hartrees)
  - Alternativamente: abrir .log, buscar "Alpha occ. eigenvalues"
- Paso 5: Convertir a eV y comparar con tabla experimental

**Tabla de resultados** (el alumno la completa)
| Átomo | Config. electrónica | ε_HOMO (Ha) | IE Koopmans (eV) | IE experimental (eV) | Error (%) |
|-------|--------------------|-----------  |------------------|----------------------|-----------|
| H     | 1s¹                | —           | —                | 13.60                | —         |
| He    | 1s²                | —           | —                | 24.59                | —         |
| Li    | [He]2s¹            | —           | —                | 5.39                 | —         |
| ...   | ...                | —           | —                | ...                  | —         |

**Visualización de orbitales**
- Results → MOs en GaussView: ver el HOMO y el LUMO
- [PROPUESTA: una captura mostrando el orbital 1s del H y el 2p del C]
- Discutir: ¿cómo cambia la forma del HOMO al recorrer el período?

**Preguntas**
- [TEXTO HUMANO]: preguntas de análisis e interpretación
- [PROPUESTA]:
  1. ¿Por qué el método HF sobreestima la IE del He pero la subestima en metales alcalinos?
  2. ¿Qué relación hay entre la IE y la electronegatividad?
  3. ¿Qué ocurre con la IE al descender un grupo de la tabla periódica? ¿Y al avanzar un período?

---

## Chat 4 — `moleculas-pes.md`

**Objetivo:** calcular y representar la PES de H₂ (singlete y triplete) en función de la distancia R(H-H); interpretar mínimos, barreras y disociación. [PROPUESTA: extender a diedro en molécula con halógenos]

### Secciones

**Introducción**
- [TEXTO HUMANO]: de los átomos a las moléculas — ¿qué mantiene unidos los átomos?
- La energía electrónica depende de la geometría nuclear (aproximación de Born-Oppenheimer)

**Fundamento teórico**
- Aproximación de Born-Oppenheimer: separación movimiento nuclear / electrónico
  - $\hat{H}\Psi = E_{\text{elec}}(R)\Psi$ — E depende paramétricamente de R
- Concepto de PES: paisaje energético en función de coordenadas nucleares
- Mínimos (estructuras estables), puntos de silla (estados de transición), asíntotas (disociación)
- Por qué singlete ≠ triplete: spines antiparalelos vs paralelos → enlace vs no-enlace

**Procedimiento**
- Paso 1: Dibujar H₂ en GaussView (2 átomos H, un enlace)
- Paso 2: Configurar scan
  - Job Type: Scan
  - Definir la coordenada a barrer: distancia R(H-H)
  - Valor inicial, paso, número de puntos
  - Multiplicidad 1 (singlete) → repetir con multiplicidad 3 (triplete)
  - [TEXTO HUMANO: instrucciones exactas de GaussView para configurar un scan]
- Paso 3: Lanzar y esperar (más lento que un cálculo SP — muchos puntos)
- Paso 4: Extraer energías
  - Results → Scan en GaussView (muestra la curva directamente)
  - Alternativamente: tabla R vs E desde el .log
- Paso 5: Representar ambas curvas (singlete y triplete) en el mismo gráfico

**Tabla de resultados** (el alumno la completa para singlete)
| R (Å) | E singlete (Ha) | E triplete (Ha) |
|-------|-----------------|-----------------|
| 0.55  | —               | —               |
| 0.65  | —               | —               |
| ...   | —               | —               |

**[PROPUESTA: celda Python/Notebook para graficar PES]**
```python
import matplotlib.pyplot as plt
import numpy as np
# Leer datos del .log o introducir manualmente
R = [...]
E_singlet = [...]
E_triplet = [...]
# Normalizar a cero en el mínimo
# Plot
```

**Preguntas**
- [TEXTO HUMANO]
- [PROPUESTA]:
  1. ¿A qué distancia está el mínimo de la curva singlete? ¿Coincide con el valor experimental (0.74 Å)?
  2. ¿Por qué el triplete no tiene mínimo? ¿Qué significa físicamente?
  3. ¿Qué representa la energía en el límite R→∞?

---

## Chat 5 — `modos-normales.md`

**Objetivo:** calcular y visualizar los modos normales de vibración de CO y CO₂; interpretar IR activo/inactivo; comparar frecuencias calculadas con experimentales.

### Secciones

**Introducción**
- [TEXTO HUMANO]: la espectroscopía IR como herramienta analítica cotidiana; qué miden los espectrómetros de IR

**Fundamento teórico**
- Aproximación armónica: PES ≈ parábola cerca del mínimo
  - $V(x) \approx \frac{1}{2}k(x-x_0)^2$
- Modos normales: combinaciones lineales donde todos los átomos oscilan en fase
- Número de modos: $3N-5$ (lineal) o $3N-6$ (no lineal)
  - CO (N=2, lineal): 1 modo; CO₂ (N=3, lineal): 4 modos (2 activos IR)
- Regla de selección IR: el modo debe cambiar el momento dipolar
- Frecuencia de vibración: $\tilde{\nu} = \frac{1}{2\pi c}\sqrt{k/\mu}$

**Procedimiento**
- Paso 1: Dibujar CO en GaussView
- Paso 2: Configurar opt + freq
  - Job Type: Opt+Freq
  - Method: B3LYP / 6-311G
  - [TEXTO HUMANO: instrucciones GaussView]
- Paso 3: Lanzar y verificar
- Paso 4: Results → Vibrations — ver la animación del modo normal de CO
  - Identificar: ¿es estiramiento o flexión?
- Paso 5: Leer la frecuencia calculada del .log (buscar "Frequencies --")
- Paso 6: Repetir para CO₂ — ver los 4 modos; identificar IR activos e inactivos

**Tabla de resultados**
| Molécula | Modo | Tipo | ν̃ calculada (cm⁻¹) | ν̃ experimental (cm⁻¹) | Error (%) |
|----------|------|------|---------------------|------------------------|-----------|
| CO       | 1    | estiramiento C-O | — | 2143 | — |
| CO₂      | 1    | estiramiento simétrico | — | 1388 | — |
| CO₂      | 2    | estiramiento asimétrico | — | 2349 | — |
| CO₂      | 3,4  | flexión (×2) | — | 667 | — |

**Preguntas**
- [TEXTO HUMANO]
- [PROPUESTA]:
  1. ¿Por qué el estiramiento simétrico de CO₂ no es activo en IR?
  2. ¿Qué significa una frecuencia imaginaria en el output de Gaussian?
  3. ¿Por qué la frecuencia calculada difiere de la experimental? (aproximación armónica, funcional DFT)

---

## Chat 6 — `espectroscopia-uv.md`

**Objetivo:** calcular el espectro UV-Vis de cetonas usando TD-DFT; identificar transiciones n→π* y π→π*; estudiar el efecto del disolvente (solvatocromismo).

### Secciones

**Introducción**
- [TEXTO HUMANO]: qué mide un espectrofotómetro UV-Vis; por qué las cetonas absorben UV

**Fundamento teórico**
- Transiciones electrónicas: n→π* (banda débil, ~290 nm) y π→π* (banda intensa, <250 nm)
- Estimación con HOMO-LUMO gap (limitaciones)
  - $\lambda \text{(nm)} \approx \frac{1239.8}{\Delta E \text{(eV)}}$
- TD-DFT: método para calcular estados excitados con mayor precisión
- Solvatación implícita (PCM): el disolvente como medio continuo dieléctrico
- Solvatocromismo: efecto del disolvente sobre λ_max
  - n→π*: blue shift en disolventes polares (estabilización del estado fundamental polar)

**Procedimiento: un cálculo completo (ejemplo: acetona en ciclohexano)**
- Paso 1: Dibujar acetona en GaussView
- Paso 2: Optimizar geometría primero (Job Type: Optimization, B3LYP/6-311G)
- Paso 3: Sobre la geometría optimizada, configurar TD-DFT
  - Job Type: TD-SCF (o Energy con keyword `td`)
  - Additional Keywords: `scrf=(solvent=cyclohexane) td`
  - [TEXTO HUMANO: instrucciones exactas GaussView para TD-DFT + scrf]
- Paso 4: Lanzar y leer "Excited State 1" del .log
  - Identificar: longitud de onda (nm), fuerza del oscilador f, carácter (n→π* si f<0.01)
- Paso 5: Repetir para los 5 disolventes (ciclohexano, cloroformo, acetonitrilo, etanol, agua)
- [PROPUESTA: repetir para 2 cetonas más para ver efecto del sustituyente]

**Tabla de resultados** (el alumno la completa)
| Cetona | Disolvente | ε (constante dieléctrica) | λ_max n→π* (nm) | f |
|--------|-----------|---------------------------|-----------------|---|
| Acetona | ciclohexano | 2.0 | — | — |
| Acetona | cloroformo | 4.8 | — | — |
| Acetona | acetonitrilo | 37.5 | — | — |
| Acetona | etanol | 24.9 | — | — |
| Acetona | agua | 78.4 | — | — |

**Preguntas**
- [TEXTO HUMANO]
- [PROPUESTA]:
  1. ¿En qué dirección se desplaza la banda n→π* al aumentar la polaridad del disolvente? ¿Por qué?
  2. ¿Qué diferencia hay entre la banda n→π* y la π→π* en términos de intensidad (f)?
  3. ¿Qué sustituyente produce el mayor desplazamiento de λ_max respecto a la acetona pura?

---

## Notas transversales para todos los chats

- Cada sección con contenido nuevo de estudiante lleva `[TEXTO HUMANO]`
- Propuestas de Claude llevan `[PROPUESTA]` — requieren aceptación antes de incluirse
- Figuras sin captura real llevan `[FIGURA: descripción]`
- Keywords que confirmar con laboratorio llevan `[CONFIRMAR]`
- Usar admonitions MyST: `{note}`, `{warning}`, `{tip}` en vez de texto plano para avisos
- Ecuaciones en LaTeX entre `$...$` (inline) o `$$...$$` (bloque)
