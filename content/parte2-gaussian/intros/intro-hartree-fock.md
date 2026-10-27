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

El potencial de campo medio depende de la forma de los orbitales ocupados, pero a su vez los orbitales moleculares solo pueden calcularse si se conoce de antemano dicho potencial, generando una dependencia circular que impide una solución directa. Para superar este bucle, las ecuaciones mecanocuánticas se resuelven mediante un procedimiento numérico iterativo. El cálculo parte de un conjunto inicial estimado de orbitales (*guess*), a partir del cual se construye el primer operador de campo medio. A continuación, se resuelven las ecuaciones matriciales de Fock para obtener nuevos coeficientes orbitales y se evalúa si la diferencia energética o de densidad respecto al paso anterior cae por debajo del umbral de tolerancia fijado. Este ciclo de refinamiento sucesivo se repite hasta alcanzar la estabilidad numérica, denominándose formalmente método del campo autoconsistente (SCF, *Self-Consistent Field*), cuyo esquema lógico resume el diagrama de flujo adjunto.

:::{admonition} Figura
:class: captura
[FIGURA: diagrama de flujo SCF: guess → campo medio → nuevos orbitales → convergencia? → si no, volver al paso 2]
:::

---

## La matriz de Fock: lo que Gaussian resuelve

El ciclo SCF se formula algebraicamente como el problema de autovalores generalizado **FC = SCε**, donde **F** es la matriz de Fock, **C** la matriz de coeficientes orbitales, **S** la matriz de solapamiento y **ε** la matriz diagonal de energías orbitales. Para un conjunto de base compuesto por dos funciones, **F** y **S** adoptan la forma de matrices de dimensión 2×2 con elementos $F_{11}, F_{12}, F_{22}$ y $S_{11}, S_{12}, S_{22}$ que Gaussian evalúa calculando las integrales analíticas sobre las funciones de base atómicas. La resolución y diagonalización de este sistema de ecuaciones matriciales proporciona los coeficientes que definen cada orbital molecular junto con sus correspondientes energías asociadas. Al extender el cálculo a bases con mayor número de funciones la dimensión de las matrices se incrementa proporcionalmente, pero la formulación matemática y el procedimiento numérico de resolución se mantienen idénticos.

---

## Energías: orbital vs total

[CONFIRMAR CON PROFESOR: E(He) HF/STO-3G]

Los autovalores obtenidos al resolver las ecuaciones de Fock representan las energías monoelectrónicas de cada orbital por separado y no la energía electrónica total del sistema. Sumar directamente las energías de todos los orbitales ocupados genera una sobreestimación física sustancial, ya que la energía de repulsión coulómbica entre cada par de electrones se contabilizaría por duplicado. Por consiguiente, la expresión formal de la energía total en el método Hartree-Fock incorpora un término corrector que sustrae de forma exacta esta interacción repetida. Gaussian calcula dicha magnitud global y la reporta en unidades de hartrees en la línea identificada como `SCF Done` del archivo de salida.

:::{warning}
La energía que aparece en el log de Gaussian es la energía total, no la energía de un orbital individual.
:::

---

## Limitaciones de HF: la correlación electrónica

Al fundamentarse en una aproximación de campo medio, el método Hartree-Fock no contempla que el movimiento instantáneo de cada electrón correlaciona con la posición de los restantes. La discrepancia energética resultante entre la energía propia del límite Hartree-Fock y la solución exacta no relativista de la ecuación de Schrödinger se define formalmente como energía de correlación electrónica. Aunque esta magnitud suele representar una fracción porcentual reducida de la energía total, resulta determinante para describir con exactitud magnitudes químicas como afinidades electrónicas, longitudes de enlace y barreras cinéticas de reacción. Por este motivo, la química cuántica contemporánea recurre a metodologías post-Hartree-Fock y a la teoría del funcional de la densidad para recuperar dicha correlación.

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} La función de onda antisimétrica y el determinante de Slater
:color: success

El principio de exclusión de Pauli impone que la función de onda electrónica total sea antisimétrica, de modo que debe cambiar de signo ante el intercambio de las coordenadas espaciales y de espín de dos electrones cualesquiera. Un producto simple de orbitales monoelectrónicos independientes (producto de Hartree) no satisface este requisito mecánico cuántico de indistinguibilidad. Para garantizar rigurosamente dicha propiedad se recurre al determinante de Slater, una construcción matricial donde las filas representan los orbitales y las columnas las coordenadas electrónicas. Al intercambiar dos electrones se permutan dos columnas de la matriz, provocando que el determinante resultante invierta automáticamente su signo algebraico.

::::

::::{dropdown} Energía de correlación y métodos post-HF
:color: success

A partir de la función de onda de referencia de Hartree-Fock se han formulado diversos métodos de correlación electrónica diseñados para superar la aproximación de campo medio. La teoría de perturbaciones de Møller-Plesset de segundo orden (MP2) incorpora correcciones dinámicas a la energía con un incremento computacional moderado. Por su parte, metodologías más avanzadas como *Coupled Cluster* con excitaciones simples y dobles (CCSD) proporcionan una precisión energética notablemente superior a expensas de una exigencia computacional elevada. Estos esquemas teóricos y sus aplicaciones prácticas se exponen con mayor detalle en la siguiente guía.

::::
