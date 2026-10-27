# El método de Hartree-Fock

## Introducción

La ecuación de Schrödinger no admite una resolución matemática exacta para átomos o moléculas con más de un electrón debido al acoplamiento continuo originado por la repulsión electrostática entre cargas negativas. El método de Hartree-Fock aborda esta dificultad mediante la aproximación de campo medio, sustituyendo las interacciones instantáneas individuales por un potencial promediado en el espacio. Esta simplificación permite que programas como Gaussian resuelvan el sistema orbital a orbital mediante algoritmos iterativos autoconsistentes, proporcionando orbitales moleculares definidos y la energía electrónica total.

---

## El problema: electrones que se repelen

:::{note}
[TEXTO HUMANO: Para He: 2 electrones, 1 núcleo. El problema es que cada electrón "siente" al otro, y ese término de repulsión acopla las ecuaciones, no se puede resolver un electrón sin saber dónde está el otro. Aquí está la dificultad central. (Longitud: 4-5 frases)]
:::

:::{admonition} Nota
:class: note
El término de repulsión interelectrónica $1/r_{12}$ en el operador hamiltoniano acopla simultáneamente las coordenadas espaciales de ambos electrones. Esta dependencia mutua impide la separación de variables y bloquea la obtención de una solución analítica exacta para sistemas con dos o más electrones. En consecuencia, el cálculo de la estructura electrónica requiere aproximar este potencial de interacción mediante métodos numéricos iterativos.
:::

---

## La idea de Hartree-Fock: el campo medio

:::{note}
[TEXTO HUMANO: Solución aproximada: cada electrón no ve al otro electrón individualmente, sino un campo medio promediado. Así las ecuaciones se desacoplan y se pueden resolver una a una. Precio: es una aproximación, ignora la correlación electrónica instantánea. (Longitud: 4-5 frases)]
:::

:::{admonition} Nota
:class: note
La aproximación de campo medio sustituye la interacción electrostática instantánea entre electrones puntuales por el potencial promediado de la nube electrónica restante. Al desacoplar las coordenadas de cada partícula, las ecuaciones de Hartree-Fock se resuelven de forma independiente para cada orbital molecular. Al ignorar la correlación instantánea entre electrones, la energía total calculada constituye siempre una cota superior a la energía no relativista exacta, de acuerdo con el teorema variacional.
:::

---

## Orbitales: la solución para un electrón

:::{note}
[TEXTO HUMANO: En HF cada electrón ocupa un orbital, una función matemática que describe su distribución en el espacio. Para He: dos electrones en el mismo orbital 1s, con espines opuestos. Figura: dibujo del orbital 1s del He (esfera). (Longitud: 4-5 frases)]
:::

:::{admonition} Figura
:class: captura
[FIGURA: orbital 1s del He, representación de densidad electrónica]
:::

---

## El ciclo SCF: resolver por iteración

:::{note}
[TEXTO HUMANO: Como no sabemos el campo medio antes de conocer los orbitales, y no conocemos los orbitales antes de conocer el campo medio, se resuelve iterativamente. Pasos: (1) adivinamos los orbitales iniciales, (2) calculamos el campo medio, (3) resolvemos los nuevos orbitales, (4) repetimos hasta convergencia. Figura: diagrama de flujo del ciclo SCF. (Longitud: 4-5 frases)]
:::

:::{admonition} Figura
:class: captura
[FIGURA: diagrama de flujo SCF: guess → campo medio → nuevos orbitales → convergencia? → si no, volver al paso 2]
:::

---

## La matriz de Fock: lo que Gaussian resuelve

:::{note}
[TEXTO HUMANO: El problema SCF se formula como un problema de autovalores: FC = SCε. Para He con una base mínima: matriz 1×1 (trivial). Con dos funciones de base: matriz 2×2. Mostrar la matriz explícitamente con los elementos nombrados (F₁₁, F₁₂, S₁₂) sin derivarlos, solo que Gaussian los calcula y resuelve el sistema. Los autovalores son las energías orbitales. (Longitud: 4-5 frases)]
:::

---

## Energías: orbital vs total

[CONFIRMAR CON PROFESOR: E(He) HF/STO-3G]

:::{note}
[TEXTO HUMANO: Diferencia crítica: la energía orbital (autovalor de Fock) no es la energía total. La energía total no es la suma de energías orbitales, se estaría contando la repulsión dos veces. Gaussian reporta la energía total HF. Unidades: Hartrees. (Longitud: 4-5 frases)]
:::

:::{warning}
La energía que aparece en el log de Gaussian es la energía total, no la energía de un orbital individual.
:::

---

## Limitaciones de HF: la correlación electrónica

:::{note}
[TEXTO HUMANO: HF trata la repulsión electrónica de forma promediada, ignora que los electrones se evitan instantáneamente. Esta diferencia entre la energía HF y la energía exacta se llama energía de correlación. Es pequeña en términos absolutos pero importante para propiedades químicas. Por eso en las prácticas usamos B3LYP, no HF. (Longitud: 3-4 frases)] [revisar:no decir en concreto b3lyp, creo que lia el mensaje, mejor en terminos generales hablar de metodos mas desarrolaldos post-HF]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: libro de texto de química cuántica recomendado (p.ej. Szabo & Ostlund, Levine, o equivalente)]`

---

::::{dropdown} La función de onda antisimétrica y el determinante de Slater
:color: success

:::{note}
[TEXTO HUMANO: Por qué la función de onda total no es simplemente el producto de orbitales, el principio de exclusión de Pauli exige antisimetría. El determinante de Slater como solución formal. Sin desarrollo matemático. (Longitud: 3-4 frases)]
:::

::::

::::{dropdown} Energía de correlación y métodos post-HF
:color: success

:::{note}
[TEXTO HUMANO: MP2, CCSD como correcciones a HF. Solo nombres y la idea de que recuperan parte de la correlación ignorada. Enlaza con intro-mas-alla-hf.md. (Longitud: 3-4 frases)]
:::

::::
