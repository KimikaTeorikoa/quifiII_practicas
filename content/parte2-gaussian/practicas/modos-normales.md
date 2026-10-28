# Modos normales de vibración

## Introducción

La absorción de radiación infrarroja surge de la interacción entre el campo electromagnético y las vibraciones nucleares. Para modelar este fenómeno, Gaussian calcula las frecuencias vibracionales diagonalizando la matriz hessiana de la energía potencial, lo que descompone el movimiento molecular en oscilaciones armónicas independientes. El análisis de los modos normales resultantes proporciona las frecuencias teóricas, permite visualizar los desplazamientos atómicos en GaussView y determina su actividad en el espectro infrarrojo según las reglas de simetría molecular.

## Objetivos

1. Calcular los grados de libertad vibracionales independientes de moléculas lineales modelo ($\text{CO}$ y $\text{CO}_2$).
2. Optimizar la geometría molecular y calcular las frecuencias armónicas mediante el método combinado `Opt+Freq` con B3LYP/6-311G.
3. Visualizar y clasificar los desplazamientos atómicos correspondientes a modos de estiramiento y flexión mediante animaciones en GaussView.
4. Evaluar la actividad espectral en el infrarrojo comprobando la variación del momento dipolar molecular ($\partial \vec{\mu}/\partial Q$) y el valor de intensidad calculada (`IR Inten`).
5. Comparar las frecuencias armónicas teóricas con las bandas de absorción experimentales para cuantificar el efecto de la anarmonicidad.

## Conceptos clave

### Las moléculas vibran: modelo del oscilador armónico

En la aproximación armónica, los núcleos oscilan en torno a la geometría de equilibrio como un oscilador. Cuanto más rígido es el enlace (mayor $k$) y cuanto menor es la masa reducida $\mu$ de los átomos implicados, mayor es la frecuencia de la vibración. Gaussian obtiene las constantes de fuerza calculando las segundas derivadas de la energía respecto a los desplazamientos nucleares en el mínimo de la PES.

$$\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}$$

:::{admonition} Nota
:class: note
Gaussian calcula las constantes de fuerza mediante las segundas derivadas de la energía potencial respecto a los desplazamientos nucleares (matriz hessiana) en la geometría optimizada. Esta aproximación trunca el desarrollo en serie de Taylor en el término cuadrático y asume un potencial armónico ideal. Como los enlaces moleculares reales presentan anarmonicidad a mayores distancias internucleares, las frecuencias calculadas suelen sobreestimar de forma sistemática los valores experimentales obtenidos por espectroscopía infrarroja.
:::

### Modos normales y grados de libertad vibracionales

En cada modo normal, todos los núcleos de la molécula oscilan en fase y a una única frecuencia característica. Una molécula de $N$ átomos tiene $3N-5$ modos vibracionales si es lineal y $3N-6$ si no lo es, una vez descontados los grados de libertad de traslación y rotación del centro de masas. La diagonalización del hessiano en coordenadas de masa ponderada proporciona directamente estas frecuencias y los vectores de desplazamiento nuclear asociados a cada modo.

### Reglas de selección en espectroscopía infrarroja

Un modo de vibración absorbe radiación infrarroja únicamente si el movimiento nuclear produce una variación neta del momento dipolar molecular ($\partial \vec{\mu}/\partial Q \neq 0$). En moléculas simétricas, algunos modos conservan la simetría de inversión durante la vibración y no alteran el dipolo: son modos inactivos en IR. En el archivo `.log`, la actividad de cada modo queda recogida en el campo `IR Inten`: un valor nulo indica inactividad.

:::{admonition} Nota
:class: note
La absorción de radiación infrarroja requiere que el movimiento vibracional altere el momento dipolar molecular ($\partial \vec{\mu}/\partial Q \neq 0$). En el estiramiento simétrico del $\text{CO}_2$, la simetría de inversión se conserva y la variación neta del dipolo es nula, por lo que el modo no se acopla con el campo electromagnético incidente. En el archivo `.log`, esta inactividad se manifiesta con un valor de intensidad infrarroja (`IR Inten`) de 0.0000.
:::

### Requisito operativo: optimización previa de geometría

El cálculo de frecuencias requiere que la geometría de partida sea un mínimo real de la PES, porque las derivadas segundas solo tienen significado físico en un punto estacionario. Si la geometría no está optimizada, algunos autovalores del hessiano resultan negativos y aparecen frecuencias imaginarias en el `.log`, sin interpretación vibracional válida.

:::{admonition} Advertencia
:class: warning
Es imprescindible optimizar la geometría antes de calcular frecuencias. El cálculo sobre geometrías no estacionarias genera frecuencias imaginarias carentes de significado físico. En esta práctica se emplea la opción combinada `Opt+Freq` para garantizar que el cálculo vibracional parte del mínimo exacto.
:::

## Procedimiento

### Paso 1: Construir CO en GaussView

Construir la molécula de CO y aplicar **Edit → Clean** para obtener una geometría inicial razonable.

### Paso 2: Configurar el cálculo combinado Opt+Freq

1. Acceder al menú **Calculate → Gaussian Calculation Setup**.
2. En la pestaña **Job Type**, seleccionar la opción **Opt+Freq**. Comprobar que en la parte inferior quedan activadas simultáneamente las tareas de optimización de geometría y cálculo de constantes de fuerza armónicas.
3. En la pestaña **Method**, configurar los parámetros de cálculo:

| Campo | Valor |
|---|---|
| Job Type | Opt+Freq |
| Method | `[MÉTODO]` |
| Basis Set | `[BASE]` |
| Charge | **0** |
| Spin (Multiplicity) | **1** |

4. En la pestaña **Title**, escribir una descripción identificativa.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup con Job Type Opt+Freq y Method B3LYP/6-311G seleccionados]
:::

### Paso 3: Guardar y lanzar

1. Pulsar **Submit**, guardar el archivo como `CO_opt_freq.gjf` en `{{practicas_folder}}ModoNormales/` y confirmar el envío.

### Paso 4: Leer la distancia de enlace optimizada

1. En GaussView, abrir el `.log` resultante mediante **File → Open** y acceder a **Results → Optimization** para situarse en el último fotograma.
2. Seleccionar los dos átomos para leer la distancia C–O en la barra inferior, o bien buscar `! R1    R(1,2)` en el `.log` con **Ctrl + F**.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Optimization en GaussView mostrando la estructura optimizada de CO y la distancia de enlace C-O en la barra inferior]
:::

### Paso 5: Extraer parámetros vibracionales del .log

Buscar `Frequencies --` en el `.log` con **Ctrl + F**. Para cada modo, anotar:
- `Frequencies --`: frecuencia vibracional en $\text{cm}^{-1}$.
- `Red. masses --`: masa reducida en uma.
- `Frc consts  --`: constante de fuerza en mdyne/Å.
- `IR Inten    --`: intensidad de absorción en km/mol.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: fragmento del archivo .log mostrando el bloque Frequencies con los valores de frecuencia, masa reducida, constante de fuerza e intensidad IR]
:::

### Paso 6: Visualizar la animación del modo normal

1. En GaussView, con el archivo `CO_opt_freq_B3LYP_6311G.log` abierto, acceder al menú **Results → Vibrations**.
2. En la lista de modos normales, seleccionar la fila correspondiente a la frecuencia calculada (2063 $\text{cm}^{-1}$).
3. Activar la casilla **Start Animation** para observar el movimiento oscilatorio de los núcleos.
4. Marcar la casilla **Show Vectors** para visualizar las flechas de desplazamiento nuclear y comprobar que los átomos se mueven a lo largo del eje del enlace (modo de estiramiento).
5. Comprobar la amplitud relativa de las flechas: el átomo de carbono, al ser más ligero, experimenta un desplazamiento mayor que el de oxígeno.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Vibrations en GaussView mostrando el modo de estiramiento de CO con vectores de desplazamiento y frecuencia asociada]
:::

### Paso 7: Repetir el procedimiento para CO₂

1. Construir CO₂ en GaussView y aplicar **Edit → Clean** para obtener la geometría lineal O=C=O.
2. Configurar el cálculo con los mismos parámetros (`[MÉTODO]/[BASE]`, Opt+Freq, carga 0, multiplicidad 1). Guardar como `CO2_opt_freq.gjf` y lanzar.
3. Una vez completado, abrir el `.log` en GaussView y acceder a **Results → Vibrations**.
4. Animar cada uno de los cuatro modos normales y anotar sus frecuencias e intensidades. Relacionar la actividad IR de cada modo con la variación del momento dipolar que provoca la vibración.

---

## Bibliografía

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 12 (Espectroscopía vibracional).
- NIST Chemistry WebBook, https://webbook.nist.gov (datos experimentales de frecuencias vibracionales para CO y CO₂).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

El espectro infrarrojo del CO en fase gas muestra, además de la banda de vibración fundamental, una estructura de líneas finas debida al acoplamiento entre vibración y rotación. Al medir la separación entre líneas adyacentes de las ramas P y R ($\Delta\tilde{\nu} \approx 2B$) se puede determinar el momento de inercia de la molécula y, a partir de él, la distancia de equilibrio C–O con precisión espectroscópica. Los datos de referencia están disponibles en el NIST Chemistry WebBook.
::::
