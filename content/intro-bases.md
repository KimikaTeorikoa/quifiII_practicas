# Funciones de base

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA — NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto. Por qué necesitamos una base: los orbitales moleculares no tienen forma
analítica conocida — los aproximamos como combinación de funciones matemáticas simples.
La base es ese conjunto de funciones. Sin base, no hay cálculo.

---

## La idea central: aproximar orbitales con funciones conocidas

Párrafo medio + figura. Analogía: igual que aproximamos una curva cualquiera con
polinomios, aproximamos un orbital con una suma de funciones gaussianas. Cuantas más
funciones, mejor la aproximación. Figura: curva exacta vs aproximación con pocas
funciones vs aproximación con más funciones.

:::{admonition} Figura
:class: captura
[FIGURA: orbital 1s exacto vs aproximación con pocas gaussianas vs aproximación con
más gaussianas — tres curvas superpuestas]
:::

---

## Precisión vs coste computacional

Párrafo medio + tabla. Relación directa: más funciones de base → más preciso → más
tiempo de cálculo. La tabla muestra solo la idea cualitativa con dos ejemplos — no
son las únicas bases posibles ni representan una escala completa.

| Base | Tamaño relativo | Coste relativo |
|------|----------------|----------------|
| STO-3G | Pequeña | Bajo |
| 6-311G | Mayor | Mayor |

Aclaración en el texto: estos son dos ejemplos para ilustrar la idea. En la práctica
existe una gran variedad de bases; cada cálculo indica cuál usar.

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional — libro de texto de química cuántica o equivalente]`

---

::::{dropdown} Qué significa la notación: 6-31G, 6-311G y funciones de polarización
:color: success

Párrafo medio. Explicar los números: cuántas gaussianas por orbital del core y de
valencia. Qué añade el asterisco o la "d" (funciones de polarización). Solo para el
alumno que quiera entender qué está eligiendo en el menú de GaussView.
::::
