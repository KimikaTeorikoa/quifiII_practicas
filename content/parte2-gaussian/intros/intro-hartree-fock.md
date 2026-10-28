# El método de Hartree-Fock

## Introducción

La ecuación de Schrödinger no admite solución matemática exacta para sistemas con más de un electrón debido al acoplamiento que genera la repulsión electrostática entre ellos. El método de Hartree-Fock aborda este problema mediante la aproximación de campo medio, sustituyendo las interacciones instantáneas individuales por un potencial promediado en el espacio. Esta simplificación permite que programas como Gaussian determinen los orbitales moleculares y la energía electrónica total mediante un procedimiento iterativo autoconsistente.

## El problema: electrones que se repelen

El átomo de helio contiene dos electrones y un núcleo. La energía cinética de cada electrón y su atracción hacia el núcleo se describen exactamente mediante operadores monoelectrónicos, pero la repulsión coulómbica entre ambos acopla sus ecuaciones de movimiento. Determinar la distribución espacial de un electrón requiere conocer la del otro y viceversa, por lo que no existe solución analítica exacta para este sistema. Esta dificultad se extiende a cualquier átomo o molécula polielectrónica y constituye el problema central de la química cuántica molecular.

:::{admonition} Nota
:class: note
El término de repulsión interelectrónica $1/r_{12}$ en el operador hamiltoniano acopla las coordenadas espaciales de ambos electrones. Esta dependencia mutua impide la separación de variables e imposibilita obtener una solución analítica exacta para sistemas con dos o más electrones. Por ello, el cálculo de la estructura electrónica requiere aproximar este potencial de interacción mediante métodos numéricos iterativos.
:::

## La idea de Hartree-Fock: el campo medio

La aproximación de campo medio simplifica el problema polielectrónico al sustituir las repulsiones instantáneas entre pares de electrones por un potencial promedio generado por el conjunto de la nube electrónica. Bajo este tratamiento, las ecuaciones se desacoplan formalmente y permiten calcular cada orbital molecular de manera independiente. El operador de Fock incorpora este potencial promediado para construir los orbitales mediante un procedimiento autoconsistente. Como contrapartida, el método ignora que los electrones se evitan dinámicamente en cada instante, fenómeno denominado correlación electrónica. Esta omisión sitúa la energía total calculada siempre por encima del valor no relativista exacto.

:::{admonition} Nota
:class: note
Al promediar la repulsión interelectrónica se desprecian las correlaciones instantáneas entre las posiciones de los electrones. De acuerdo con el teorema variacional, cualquier función de onda aproximada proporciona una energía superior a la del estado fundamental exacto. Por tanto, la energía obtenida en el límite Hartree-Fock constituye una cota superior a la energía exacta no relativista del sistema.
:::

## Orbitales: la solución para un electrón

En el formalismo de Hartree-Fock, el estado espacial de cada electrón se describe mediante un orbital que depende únicamente de las coordenadas espaciales de dicha partícula. En el átomo de helio, los dos electrones ocupan el mismo orbital espacial 1s con espines opuestos ($\alpha$ y $\beta$), cumpliendo el principio de exclusión de Pauli. Para calcular estos estados en sistemas atómicos y moleculares, cada orbital se expande como una combinación lineal de funciones de base predefinidas. La figura muestra el orbital 1s del helio como una superficie de contorno esférica que delimita la región de mayor densidad electrónica.

:::{figure} /_static/figures/orbital_1s_he.svg
:alt: Representación de la densidad electrónica del orbital 1s del átomo de helio mediante isosuperficies concéntricas
:width: 50%
:align: center
:::

## El ciclo SCF: resolver por iteración

El potencial de campo medio depende de los orbitales ocupados, pero estos solo pueden calcularse si se conoce previamente dicho potencial. Esta dependencia circular impide una solución directa. Para resolverla, las ecuaciones se tratan mediante un procedimiento numérico iterativo. El cálculo parte de una estimación inicial de los orbitales (*guess*), con la que se construye un primer operador de Fock. A continuación, se resuelven las ecuaciones matriciales para obtener nuevos coeficientes orbitales y se comprueba si la variación en la energía o en la densidad respecto a la iteración anterior queda por debajo del umbral de tolerancia. Este ciclo se repite hasta alcanzar la convergencia numérica en el denominado método del campo autoconsistente (SCF, *Self-Consistent Field*), cuyo esquema resume el diagrama adjunto.

:::{figure} /_static/figures/scf_flowchart.svg
:alt: Diagrama de flujo del ciclo SCF desde la estimación inicial hasta la convergencia
:width: 55%
:align: center
:::

## La matriz de Fock: lo que Gaussian resuelve

El ciclo SCF se formula algebraicamente como el problema de autovalores generalizado **FC = SCε**, donde **F** es la matriz de Fock, **C** la matriz de coeficientes orbitales, **S** la matriz de solapamiento y **ε** la matriz diagonal de energías orbitales. Para una base compuesta por dos funciones, **F** y **S** son matrices de dimensión 2×2 con elementos $F_{11}, F_{12}, F_{22}$ y $S_{11}, S_{12}, S_{22}$, que Gaussian evalúa calculando analíticamente las integrales sobre las funciones de base. La diagonalización de este sistema proporciona los coeficientes que definen cada orbital molecular y sus energías orbitales. Al ampliar la base a un mayor número de funciones, la dimensión de las matrices aumenta proporcionalmente, pero la formulación matemática y el procedimiento de resolución se mantienen idénticos.

## Energías: orbital vs total

Los autovalores obtenidos al resolver las ecuaciones de Fock corresponden a las energías de cada orbital y no a la energía electrónica total del sistema. Si se sumaran directamente las energías de todos los orbitales ocupados, se sobreestimaría la energía real porque la repulsión coulómbica entre cada par de electrones se contabilizaría dos veces. Por esta razón, la energía total en el método de Hartree-Fock incluye un término corrector que resta exactamente esa interacción duplicada. Gaussian calcula esta energía global y la muestra en hartrees en la línea `SCF Done` del archivo de salida.

:::{admonition} Advertencia
:class: warning
La energía que aparece en el log de Gaussian es la energía total, no la energía de un orbital individual.
:::

## Limitaciones de HF: la correlación electrónica

Al basarse en una aproximación de campo medio, el método de Hartree-Fock no considera que el movimiento instantáneo de cada electrón depende de la posición de los demás. La diferencia entre la energía del límite Hartree-Fock y la solución exacta no relativista de la ecuación de Schrödinger se define como energía de correlación electrónica. Aunque esta magnitud suele representar una fracción pequeña de la energía total, resulta determinante para describir con exactitud propiedades químicas como afinidades electrónicas, longitudes de enlace y barreras de activación. Por ello, la química cuántica contemporánea recurre a métodos post-Hartree-Fock y a la teoría del funcional de la densidad para recuperar dicha correlación.

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} La función de onda antisimétrica y el determinante de Slater
:color: success

El principio de exclusión de Pauli exige que la función de onda electrónica sea antisimétrica, es decir, que cambie de signo al intercambiar las coordenadas de dos electrones cualesquiera. Un producto simple de orbitales independientes (producto de Hartree) no satisface esta condición de indistinguibilidad. Para cumplirla se recurre al determinante de Slater, una matriz cuyas filas representan los orbitales y cuyas columnas corresponden a las coordenadas de cada electrón. Intercambiar dos electrones equivale a permutar dos columnas, lo que invierte automáticamente el signo del determinante.

::::

::::{dropdown} Energía de correlación y métodos post-HF
:color: success

A partir de la función de onda de Hartree-Fock se han desarrollado diversos métodos para recuperar la correlación electrónica y superar la aproximación de campo medio. La teoría de perturbaciones de Møller-Plesset de segundo orden (MP2) añade correcciones dinámicas a la energía con un coste computacional moderado. Por su parte, métodos como *Coupled Cluster* con excitaciones simples y dobles (CCSD) ofrecen una precisión muy superior a expensas de un esfuerzo de cálculo elevado. Estos esquemas se analizan con detalle en la siguiente sección teórica.

::::
