# El método de Hartree-Fock

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA — NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto. Por qué necesitamos un método: la ecuación de Schrödinger no tiene
solución analítica para sistemas con más de un electrón. Necesitamos aproximaciones.
HF es la más fundamental — no la más precisa, pero la base de todo lo demás.

---

## El problema: electrones que se repelen

Párrafo medio. Para He: 2 electrones, 1 núcleo. El problema es que cada electrón
"siente" al otro, y ese término de repulsión acopla las ecuaciones — no se puede
resolver un electrón sin saber dónde está el otro. Aquí está la dificultad central.

:::{admonition} Intuición
:class: intuicion
[TEXTO HUMANO: analogía — dos personas que se evitan en una habitación; no puedes
predecir dónde está una sin saber dónde está la otra]
:::

---

## La idea de Hartree-Fock: el campo medio

Párrafo medio. Solución aproximada: cada electrón no ve al otro electrón
individualmente, sino un campo medio promediado. Así las ecuaciones se desacoplan
y se pueden resolver una a una. Precio: es una aproximación — ignora la correlación
electrónica instantánea.

:::{admonition} Intuición
:class: intuicion
[TEXTO HUMANO: analogía — en lugar de modelar cada coche en el tráfico, usas la
densidad media de tráfico]
:::

---

## Orbitales: la solución para un electrón

Párrafo medio + figura. En HF cada electrón ocupa un orbital — una función matemática
que describe su distribución en el espacio. Para He: dos electrones en el mismo orbital
1s, con espines opuestos. Figura: dibujo del orbital 1s del He (esfera).

:::{admonition} Figura
:class: captura
[FIGURA: orbital 1s del He, representación de densidad electrónica]
:::

---

## El ciclo SCF: resolver por iteración

Párrafo medio + figura. Como no sabemos el campo medio antes de conocer los orbitales,
y no conocemos los orbitales antes de conocer el campo medio, se resuelve
iterativamente. Pasos: (1) adivinamos los orbitales iniciales, (2) calculamos el campo
medio, (3) resolvemos los nuevos orbitales, (4) repetimos hasta convergencia. Figura:
diagrama de flujo del ciclo SCF.

:::{admonition} Figura
:class: captura
[FIGURA: diagrama de flujo SCF — guess → campo medio → nuevos orbitales → convergencia?
→ si no, volver al paso 2]
:::

---

## La matriz de Fock: lo que Gaussian resuelve

Párrafo medio. El problema SCF se formula como un problema de autovalores: FC = SCε.
Para He con una base mínima: matriz 1×1 (trivial). Con dos funciones de base: matriz
2×2. Mostrar la matriz explícitamente con los elementos nombrados (F₁₁, F₁₂, S₁₂)
sin derivarlos — solo que Gaussian los calcula y resuelve el sistema. Los autovalores
son las energías orbitales.

---

## Energías: orbital vs total

Párrafo medio. Diferencia crítica: la energía orbital (autovalor de Fock) no es la
energía total. La energía total no es la suma de energías orbitales — se estaría
contando la repulsión dos veces. Gaussian reporta la energía total HF. Unidades:
Hartrees. Para He: `[CONFIRMAR CON PROFESOR: E(He) HF/STO-3G]`.

:::{warning}
La energía que aparece en el log de Gaussian es la energía total, no la energía de
un orbital individual.
:::

---

## Limitaciones de HF: la correlación electrónica

Párrafo corto. HF trata la repulsión electrónica de forma promediada — ignora que los
electrones se evitan instantáneamente. Esta diferencia entre la energía HF y la energía
exacta se llama energía de correlación. Es pequeña en términos absolutos pero importante
para propiedades químicas. Por eso en las prácticas usamos B3LYP, no HF.

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: libro de texto de química cuántica recomendado — p.ej. Szabo & Ostlund,
  Levine, o equivalente]`

---

::::{dropdown} La función de onda antisimétrica y el determinante de Slater
:color: success

Párrafo corto. Por qué la función de onda total no es simplemente el producto de
orbitales — el principio de exclusión de Pauli exige antisimetría. El determinante
de Slater como solución formal. Sin desarrollo matemático.
::::

::::{dropdown} Energía de correlación y métodos post-HF
:color: success

Párrafo corto. MP2, CCSD como correcciones a HF. Solo nombres y la idea de que
recuperan parte de la correlación ignorada. Enlaza con intro-mas-alla-hf.md.
::::
