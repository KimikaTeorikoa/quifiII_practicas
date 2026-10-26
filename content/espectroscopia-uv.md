# P2-D: Espectroscopía UV-Vis de Cetonas

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA - NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto (3-4 líneas). Motivación sobre la espectroscopía electrónica ultravioleta-visible en la caracterización de cromóforos orgánicos. Absorción de fotones mediante transiciones de capa de valencia en compuestos carbonílicos y sensibilidad espectral frente a la polaridad del medio disolvente (solvatocromismo).

:::{note}
[TEXTO HUMANO: introducción y motivación sobre espectroscopía UV-Vis de cromóforos carbonílicos]
:::

---

## Objetivos

Párrafo corto (lista numerada). Objetivos formativos de la sesión:
1. Estimación preliminar de longitudes de onda de absorción a partir de la diferencia energética orbital HOMO-LUMO.
2. Cálculo de estados electrónicos excitados singlete mediante el método TD-DFT con funcional híbrido B3LYP/6-311G.
3. Caracterización y asignación de transiciones $n \rightarrow \pi^*$ y $\pi \rightarrow \pi^*$ mediante energías de transición y fuerza del oscilador ($f$).
4. Evaluación del desplazamiento solvatocrómico en acetona utilizando el modelo continuo de polarización del disolvente (PCM).
5. Análisis del efecto electrónico de sustituyentes sobre el grupo carbonilo en una serie homóloga de cetonas.

:::{note}
[TEXTO HUMANO: lista de objetivos formativos adaptada al guion del curso]
:::

---

## ¿Qué software vamos a usar?

Párrafo muy corto. Referencia al uso combinado de GaussView para la parametrización de cálculos de estados excitados y solvatación continua, y {{gaussian_version}} para la resolución de las ecuaciones TD-DFT y PCM.

---

## Conceptos clave

### Transiciones electrónicas en compuestos carbonílicos

Párrafo medio + figura. Promoción de electrones de valencia desde orbitales ocupados a orbitales virtuales desocupados. Distinción entre la transición $n \rightarrow \pi^*$ (electrón no enlazante del oxígeno al orbital antienlazante $\pi^*$ del carbonilo, prohibida por simetría, baja fuerza de oscilador, $\lambda \approx 280-300\text{ nm}$) y la transición $\pi \rightarrow \pi^*$ (orbital enlazante $\pi$ al antienlazante $\pi^*$, permitida, alta fuerza de oscilador, $\lambda < 250\text{ nm}$).

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: analogía de orbitales moleculares y saltos cuánticos inducidos por absorción de radiación ultravioleta]
:::

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: diagrama de niveles de orbitales moleculares del grupo carbonilo con flechas de transición n a pi* y pi a pi*]
```

### El gap HOMO-LUMO como estimación preliminar

Párrafo medio + tabla. Relación directa entre la diferencia de energías orbitales y la energía de excitación elemental. Expresiones de conversión de unidades atómicas a electronvoltios y longitud de onda en nanómetros. Discusión de aproximaciones implícitas (orbitales no relajados e ignorancia de repulsión entre estados excitados).

$$\Delta E_{\text{gap}}\text{ (eV)} = (\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}) \times {{ha_to_ev}}$$

$$\lambda_{\text{estimada}}\text{ (nm)} = \frac{1239.8}{\Delta E_{\text{gap}}\text{ (eV)}}$$

Ejemplo metodológico de referencia con autovalores del formaldehído en acetonitrilo:

| Nivel | Energía (Ha) |
|---|:---:|
| HOMO | −0.27636 |
| LUMO | −0.06005 |
| Gap (Ha) | 0.21631 |
| Gap (eV) | 5.89 |
| $\lambda$ estimada (nm) | 210 |

### Fundamento del método TD-DFT

Párrafo medio. Descripción del formalismo de DFT dependiente del tiempo para evaluar respuestas a perturbaciones electromagnéticas dinámicas. Concepto de fuerza del oscilador ($f$) como magnitud proporcional a la probabilidad de transición y a la intensidad de la banda observada.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicación de fuerza del oscilador como probabilidad de absorción cuántica y su correlación con la intensidad de pico]
:::

### Efecto del disolvente: solvatocromismo

Párrafo medio + tabla. Modelo de polarización continua (PCM) para el disolvente. Mecanismo de estabilización diferencial del estado fundamental dipolar frente al estado excitado menos polar en la transición $n \rightarrow \pi^*$, con el consiguiente ensanchamiento del gap energético y desplazamiento hacia longitudes de onda menores (desplazamiento al azul o hipsocrómico).

Valores experimentales de referencia para acetona:

| Disolvente | $\lambda\ (n \rightarrow \pi^*)$ experimental (nm) |
|---|:---:|
| Ciclohexano (apolar) | 279 |
| Agua (muy polar) | 264 |
| Variación ($\Delta \lambda$) | −15 nm (desplazamiento al azul) |

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicación intuitiva de solvatación preferente del par solitario en estado fundamental y aumento del gap en disolventes próticos polares]
:::

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la línea final exacta:
{{termination_ok}}
:::

### Parte A: Estimación preliminar con el gap HOMO-LUMO

#### Paso A1: Optimizar la geometría en disolvente

Párrafo corto + tabla + figura. Construcción de la molécula de acetona en GaussView. Configuración en **Calculate → Gaussian Calculation Setup**: Job Type Optimization, Method B3LYP, Basis Set 6-311G, Charge 0, Spin 1, y palabra clave `scrf=(solvent=acetonitrile)` en Additional Keywords.

| Campo | Valor |
|---|---|
| Job Type | Optimization |
| Method | B3LYP |
| Basis Set | 6-311G |
| Charge | 0 |
| Spin (Multiplicity) | 1 |
| Additional Keywords | `scrf=(solvent=acetonitrile)` |

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: configuración de optimización de geometría de acetona en GaussView con palabra clave scrf]
```

#### Paso A2: Extraer autovalores HOMO y LUMO

Párrafo corto + figura. Búsqueda de las líneas `Alpha occ. eigenvalues` y `Alpha virt. eigenvalues` en el `.log` optimizado. Lectura de energías en Hartrees y cálculo de la longitud de onda estimada en nanómetros.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: líneas de autovalores Alpha occ y virt en el archivo .log destacando las energías de HOMO y LUMO]
```

---

### Parte B: Cálculo TD-DFT del espectro de absorción

#### Paso B1: Configurar el cálculo TD-DFT

Párrafo corto + figura. Apertura de la estructura optimizada previa en GaussView. Configuración de cálculo Job Type Energy con palabras clave `td scrf=(solvent=acetonitrile) geom=connectivity` en la pestaña Additional Keywords.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: pestaña Additional Keywords con las palabras clave td y scrf introducidas para el cálculo TD-DFT]
```

#### Paso B2: Extraer datos de los estados excitados del .log

Párrafo medio + tabla + figura. Búsqueda de la sección `Excited State 1` en el archivo `.log`. Registro de los cuatro parámetros característicos de la transición: energía en eV, longitud de onda ($\lambda$ en nm), fuerza del oscilador ($f$) y contribuciones orbitales.

Campos del bloque de estado excitado:

| Campo | Significado físico |
|---|---|
| Simetría de estado | Representación irreducible del estado excitado |
| Energía (eV) | Diferencia energética entre estado fundamental y excitado |
| Longitud de onda (nm) | Posición del máximo de absorción en el espectro |
| Fuerza del oscilador ($f$) | Intensidad relativa de la banda espectral |
| Contribución orbital | Índices de los orbitales ocupados y virtuales implicados |

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: bloque de Excited State 1 en el archivo .log con valores de energía, longitud de onda y fuerza de oscilador]
```

#### Paso B3: Visualizar el espectro en GaussView

Párrafo corto + figura. Apertura de **Results → UV-Vis** para observar la convolución de estados excitados y contrastar la banda débil $n \rightarrow \pi^*$ frente a la banda intensa $\pi \rightarrow \pi^*$.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Results → UV-Vis en GaussView mostrando el espectro electrónico de acetona con bandas señaladas]
```

---

### Parte C: Serie de disolventes y solvatocromismo

Párrafo medio + tabla. Procedimiento para repetir el cálculo TD-DFT en acetona modificando la palabra clave de disolvente en `scrf=(solvent=...)` para seis medios de constante dieléctrica creciente.

| Disolvente | Constante dieléctrica ($\varepsilon$) | Palabra clave en Additional Keywords |
|---|:---:|---|
| Vacío (gas) | 1.0 | *(sin palabra clave scrf)* |
| Ciclohexano | 2.0 | `scrf=(solvent=cyclohexane)` |
| Cloroformo | 4.8 | `scrf=(solvent=chloroform)` |
| Etanol | 24.9 | `scrf=(solvent=ethanol)` |
| Acetonitrilo | 37.5 | `scrf=(solvent=acetonitrile)` |
| Agua | 78.4 | `scrf=(solvent=water)` |

---

### Parte D: Serie de cetonas sustituidas

Párrafo medio + tabla. Protocolo de cálculo para optimizar y calcular el estado excitado $n \rightarrow \pi^*$ en cinco cetonas y derivados carbonílicos en medio acetonitrilo. Recomendación operativa de organización en subcarpetas para gestionar los archivos de cálculo.

| Compuesto | Estructura química | Denominación |
|---|---|---|
| Acetona | CH₃–CO–CH₃ | Propanona |
| Cloruro de acetilo | CH₃–CO–Cl | Cloruro de etanoilo |
| Acetofenona | CH₃–CO–C₆H₅ | 1-feniletanona |
| Ácido acético | CH₃–CO–OH | Ácido etanoico |
| Metil-etil-cetona | CH₃–CO–CH₂CH₃ | Butanona |

:::{warning}
Cada molécula requiere una optimización geométrica previa en disolvente antes de ejecutar el cálculo TD-DFT correspondiente.
:::

---

## Resultados y análisis

### Tabla A: Estimación del gap HOMO-LUMO para acetona

Párrafo corto + tabla. Registro de autovalores de energía orbital y cálculo de longitud de onda estimada para acetona en los diferentes disolventes.

| Disolvente | HOMO (Ha) | LUMO (Ha) | Gap (Ha) | Gap (eV) | $\lambda$ estimada (nm) |
|---|:---:|:---:|:---:|:---:|:---:|
| Vacío | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Ciclohexano | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Acetonitrilo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Agua | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Tabla B: Solvatocromismo de acetona por TD-DFT

Párrafo corto + tabla. Vaciado de longitudes de onda calculadas por TD-DFT y fuerzas de oscilador frente a datos experimentales disponibles.

| Disolvente | $\lambda$ calculada (nm) | $f$ calculada | $\lambda$ experimental (nm) | Desviación (nm) |
|---|:---:|:---:|:---:|:---:|
| Ciclohexano | [TEXTO HUMANO] | [TEXTO HUMANO] | 279 | [TEXTO HUMANO] |
| Agua | [TEXTO HUMANO] | [TEXTO HUMANO] | 264 | [TEXTO HUMANO] |
| Acetonitrilo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Etanol | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Cloroformo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Tabla C: Efecto del sustituyente en la banda n a pi*

Párrafo corto + tabla. Comparación sistemática de longitudes de onda y fuerzas de oscilador para las cinco cetonas evaluadas en medio acetonitrilo.

| Compuesto | $\lambda$ calculada (nm) | $f$ calculada | Comentario sobre el desplazamiento |
|---|:---:|:---:|---|
| Acetona | [TEXTO HUMANO] | [TEXTO HUMANO] | Referencia |
| Cloruro de acetilo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Acetofenona | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Ácido acético | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Metil-etil-cetona | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Directrices de recogida de datos

Párrafo corto. Pautas metodológicas para transferir con exactitud los valores de $\lambda$ y $f$ desde el archivo `.log` o desde el panel de visualización espectral de GaussView hacia las tablas del informe.

---

## Preguntas y pruebas

Párrafo corto (cuestionario de análisis e interpretación). Cuestiones formativas para consolidar la interpretación fotofísica de los resultados:
1. Magnitud del error y dirección de la discrepancia sistemática entre la estimación estática del gap HOMO-LUMO y el cálculo TD-DFT de estados excitados.
2. Sentido del desplazamiento de la banda $n \rightarrow \pi^*$ al incrementar la polaridad del medio disolvente y justificación mediante interacción soluto-disolvente.
3. Influencia del sustituyente en posición alfa sobre el máximo de absorción carbonílico: correlación con conjugación electrónica del anillo aromático en acetofenona o efectos inductivos en cloruro de acetilo.
4. Diferencia de magnitud en la fuerza del oscilador entre la transición $n \rightarrow \pi^*$ ($f \approx 10^{-4}$) y $\pi \rightarrow \pi^*$ ($f > 0.1$) y su reflejo en la absorbancia experimental.
5. Grado de acuerdo entre los resultados calculados por TD-DFT en disolventes próticos y las mediciones de laboratorio reportadas en literatura.

:::{note}
[TEXTO HUMANO: formulación detallada de preguntas y criterios de corrección]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 13 (Espectroscopía electrónica).
- Casida, M. E. *Time-Dependent Density Functional Theory for Molecules*. In *Recent Advances in Density Functional Methods*; World Scientific, 1995.
- NIST Chemistry WebBook, https://webbook.nist.gov (espectros de absorción ultravioleta-visible de referencia).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Párrafo medio. Ejercicio opcional sobre la simulación de espectros UV-Vis continuos mediante convolución gaussiana de los estados discretos calculados, y contraste gráfico entre la aproximación estática de gap y TD-DFT para la serie de cetonas.

:::{note}
[TEXTO HUMANO: instrucciones para exportar estados excitados y generar el perfil de absorbancia espectral convolucionado]
:::
::::
