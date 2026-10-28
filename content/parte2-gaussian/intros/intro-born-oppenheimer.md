# Geometría molecular y la aproximación de Born-Oppenheimer

## Introducción

Determinar cualquier propiedad fisicoquímica en una molécula exige conocer con precisión las coordenadas espaciales de sus átomos. La aproximación de Born-Oppenheimer aprovecha la gran diferencia de masa entre núcleos y electrones para desacoplar sus movimientos, lo que permite resolver la distribución electrónica sobre disposiciones nucleares fijas. Este marco teórico fundamenta la distinción entre cálculos de energía puntual a coordenadas constantes y optimizaciones de geometría orientadas a localizar mínimos energéticos estables.

---

## La aproximación de Born-Oppenheimer

La masa de un protón es aproximadamente 1836 veces mayor que la del electrón, por lo que los núcleos atómicos se mueven con mucha mayor lentitud. La aproximación de Born-Oppenheimer aprovecha esta disparidad temporal tratando a los núcleos como centros de carga estacionarios mientras se resuelve el movimiento electrónico. De este modo, la energía electrónica se obtiene como una magnitud que depende paramétricamente de las posiciones nucleares elegidas. Sin este desacoplamiento, la resolución mecanocuántica de cualquier molécula resultaría computacionalmente inviable.

:::{admonition} Nota
:class: note
Al fijar los núcleos en diferentes disposiciones espaciales y calcular la energía electrónica para cada una de ellas, se genera la superficie de energía potencial (PES, *Potential Energy Surface*). Sobre esta superficie hiperdimensional se describe posteriormente la dinámica de los núcleos, la vibración molecular y el avance de las reacciones químicas.
:::

---

## Geometría molecular: distancias, ángulos y diedros

La geometría de una molécula queda definida por tres parámetros geométricos principales: distancias de enlace (en ángstroms, Å), ángulos de enlace (en grados) y ángulos diedros de torsión (en grados). Las distancias y los ángulos determinan la conectividad local entre átomos contiguos, mientras que los diedros describen la rotación espacial entre planos que comparten un enlace central. Estas coordenadas internas constituyen la base con la que Gaussian calcula gradientes y realiza optimizaciones de estructura. En GaussView, estos tres parámetros pueden medirse y visualizarse directamente sobre el modelo molecular.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA o FIGURA: molécula con los tres parámetros geométricos anotados]
:::

---

## Energía puntual: calcular sin mover

En un cálculo de energía puntual (*Single Point*), las posiciones nucleares permanecen fijas según las coordenadas del archivo de entrada. Con esa geometría constante, Gaussian resuelve la estructura electrónica sin desplazar ningún átomo. El resultado obtenido es la energía electrónica total (en hartrees) correspondiente a esa conformación específica. En GaussView, este cálculo se selecciona en la pestaña **Job Type → Single Point** (etiquetada habitualmente como *Energy*).

---

## Optimización de geometría: encontrar el mínimo

En un cálculo de optimización de geometría, Gaussian calcula la energía sobre la estructura inicial y evalúa sus derivadas respecto a las coordenadas nucleares (el vector gradiente). A partir de las fuerzas resultantes, el programa desplaza los núcleos en la dirección que reduce la energía del sistema. En cada nueva geometría se recalculan la función de onda y el gradiente. Este ciclo se repite hasta que tanto las fuerzas sobre los átomos como los desplazamientos geométricos caen por debajo de los umbrales de convergencia fijados, alcanzando así un mínimo local de energía. En GaussView, este tipo de cálculo se selecciona en **Job Type → Optimization**.

:::{admonition} Figura
:class: captura
[FIGURA: curva E vs coordenada con 3-4 pasos de optimización marcados y flecha al mínimo]
:::

---

## ¿Cuándo usar Single Point y cuándo Optimization?

El cálculo de energía puntual (*Single Point*) se utiliza cuando la geometría molecular ya es conocida experimentalmente, o bien cuando se desea evaluar la energía en una serie de configuraciones fijas (por ejemplo, al trazar manualmente una curva de energía potencial variando una distancia). Por el contrario, la optimización (*Optimization*) se emplea cuando se parte de una estructura aproximada y se necesita encontrar la geometría de equilibrio estable de la molécula antes de calcular otras propiedades. La tabla resume ambos casos:

| Situación | Job Type |
|-----------|----------|
| Quiero la energía de una geometría específica (p.ej. escanear distancias a mano) | Single Point |
| Quiero la geometría de equilibrio real de la molécula | Optimization |

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} ¿Qué pasa si la geometría inicial es muy mala?
:color: success

Si la geometría inicial está muy alejada de la estructura de equilibrio, el algoritmo puede necesitar un número excesivo de pasos, quedar atrapado en un mínimo local o no converger. En el archivo `.log`, esta situación se identifica cuando se alcanza el límite de ciclos de optimización sin satisfacer los criterios de convergencia. Para evitarlo, conviene construir las moléculas empleando los fragmentos estándar de GaussView, que proporcionan distancias y ángulos iniciales químicamente razonables.

::::

::::{dropdown} Más sobre gradientes y algoritmos de optimización
:color: success

Los algoritmos de optimización por defecto en Gaussian (como el método Berny) emplean técnicas de tipo cuasi-Newton, que actualizan iterativamente una aproximación del hessiano (la matriz de segundas derivadas) para proyectar el desplazamiento hacia el mínimo. Como cada ciclo exige calcular la función de onda y el gradiente completo, optimizar moléculas grandes o conformacionalmente flexibles puede requerir un coste computacional elevado y decenas de pasos de optimización.

::::
