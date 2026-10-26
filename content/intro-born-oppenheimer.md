# Geometría molecular y la aproximación de Born-Oppenheimer

## Introducción

:::{note}
[TEXTO HUMANO: Plantear la determinación de las posiciones nucleares como el requisito geométrico fundamental para el cómputo de cualquier propiedad molecular mecanocuántica. Longitud: 2-3 frases.]
:::

---

## La aproximación de Born-Oppenheimer

:::{note}
[TEXTO HUMANO: Justificar la separación del movimiento nuclear y electrónico a partir de la acusada diferencia de masas, formulando el cálculo de la densidad electrónica bajo la premisa de núcleos estacionarios. Longitud: 4-5 frases.]
[ECUACIÓN: ecuación de Schrödinger electrónica paramétrica en Born-Oppenheimer, $\hat{H}_{\text{elec}}\Psi_{\text{elec}}(\mathbf{r}; \mathbf{R}) = E_{\text{elec}}(\mathbf{R})\Psi_{\text{elec}}(\mathbf{r}; \mathbf{R})$]
:::

:::{admonition} 💡 Intuición
:class: intuicion
[TEXTO HUMANO: Analogía de una fotografía de larga exposición donde los centros nucleares permanecen estáticos y nítidos mientras la nube electrónica genera un contorno difuso continuo. Longitud: 2-3 frases.]
:::

---

## Geometría molecular: distancias, ángulos y diedros

:::{note}
[TEXTO HUMANO: Definir los tres parámetros de coordenadas internas que determinan la conformación espacial (longitud de enlace en Å, ángulo de enlace en grados y ángulo diedro de torsión en grados) empleando agua y etano como modelos. Longitud: 4-5 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: modelos moleculares con anotación explícita de distancia de enlace, ángulo planar y ángulo diedro de torsión]
:::

---

## Energía puntual: calcular sin mover

:::{note}
[TEXTO HUMANO: Describir el cálculo de energía puntual (Single Point) como una evaluación estática sobre una geometría fija sin modificar coordenadas, indicando su ruta de configuración en GaussView y su resultado en Hartrees. Longitud: 3-4 frases.]
:::

---

## Optimización de geometría: encontrar el mínimo

:::{note}
[TEXTO HUMANO: Explicar el algoritmo de optimización donde Gaussian calcula el gradiente de energía respecto a las coordenadas nucleares y desplaza los átomos siguiendo la máxima pendiente hasta que las fuerzas se anulan en un mínimo local. Longitud: 4-5 frases.]
[ECUACIÓN: condición de convergencia geométrica sobre la superficie de energía potencial, $\mathbf{g} = -\nabla_{\mathbf{R}} E(\mathbf{R}) \approx \mathbf{0}$]
:::

:::{admonition} 💡 Intuición
:class: intuicion
[TEXTO HUMANO: Analogía de una esfera rodando por la pendiente de un relieve topográfico hasta estabilizarse en el fondo de una cuenca. Longitud: 2-3 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: perfil energético frente a la coordenada de optimización mostrando pasos sucesivos convergentes hacia el mínimo]
:::

---

## ¿Cuándo usar Single Point y cuándo Optimization?

:::{note}
[TEXTO HUMANO: Criterios operativos para discernir cuándo aplicar un cálculo puntual frente a una relajación geométrica completa. Longitud: 2-3 frases.]
:::

| Situación | Job Type |
|---|---|
| Quiero la energía de una geometría específica (p.ej. escanear distancias a mano) | Single Point |
| Quiero la geometría de equilibrio real de la molécula | Optimization |

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional : libro de texto de química cuántica o equivalente)]`

---

::::{dropdown} ¿Qué pasa si la geometría inicial es muy mala?
:color: success

:::{note}
[TEXTO HUMANO: Advertir sobre los fallos de convergencia o caídas en mínimos no deseados cuando la estructura inicial está distorsionada, recomendando el empleo de fragmentos estándar de GaussView. Longitud: 3-4 frases.]
:::

::::

::::{dropdown} Más sobre gradientes y algoritmos de optimización
:color: success

:::{note}
[TEXTO HUMANO: Introducción cualitativa a los algoritmos de búsqueda basados en gradientes (descenso más pronunciado, quasi-Newton) y justificación del carácter iterativo del proceso. Longitud: 3-4 frases.]
:::

::::
