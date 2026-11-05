# Más allá de Hartree-Fock

## Introducción

El tratamiento de campo medio de Hartree-Fock no considera que los electrones se repelen instantáneamente debido a su interacción coulómbica, omitiendo la energía de correlación electrónica. Para superar esta limitación, la química computacional recurre a métodos post-Hartree-Fock y a la teoría del funcional de la densidad (DFT). Ambos enfoques permiten calcular energías moleculares y propiedades químicas con mayor precisión: los primeros incorporan múltiples configuraciones electrónicas a partir de una función de onda de referencia, mientras que DFT modela la correlación mediante funcionales de intercambio y correlación como B3LYP.

## Más allá del campo medio: añadir configuraciones

La aproximación de Hartree-Fock describe el estado electrónico mediante una única configuración, es decir, una asignación fija de electrones a orbitales ocupados. Los métodos de interacción de configuraciones mejoran esta descripción incorporando combinaciones lineales de configuraciones donde uno o más electrones se promueven a orbitales virtuales. En particular, el método CISD incluye todas las excitaciones simples y dobles a partir del determinante de referencia. Este enfoque recupera una parte sustancial de la correlación electrónica, aunque con un coste computacional y de memoria muy superior al de Hartree-Fock.

## DFT: un enfoque diferente

La teoría del funcional de la densidad (DFT) aborda el problema de la estructura electrónica desde una perspectiva distinta: sustituye la función de onda multielectrónica por la densidad electrónica espacial. Según los teoremas de Hohenberg y Kohn, la energía del estado fundamental queda determinada de forma exacta por esta densidad tridimensional. La pieza central del método es el funcional de intercambio y correlación, responsable de modelar los efectos electrónicos que Hartree-Fock omite o aproxima de forma incompleta. Entre las diversas opciones disponibles, los funcionales híbridos como B3LYP combinan una fracción del intercambio exacto de Hartree-Fock con términos de correlación propios de DFT. Para moléculas orgánicas de tamaño medio, B3LYP reproduce geometrías y frecuencias con errores típicos por debajo del 3% a un coste computacional comparable al de HF.

:::{admonition} Nota
:class: note
Mientras que la función de onda de un sistema de $N$ electrones depende de $3N$ coordenadas espaciales (lo que hace inviable su cálculo exacto para moléculas medianas o grandes), la densidad electrónica $\rho(\mathbf{r})$ es una magnitud observable que solo depende de tres variables espaciales $(x, y, z)$. Esta drástica reducción dimensional permite a DFT incluir efectos de correlación electrónica con un coste computacional comparable al del método Hartree-Fock.
:::

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
