# El método de Hartree-Fock

## Introducción

:::{note}
[TEXTO HUMANO: Justificar la necesidad de métodos aproximados debido a que la ecuación de Schrödinger carece de solución analítica para sistemas polielectrónicos, situando a Hartree-Fock como el pilar conceptual de la estructura electrónica cuántica. Longitud: 3-4 frases.]
[ECUACIÓN: ecuación de Schrödinger independiente del tiempo, $\hat{H}\Psi = E\Psi$]
:::

---

## El problema: electrones que se repelen

:::{note}
[TEXTO HUMANO: Plantear el caso del átomo de helio con dos electrones y un núcleo, explicando cómo el operador de repulsión interelectrónica acopla las coordenadas espaciales e impide la separación exacta de variables. Longitud: 4-5 frases.]
:::

:::{admonition} 💡 Intuición
:class: intuicion
[TEXTO HUMANO: Analogía de dos personas que se evitan en una habitación cerrada sin poder predecir la posición de una sin conocer simultáneamente la de la otra. Longitud: 2-3 frases.]
:::

---

## La idea de Hartree-Fock: el campo medio

:::{note}
[TEXTO HUMANO: Explicar la aproximación de campo medio, donde cada electrón experimenta el potencial promediado generado por el resto de electrones, desacoplando las ecuaciones a costa de omitir la correlación electrónica instantánea. Longitud: 4-5 frases.]
:::

:::{admonition} 💡 Intuición
:class: intuicion
[TEXTO HUMANO: Analogía del flujo de tráfico vehicular, donde se modela la densidad media de circulación en lugar de la trayectoria individual de cada automóvil. Longitud: 2-3 frases.]
:::

---

## Orbitales: la solución para un electrón

:::{note}
[TEXTO HUMANO: Definir el concepto de orbital molecular como función monoelectrónica de distribución espacial y describir la configuración del estado fundamental del helio con dos electrones de espines apareados en el orbital 1s. Longitud: 4-5 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: representación de densidad electrónica del orbital 1s esférico del helio]
:::

---

## El ciclo SCF: resolver por iteración

:::{note}
[TEXTO HUMANO: Detallar el carácter autoconsistente del ciclo SCF, explicando las etapas secuenciales (adivinación inicial de coeficientes, cálculo del operador de Fock, diagonalización y comprobación de convergencia energética). Longitud: 4-5 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: diagrama de flujo del ciclo SCF iterativo indicando las etapas desde el guess inicial hasta la convergencia]
:::

---

## La matriz de Fock: lo que Gaussian resuelve

:::{note}
[TEXTO HUMANO: Presentar la formulación matricial de Roothaan-Hall que resuelve Gaussian, ejemplificando matrices de dimensiones 1x1 y 2x2 para ilustrar cómo los autovalores corresponden a las energías orbitales sin necesidad de desarrollos analíticos manuales. Longitud: 4-5 frases.]
[ECUACIÓN: ecuaciones de Roothaan-Hall en forma matricial, $\mathbf{F}\mathbf{C} = \mathbf{S}\mathbf{C}\boldsymbol{\varepsilon}$ con elementos de matriz $F_{\mu\nu}$ y $S_{\mu\nu}$]
:::

---

## Energías: orbital vs total

[CONFIRMAR CON PROFESOR: E(He) HF/STO-3G]

:::{note}
[TEXTO HUMANO: Clarificar la diferencia conceptual entre las energías orbitales monoelectrónicas y la energía electrónica total del sistema, advirtiendo que la suma directa de autovalores duplicaría el cómputo de la repulsión coulómbica. Longitud: 4-5 frases.]
[ECUACIÓN: relación entre la energía total Hartree-Fock y las energías orbitales, $E_{\text{HF}} = \sum_i \varepsilon_i - \frac{1}{2}\sum_{i,j}(J_{ij} - K_{ij}) + V_{NN}$]
:::

:::{warning}
La energía que aparece en el log de Gaussian es la energía total, no la energía de un orbital individual.
:::

---

## Limitaciones de HF: la correlación electrónica

:::{note}
[TEXTO HUMANO: Definir la energía de correlación como la discrepancia entre la energía del límite de Hartree-Fock y la solución exacta no relativista, justificando por qué las aplicaciones prácticas de laboratorio recurren a funcionales DFT como B3LYP. Longitud: 3-4 frases.]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: libro de texto de química cuántica recomendado (p.ej. Szabo & Ostlund, Levine, o equivalente)]`

---

::::{dropdown} La función de onda antisimétrica y el determinante de Slater
:color: success

:::{note}
[TEXTO HUMANO: Explicación conceptual del postulado de antisimetría de Pauli para fermiones y formulación del determinante de Slater como construcción matemática elemental. Longitud: 3-4 frases.]
[ECUACIÓN: determinante de Slater para $N$ electrones, $\Psi(\mathbf{x}_1, \dots, \mathbf{x}_N) = \frac{1}{\sqrt{N!}} \det|\chi_1 \cdots \chi_N|$]
:::

::::

::::{dropdown} Energía de correlación y métodos post-HF
:color: success

:::{note}
[TEXTO HUMANO: Resumen introductorio de metodologías post-Hartree-Fock (MP2, CCSD) orientadas a recuperar la energía de correlación dinámica omitida en campo medio. Longitud: 3-4 frases.]
:::

::::
