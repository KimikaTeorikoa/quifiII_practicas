# P2-B: Superficie de Energía Potencial

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA - NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto (3-4 líneas). Motivación química sobre el origen de las fuerzas que mantienen unidos los átomos en una molécula. Dependencia de la energía electrónica respecto a las coordenadas nucleares (aproximación de Born-Oppenheimer). Estudio de la disociación en H₂ y de la rotación conformacional en dihaloetanos.

:::{note}
[TEXTO HUMANO: introducción y motivación química sobre superficies de energía potencial y enlace químico]
:::

---

## Objetivos

Párrafo corto (lista numerada). Objetivos formativos de la práctica:
1. Comprensión conceptual de una superficie de energía potencial (PES) en sistemas moleculares.
2. Cálculo de la PES de H₂ en función de la distancia internuclear $R(\text{H–H})$ para estados singlete y triplete.
3. Determinación de la distancia de equilibrio y contraste con el valor experimental.
4. Cálculo de la curva de torsión diedro en 1,2-dihaloetanos e identificación de confórmeros estables.
5. Representación gráfica y comparación de barreras rotacionales relativas.

:::{note}
[TEXTO HUMANO: lista de objetivos formativos adaptada al guion del curso]
:::

---

## ¿Qué software vamos a usar?

Párrafo muy corto. Referencia al uso de GaussView para la preparación gráfica de coordenadas internas de barrido y {{gaussian_version}} para la ejecución de cálculos tipo Scan.

---

## Conceptos clave

### ¿Qué es una superficie de energía potencial?

Párrafo medio + figura. Concepto de paisaje energético en el marco de la aproximación de Born-Oppenheimer. Significado físico de mínimos locales y globales (geometrías de equilibrio), estados de transición (barreras) y asíntotas de disociación.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: analogía del paisaje topográfico y movimiento en valles de energía estable]
:::

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: curva esquemática unidimensional de PES con mínimo, barrera y asíntota de disociación anotados]
```

### Singlete y triplete: por qué importa el espín

Párrafo medio. Contraste entre estados de espín en la molécula de H₂: singlete (espines antiparalelos, densidad electrónica internuclear compartida y formación de enlace) frente a triplete (espines paralelos, repulsión cuántica de Pauli y curva puramente repulsiva).

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicación cualitativa de espines paralelos y principio de exclusión de Pauli en la interacción interatómica]
:::

### Ángulo diedro y análisis conformacional

Párrafo medio + figura. Definición geométrica del ángulo diedro de torsión entre cuatro átomos enlazados (X–C–C–X). Relación con proyecciones de Newman y clasificación conformacional: confórmero anti (mínimo global), confórmero gauche (mínimo local) y conformaciones eclipsadas (máximos de barrera).

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: analogía de rotación de aspas o hélices y proyecciones de Newman para confórmeros rotacionales]
:::

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: diagrama de Newman de 1,2-dicloroetano con confórmeros anti y gauche identificados]
```

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la línea final exacta:
{{termination_ok}}
:::

### Parte 1: PES de la molécula de H₂

#### Paso 1: Dibujar H₂ en GaussView

Párrafo muy corto + figura. Adición de dos centros de hidrógeno unidos por enlace simple en la ventana de dibujo de GaussView.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: molécula H2 dibujada en GaussView con enlace simple visible]
```

#### Paso 2: Configurar el cálculo de barrido (Scan)

Párrafo medio + tabla + figura. Acceso a **Calculate → Gaussian Calculation Setup**. Selección de Job Type Relaxed PES Scan, Method HF/STO-3G, Charge 0, Spin 1 (singlete) y repetición con Spin 3 (triplete). Configuración de la coordenada internuclear $R(\text{H–H})$ y sus límites.

| Campo | Singlete | Triplete |
|---|:---:|:---:|
| Job Type | Relaxed PES Scan | Relaxed PES Scan |
| Method | HF | HF |
| Basis Set | STO-3G | STO-3G |
| Charge | 0 | 0 |
| Spin (Multiplicity) | 1 | 3 |
| Additional Keywords | `geom=connectivity` | `geom=connectivity` |

Parámetros de barrido internuclear:

| Parámetro | Valor |
|---|---|
| Coordenada | $R(\text{H}_1\text{–H}_2)$ |
| Valor inicial | 0.55 Å |
| Incremento de paso | 0.05 Å |
| Número de pasos | 21 |
| Valor final | 1.55 Å |

:::{warning}
Introducir los parámetros de incremento y número de pasos con exactitud para asegurar una malla geométrica homogénea en ambos estados de espín.
:::

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup con selección de Job Type Relaxed PES Scan y parámetros del enlace H-H]
```

#### Paso 3: Lanzar y verificar

Párrafo corto. Guardado de archivos `.gjf` en `{{practicas_folder}}PES/` con nombres descriptivos (`H2_singlete_scan_STO3G.gjf` y `H2_triplete_scan_STO3G.gjf`), supervisión de los 21 puntos calculados y verificación de salida normal.

#### Paso 4: Visualizar la curva en GaussView

Párrafo muy corto + figura. Acceso a la herramienta interactiva **Results → Scan** para examinar la curva energética resultante y la localización del mínimo.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: gráfica interactiva en GaussView Results → Scan mostrando la curva del singlete de H2 con su mínimo]
```

#### Paso 5: Extraer energías y calcular valores relativos

Párrafo corto. Búsqueda secuencial de las 21 líneas `SCF Done` en el `.log`, anotación de energías en Hartrees y cálculo de la energía potencial relativa referida al mínimo en kcal/mol.

$$\Delta E(R) = \bigl[E(R) - E_{\min}\bigr] \times {{ha_to_kcal}} \quad [\text{kcal/mol}]$$

---

### Parte 2: PES diedro de los dihaloetanos

Párrafo corto + tabla. Extensión metodológica del barrido unidimensional al ángulo de torsión en 1,2-dihaloetanos homólogos con halógenos de volumen creciente.

| Compuesto | Halógeno | Fórmula molecular | Código |
|---|---|---|:---:|
| 1,2-dicloroetano | Cl | ClCH₂–CH₂Cl | DCE |
| 1,2-dibromoetano | Br | BrCH₂–CH₂Br | DBE |
| 1,2-diyodoetano | I | ICH₂–CH₂I | DIE |

#### Paso 1: Dibujar el dihaloetano en GaussView

Párrafo corto + figura. Construcción del esqueleto C–C, adición de halógenos e hidrógenos correspondientes y optimización estructural inicial con **Edit → Clean**.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: estructura tridimensional de 1,2-dicloroetano construida en GaussView]
```

#### Paso 2: Configurar el barrido del ángulo diedro

Párrafo medio + tabla. Definición de la coordenada de torsión X–C–C–X en el panel de cálculo y especificación de parámetros angulares de 0° a 360°.

| Parámetro | Valor |
|---|---|
| Coordenada | Diedro X–C–C–X |
| Valor inicial | 0° `[CONFIRMAR CON PROFESOR]` |
| Incremento angular | 10° `[CONFIRMAR CON PROFESOR]` |
| Número de puntos | 36 `[CONFIRMAR CON PROFESOR]` |
| Método y base | `[CONFIRMAR CON PROFESOR: método y base recomendados para halógenos]` |

:::{warning}
El cálculo de barrido conformacional en moléculas poliatómicas requiere mayor tiempo de procesador. Ejecutar secuencialmente para DCE, DBE y DIE.
:::

#### Paso 3: Lanzar, verificar y extraer datos

Párrafo corto. Guardado de los inputs en `{{practicas_folder}}PES/`, verificación de terminación normal en cada archivo `.log` y extracción de las energías relativas frente al ángulo diedro.

---

## Resultados y análisis

### Tabla 1: PES de H₂ (energías calculadas)

Párrafo corto + tabla. Registro de las energías absolutas de `SCF Done` y evaluación de las energías relativas $\Delta E$ en kcal/mol para los 21 puntos calculados.

| Punto | $R$ (Å) | $E$ singlete (Ha) | $E$ triplete (Ha) | $\Delta E$ singlete (kcal/mol) | $\Delta E$ triplete (kcal/mol) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.55 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 2 | 0.60 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 3 | 0.65 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 4 | 0.70 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 5 | 0.75 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 6 | 0.80 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 7 | 0.85 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 8 | 0.90 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 9 | 0.95 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 10 | 1.00 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 11 | 1.05 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 12 | 1.10 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 13 | 1.15 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 14 | 1.20 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 15 | 1.25 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 16 | 1.30 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 17 | 1.35 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 18 | 1.40 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 19 | 1.45 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 20 | 1.50 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 21 | 1.55 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Gráfico de la PES de H₂

Párrafo corto + figura. Procedimiento para representar $\Delta E$ (kcal/mol) frente a $R$ (Å) superponiendo singlete y triplete en un mismo gráfico mediante LibreOffice Calc u hoja de cálculo externa.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: gráfico con las dos curvas superpuestas de H2: singlete con pozo de potencial y triplete repulsivo]
```

### Tablas 2 a 4: Curvas de torsión diedro en dihaloetanos

Párrafo corto + tabla de estructura modelo. Organización de datos para el vaciado de energías en función del ángulo diedro (0° a 360°) para DCE, DBE y DIE.

| Diedro (°) | $E$ DCE (Ha) | $\Delta E$ DCE (kcal/mol) | $E$ DBE (Ha) | $\Delta E$ DBE (kcal/mol) | $E$ DIE (Ha) | $\Delta E$ DIE (kcal/mol) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 60 (gauche) | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 120 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 180 (anti) | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 240 (gauche) | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 300 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 360 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Gráfico comparativo de barreras rotacionales

Párrafo corto. Representación gráfica superpuesta de las tres curvas de energía potencial conformacional frente al ángulo diedro (0°–360°) para evidenciar el incremento de la barrera con el radio de Van der Waals del halógeno.

---

## Preguntas y pruebas

Párrafo corto (cuestionario de análisis e interpretación). Cuestiones clave para la discusión en el informe:
1. Posición del mínimo de energía en la curva del singlete de H₂ y comparación con el valor experimental (0.74 Å).
2. Justificación mecanocuántica de la ausencia de enlace estable en el triplete de H₂.
3. Comportamiento asintótico de ambas curvas de H₂ a distancias internucleares elevadas y su límite de disociación.
4. Identificación de los ángulos diedro correspondientes a los confórmeros anti, gauche y eclipsado en el 1,2-dicloroetano.
5. Efecto del tamaño del átomo de halógeno (Cl vs Br vs I) sobre la altura de la barrera de rotación conformacional.
6. Estimación de la probabilidad de rotación libre a temperatura ambiente considerando la energía térmica media ($kT \approx 0.6\text{ kcal/mol}$ a 300 K).

:::{note}
[TEXTO HUMANO: formulación detallada de preguntas y criterios de evaluación]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 11 (Estructura molecular y superficies de energía potencial).
- Clayden, J.; Greeves, N.; Warren, S. *Organic Chemistry*, 2ª ed.; Oxford University Press, 2012. Cap. 18 (Conformational analysis).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Párrafo medio. Estudio opcional de la barrera de rotación interna en el etano no sustituido (CH₃–CH₃). Comparación de la magnitud energética de la barrera debida exclusivamente a repulsiones C–H frente a la presencia de halógenos voluminosos.

:::{note}
[TEXTO HUMANO: pautas para configurar el cálculo de torsión en etano e interpretar la contribución estérica e hiperconjugativa]
:::
::::
