# P2-B: Superficie de Energía Potencial

## Introducción

La estabilidad del enlace covalente y las preferencias conformacionales moleculares dependen de la variación de la energía electrónica frente a cambios en las posiciones relativas de los núcleos. La aproximación de Born-Oppenheimer permite representar estas variaciones como una superficie de energía potencial que se cartografía mediante barridos geométricos sistemáticos en Gaussian 16. Este procedimiento genera tanto la curva de disociación internuclear de la molécula de hidrógeno para diferentes multiplicidades de espín como el perfil energético de rotación del ángulo diedro en dihaloetanos.

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

En el marco de la aproximación de Born-Oppenheimer, la energía electrónica constituye una función continua de las coordenadas espaciales de los núcleos, lo que define formalmente la superficie de energía potencial (SEP) del sistema:

$$
E = E(\mathbf{R})
$$

Los mínimos de esta hipersuperficie corresponden a geometrías moleculares de equilibrio estables, en las que el gradiente de energía sobre cada núcleo es nulo y cualquier deformación espacial incrementa la energía potencial. Los puntos de silla de primer orden conectan pares de mínimos contiguos y definen los estados de transición de las transformaciones químicas y los procesos conformacionales. A distancias internucleares grandes la energía potencial converge hacia el límite asintótico de disociación, región en la que los fragmentos atómicos o moleculares dejan de interaccionar entre sí.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: curva esquemática unidimensional de energía potencial con mínimo, barrera y asíntota de disociación anotados]
:::

### Singlete y triplete: por qué importa el espín

En el estado singlete los dos electrones presentan espines antiparalelos asociados a una multiplicidad de espín unitaria, lo que les permite compartir la misma región orbital y favorecer la acumulación de densidad electrónica en el espacio internuclear. Esta concentración de carga apantalla la repulsión mutua entre los núcleos y estabiliza termodinámicamente el enlace covalente, generando una curva de energía potencial con un pozo y un mínimo de energía bien definido a la distancia de enlace de equilibrio. Por el contrario, en el estado triplete los dos electrones poseen espines paralelos con multiplicidad 3, por lo que el principio de exclusión de Pauli prohíbe que ambas partículas ocupen simultáneamente la región interatómica. Como consecuencia directa, la curva de energía potencial del triplete resulta estrictamente repulsiva en todo el rango internuclear y carece de mínimo, impidiendo la formación de una molécula químicamente ligada.

:::{admonition} Nota
:class: note
En el estado singlete ($^1\Sigma_g^+$), la función de onda espacial es simétrica respecto a la permutación electrónica, lo que permite acumular densidad de carga entre los núcleos y estabilizar el enlace covalente a distancias cortas. En el estado triplete ($^3\Sigma_u^+$), el principio de Pauli impone una función de onda espacial antisimétrica con un nodo internuclear donde la densidad electrónica se anula. Al carecer de apantallamiento electrónico entre protones, las fuerzas repulsivas nucleares dominan a cualquier distancia, produciendo una curva potencial monótonamente decreciente hacia la disociación.
:::

### Ángulo diedro y análisis conformacional

El ángulo diedro de torsión cuantifica la rotación geométrica relativa entre dos grupos moleculares unidos por un enlace simple central y se define formalmente como el ángulo diedro delimitado por los planos atómicos X-C-C y C-C-X en un rango angular de 0° a 360°. En la representación de proyecciones de Newman, las conformaciones moleculares se ordenan sistemáticamente según este valor angular. La conformación anti (180°) sitúa los sustituyentes voluminosos en posiciones espaciales opuestas, reduciendo las interacciones estéricas y electrostáticas para configurar el mínimo de energía global. En cambio, los confórmeros gauche (60° y 300°) definen mínimos locales de energía caracterizados por una mayor proximidad repulsiva entre sustituyentes. Las crestas y máximos del perfil de torsión corresponden a las conformaciones eclipsadas, en las que el solapamiento angular entre enlaces genera la barrera de energía requerida para la rotación interna molecular.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: proyección de Newman de un dihaloetano identificando los ángulos diedros de confórmeros anti, gauche y eclipsado]
:::

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la última línea exacta:
{{termination_ok}}
:::

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
   - Método: **Hartree-Fock** (**HF**).
   - Conjunto de base: **STO-3G**.
   - Carga: `0`.
   - Para el estado singlete: **Spin = Singlet** (Multiplicity = `1`).
   - Para el estado triplete: **Spin = Triplet** (Multiplicity = `3`).
5. En la pestaña **Title**, escribir: `H2 scan HF STO-3G`.
6. En la pestaña **Additional Keywords**, escribir: `scan`.

Tabla de parámetros de cálculo para $\text{H}_2$:

| Parámetro | Estado singlete | Estado triplete |
|---|:---:|:---:|
| Job Type | Scan | Scan |
| Method | HF | HF |
| Basis Set | STO-3G | STO-3G |
| Charge | 0 | 0 |
| Multiplicity | 1 (Singlet) | 3 (Triplet) |
| Coordenada | Enlace H(1)–H(2) | Enlace H(1)–H(2) |
| Rango de distancias | 0.5 a 3.0 Å | 0.5 a 3.0 Å |
| Incremento de paso | 0.1 Å | 0.1 Å |
| Número de puntos | 26 | 26 |

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

#### Paso 4: Verificar la terminación correcta

1. Abrir con el editor de texto los archivos `H2_singlete_scan.log` y `H2_triplete_scan.log`.
2. Desplazarse al final de cada archivo (**Ctrl + Fin**).
3. Confirmar que la última línea es: `{{termination_ok}}`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: sección final de H2_singlete_scan.log en el editor de texto mostrando la línea Normal termination of Gaussian 16]
:::

#### Paso 5: Leer la tabla de energías del escaneo en el .log

1. En el archivo `H2_singlete_scan.log` abierto en el editor de texto, buscar con **Ctrl + F** el texto:
   `Summary of the potential` (o `Summary of Optimized Potential Surface Scan`).
2. Localizar la tabla de autovalores donde se listan las energías en Hartrees (`Eigenvalues --`) para cada valor de la distancia $R_1$:
   - Comprobar la indicación de energía base si aparece en la cabecera (por ejemplo, `add -1.0 to energies`).
   - Identificar el valor de $R$ correspondiente al mínimo de energía de la curva del singlete ($R_{\text{eq}}$).
3. Repetir la búsqueda en `H2_triplete_scan.log` y observar que las energías descienden monótonamente hacia el límite de disociación sin presentar ningún mínimo de energía.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: bloque Summary of the potential en el archivo .log mostrando la tabla de valores R1 y Eigenvalues]
:::

#### Paso 6: Visualizar la PES en GaussView

1. En GaussView, abrir el archivo `H2_singlete_scan.log` mediante **File → Open**.
2. Acceder al menú **Results → Scan**.
3. Aparece una gráfica bidimensional interactiva con la energía frente a la distancia $R(\text{H–H})$.
4. Abrir simultáneamente el archivo `H2_triplete_scan.log` para superponer la curva del triplete sobre la del singlete en la misma ventana de visualización.
5. Observar la forma de pozo de potencial en la curva singlete y la ausencia de pozo en la curva triplete.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Scan con las dos curvas (singlete y triplete) superpuestas en GaussView]
:::

---

### Parte 2: PES diedro del dihaloetano

[CONFIRMAR CON PROFESOR: qué dihaloetano usar — 1,2-dicloroetano, 1,2-difluoroetano u otro]

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
   - Rango angular: `[CONFIRMAR CON PROFESOR: rango y paso del escaneo diedro (0°–360°, paso 10° o 15°)]`.
5. En la pestaña **Method**, configurar:
   - Método y base: `[CONFIRMAR CON PROFESOR: método y conjunto de base para el escaneo diedro del dihaloetano]`.
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
3. Al finalizar, abrir el archivo `.log` en el editor de texto y confirmar la terminación con: `{{termination_ok}}`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: editor de texto con la línea final Normal termination of Gaussian 16 del dihaloetano]
:::

#### Paso 4: Extraer datos y visualizar la curva diedro en GaussView

1. En GaussView, abrir el archivo de salida del barrido mediante **File → Open**.
2. Acceder al menú **Results → Scan**.
3. Identificar los mínimos locales (confórmero gauche) y el mínimo global (confórmero anti a 180°), así como las barreras rotacionales intermedias.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Scan mostrando la curva de energía potencial en función del ángulo diedro de torsión]
:::

---

## Resultados y análisis

### Tabla 1: Parámetros característicos de la PES de H₂

La siguiente tabla recoge los valores calculados para la distancia de enlace de equilibrio ($R_{\text{eq}}$) y la energía de disociación ($D_e$) de la molécula de $\text{H}_2$, confrontándolos de forma directa con los datos experimentales de referencia. En condiciones empíricas de laboratorio, la distancia de equilibrio es de 0.741 Å y la energía de disociación alcanza 4.75 eV (equivalentes a 109.5 kcal/mol). La comparación sistemática entre ambos conjuntos de valores permite evaluar cuantitativamente el error relativo porcentual derivado del método Hartree-Fock y del empleo de la base mínima STO-3G.

| Parámetro | Valor calculado (HF/STO-3G) | Valor experimental | Error (%) |
|---|:---:|:---:|:---:|
| $R_{\text{eq}}$ (Å) | [TEXTO HUMANO] | 0.741 | [TEXTO HUMANO] |
| $E(R_{\text{eq}})$ (Ha) | [TEXTO HUMANO] | — | — |
| $E(R \to \infty)$ (Ha) | [TEXTO HUMANO] | — | — |
| $D_e$ (eV) | [TEXTO HUMANO] | 4.75 | [TEXTO HUMANO] |
| $D_e$ (kcal/mol) | [TEXTO HUMANO] | 109.5 | [TEXTO HUMANO] |

La energía de disociación $D_e$ se calcula a partir de la diferencia entre la energía a distancia internuclear infinita (límite asintótico a 3.0 Å) y la energía en el mínimo de equilibrio:

$$D_e = E(R \to \infty) - E(R_{\text{eq}})$$

### Tabla 2: Barrido internuclear de H₂ (singlete y triplete)

La tabla siguiente recopila las energías electrónicas absolutas expresadas en hartrees para los estados singlete y triplete a lo largo de cada una de las distancias internucleares evaluadas. Asimismo, se incluyen las energías relativas ($\Delta E$) calculadas en kilocalorías por mol tomando como nivel de referencia cero el mínimo energético del estado singlete. Esta serie de datos tabulados suministra las coordenadas numéricas necesarias para construir y analizar la representación gráfica de las curvas de potencial en el siguiente apartado.

| Punto | $R$ (Å) | $E$ singlete (Ha) | $E$ triplete (Ha) | $\Delta E$ singlete (kcal/mol) | $\Delta E$ triplete (kcal/mol) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.5 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 2 | 0.6 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 3 | 0.7 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 4 | 0.8 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 5 | 0.9 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| 6 | 1.0 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| ... | ... | ... | ... | ... | ... |
| 26 | 3.0 | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Gráfico de la PES de H₂

A partir de los valores de la tabla precedente, se deben representar en una misma gráfica las curvas de energía relativa en kilocalorías por mol frente a la distancia internuclear $R$ en ángstroms para los estados singlete y triplete. El eje de abscisas debe abarcar el intervalo completo de distancias calculado entre 0.5 y 3.0 Å, mientras que el eje de ordenadas ha de mostrar con claridad el cero de referencia fijado en el mínimo del singlete. Ambas curvas deben diferenciarse con nitidez en la leyenda mediante su respectiva multiplicidad de espín. Para generar esta figura se pueden transferir los valores a una hoja de cálculo estándar o emplear las herramientas gráficas disponibles en los equipos del aula.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: gráfico con las dos curvas superpuestas de H2: singlete con pozo de potencial y triplete repulsivo]
:::

### Tabla 3: Barreras conformacionales del dihaloetano

:::{note}
[TEXTO HUMANO: Registro de las energías relativas asociadas a los ángulos diedros característicos del dihaloetano seleccionado para evaluar la estabilidad diferencial de los confórmeros anti y gauche y la magnitud de la barrera rotacional. Longitud: 3-4 frases.]
:::

| Conformación | Ángulo diedro (°) | $E$ calculada (Ha) | $\Delta E$ (kcal/mol) |
|---|:---:|:---:|:---:|
| Eclipsado (sin-periplanar) | 0 | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Gauche | 60 | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Eclipsado intermedio | 120 | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Anti (anti-periplanar) | 180 | [TEXTO HUMANO] | 0.00 (referencia) |
| Eclipsado intermedio | 240 | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Gauche | 300 | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Eclipsado (sin-periplanar) | 360 | [TEXTO HUMANO] | [TEXTO HUMANO] |

---

## Preguntas

1. ¿Qué valor de energía en Hartrees aparece en la tabla `Summary of Optimized Potential Surface Scan` del archivo `H2_singlete_scan.log` para el punto de menor energía, y a qué distancia internuclear $R_1$ en Ångstroms corresponde?
2. A partir de la curva del estado singlete, determinar la energía de disociación teórica $D_e$ en eV restando la energía del mínimo de la energía en el límite asintótico ($R = 3.0\text{ \AA}$). Justificar la presencia del pozo de potencial enlazante en el singlete frente al perfil puramente repulsivo del triplete en función del espín electrónico y la densidad de carga internuclear.
3. Comparar la distancia de equilibrio calculada para el singlete ($R_{\text{eq}} \approx 0.71\text{ \AA}$) con el valor experimental ($0.741\text{ \AA}$). ¿Por qué el método Hartree-Fock con base mínima STO-3G subestima la distancia de enlace y sobreestima la energía de disociación respecto al experimento?
4. Comparar las curvas de energía potencial del estado singlete y del estado triplete de $\text{H}_2$ a distancias internucleares cortas ($R = 0.5\text{ \AA}$) y largas ($R = 3.0\text{ \AA}$). ¿A partir de qué distancia la diferencia de energía entre ambos estados se vuelve despreciable y por qué convergen hacia el mismo límite asintótico de dos átomos de hidrógeno neutros aislados?
5. [PENDIENTE CONFIRMACIÓN PROFESOR: esta pregunta aplica cuando se complete la parte del dihaloetano] A partir de la curva del ángulo diedro en el dihaloetano, contrastar la barrera rotacional calculada con la energía térmica media a temperatura ambiente ($kT \approx 0.6\text{ kcal/mol}$ a 298 K) para deducir si la rotación alrededor del enlace C–C está libre o restringida.

---

## Bibliografía

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 11 (Estructura molecular y superficies de energía potencial).
- Clayden, J.; Greeves, N.; Warren, S. *Organic Chemistry*, 2ª ed.; Oxford University Press, 2012. Cap. 18 (Conformational analysis).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} 🚀 Para ir más lejos (opcional)
:color: success
:icon: rocket

Como actividad de extensión opcional, se propone repetir el barrido del ángulo diedro en la molécula de etano ($\text{CH}_3\text{-CH}_3$) aplicando idéntico nivel de teoría mecanocuántica. La barrera de rotación interna calculada para el etano, próxima a 3 kcal/mol, es notablemente inferior a la determinada en el dihaloetano y permite contrastar el impacto estérico de los enlaces carbono-hidrógeno frente al volumen de los átomos de halógeno. La comparación directa de ambos perfiles conformacionales evidencia cómo el radio atómico, la polaridad de enlace y la electronegatividad de los sustituyentes condicionan las preferencias conformacionales en sistemas orgánicos sencillos.

::::
