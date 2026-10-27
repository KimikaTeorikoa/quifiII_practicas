# Más allá de Hartree-Fock

## Introducción

El tratamiento de campo medio en el método de Hartree-Fock ignora que los electrones se evitan instantáneamente debido a su repulsión coulómbica, omitiendo la denominada energía de correlación electrónica. Para superar este límite físico, la química computacional moderna emplea metodologías avanzadas post-Hartree-Fock y la teoría del funcional de la densidad (DFT), ampliamente implementadas en Gaussian. Estas alternativas permiten calcular energías moleculares y propiedades reactivas con una exactitud química muy superior, ya sea combinando múltiples configuraciones electrónicas o evaluando funcionales de intercambio y correlación como B3LYP.

---

## Más allá del campo medio: añadir configuraciones

La aproximación de Hartree-Fock describe el estado electrónico del sistema mediante una única configuración, es decir, mediante una asignación estricta de electrones a orbitales moleculares ocupados. Los métodos de interacción de configuraciones superan esta limitación incorporando en la función de onda multielectrónica combinaciones lineales de configuraciones donde uno o más electrones se promocionan hacia orbitales virtuales desocupados. En particular, el método CISD evalúa todas las excitaciones simples y dobles generadas a partir del determinante de referencia del estado fundamental. Este tratamiento recupera una fracción sustancial de la correlación electrónica, aunque a expensas de un incremento notable en el coste computacional y de memoria frente a Hartree-Fock.

---

## DFT: un enfoque diferente

La teoría del funcional de la densidad (DFT) reformula el tratamiento mecanocuántico sustituyendo la función de onda multielectrónica por la densidad electrónica espacial. Según los teoremas de Hohenberg y Kohn, la energía total del estado electrónico queda unívocamente determinada por esta densidad tridimensional. El componente central del método es el funcional de intercambio y correlación, encargado de cuantificar los efectos electrónicos que Hartree-Fock omite o aproxima de forma incompleta. Entre las diversas formulaciones existentes, los funcionales híbridos como B3LYP combinan una fracción del intercambio exacto de Hartree-Fock con términos de correlación propios de DFT. Esta combinación proporciona un equilibrio adecuado entre precisión fisicoquímica y coste computacional para el estudio de sistemas orgánicos.

:::{admonition} Nota
:class: note
Para un sistema polielectrónico, la función de onda mecanocuántica depende de $3N$ coordenadas espaciales, lo que encarece de forma exponencial el tratamiento de sistemas moleculares grandes. Los teoremas de Hohenberg y Kohn demuestran que la energía del estado fundamental queda determinada de manera unívoca por la densidad electrónica $\rho(\mathbf{r})$, una magnitud física observable que depende únicamente de tres variables espaciales. Esta reducción dimensional permite incorporar efectos de correlación electrónica con un coste computacional similar al de Hartree-Fock.
:::

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
