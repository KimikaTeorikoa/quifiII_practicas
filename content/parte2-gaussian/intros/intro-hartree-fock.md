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

La aproximación de campo medio simplifica el problema polielectrónico al sustituir las interacciones repulsivas instantáneas entre pares de partículas por un potencial electrostático promedio originado por el conjunto de la nube electrónica. Bajo este tratamiento, las ecuaciones mecanocuánticas se desacoplan formalmente, permitiendo calcular la distribución espacial de cada electrón de forma individual e independiente. El operador de Fock incorpora este potencial promediado para construir orbitales monoelectrónicos a través de un procedimiento autoconsistente. Como contrapartida teórica, el método ignora que los electrones tienden a evitarse dinámicamente en cada instante, fenómeno denominado correlación electrónica. Esta omisión condiciona la exactitud cuantitativa de la energía total, situándola siempre por encima del valor exacto no relativista.

:::{admonition} Nota
:class: note
La aproximación de campo medio sustituye la interacción electrostática instantánea entre electrones puntuales por el potencial promediado de la nube electrónica restante. Al desacoplar las coordenadas de cada partícula, las ecuaciones de Hartree-Fock se resuelven de forma independiente para cada orbital molecular. Al ignorar la correlación instantánea entre electrones, la energía total calculada constituye siempre una cota superior a la energía no relativista exacta, de acuerdo con el teorema variacional.
:::

---

## Orbitales: la solución para un electrón

En el formalismo de Hartree-Fock, el estado espacial de cada electrón se describe mediante un orbital molecular monoelectrónico que depende únicamente de las coordenadas espaciales de esa partícula. En el caso del átomo de helio, los dos electrones se alojan en el mismo orbital espacial 1s con funciones de espín opuestas ($\alpha$ y $\beta$), satisfaciendo el principio de exclusión de Pauli. Para resolver numéricamente estos estados en sistemas moleculares o atómicos, cada orbital se expande matemáticamente como una combinación lineal de funciones de base predefinidas. La figura adjunta representa el orbital 1s del helio como una superficie de contorno esférica que delimita la región de mayor densidad de probabilidad electrónica.

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

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

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
