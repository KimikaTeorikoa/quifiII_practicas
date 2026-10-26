# Geometría molecular y la aproximación de Born-Oppenheimer

## Introducción

:::{note}
[TEXTO HUMANO: Motivación: para calcular cualquier propiedad de una molécula, lo primero que necesitamos es saber dónde están los átomos. La geometría es el punto de partida de todo. (Longitud: 2-3 frases)]
:::

---

## La aproximación de Born-Oppenheimer

:::{note}
[TEXTO HUMANO: Idea central: los núcleos son mucho más pesados que los electrones, se mueven mucho más despacio. En la práctica: tratamos los núcleos como fijos y calculamos cómo se distribuyen los electrones alrededor de ellos. Sin esta aproximación el problema sería irresoluble. (Longitud: 4-5 frases)]
:::

:::{admonition} Intuición
:class: intuicion
[TEXTO HUMANO: analogía: p.ej. fotografía de larga exposición donde los núcleos salen nítidos y los electrones borrosos]
:::

---

## Geometría molecular: distancias, ángulos y diedros

:::{note}
[TEXTO HUMANO: Los tres parámetros que definen una geometría: distancia de enlace (Å), ángulo de enlace (°), ángulo diedro (°). Figura esquemática con H₂O (distancia + ángulo) y una molécula sencilla con diedro (p.ej. etano). Los diedros se introducen aquí brevemente, aparecerán en detalle en P2-B. (Longitud: 4-5 frases)]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA o FIGURA: molécula con los tres parámetros geométricos anotados]
:::

---

## Energía puntual: calcular sin mover

:::{note}
[TEXTO HUMANO: Dado una geometría fija, Gaussian calcula la energía electrónica. Es como tomar una fotografía: la molécula no se mueve. En GaussView: Job Type → **Single Point**. Resultado: un número en Hartrees. (Longitud: 3-4 frases)]
:::

---

## Optimización de geometría: encontrar el mínimo

:::{note}
[TEXTO HUMANO: Gaussian no conoce la geometría real, la busca. Parte de la geometría que dibujó el alumno, calcula el gradiente (la pendiente de la energía respecto a cada coordenada), y mueve los átomos cuesta abajo. Repite hasta que el gradiente es prácticamente cero. (Longitud: 4-5 frases)]
:::

:::{admonition} Intuición
:class: intuicion
[TEXTO HUMANO: analogía: una bola rodando por un valle hasta detenerse en el punto más bajo]
:::

:::{admonition} Figura
:class: captura
[FIGURA: curva E vs coordenada con 3-4 pasos de optimización marcados y flecha al mínimo]
:::

---

## ¿Cuándo usar Single Point y cuándo Optimization?

:::{note}
[TEXTO HUMANO: Criterios para elegir entre cálculo puntual (Single Point) y optimización de geometría según el objetivo. (Longitud: 2-3 frases)]
:::

| Situación | Job Type |
|-----------|----------|
| Quiero la energía de una geometría específica (p.ej. escanear distancias a mano) | Single Point |
| Quiero la geometría de equilibrio real de la molécula | Optimization |

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional (libro de texto de química cuántica o equivalente)]`

---

::::{dropdown} ¿Qué pasa si la geometría inicial es muy mala?
:color: success

:::{note}
[TEXTO HUMANO: Si el alumno dibuja una geometría muy alejada del mínimo real, la optimización puede no converger o acabar en un mínimo equivocado. Señales de alerta en el log. Consejo práctico: usar siempre fragmentos de GaussView en lugar de dibujar átomos sueltos. (Longitud: 3-4 frases)]
:::

::::

::::{dropdown} Más sobre gradientes y algoritmos de optimización
:color: success

:::{note}
[TEXTO HUMANO: Nombres de los algoritmos más comunes (gradient descent, quasi-Newton) sin entrar en matemáticas. Por qué Gaussian necesita varias iteraciones. Para el alumno que quiera entender por qué a veces el cálculo tarda mucho. (Longitud: 3-4 frases)]
:::

::::
