# Geometría molecular y la aproximación de Born-Oppenheimer

## Introducción

La determinación de cualquier propiedad físico-química en una molécula parte del conocimiento preciso de las coordenadas relativas de sus átomos. La aproximación de Born-Oppenheimer aprovecha la gran diferencia de masa entre núcleos y electrones para desacoplar sus dinámicas, permitiendo que Gaussian resuelva la distribución electrónica sobre disposiciones nucleares fijas. Este marco teórico establece la base operativa para distinguir entre cálculos de energía puntual a coordenadas constantes y procedimientos de optimización geométrica dirigidos a localizar mínimos de energía estables.

---

## La aproximación de Born-Oppenheimer

:::{note}
[TEXTO HUMANO: Idea central: los núcleos son mucho más pesados que los electrones, se mueven mucho más despacio. En la práctica: tratamos los núcleos como fijos y calculamos cómo se distribuyen los electrones alrededor de ellos. Sin esta aproximación el problema sería irresoluble. (Longitud: 4-5 frases)]
:::

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

:::{note}
[TEXTO HUMANO: Gaussian no conoce la geometría real, la busca. Parte de la geometría que dibujó el alumno, calcula el gradiente (la pendiente de la energía respecto a cada coordenada), y mueve los átomos cuesta abajo. Repite hasta que el gradiente es prácticamente cero. (Longitud: 4-5 frases)]
:::

:::{admonition} Figura
:class: captura
[FIGURA: curva E vs coordenada con 3-4 pasos de optimización marcados y flecha al mínimo]
:::

---

## ¿Cuándo usar Single Point y cuándo Optimization?

:::{note}
[TEXTO HUMANO: Criterios para elegir entre cálculo puntual (Single Point) y optimización de geometría según el objetivo. (Longitud: 2-3 frases)]
:::

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

:::{note}
[TEXTO HUMANO: Si el alumno dibuja una geometría muy alejada del mínimo real, la optimización puede no converger o acabar en un mínimo equivocado. Señales de alerta en el log. Consejo práctico: usar siempre fragmentos de GaussView en lugar de dibujar átomos sueltos. (Longitud: 3-4 frases)]
:::

::::

::::{dropdown} Más sobre gradientes y algoritmos de optimización
:color: success

:::{note}
[TEXTO HUMANO: Nombres de los algoritmos más comunes (gradient descent, quasi-Newton) sin entrar en matemáticas. Por qué Gaussian necesita varias iteraciones. Para el alumno que quiera entender por qué a veces el cálculo tarda mucho. (Longitud: 3-4 frases)]
:::

::::
