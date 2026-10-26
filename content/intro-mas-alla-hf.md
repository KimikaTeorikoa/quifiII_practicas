# Más allá de Hartree-Fock

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA — NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo muy corto. HF es el punto de partida, pero no el final. Este archivo presenta
brevemente los métodos que mejoran sobre HF — el alumno los verá nombrados en las
prácticas y en la literatura.

---

## Más allá del campo medio: añadir configuraciones

Párrafo corto. La limitación de HF es que usa una sola configuración electrónica.
CISD (Configuration Interaction Singles and Doubles) mejora esto mezclando la
configuración del estado fundamental con configuraciones excitadas. Más preciso,
pero mucho más costoso computacionalmente.

---

## DFT: un enfoque diferente

Párrafo medio. DFT no trabaja con la función de onda sino con la densidad electrónica
— una función de 3 variables en lugar de 3N. Idea central: la energía del sistema
queda determinada por la densidad. El funcional de intercambio-correlación recoge todo
lo que HF ignora. B3LYP es el funcional más usado en química orgánica: buen equilibrio
entre precisión y coste.

:::{admonition} Intuición
:class: intuicion
[TEXTO HUMANO: analogía — en lugar de seguir a cada persona en una multitud, describes
la densidad de gente en cada zona]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional — libro de texto o review de DFT accesible]`
