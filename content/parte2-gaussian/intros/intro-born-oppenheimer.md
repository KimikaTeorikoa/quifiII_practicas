# Geometría molecular y la aproximación de Born-Oppenheimer

## Introducción

La determinación de cualquier propiedad físico-química en una molécula parte del conocimiento preciso de las coordenadas relativas de sus átomos. La aproximación de Born-Oppenheimer aprovecha la gran diferencia de masa entre núcleos y electrones para desacoplar sus dinámicas, permitiendo que Gaussian resuelva la distribución electrónica sobre disposiciones nucleares fijas. Este marco teórico establece la base operativa para distinguir entre cálculos de energía puntual a coordenadas constantes y procedimientos de optimización geométrica dirigidos a localizar mínimos de energía estables.

---

## La aproximación de Born-Oppenheimer

La masa de un protón es aproximadamente 1836 veces superior a la masa del electrón, por lo que los núcleos atómicos se desplazan en una escala temporal varios órdenes de magnitud más lenta que los electrones. La aproximación de Born-Oppenheimer aprovecha esta disparidad dinámica tratando a los núcleos como centros de carga fijos en el espacio mientras se resuelve el movimiento electrónico. De este modo, la energía electrónica total se obtiene como un valor que depende de manera paramétrica de las coordenadas nucleares fijadas. Sin este desacoplamiento entre las variables nucleares y electrónicas, el problema mecanocuántico de muchos cuerpos resultaría computacionalmente inabordable para sistemas moleculares.

:::{admonition} Nota
:class: note
La masa de los núcleos atómicos supera en más de tres órdenes de magnitud a la masa del electrón, por lo que las velocidades nucleares son muy inferiores a las electrónicas. Esta diferencia de escalas temporales permite desacoplar los movimientos y resolver la ecuación de Schrödinger electrónica considerando a los núcleos en posiciones fijas. La energía electrónica resultante para cada disposición nuclear genera la superficie de energía potencial sobre la cual se estudia posteriormente el movimiento de los núcleos.
:::

---

## Geometría molecular: distancias, ángulos y diedros

La disposición espacial de una estructura molecular queda unívocamente determinada por tres parámetros geométricos elementales: distancias de enlace (medidas en ángstroms, Å), ángulos de valencia (en grados sexagesimales) y ángulos diedros de torsión (en grados sexagesimales). Mientras que las distancias y los ángulos definen la conectividad local entre átomos contiguos, los ángulos diedros describen la rotación relativa entre dos planos que comparten un enlace químico central. Este conjunto de coordenadas internas constituye la base sobre la que los algoritmos de Gaussian evalúan los gradientes de energía y ejecutan la optimización estructural. Asimismo, el entorno gráfico de GaussView ofrece herramientas específicas para medir, modificar y visualizar directamente cada uno de estos tres parámetros sobre el modelo tridimensional.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA o FIGURA: molécula con los tres parámetros geométricos anotados]
:::

---

## Energía puntual: calcular sin mover

En un cálculo de energía puntual (*Single Point*), las posiciones relativas de los núcleos atómicos permanecen fijas según las coordenadas indicadas en el archivo de entrada. Bajo esta geometría nuclear constante, Gaussian resuelve la estructura electrónica evaluando las integrales mecanocuánticas de forma autoconsistente. El valor devuelto al finalizar el cálculo es la energía electrónica total del sistema en hartrees correspondiente a esa configuración geométrica precisa. En el panel de configuración de GaussView, este cálculo se selecciona en la pestaña **Job Type → Single Point** (etiquetada como *Energy* en el menú principal).

---

## Optimización de geometría: encontrar el mínimo

En un cálculo de optimización de geometría, Gaussian evalúa en primer lugar la energía electrónica total sobre la estructura tridimensional inicial introducida por el usuario y calcula las primeras derivadas espaciales de dicha energía respecto a cada coordenada nuclear, magnitud denominada vector gradiente. A partir de las fuerzas resultantes, los núcleos atómicos se desplazan colectivamente en la dirección geométrica que reduce la energía potencial del sistema. Tras cada desplazamiento nuclear, el programa recalcula la función de onda electrónica y el nuevo gradiente sobre las coordenadas actualizadas. Este procedimiento se repite iterativamente paso a paso hasta que tanto las fuerzas residuales como los desplazamientos atómicos caen simultáneamente por debajo de los umbrales de convergencia numéricos establecidos. En el entorno gráfico de GaussView, este cálculo se activa seleccionando la opción **Job Type → Optimization**.

:::{admonition} Figura
:class: captura
[FIGURA: curva E vs coordenada con 3-4 pasos de optimización marcados y flecha al mínimo]
:::

---

## ¿Cuándo usar Single Point y cuándo Optimization?

Se realiza un cálculo de energía puntual (*Single Point*) cuando la geometría molecular ya es conocida o se desea evaluar la energía electrónica en una configuración nuclear fija sin alterar las coordenadas espaciales. Por el contrario, se recurre a un cálculo de optimización cuando se parte de una estructura tridimensional aproximada y resulta indispensable determinar la disposición nuclear de mínima energía potencial antes de calcular cualquier propiedad fisicoquímica. La siguiente tabla resume la correspondencia directa entre el objetivo planteado y la modalidad de cálculo que debe seleccionarse en Gaussian.

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

Si la geometría inicial propuesta se encuentra excesivamente apartada de la estructura de equilibrio real, el algoritmo de búsqueda puede requerir un número excesivo de pasos, quedar atrapado en un mínimo local o no converger. En el archivo `.log`, esta dificultad se reconoce cuando el número de ciclos alcanza el límite permitido sin que los criterios numéricos de fuerza y desplazamiento queden satisfechos. Para prevenir este fallo computacional, se aconseja ensamblar las moléculas partiendo de la biblioteca de fragmentos estándar de GaussView, que suministran distancias y ángulos iniciales químicamente coherentes, en vez de incorporar átomos individuales en coordenadas arbitrarias.

::::

::::{dropdown} Más sobre gradientes y algoritmos de optimización
:color: success

Los procedimientos de optimización implementados por defecto en Gaussian emplean algoritmos de tipo quasi-Newton, como el método Berny, los cuales actualizan progresivamente una aproximación numérica de la matriz de segundas derivadas (hessiano) para proyectar el desplazamiento geométrico óptimo hacia el mínimo. Cada iteración de optimización exige evaluar de forma completa la energía electrónica y el vector gradiente en las nuevas coordenadas nucleares, lo que conlleva un coste de cálculo acumulativo. El número total de ciclos requeridos depende estrechamente de la complejidad topológica de la superficie de potencial y del grado de proximidad de la estructura inicial, pudiendo prolongarse durante decenas de iteraciones en moléculas conformacionalmente flexibles.

::::
