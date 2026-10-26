# P2-C: Modos Normales de Vibración

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA - NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto (3-4 líneas). Motivación sobre la espectroscopía infrarroja como método experimental de identificación estructural. Interpretación física del movimiento oscilatorio de los núcleos en torno a sus posiciones de equilibrio molecular. Estudio comparativo de dos moléculas lineales modelo: monóxido de carbono (CO) y dióxido de carbono (CO₂).

:::{note}
[TEXTO HUMANO: introducción y motivación sobre espectroscopía infrarroja y frecuencias de vibración molecular]
:::

---

## Objetivos

Párrafo corto (lista numerada). Objetivos de aprendizaje de la práctica:
1. Comprensión conceptual de los modos normales de vibración y cálculo de grados de libertad independientes.
2. Optimización geométrica y cálculo de frecuencias armónicas mediante el método combinado Opt+Freq con B3LYP/6-311G.
3. Visualización dinámica y caracterización del tipo de movimiento (estiramiento y flexión) en GaussView.
4. Aplicación de las reglas de selección de actividad infrarroja según la derivada del momento dipolar.
5. Contraste cuantitativo de las frecuencias armónicas calculadas frente a datos espectroscópicos experimentales.

:::{note}
[TEXTO HUMANO: lista de objetivos formativos adaptada al guion del curso]
:::

---

## ¿Qué software vamos a usar?

Párrafo muy corto. Referencia al uso coordinado de GaussView para el modelado tridimensional y animación de vectores de desplazamiento, y {{gaussian_version}} para la evaluación de derivadas segundas de la energía respecto a coordenadas nucleares.

---

## Conceptos clave

### Las moléculas vibran: modelo del oscilador armónico

Párrafo medio. Aproximación armónica de la superficie de energía potencial en las proximidades del mínimo. Expresión de la frecuencia vibracional en función de la constante de fuerza ($k$) del enlace y la masa reducida ($\mu$) del sistema.

$$\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}$$

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: analogía mecánica de bolas unidas por muelles y relación entre rigidez de enlace, masa atómica y frecuencia]
:::

### Modos normales y grados de libertad vibracionales

Párrafo medio + tabla. Definición de modo normal como coordenada colectiva en la que todos los núcleos oscilan en fase a una única frecuencia característica. Deducción del número de grados de libertad vibracionales independientes: $3N-5$ para moléculas lineales y $3N-6$ para no lineales.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicación de desacoplamiento de movimientos moleculares complejos en patrones independientes elementales]
:::

Tabla de grados de libertad vibracionales:

| Molécula | $N$ | Geometría | Expresión | Modos vibracionales |
|---|:---:|---|:---:|:---:|
| CO | 2 | Lineal | $3N-5$ | 1 |
| CO₂ | 3 | Lineal | $3N-5$ | 4 |

### Reglas de selección en espectroscopía infrarroja

Párrafo medio. Condición de absorción de radiación infrarroja: variación neta del momento dipolar molecular a lo largo de la coordenada normal ($\partial \vec{\mu}/\partial Q \neq 0$). Explicación de por qué el estiramiento simétrico en CO₂ resulta inactivo en IR mientras que el asimétrico y las flexiones son activos.

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicación cualitativa de simetría molecular, cancelación de momentos dipolares y acoplamiento con el campo electromagnético]
:::

### Requisito operativo: optimización previa de geometría

Párrafo corto + advertencia. Justificación mecanocuántica de calcular derivadas segundas de la energía exclusivamente sobre geometrías optimizadas en el mínimo de la PES. Significado de autovalores imaginarios (frecuencias negativas) como indicativo de geometrías fuera de equilibrio o puntos de silla.

:::{warning}
Es imprescindible optimizar la geometría antes de calcular frecuencias. El cálculo sobre geometrías no estacionarias genera frecuencias imaginarias carentes de significado físico. En esta práctica se emplea la opción combinada `Opt+Freq` para garantizar que el cálculo vibracional parte del mínimo exacto.
:::

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la línea final exacta y la sección de frecuencias:
{{termination_ok}}
:::

### Paso 1: Dibujar CO en GaussView

1. Abrir GaussView desde el menú de aplicaciones o lanzador del sistema.
2. Abrir la paleta de elementos mediante **View → Element Fragments** (o haciendo clic en el icono de la tabla periódica en la barra superior).
3. Seleccionar el elemento carbono (**C**) y hacer clic en el área central de dibujo.
4. Seleccionar el elemento oxígeno (**O**) en la paleta de fragmentos.
5. Hacer clic sobre el átomo de carbono para añadir el átomo de oxígeno enlazado.
6. Aplicar una limpieza geométrica preliminar mediante **Edit → Clean** (o pulsar el icono de escoba en la barra de herramientas).

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: molécula CO construida en GaussView con enlace simple o múltiple visible]
:::

### Paso 2: Configurar el cálculo combinado Opt+Freq

1. Acceder al menú **Calculate → Gaussian Calculation Setup**.
2. En la pestaña **Job Type**, seleccionar la opción **Opt+Freq**. Comprobar que en la parte inferior quedan activadas simultáneamente las tareas de optimización de geometría y cálculo de constantes de fuerza armónicas.
3. En la pestaña **Method**, configurar los parámetros de cálculo:

| Campo | Valor |
|---|---|
| Job Type | Opt+Freq |
| Method | **B3LYP** |
| Basis Set | **6-311G** |
| Charge | **0** |
| Spin (Multiplicity) | **1** (Singlet) |
| Additional Keywords | `geom=connectivity` |

4. En la pestaña **Title**, escribir: `CO opt freq B3LYP 6-311G`.
5. En la pestaña **Additional Keywords**, escribir: `geom=connectivity`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup con Job Type Opt+Freq y Method B3LYP/6-311G seleccionados]
:::

### Paso 3: Lanzar y verificar

1. Pulsar el botón **Submit** en la ventana de configuración.
2. En el cuadro de diálogo de guardado, escribir el nombre del archivo: `CO_opt_freq_B3LYP_6311G.gjf`. Guardarlo en el directorio de trabajo: `{{practicas_folder}}ModoNormales/`.
3. Confirmar pulsando **Save** y seguidamente **Submit**.
4. Esperar a que el cálculo finalice en la barra de estado de GaussView (tiempo aproximado: 1-2 minutos).
5. Abrir el archivo `.log` (`CO_opt_freq_B3LYP_6311G.log`) en el editor de texto y desplazarse al final con **Ctrl + Fin** para verificar la presencia de la línea: `{{termination_ok}}`.
6. Confirmar que la etapa de frecuencias se ejecutó correctamente buscando la sección `Frequencies --`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: seccion final del archivo .log en el editor de texto mostrando la linea Normal termination of Gaussian 16 y el inicio del bloque de frecuencias]
:::

### Paso 4: Leer la distancia de enlace optimizada

1. En GaussView, abrir el archivo `.log` resultante mediante **File → Open**.
2. Acceder al menú **Results → Optimization** para visualizar la trayectoria de optimización y situarse en el último fotograma correspondiente al mínimo de energía.
3. Medir la longitud de enlace C–O optimizada seleccionando sucesivamente el átomo de carbono y el de oxígeno (el valor en Ångströms se muestra en la barra inferior de la ventana gráfica).
4. Alternativamente, en el archivo `.log` abierto en el editor de texto, buscar con **Ctrl + F** el texto: `! R1    R(1,2)`. El valor numérico adyacente (1.1473 Å) es la distancia de enlace de equilibrio.
5. Copiar la distancia calculada en la Tabla 1 de resultados.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Optimization en GaussView mostrando la estructura optimizada de CO y la distancia de enlace C-O en la barra inferior]
:::

### Paso 5: Extraer parámetros vibracionales del .log

1. En el archivo `.log` abierto en el editor de texto, buscar con **Ctrl + F** el texto: `Frequencies --`.
2. Localizar el bloque de datos correspondiente al único modo vibracional de la molécula de CO:
   - `Frequencies --`: frecuencia vibracional armónica en $\text{cm}^{-1}$ (valor calculado: 2063.4 $\text{cm}^{-1}$).
   - `Red. masses --`: masa reducida del oscilador en uma (13.44 uma).
   - `Frc consts  --`: constante de fuerza del enlace en mdyne/Å (33.71 mdyne/Å).
   - `IR Inten    --`: intensidad de absorción infrarroja en km/mol (70.16 km/mol).
3. Registrar estos valores en la Tabla 1 de resultados.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: fragmento del archivo .log mostrando el bloque Frequencies con los valores de frecuencia, masa reducida, constante de fuerza e intensidad IR]
:::

### Paso 6: Visualizar la animación del modo normal

1. En GaussView, con el archivo `CO_opt_freq_B3LYP_6311G.log` abierto, acceder al menú **Results → Vibrations**.
2. En la lista de modos normales, seleccionar la fila correspondiente a la frecuencia calculada (2063 $\text{cm}^{-1}$).
3. Activar la casilla **Start Animation** para observar el movimiento oscilatorio de los núcleos.
4. Activar la casilla **Show Vectors** para visualizar las flechas de desplazamiento nuclear y comprobar que los átomos se mueven a lo largo del eje del enlace (modo de estiramiento).
5. Observar la amplitud relativa de las flechas: el carbono (átomo más ligero) experimenta un desplazamiento mayor que el oxígeno (átomo más pesado).

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Vibrations en GaussView mostrando el modo de estiramiento de CO con vectores de desplazamiento y frecuencia asociada]
:::

### Paso 7: Repetir el procedimiento para CO₂

1. En GaussView, abrir una nueva ventana de trabajo mediante **File → New → Molecule Group**.
2. Abrir la paleta con **View → Element Fragments**, seleccionar carbono (**C**) y colocarlo en el centro de la ventana de dibujo.
3. Seleccionar oxígeno (**O**) y hacer clic a ambos lados del carbono para formar la estructura lineal O=C=O.
4. Aplicar **Edit → Clean** para orientar la geometría lineal preliminar con simetría $D_{\infty h}$.
5. Acceder a **Calculate → Gaussian Calculation Setup**:
   - Pestaña **Job Type**: seleccionar **Opt+Freq**.
   - Pestaña **Method**: Method **B3LYP**, Basis Set **6-311G**, Charge **0**, Spin **1**.
   - Pestaña **Title**: escribir `CO2 opt freq B3LYP 6-311G`.
   - Pestaña **Additional Keywords**: escribir `geom=connectivity`.
6. Pulsar **Submit**, guardar como `CO2_opt_freq_B3LYP_6311G.gjf` en `{{practicas_folder}}ModoNormales/` y confirmar el cálculo.
7. Verificar la terminación normal en el archivo `.log` (`CO2_opt_freq_B3LYP_6311G.log`).
8. Abrir el archivo `.log` en GaussView y acceder a **Results → Vibrations**.
9. Seleccionar sucesivamente cada uno de los 4 modos normales para animarlos y caracterizarlos:
   - Modo 1 (estiramiento simétrico, ~1388 $\text{cm}^{-1}$): los dos átomos de oxígeno se alejan y acercan al carbono en fase opuesta, manteniendo invariante el momento dipolar nulo (`IR Inten ≈ 0`, inactivo en IR).
   - Modo 2 (estiramiento asimétrico, ~2349 $\text{cm}^{-1}$): un enlace C–O se contrae mientras el otro se estira, generando una variación periódica del momento dipolar (`IR Inten` elevada, activo en IR).
   - Modos 3 y 4 (flexiones degeneradas, ~667 $\text{cm}^{-1}$): variación del ángulo de enlace O–C–O en dos planos mutuamente perpendiculares; ambas frecuencias presentan valores idénticos y son activas en IR.
10. Registrar las frecuencias calculadas de los cuatro modos en la Tabla 2 de resultados.

Clasificación de los modos esperados para CO₂:

| Modo | Tipo de movimiento | Actividad IR esperada |
|:---:|---|:---:|
| 1 | Estiramiento simétrico | Inactivo |
| 2 | Estiramiento asimétrico | Activo |
| 3 | Flexión en el plano | Activo |
| 4 | Flexión fuera del plano | Activo |

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Vibrations en GaussView mostrando la lista de los cuatro modos normales de CO2 y la animacion de un modo de flexion activada]
:::

---

## Resultados y análisis

### Tabla 1: Geometría y frecuencias de CO

Párrafo corto + tabla. Registro de la distancia de enlace optimizada y de la frecuencia vibracional calculada frente a los datos experimentales de referencia para CO.

| Magnitud | Calculado (B3LYP/6-311G) | Experimental | Error (%) |
|---|:---:|:---:|:---:|
| $R(\text{C–O})$ (Å) | [TEXTO HUMANO] | 1.128 | [TEXTO HUMANO] |
| $\tilde{\nu}$ CO ($\text{cm}^{-1}$) | [TEXTO HUMANO] | 2143 | [TEXTO HUMANO] |

### Tabla 2: Modos normales de vibración de CO₂

Párrafo corto + tabla. Vaciado sistemático de frecuencias calculadas para los cuatro modos normales de CO₂, identificación del tipo de movimiento vibracional, verificación de actividad IR e indicación del error relativo porcentual.

| Modo | Tipo de movimiento | $\tilde{\nu}$ calculada ($\text{cm}^{-1}$) | $\tilde{\nu}$ experimental ($\text{cm}^{-1}$) | Actividad IR | Error (%) |
|:---:|---|:---:|:---:|:---:|:---:|
| 1 | Estiramiento simétrico | [TEXTO HUMANO] | 1388 | Inactivo | [TEXTO HUMANO] |
| 2 | Estiramiento asimétrico | [TEXTO HUMANO] | 2349 | Activo | [TEXTO HUMANO] |
| 3 | Flexión (degenerada) | [TEXTO HUMANO] | 667 | Activo | [TEXTO HUMANO] |
| 4 | Flexión (degenerada) | [TEXTO HUMANO] | 667 | Activo | [TEXTO HUMANO] |

### Interpretación de resultados

Párrafo corto + figura. Pautas para el análisis de discrepancias sistemáticas entre el cálculo armónico DFT y las frecuencias fundamentales experimentales (efecto de la anarmonicidad y elección del funcional).

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: espectro IR sintetizado en GaussView Results → Vibrations para la molécula de CO2 con picos activos identificados]
```

---

## Preguntas y pruebas

Párrafo corto (cuestionario de discusión conceptual). Cuestiones orientadas a evaluar la asimilación física del contenido:
1. Comprobación del número de modos calculados frente a la relación teórica $3N-5$ en moléculas lineales.
2. Justificación rigurosa de la inactividad infrarroja del estiramiento simétrico de CO₂ mediante el análisis del momento dipolar.
3. Magnitud y signo del error relativo en las frecuencias calculadas de CO y CO₂: papel de la aproximación armónica frente al potencial real de Morse.
4. Consecuencias teóricas e interpretación práctica de la aparición eventual de frecuencias imaginarias en un archivo de salida.
5. Análisis de los vectores de desplazamiento en el estiramiento de CO: relación de amplitudes de desplazamiento entre carbono y oxígeno en función de sus masas atómicas relativas.

:::{note}
[TEXTO HUMANO: formulación detallada de preguntas y criterios de corrección]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 12 (Espectroscopía vibracional).
- NIST Chemistry WebBook, https://webbook.nist.gov (datos experimentales de frecuencias vibracionales para CO y CO₂).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Párrafo medio. Ampliación voluntaria sobre el acoplamiento rovibracional en moléculas diatómicas. Estudio de la estructura fina de ramas P y R en el espectro infrarrojo de CO y determinación de la constante rotacional $B$.

:::{note}
[TEXTO HUMANO: instrucciones para la extracción de constantes rotacionales del archivo .log y comparación con el espectro experimental]
:::
::::
