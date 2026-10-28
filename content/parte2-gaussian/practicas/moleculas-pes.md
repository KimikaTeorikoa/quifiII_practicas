# Superficie de energía potencial

## Introducción

La estabilidad del enlace químico y las preferencias conformacionales de las moléculas dependen de cómo varía la energía electrónica al modificar las posiciones de los núcleos. Gracias a la aproximación de Born-Oppenheimer, estas variaciones pueden representarse como una superficie de energía potencial calculada mediante barridos geométricos sistemáticos en Gaussian. En esta práctica se analiza la curva de disociación de la molécula de hidrógeno para diferentes estados de espín y el perfil energético de rotación del ángulo diedro en derivados halogenados del etano.

---

## Objetivos

1. Construir la curva de energía potencial de la molécula de $\text{H}_2$ mediante un barrido de la distancia internuclear $R(\text{H–H})$ para los estados singlete y triplete con HF/STO-3G.
2. Determinar la distancia internuclear de equilibrio ($R_{\text{eq}}$) y la energía de disociación de $\text{H}_2$, contrastando los valores calculados con datos experimentales.
3. Realizar el barrido conformacional del ángulo diedro en dihaloetanos para identificar los confórmeros anti y gauche en la superficie de energía potencial.
4. Cuantificar las barreras de rotación conformacional evaluando la diferencia de energía frente a las conformaciones eclipsadas.

---

## ¿Qué software vamos a usar?

En esta práctica empleamos GaussView como interfaz gráfica para la construcción molecular y la definición de coordenadas de barrido geométrico, y {{gaussian_version}} como motor computacional para ejecutar los cálculos de tipo Scan.

---

## Conceptos clave

### ¿Qué es una superficie de energía potencial?

Bajo la aproximación de Born-Oppenheimer, la energía electrónica es una función continua de las coordenadas nucleares que define la superficie de energía potencial (SEP) del sistema:

$$
E = E(\mathbf{R})
$$

Los mínimos de esta superficie corresponden a geometrías de equilibrio estables, en las que las fuerzas sobre cada núcleo son nulas y cualquier deformación incrementa la energía. Los puntos de silla de primer orden conectan mínimos contiguos y representan los estados de transición de reacciones químicas o cambios conformacionales. A distancias internucleares grandes, la energía potencial alcanza el límite de disociación, donde los átomos dejan de interaccionar entre sí.

:::{figure} /_static/figures/pes_1d_esquema.svg
:alt: Curva unidimensional de energía potencial con mínimo de equilibrio, barrera y asíntota de disociación
:width: 60%
:align: center
:::

### Singlete y triplete: por qué importa el espín

En el estado singlete, los dos electrones de H₂ tienen espines antiparalelos (multiplicidad 1). Esto les permite compartir la misma región del espacio y concentrar densidad electrónica entre los dos núcleos, apantallando su repulsión mutua y estabilizando el enlace covalente en un mínimo de energía a la distancia de equilibrio. En cambio, en el estado triplete los espines son paralelos (multiplicidad 3) y el principio de exclusión de Pauli impide que ambos electrones se sitúen simultáneamente en la región internuclear. Por este motivo, la curva de energía potencial del triplete es puramente repulsiva en todo el recorrido y no presenta ningún mínimo de enlace.

:::{admonition} Nota
:class: note
Desde el punto de vista mecanocuántico, la función de onda espacial del singlete ($^1\Sigma_g^+$) es simétrica ante la permutación de electrones, lo que favorece la acumulación de carga internuclear. En el triplete ($^3\Sigma_u^+$), la función espacial es antisimétrica y presenta un plano nodal internuclear donde la densidad de probabilidad es nula. Al no haber densidad electrónica que apantalle a los protones, la repulsión internuclear domina a cualquier distancia.
:::

### Ángulo diedro y análisis conformacional

El ángulo diedro describe la rotación relativa entre dos grupos unidos por un enlace simple central y se define a través de los cuatro átomos que forman la secuencia X–C–C–X en un rango de 0° a 360°. En una proyección de Newman, cada conformación queda determinada por este ángulo. La conformación *anti* (180°) sitúa los sustituyentes más voluminosos en posiciones opuestas, minimizando las repulsiones estéricas y configurando el mínimo global de energía. Los confórmeros *gauche* (60° y 300°) constituyen mínimos locales con mayor repulsión mutua. Los máximos de la curva corresponden a las conformaciones eclipsadas, cuyo solapamiento determina la barrera de rotación interna.

:::{figure} /_static/figures/newman_dihaloetano.svg
:alt: Proyección de Newman de un dihaloetano con las conformaciones anti, gauche y eclipsada anotadas
:width: 70%
:align: center
:::

---

## Procedimiento

### Parte 1: PES de la molécula de H₂

#### Paso 1: Dibujar H₂ en GaussView

1. Abrir GaussView.
2. En la paleta flotante de fragmentos, seleccionar el átomo de hidrógeno (**H**).
3. Hacer clic en la ventana central 3D para colocar el primer átomo de hidrógeno.
4. Hacer un segundo clic sobre el átomo creado para generar la molécula diatómica de $\text{H}_2$ con enlace simple.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana 3D de GaussView con la molécula de H2 recién construida]
:::

#### Paso 2: Configurar el cálculo de barrido (Scan)

1. En la barra de menús de GaussView, acceder a **Calculate → Gaussian Calculation Setup**.
2. En la pestaña **Job Type**, seleccionar la opción **Scan** (o **Relaxed PES Scan**).
3. Seleccionar la coordenada de enlace entre los dos átomos de hidrógeno:
   - Tipo de coordenada: **Bond**.
   - Átomos: **1** y **2**.
   - Definir los parámetros de barrido:
     - Valor inicial: `0.5` Å.
     - Paso (Step size): `0.1` Å.
     - Número de pasos: `25` (rango final: `3.0` Å).
4. En la pestaña **Method**, seleccionar:
   - Método: `[MÉTODO]`.
   - Conjunto de base: `[BASE]`.
   - Carga: `0`.
   - Para el estado singlete: **Spin = Singlet** (Multiplicity = `1`).
   - Para el estado triplete: **Spin = Triplet** (Multiplicity = `3`).
5. En la pestaña **Title**, escribir: `H2 scan [MÉTODO] [BASE]`.
6. En la pestaña **Additional Keywords**, escribir: `scan`.

| Parámetro | Estado singlete | Estado triplete |
|---|:---:|:---:|
| Method | [MÉTODO] | [MÉTODO] |
| Basis Set | [BASE] | [BASE] |
| Charge | 0 | 0 |
| Multiplicity | 1 | 3 |
| Rango de distancias | [PARÁMETRO] | [PARÁMETRO] |
| Incremento de paso | [PARÁMETRO] | [PARÁMETRO] |

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup con Job Type Scan y parámetros del barrido del enlace H-H]
:::

#### Paso 3: Guardar y lanzar los cálculos

1. En la ventana **Gaussian Calculation Setup**, pulsar el botón **Submit**.
2. Guardar el archivo del singlete con el nombre: `H2_singlete_scan.gjf` en la carpeta de trabajo `{{practicas_folder}}PES/`.
3. Confirmar el diálogo para iniciar el cálculo.
4. Repetir el proceso modificando la multiplicidad a 3 y guardar como: `H2_triplete_scan.gjf`.
5. Comprobar que ambos cálculos progresan en la barra de ejecución.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: cuadro de diálogo para guardar H2_singlete_scan.gjf en la carpeta de trabajo]
:::

#### Paso 4: Visualizar la PES en GaussView

1. En GaussView, abrir el archivo `H2_singlete_scan.log` mediante **File → Open**.
2. Acceder al menú **Results → Scan**.
3. Aparece una gráfica bidimensional interactiva con la energía frente a la distancia $R(\text{H–H})$.
4. Abrir simultáneamente el archivo `H2_triplete_scan.log` para superponer la curva del triplete sobre la del singlete en la misma ventana de visualización.
5. Observar la forma de pozo de potencial en la curva singlete y la ausencia de pozo en la curva triplete.

---

### Parte 2: PES diedro del dihaloetano

Se realizará el barrido conformacional para los tres dihaloetanos siguientes: 1,2-dicloroetano, 1,2-dibromoetano y 1,2-diyodoetano. El procedimiento es idéntico para los tres; repetirlo cambiando únicamente el halógeno en el paso de construcción molecular.

#### Paso 1: Dibujar el dihaloetano en GaussView

1. Abrir una nueva ventana en GaussView (**File → New → Molecule Group**).
2. Construir la molécula de dihaloetano seleccionando la cadena carbonada y sustituyendo dos átomos de hidrógeno por halógenos en carbonos vecinales.
3. Aplicar una limpieza geométrica preliminar mediante **Edit → Clean**.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: estructura tridimensional del dihaloetano construida y orientada en GaussView]
:::

#### Paso 2: Configurar el cálculo del barrido diedro

1. Acceder al menú **Calculate → Gaussian Calculation Setup**.
2. En la pestaña **Job Type**, seleccionar **Scan**.
3. Definir la coordenada interna de tipo **Dihedral** seleccionando los cuatro átomos enlazados: $\text{X–C–C–X}$.
4. Especificar los parámetros angulares del barrido:
   - Coordenada: diedro $\text{X–C–C–X}$.
   - Rango angular: `[PARÁMETRO]`.
5. En la pestaña **Method**, configurar:
   - Método: `[MÉTODO]`.
   - Conjunto de base: `[BASE]`.
   - Carga: `0`.
   - Multiplicidad: `1` (Singlete).
6. En la pestaña **Title**, escribir: `Dihaloetano diedro scan`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup con la selección del diedro X-C-C-X y parámetros de escaneo conformacional]
:::

#### Paso 3: Guardar, lanzar y verificar

1. Guardar el archivo como `dihaloetano_scan.gjf` en `{{practicas_folder}}PES/`.
2. Confirmar el envío del cálculo pulsando **Submit**.

#### Paso 4: Visualizar la curva diedro en GaussView

1. En GaussView, abrir el archivo de salida del barrido mediante **File → Open**.
2. Acceder al menú **Results → Scan**.
3. Identificar los mínimos locales (confórmero gauche) y el mínimo global (confórmero anti a 180°), así como las barreras rotacionales intermedias.

---

## Bibliografía

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 11 (Estructura molecular y superficies de energía potencial).
- Clayden, J.; Greeves, N.; Warren, S. *Organic Chemistry*, 2ª ed.; Oxford University Press, 2012. Cap. 18 (Conformational analysis).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} Para ir más lejos (opcional)
:color: success
:icon: rocket

Como actividad de extensión opcional, se propone repetir el barrido del ángulo diedro en la molécula de etano ($\text{CH}_3\text{-CH}_3$) aplicando idéntico nivel de teoría mecanocuántica. La barrera de rotación interna calculada para el etano, próxima a 3 kcal/mol, es notablemente inferior a la determinada en el dihaloetano y permite contrastar el impacto estérico de los enlaces carbono-hidrógeno frente al volumen de los átomos de halógeno. La comparación directa de ambos perfiles conformacionales evidencia cómo el radio atómico, la polaridad de enlace y la electronegatividad de los sustituyentes condicionan las preferencias conformacionales en sistemas orgánicos sencillos.

::::
