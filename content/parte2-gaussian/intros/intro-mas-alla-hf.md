# Más allá de Hartree-Fock

## Introducción

El tratamiento de campo medio en el método de Hartree-Fock ignora que los electrones se evitan instantáneamente debido a su repulsión coulómbica, omitiendo la denominada energía de correlación electrónica. Para superar este límite físico, la química computacional moderna emplea metodologías avanzadas post-Hartree-Fock y la teoría del funcional de la densidad (DFT), ampliamente implementadas en Gaussian. Estas alternativas permiten calcular energías moleculares y propiedades reactivas con una exactitud química muy superior, ya sea combinando múltiples configuraciones electrónicas o evaluando funcionales de intercambio y correlación como B3LYP.

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

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
