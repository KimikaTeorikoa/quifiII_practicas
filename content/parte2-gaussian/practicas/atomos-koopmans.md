# Átomos y el teorema de Koopmans

## Introducción

La energía de ionización mide la fuerza de atracción que ejerce el núcleo sobre los electrones más externos y determina la reactividad química y las tendencias periódicas de los elementos. Mediante cálculos de Hartree-Fock en Gaussian, se aplican dos aproximaciones complementarias para evaluar esta propiedad: la diferencia directa de energía total entre el átomo neutro y su catión ($\Delta E$), y la estimación a partir del orbital ocupado de mayor energía mediante el teorema de Koopmans ($-\varepsilon_{\text{HOMO}}$).

---

## Objetivos

1. Calcular la energía electrónica total de átomos neutros y cationes monocargados mediante el método Hartree-Fock en {{gaussian_version}}.
2. Determinar la energía de ionización por diferencia autoconsistente ($\Delta E$) y por estimación orbital mediante el teorema de Koopmans ($-\varepsilon_{\text{HOMO}}$).
3. Comparar las energías de ionización calculadas frente a valores experimentales a lo largo del primer y segundo período.
4. Visualizar la distribución espacial y la simetría de los orbitales atómicos ocupados de mayor energía (HOMO) en GaussView.

---

## ¿Qué software vamos a usar?

En esta práctica se trabaja con GaussView como entorno gráfico de construcción y visualización, y {{gaussian_version}} como motor de cálculo de estructura electrónica. Antes de comenzar, conviene haber revisado la guía de introducción a GaussView.

---

## Conceptos clave

### ¿Por qué las energías son negativas?

La energía electrónica de un átomo se mide respecto al estado de referencia en que el núcleo y todos los electrones se encuentran en reposo y separados en el infinito, con interacción nula. Como el átomo ligado es más estable que ese estado de referencia, su energía es siempre negativa. Cuanto más negativo es el valor que aparece en la línea `SCF Done`, mayor es la estabilidad del sistema. Un resultado positivo en la energía total indicaría un error en la configuración del cálculo.

### El HOMO y el LUMO

Los orbitales moleculares se ordenan de menor a mayor energía. El orbital ocupado de mayor energía recibe el nombre de HOMO (del inglés *Highest Occupied Molecular Orbital*) y contiene los electrones más fáciles de extraer. El primer orbital desocupado, el LUMO (*Lowest Unoccupied Molecular Orbital*), es el orbital disponible para recibir electrones. La diferencia entre el nivel del HOMO y el nivel de vacío constituye una primera estimación de la energía necesaria para arrancar un electrón del sistema.

:::{admonition} Nota
:class: note
En la salida de Gaussian con `pop=full`, la energía del HOMO corresponde al último valor numérico de la última línea `Alpha occ. eigenvalues`. El primer valor de la línea siguiente `Alpha virt. eigenvalues` corresponde al LUMO.
:::

:::{figure} /_static/figures/homo_lumo_ionizacion.svg
:alt: Diagrama de niveles de orbitales con HOMO y LUMO señalados y flecha de energía de ionización
:width: 60%
:align: center
:::

### La energía de ionización y el Teorema de Koopmans

La energía de ionización de un átomo neutro $A$ en fase gas es la energía mínima necesaria para extraer un electrón y generar el catión $A^+$ según el proceso $A \rightarrow A^+ + e^-$. En esta práctica se calcula por dos vías independientes. La primera es la diferencia directa de energías SCF entre el catión y el átomo neutro, lo que exige dos cálculos separados. La segunda se basa en el teorema de Koopmans, que permite estimar ese valor a partir únicamente de la energía del orbital HOMO del átomo neutro, sin necesidad de calcular el catión.

$$\text{IE}_{\Delta E} = E(A^+) - E(A)$$

$$\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}$$

:::{admonition} Nota
:class: note
El teorema de Koopmans adopta la aproximación de orbitales congelados, asumiendo que los orbitales del catión $A^+$ son idénticos a los del átomo neutro $A$. En un proceso físico de ionización, la pérdida de un electrón reduce la repulsión interelectrónica global y provoca la contracción de la nube electrónica restante hacia el núcleo (relajación orbital). Como la aproximación de Koopmans ignora tanto esta relajación estabilizadora como las diferencias de energía de correlación, $-\varepsilon_{\text{HOMO}}$ discrepa ligeramente del valor calculado por diferencia autoconsistente $\text{IE}_{\Delta E}$.
:::

### La multiplicidad de espín

La multiplicidad de espín indica cuántos estados cuánticos de espín son accesibles para el sistema y se calcula como $2S+1$, donde $S$ es la suma de los espines de los electrones desapareados. Un átomo con todos los electrones apareados tiene $S=0$ y multiplicidad 1 (singlete). Un electrón desapareado da $S=1/2$ y multiplicidad 2 (doblete). Asignar un valor de multiplicidad incorrecto provoca que Gaussian distribuya mal los electrones entre los orbitales $\alpha$ y $\beta$, lo que invalida el resultado o impide la convergencia del ciclo SCF.

:::{warning}
Verificar siempre el valor de multiplicidad de espín antes de enviar el cálculo: un valor incorrecto invalida los resultados o impide la convergencia SCF.
:::

### Unidades de energía

Gaussian reporta todas las energías en unidades atómicas (Hartrees, Ha). Para comparar con los datos experimentales, que habitualmente se expresan en electronvoltios (eV), se aplica el factor de conversión siguiente:

$$1\text{ Ha} = {{ha_to_ev}}\text{ eV}$$

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la línea final exacta:
{{termination_ok}}
:::

### Paso 1: Abrir GaussView y dibujar el átomo

1. Abrir GaussView desde el menú de aplicaciones o lanzador del sistema.
2. Abrir la paleta de fragmentos atómicos mediante **View → Element Fragments** (o pulsando el icono de la tabla periódica en la barra de herramientas superior).
3. Seleccionar el elemento químico que se desea calcular (por ejemplo, carbono, **C**).
4. Hacer un único clic con el botón izquierdo sobre la ventana central de dibujo. Aparecerá un centro atómico aislado sin enlaces.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana principal de GaussView con la paleta Element Fragments abierta y un unico centro atomico de carbono en la vista 3D]
:::

### Paso 2: Configurar el cálculo del átomo neutro

1. Acceder al menú **Calculate → Gaussian Calculation Setup**.
2. En la pestaña **Job Type**, seleccionar **Energy**.
3. En la pestaña **Method**, configurar los parámetros del cálculo:

| Campo | Valor |
|---|---|
| Method | **HF** |
| Basis Set | **STO-3G** |
| Charge | **0** |
| Spin (Multiplicity) | Consultar la tabla de multiplicidades para cada átomo neutro |

4. En la pestaña **Title**, escribir una descripción identificativa (por ejemplo, `C neutro HF STO-3G`).
5. En la pestaña **Additional Keywords**, escribir exactamente: `pop=full`. Esta instrucción incluye las energías de todos los orbitales moleculares en el archivo de salida.

Tabla de multiplicidades de referencia ($2S+1$):

| Átomo | $Z$ | Configuración | Multiplicidad |
|---|:---:|---|:---:|
| H | 1 | 1s¹ | 2 |
| He | 2 | 1s² | 1 |
| Li | 3 | [He] 2s¹ | 2 |
| Be | 4 | [He] 2s² | 1 |
| B | 5 | [He] 2s² 2p¹ | 2 |
| C | 6 | [He] 2s² 2p² | 3 |
| N | 7 | [He] 2s² 2p³ | 4 |
| O | 8 | [He] 2s² 2p⁴ | 3 |
| F | 9 | [He] 2s² 2p⁵ | 2 |
| Ne | 10 | [He] 2s² 2p⁶ | 1 |

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup con pestana Method, HF/STO-3G configurado y Additional Keywords pop=full]
:::

### Paso 3: Lanzar el cálculo y guardar el archivo

1. Pulsar el botón **Submit** en la parte inferior de la ventana **Gaussian Calculation Setup**.
2. En el cuadro de diálogo para guardar, indicar el nombre del archivo de entrada `.gjf` (por ejemplo, `C_neutro_HF_STO3G.gjf`) y guardarlo en el directorio de trabajo del laboratorio: `{{practicas_folder}}`.
3. Confirmar el cuadro de diálogo pulsando **Save** y a continuación **Submit**.
4. Observar el estado de ejecución en la barra inferior de GaussView hasta que el cálculo finalice (pocos segundos para elementos ligeros).

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: cuadro de dialogo para guardar el archivo .gjf y barra de estado de GaussView indicando la ejecucion del calculo]
:::

### Paso 4: Verificar la terminación correcta

1. Abrir el archivo `.log` generado (`C_neutro_HF_STO3G.log`) con el editor de texto del sistema (**File → Open** en el editor o clic derecho en el archivo).
2. Desplazarse al final del archivo con **Ctrl + Fin**.
3. Confirmar que la última línea del archivo coincide exactamente con: `{{termination_ok}}`. Si no aparece, el cálculo falló y no deben usarse sus datos.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: seccion final del archivo .log en el editor de texto mostrando la linea Normal termination of Gaussian 16]
:::

### Paso 5: Leer la energía total E(N)

1. En el archivo `.log` abierto en el editor de texto, pulsar **Ctrl + F** para activar la búsqueda.
2. Escribir el texto de búsqueda: `SCF Done`.
3. Localizar la energía total en la línea `SCF Done:  E(RHF) = ...` (para sistemas de capa cerrada con multiplicidad 1) o `SCF Done:  E(ROHF) = ...` (para capa abierta con multiplicidad distinta de 1).
4. Copiar el valor numérico en unidades atómicas (A.U. / Hartrees) y pegarlo en la columna $E(N)$ de la tabla de resultados.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: fragmento del archivo .log mostrando el resultado de busqueda de la linea SCF Done con el valor de energia total en Hartrees]
:::

### Paso 6: Leer la energía orbital del HOMO

1. En el mismo archivo `.log`, buscar con **Ctrl + F** el texto: `Alpha occ. eigenvalues`.
2. Localizar el último número de la última línea `Alpha occ. eigenvalues --`. Ese valor numérico corresponde a la energía del orbital ocupado de mayor energía, $\varepsilon_{\text{HOMO}}$ (en Hartrees).
3. Localizar el primer número de la línea inmediata siguiente `Alpha virt. eigenvalues --`, correspondiente al orbital desocupado de menor energía ($\varepsilon_{\text{LUMO}}$).
4. Copiar el valor de $\varepsilon_{\text{HOMO}}$ (en Hartrees) en la columna correspondiente de la tabla de resultados.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: fragmento del archivo .log mostrando las lineas Alpha occ. eigenvalues y Alpha virt. eigenvalues con los autovalores de HOMO y LUMO senalados]
:::

### Paso 7: Configurar y calcular el catión A⁺

1. Regresar a GaussView con el mismo centro atómico en pantalla.
2. Abrir nuevamente el panel **Calculate → Gaussian Calculation Setup**.
3. En la pestaña **Method**, modificar los siguientes parámetros:
   - **Charge**: cambiar de `0` a `1`.
   - **Spin**: ajustar a la multiplicidad correspondiente a la especie catiónica (ver tabla inferior). Al arrancar un electrón del HOMO, el número de electrones desapareados cambia.
4. Mantener **Job Type** en `Energy`, **Method** en `HF`, **Basis Set** en `STO-3G` y la palabra clave `pop=full` en **Additional Keywords**.
5. En la pestaña **Title**, escribir: `C cation HF STO-3G`.
6. Pulsar **Submit**, guardar con nombre representativo (por ejemplo, `C_cation_HF_STO3G.gjf`) en `{{practicas_folder}}` y confirmar el envío.
7. Verificar la terminación correcta en el nuevo `.log` y extraer la energía total $E(A^+)$ en la línea `SCF Done`.

| Campo | Neutro | Catión |
|---|:---:|:---:|
| Charge | 0 | +1 |
| Spin | Multiplicidad neutro | Multiplicidad catión |

Tabla de multiplicidades para los cationes ($A^+$):

| Catión | $Z$ | Configuración | Electrones desapareados | Multiplicidad ($2S+1$) |
|---|:---:|---|:---:|:---:|
| He⁺ | 2 | 1s¹ | 1 | 2 |
| Li⁺ | 3 | [He] | 0 | 1 |
| Be⁺ | 4 | [He] 2s¹ | 1 | 2 |
| B⁺ | 5 | [He] 2s² | 0 | 1 |
| C⁺ | 6 | [He] 2s² 2p¹ | 1 | 2 |
| N⁺ | 7 | [He] 2s² 2p² | 2 | 3 |
| O⁺ | 8 | [He] 2s² 2p³ | 3 | 4 |
| F⁺ | 9 | [He] 2s² 2p⁴ | 2 | 3 |
| Ne⁺ | 10 | [He] 2s² 2p⁵ | 1 | 2 |

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup para el cation mostrando la pestana Method con Charge=1 y multiplicidad correspondiente]
:::

### Paso 8: Calcular las energías de ionización

1. Calcular la energía de ionización por diferencia directa ($\text{IE}_{\Delta E}$):
   $$\text{IE}_{\Delta E} = \bigl[E(A^+) - E(A)\bigr] \times {{ha_to_ev}} \quad [\text{eV}]$$
2. Calcular la estimación del teorema de Koopmans ($\text{IE}_{\text{Koopmans}}$):
   $$\text{IE}_{\text{Koopmans}} = -\varepsilon_{\text{HOMO}} \times {{ha_to_ev}} \quad [\text{eV}]$$
3. Registrar ambos valores en electronvoltios en la tabla de datos y calcular la desviación porcentual respecto al valor experimental de referencia.

---

## Resultados y análisis

Para cada átomo calculado, se registran las dos energías extraídas del archivo `.log` y se calculan ambas estimaciones de la energía de ionización. La tabla siguiente recoge los valores en Hartrees y los resultados ya convertidos a eV. Los valores experimentales de referencia se incluyen para calcular el error porcentual.

| Átomo | $E(N)$ (Ha) | $E(A^+)$ (Ha) | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\Delta E}$ (eV) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| H | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 13.60 | [TEXTO HUMANO] |
| He | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 24.59 | [TEXTO HUMANO] |
| Li | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 5.39 | [TEXTO HUMANO] |
| Be | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 9.32 | [TEXTO HUMANO] |
| B | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 8.30 | [TEXTO HUMANO] |
| C | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| N | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 14.53 | [TEXTO HUMANO] |
| O | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 13.62 | [TEXTO HUMANO] |
| F | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 17.42 | [TEXTO HUMANO] |
| Ne | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | 21.56 | [TEXTO HUMANO] |

### Visualización de orbitales

Para visualizar el HOMO de un átomo calculado, se abre el archivo `.log` en GaussView desde **File → Open** y se accede al menú **Results → MOs**. En el panel de orbitales moleculares, se selecciona el orbital de mayor energía marcado como ocupado y se genera la isosuperficie tridimensional ajustando el valor de contorno a 0.04 unidades atómicas. Para orbitales de tipo $s$, la isosuperficie adopta forma esférica sin planos nodales. Para orbitales de tipo $p$, aparecen dos lóbulos separados por un plano nodal perpendicular al eje de simetría.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: isosuperficie tridimensional del orbital HOMO del carbono en GaussView Results → MOs]
:::

:::{note}
A lo largo del período Li-Ne, la morfología del HOMO cambia de un orbital 2s esférico (Li, Be) a un orbital 2p con un plano nodal (B hasta Ne). En los átomos con la subcapa 2p semillena (N) o completa (Ne), la distribución de densidad resultante es especialmente compacta. Observar estos cambios de forma en GaussView permite relacionar la geometría del orbital con la energía de ionización calculada.
:::

---

## Preguntas

1. ¿Qué valor numérico de energía en Hartrees reporta la línea `SCF Done` para el átomo de carbono neutro y cuál es el autovalor del orbital HOMO en la línea `Alpha occ. eigenvalues`? Convertir ambos valores a electronvoltios mediante el factor {{ha_to_ev}}.
2. Analizar la evolución de la energía de ionización a lo largo del período litio-neón. Justificar la caída observada al pasar del nitrógeno ($Z=7$) al oxígeno ($Z=8$) relacionando la ocupación de los orbitales $2p$ con la repulsión coulómbica interelectrónica.
3. El teorema de Koopmans asume que los orbitales moleculares permanecen invariables tras la ionización (aproximación de orbitales congelados). Explicar por qué la relajación orbital reduce la energía real del catión y describir cómo la falta de correlación electrónica en Hartree-Fock compensa parcialmente esta desviación.
4. Comparar los valores de $\text{IE}_{\Delta E}$ y $\text{IE}_{\text{Koopmans}}$ obtenidos con la base STO-3G para helio y neón frente a los datos experimentales ($24.59\text{ eV}$ y $21.56\text{ eV}$ respectivamente). Justificar por qué una base mínima describe con menor fidelidad los sistemas compactos o con mayor densidad electrónica frente a bases extendidas con funciones difusas.
5. Si en GaussView se configurase el cálculo del átomo de boro neutro ($Z=5$) con multiplicidad 1 en lugar de 2, ¿qué inconsistencia numérica registraría Gaussian en el reparto de electrones $\alpha$ y $\beta$? Explicar por qué el formalismo RHF resulta inaplicable a sistemas atómicos de capa abierta.

---

## Bibliografía

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 9 (Estructura electrónica atómica).
- NIST Chemistry WebBook, https://webbook.nist.gov (datos experimentales de energía de ionización).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Esta exploración estudia cómo varía la calidad del resultado al ampliar el conjunto de funciones de base. Se repite el cálculo del átomo de carbono neutro con tres bases de diferente tamaño y se comparan la energía del HOMO y la energía de ionización estimada por Koopmans frente al valor experimental de referencia. El procedimiento es idéntico al de la práctica principal, cambiando únicamente el campo **Basis Set** en la pestaña **Method** de **Gaussian Calculation Setup**.

| Base | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:---:|:---:|:---:|:---:|:---:|
| STO-3G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| 3-21G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| 6-311G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |

:::{note}
¿En qué sentido varía $\varepsilon_{\text{HOMO}}$ al aumentar el tamaño de la base? ¿Disminuye el error respecto al valor experimental de forma monótona, o hay algún caso en que una base mayor no mejora el resultado? Relaciona las diferencias con la capacidad de cada base para describir la densidad electrónica en la región de valencia.
:::
::::
