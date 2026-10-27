# Funciones de base

## Introducción

Los orbitales atómicos y moleculares de sistemas con múltiples electrones presentan geometrías espaciales continuas que no pueden describirse mediante funciones analíticas simples. Para resolver computacionalmente estos estados, la teoría cuántica recurre a conjuntos de funciones matemáticas conocidas, habitualmente combinaciones de gaussianas, denominadas funciones de base. La elección del conjunto de base en Gaussian define la flexibilidad numérica para modelar la distribución electrónica, condicionando directamente el grado de aproximación física y el coste de cálculo requerido.

---

## La idea central: aproximar orbitales con funciones conocidas

:::{note} [revisar, de nuevo, cuidado con las analogias]
[TEXTO HUMANO: Analogía: igual que aproximamos una curva cualquiera con polinomios, aproximamos un orbital con una suma de funciones gaussianas. Cuantas más funciones, mejor la aproximación. Figura: curva exacta vs aproximación con pocas funciones vs aproximación con más funciones. (Longitud: 4-5 frases)]
:::

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

:::{note}
[TEXTO HUMANO: Explicar los números: cuántas gaussianas por orbital del core y de valencia. Qué añade el asterisco o la "d" (funciones de polarización). Solo para el alumno que quiera entender qué está eligiendo en el menú de GaussView. (Longitud: 4-5 frases)]
:::

::::
