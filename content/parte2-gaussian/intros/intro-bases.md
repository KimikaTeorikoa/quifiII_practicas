# Funciones de base

## Introducción

Los orbitales atómicos y moleculares de sistemas con múltiples electrones presentan geometrías espaciales continuas que no pueden describirse mediante funciones analíticas simples. Para resolver computacionalmente estos estados, la teoría cuántica recurre a conjuntos de funciones matemáticas conocidas, habitualmente combinaciones de gaussianas, denominadas funciones de base. La elección del conjunto de base en Gaussian define la flexibilidad numérica para modelar la distribución electrónica, condicionando directamente el grado de aproximación física y el coste de cálculo requerido.

---

## La idea central: aproximar orbitales con funciones conocidas

En los métodos computacionales de estructura electrónica, los orbitales moleculares no se resuelven como funciones continuas arbitrarias, sino como combinaciones lineales de un conjunto finito de funciones predefinidas denominadas funciones de base. Las funciones de base de tipo gaussiano constituyen el estándar habitual en programas como Gaussian debido a que permiten evaluar con gran rapidez matemática las integrales analíticas de atracción y repulsión. Al incorporar un mayor número de funciones primitivas al conjunto, se incrementa la flexibilidad numérica para reproducir con fidelidad la distribución espacial de la densidad electrónica. Por tanto, la selección del conjunto de base establece un compromiso directo entre la exactitud física del cálculo y el tiempo de cómputo requerido.

:::{admonition} Figura
:class: captura
[FIGURA: orbital 1s exacto vs aproximación con pocas gaussianas vs aproximación con más gaussianas (tres curvas superpuestas)]
:::

---

## Precisión vs coste computacional

El tamaño y la complejidad del conjunto de base determinan el límite superior de precisión física que puede alcanzar un cálculo cuántico. Al incrementar el número de funciones matemáticas por átomo se describe con mayor fidelidad la relajación de la densidad electrónica, aunque el tiempo de cómputo y el consumo de memoria aumentan notablemente. La tabla comparativa resume esta tendencia cualitativa utilizando dos bases representativas habituales, sin pretender constituir un catálogo exhaustivo. En la práctica cotidiana existe una gran variedad de conjuntos adaptados a diferentes niveles de teoría y tipos de átomos. Para evitar ambigüedades operativas, el protocolo de cada sesión práctica especifica con claridad el conjunto exacto que debe seleccionarse en GaussView.

| Base | Tamaño relativo | Coste relativo |
|------|----------------|----------------|
| STO-3G | Pequeña | Bajo |
| 6-311G | Mayor | Mayor |

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} Qué significa la notación: 6-31G, 6-311G y funciones de polarización
:color: success

En la notación estándar de bases de valencia dividida de Pople, los dígitos indican el número de funciones gaussianas primitivas empleadas para describir los orbitales internos del núcleo y los orbitales de valencia. Por ejemplo, la base 6-311G contrae seis gaussianas para representar cada orbital del núcleo interno, mientras que divide la capa de valencia en tres funciones independientes formadas por contracciones de tres, una y una función gaussiana respectivamente. El asterisco o sufijo `*` denota la incorporación de funciones de polarización de tipo d sobre los átomos pesados distintos del hidrógeno. Estas funciones adicionales aportan flexibilidad angular para describir con fidelidad las deformaciones espaciales de la densidad de carga durante la formación del enlace químico. Su inclusión no modifica el modo de trabajo en GaussView, donde el conjunto de base completo se escoge de forma directa en el menú desplegable de la pestaña Method.

::::
