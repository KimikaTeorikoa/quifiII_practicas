# Más allá de Hartree-Fock

## Introducción

:::{note}
[TEXTO HUMANO: HF es el punto de partida, pero no el final. Este archivo presenta brevemente los métodos que mejoran sobre HF, el alumno los verá nombrados en las prácticas y en la literatura. (Longitud: 1-2 frases)]
:::

---

## Más allá del campo medio: añadir configuraciones

:::{note}
[TEXTO HUMANO: La limitación de HF es que usa una sola configuración electrónica. CISD (Configuration Interaction Singles and Doubles) mejora esto mezclando la configuración del estado fundamental con configuraciones excitadas. Más preciso, pero mucho más costoso computacionalmente. (Longitud: 3-4 frases)]
:::

---

## DFT: un enfoque diferente

:::{note}
[TEXTO HUMANO: DFT no trabaja con la función de onda sino con la densidad electrónica, una función de 3 variables en lugar de 3N. Idea central: la energía del sistema queda determinada por la densidad. El funcional de intercambio-correlación recoge todo lo que HF ignora. B3LYP es el funcional más usado en química orgánica: buen equilibrio entre precisión y coste. (Longitud: 4-5 frases)]
:::

:::{admonition} Nota
:class: note
Para un sistema polielectrónico, la función de onda mecanocuántica depende de $3N$ coordenadas espaciales, lo que encarece de forma exponencial el tratamiento de sistemas moleculares grandes. Los teoremas de Hohenberg y Kohn demuestran que la energía del estado fundamental queda determinada de manera unívoca por la densidad electrónica $\rho(\mathbf{r})$, una magnitud física observable que depende únicamente de tres variables espaciales. Esta reducción dimensional permite incorporar efectos de correlación electrónica con un coste computacional similar al de Hartree-Fock.
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional (libro de texto o review de DFT accesible)]`
