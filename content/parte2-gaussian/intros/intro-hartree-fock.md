# El método de Hartree-Fock

## Introducción

:::{note}
[TEXTO HUMANO: Por qué necesitamos un método: la ecuación de Schrödinger no tiene solución analítica para sistemas con más de un electrón. Necesitamos aproximaciones. HF es la más fundamental, no la más precisa, pero la base de todo lo demás. (Longitud: 3-4 frases)]
:::

---

## El problema: electrones que se repelen

:::{note}
[TEXTO HUMANO: Para He: 2 electrones, 1 núcleo. El problema es que cada electrón "siente" al otro, y ese término de repulsión acopla las ecuaciones, no se puede resolver un electrón sin saber dónde está el otro. Aquí está la dificultad central. (Longitud: 4-5 frases)]
:::

:::{admonition} Intuición
:class: intuicion [revisar: no quiero metaforas o analogias tan tontas. no corresponden al texto escrito, sino a la parte hablada. el texto debe ser profesional y no infantilizador. son estudiantes y estan iniciando pero no significa tratarles de tondos]
Imagina dos personas en una habitación pequeña que intentan no cruzarse la mirada ni tropezar: ninguna puede dar un paso sin mirar de reojo dónde se encuentra la otra. En un sistema con varios electrones sucede lo mismo, porque la repulsión mutua acopla sus movimientos y te impide resolver la ecuación de uno sin conocer la posición exacta del resto. Esa interdependencia instantánea rompe cualquier intento de solución matemática exacta para átomos más pesados que el hidrógeno. Por ese motivo, cuando ejecutes Gaussian verás que el programa recurre obligatoriamente a métodos numéricos aproximados.
:::

---

## La idea de Hartree-Fock: el campo medio

:::{note}
[TEXTO HUMANO: Solución aproximada: cada electrón no ve al otro electrón individualmente, sino un campo medio promediado. Así las ecuaciones se desacoplan y se pueden resolver una a una. Precio: es una aproximación, ignora la correlación electrónica instantánea. (Longitud: 4-5 frases)]
:::

:::{admonition} Intuición
:class: intuicion [reviasr: lo mismo, sin analogias tan tontas. mejores explicaciones]
Es como planificar una ruta en coche guiándote por el mapa de tráfico de tu aplicación móvil: no sigues la posición de cada vehículo individual, sino la densidad media de la circulación en cada avenida. Hartree-Fock aplica esta misma simplificación al sustituir la posición instantánea de los electrones por una nube de carga continua y promediada en el espacio. Gracias a esta aproximación las ecuaciones se desacoplan y Gaussian puede calcular los orbitales uno a uno de forma rápida. La contrapartida visible en tus resultados es que la energía total de Hartree-Fock siempre quedará ligeramente por encima de la energía real exacta.
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
