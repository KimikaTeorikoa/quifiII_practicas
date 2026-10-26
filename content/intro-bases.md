# Funciones de base

## Introducción

:::{note}
[TEXTO HUMANO: Explicar la necesidad de emplear funciones de base debido a que los orbitales moleculares carecen de formulación analítica conocida, presentándolos como combinaciones lineales de funciones matemáticas predefinidas. Longitud: 3-4 frases.]
[ECUACIÓN: aproximación LCAO-MO para orbitales moleculares, $\psi_i = \sum_\mu c_{\mu i} \phi_\mu$]
:::

---

## La idea central: aproximar orbitales con funciones conocidas

:::{note}
[TEXTO HUMANO: Desarrollar la analogía del ajuste de curvas mediante polinomios para ilustrar cómo un orbital atómico tipo Slater se aproxima mediante combinaciones lineales de primitivas gaussianas, enfatizando la ganancia en precisión al aumentar el número de funciones. Longitud: 4-5 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: orbital 1s exacto frente a aproximación con pocas gaussianas y con base extendida mostrando tres curvas superpuestas]
:::

---

## Precisión vs coste computacional

:::{note}
[TEXTO HUMANO: Exponer el compromiso metodológico entre exactitud química y demanda de tiempo de cálculo, señalando que STO-3G y 6-311G son ejemplos ilustrativos dentro de un amplio abanico de bases disponibles. Longitud: 4-5 frases.]
:::

| Base | Tamaño relativo | Coste relativo |
|---|---|---|
| STO-3G | Pequeña | Bajo |
| 6-311G | Mayor | Mayor |

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional : libro de texto de química cuántica o equivalente)]`

---

::::{dropdown} Qué significa la notación: 6-31G, 6-311G y funciones de polarización
:color: success

:::{note}
[TEXTO HUMANO: Desglosar la nomenclatura de bases de Pople, explicando la distribución de primitivas gaussianas entre capas internas y de valencia, así como la adición de funciones de polarización tipo d o difusas. Longitud: 4-5 frases.]
:::

::::
