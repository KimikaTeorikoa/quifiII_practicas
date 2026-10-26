# P2-A: Átomos y el Teorema de Koopmans

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA - NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto (3-4 líneas). Motivación química sobre la energía de ionización y su relación con las tendencias periódicas en la tabla periódica. Contraste del modelo teórico Hartree-Fock frente a datos experimentales e interpretación física del orbital más alto ocupado (HOMO).

:::{note}
[TEXTO HUMANO: introducción y motivación química sobre tendencias periódicas de energía de ionización]
:::

---

## Objetivos

Párrafo corto (lista numerada). Objetivos de aprendizaje de la sesión práctica:
1. Realización de cálculos de energía electrónica en átomos aislados mediante GaussView y {{gaussian_version}}.
2. Determinación de la energía de ionización por dos métodos: diferencia de energías totales ($\Delta E$) y teorema de Koopmans.
3. Comparación sistemática de los valores calculados con datos experimentales para los elementos del primer y segundo período.
4. Visualización tridimensional e interpretación de la simetría de los orbitales atómicos HOMO.

:::{note}
[TEXTO HUMANO: lista de objetivos formativos adaptada al guion del curso]
:::

---

## ¿Qué software vamos a usar?

Párrafo muy corto. Referencia al uso combinado de GaussView como entorno gráfico interactivo y {{gaussian_version}} como motor de cálculo de estructura electrónica. Consulta previa obligatoria de la guía de introducción a GaussView.

---

## Conceptos clave

### ¿Por qué las energías son negativas?

Párrafo corto. Explicación cualitativa del origen del signo negativo en sistemas ligados frente a partículas en reposo separadas en el infinito. Interpretación del pozo de potencial atractivo núcleo-electrón y comprobación de coherencia física en la salida del cálculo.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: analogía del pozo de potencial y estabilidad de sistemas ligados, sin fórmulas matemáticas]
:::

### El HOMO y el LUMO

Párrafo corto + figura. Definición de orbitales frontera: orbital ocupado de mayor energía (HOMO) y primer orbital desocupado (LUMO). Relación entre el nivel energético del electrón más externo y la energía necesaria para su remoción.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: analogía de niveles energéticos discretos y extracción del electrón del nivel más externo]
:::

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: diagrama de niveles de orbitales con HOMO y LUMO señalados y flecha indicando energía de ionización]
```

### La energía de ionización y el Teorema de Koopmans

Párrafo medio. Definición de energía de ionización para un átomo neutro en fase gas ($A \rightarrow A^+ + e^-$). Formulación de las dos vías metodológicas de evaluación cuántica: cálculo autoconsistente del catión (vía $\Delta E$) y aproximación por energía orbital (teorema de Koopmans).

$$\text{IE}_{\Delta E} = E(A^+) - E(A)$$

$$\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}$$

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: justificación de las discrepancias entre ambas vías, aproximación de orbitales congelados y ausencia de correlación electrónica instantánea en Hartree-Fock]
:::

### La multiplicidad de espín

Párrafo corto + tabla. Regla $2S+1$ para la multiplicidad a partir de electrones desapareados. Importancia de la asignación exacta en capas abiertas para evitar estados de espín erróneos o fallos de convergencia SCF.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicación cualitativa de espines electrónicos paralelos y apareados]
:::

:::{warning}
Verificar siempre el valor de multiplicidad de espín antes de enviar el cálculo: un valor incorrecto invalida los resultados o impide la convergencia SCF.
:::

### Unidades de energía

Párrafo muy corto. Uso de unidades atómicas (Hartrees) en el motor de cálculo y factor de conversión a electronvoltios (eV) para la comparación experimental.

$$1\text{ Ha} = {{ha_to_ev}}\text{ eV}$$

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la línea final exacta:
{{termination_ok}}
:::

### Paso 1: Abrir GaussView y dibujar el átomo

Párrafo muy corto + figura. Apertura de la interfaz gráfica, selección del elemento químico correspondiente en la tabla periódica (**View → Element Fragments**) e inserción de un único centro atómico aislado en el espacio de trabajo.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana principal de GaussView con un único centro atómico sin enlaces]
```

### Paso 2: Configurar el cálculo del átomo neutro

Párrafo medio + tabla + figura. Acceso al panel **Calculate → Gaussian Calculation Setup**. Selección de opciones: Job Type Energy, Method HF, Basis Set STO-3G, Charge 0, y asignación de multiplicidad de espín según el átomo. Inclusión de la palabra clave `pop=full` en la pestaña Additional Keywords para obtener la totalidad de energías orbitales.

| Campo | Valor |
|---|---|
| Job Type | Energy |
| Method | HF |
| Basis Set | STO-3G |
| Charge | 0 |
| Spin (Multiplicity) | Según configuración electrónica (ver tabla) |
| Additional Keywords | `pop=full` |

Tabla de multiplicidades de referencia ($2S+1$):

| Átomo | $Z$ | Configuración | Multiplicidad |
|---|:---:|---|:---:|
| H | 1 | 1s¹ | 2 |
| He | 2 | 1s² | 1 |
| Li | 3 | [He] 2s¹ | 2 |
| Be | 4 | [He] 2s² | 1 |
| B | 5 | [He] 2s² 2p¹ | 2 |
| C | 6 | [He] 2s² 2p² | 3 |
| N | 7 | [He] 2s² 2p³ | 4 |
| O | 8 | [He] 2s² 2p⁴ | 3 |
| F | 9 | [He] 2s² 2p⁵ | 2 |
| Ne | 10 | [He] 2s² 2p⁶ | 1 |

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup con pestaña Method y Additional Keywords pop=full]
```

### Paso 3: Lanzar el cálculo y guardar el archivo

Párrafo corto. Envío mediante botón Submit, guardado del archivo `.gjf` en la ruta de trabajo `{{practicas_folder}}` bajo nomenclatura descriptiva (elemento, estado y método), y estimación de tiempo de cómputo en segundos.

`[CONFIRMAR CON PROFESOR: ruta exacta del directorio de trabajo en las estaciones del laboratorio]`

### Paso 4: Verificar la terminación correcta

Párrafo muy corto + figura. Apertura del archivo de salida `.log` en el editor de texto y desplazamiento a la última línea para comprobar la terminación normal.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: sección final del archivo .log con el mensaje de terminación correcta de Gaussian]
```

### Paso 5: Leer la energía total E(N)

Párrafo corto. Búsqueda de la cadena `SCF Done` en el `.log` y lectura del autovalor de energía total en Hartrees (`E(RHF)` para capa cerrada o `E(ROHF)` para capa abierta).

### Paso 6: Leer la energía orbital del HOMO

Párrafo corto. Búsqueda de la sección `Alpha occ. eigenvalues` en el `.log`. Identificación del último autovalor ocupado ($\varepsilon_{\text{HOMO}}$) y del primer autovalor de la línea `Alpha virt.` ($\varepsilon_{\text{LUMO}}$).

### Paso 7: Configurar y calcular el catión A⁺

Párrafo medio + tabla. Duplicación del cálculo para la especie catiónica modificando los campos en la pestaña **Method**: Charge = +1 y ajuste de la multiplicidad de espín correspondiente al número de electrones resultante.

| Campo | Neutro | Catión |
|---|:---:|:---:|
| Charge | 0 | +1 |
| Spin | Multiplicidad neutro | Multiplicidad catión |

:::{note}
[TEXTO HUMANO: explicación de la deducción de multiplicidad catiónica tras la extracción del electrón HOMO]
:::

### Paso 8: Calcular las energías de ionización

Párrafo corto. Aplicación de las expresiones de conversión para obtener las energías de ionización en electronvoltios (eV).

$$\text{IE}_{\Delta E} = \bigl[E(A^+) - E(A)\bigr] \times {{ha_to_ev}} \quad [\text{eV}]$$

$$\text{IE}_{\text{Koopmans}} = -\varepsilon_{\text{HOMO}} \times {{ha_to_ev}} \quad [\text{eV}]$$

---

## Resultados y análisis

Párrafo corto + tabla. Recopilación de los datos extraídos de los archivos `.log` y cálculo de las desviaciones porcentuales respecto a los valores experimentales tabulados.

| Átomo | $E(N)$ (Ha) | $E(A^+)$ (Ha) | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\Delta E}$ (eV) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| H | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 13.60 | [TEXTO HUMANO] |
| He | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 24.59 | [TEXTO HUMANO] |
| Li | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 5.39 | [TEXTO HUMANO] |
| Be | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 9.32 | [TEXTO HUMANO] |
| B | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 8.30 | [TEXTO HUMANO] |
| C | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| N | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 14.53 | [TEXTO HUMANO] |
| O | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 13.62 | [TEXTO HUMANO] |
| F | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 17.42 | [TEXTO HUMANO] |
| Ne | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 21.56 | [TEXTO HUMANO] |

### Visualización de orbitales

Párrafo corto + figura. Procedimiento en GaussView para acceder al menú **Results → MOs**, selección de isosuperficie tridimensional del orbital HOMO y ajuste del valor de contorno para examinar simetrías tipo s frente a lóbulos nodales p.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: isosuperficie tridimensional del orbital HOMO del carbono en GaussView Results → MOs]
```

:::{note}
[TEXTO HUMANO: descripción comparativa de la morfología del HOMO a lo largo del período y presencia de planos nodales]
:::

---

## Preguntas y pruebas

Párrafo corto (preguntas de reflexión e interpretación). Batería de cuestiones para consolidar la comprensión física de los resultados:
1. Grado de concordancia entre IE$_{\Delta E}$ e IE$_{\text{Koopmans}}$ a lo largo de la serie y causas físicas de las mayores divergencias.
2. Reproducción de las tendencias periódicas generales e interpretación de anomalías locales (como la caída de IE entre N y O según la regla de Hund, o entre Be y B).
3. Comparación morfológica entre el orbital HOMO del hidrógeno (simetría esférica) y del carbono (lóbulos con plano nodal).
4. Magnitud relativa de los errores asociados a cada vía y factores no considerados por Hartree-Fock.
5. Consecuencias operativas de introducir una multiplicidad de espín incorrecta y mecanismos de detección en el archivo `.log`.

:::{note}
[TEXTO HUMANO: formulación detallada de preguntas y criterios de corrección]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 9 (Estructura electrónica atómica).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Párrafo medio + tabla. Exploración voluntaria sobre el efecto del conjunto de base en el átomo de carbono neutro. Comparación sistemática de la energía del HOMO y la IE calculada al ampliar la base desde STO-3G hacia 3-21G y 6-311G.

| Base | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:---:|:---:|:---:|:---:|:---:|
| STO-3G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| 3-21G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| 6-311G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |

:::{note}
[TEXTO HUMANO: preguntas de profundización sobre la convergencia del error respecto al tamaño de la base]
:::
::::
