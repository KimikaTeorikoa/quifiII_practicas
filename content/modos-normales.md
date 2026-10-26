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

Párrafo muy corto + figura. Construcción de la molécula diatómica de monóxido de carbono en la ventana de dibujo de GaussView mediante la adición sucesiva de átomos de C y O enlazados.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: molécula CO construida en GaussView con enlace simple o múltiple visible]
```

### Paso 2: Configurar el cálculo combinado Opt+Freq

Párrafo medio + tabla + figura. Selección de opciones en **Calculate → Gaussian Calculation Setup**: Job Type Opt+Freq, Method B3LYP, Basis Set 6-311G, Charge 0, Spin 1, y palabra clave `geom=connectivity` en Additional Keywords.

| Campo | Valor |
|---|---|
| Job Type | Opt+Freq |
| Method | B3LYP |
| Basis Set | 6-311G |
| Charge | 0 |
| Spin (Multiplicity) | 1 |
| Additional Keywords | `geom=connectivity` |

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup con Job Type Opt+Freq y Method B3LYP/6-311G seleccionados]
```

### Paso 3: Lanzar y verificar

Párrafo corto. Guardado del archivo como `CO_opt_freq_B3LYP_6311G.gjf` en `{{practicas_folder}}ModoNormales/`, seguimiento del cálculo en la barra de estado y confirmación de finalización correcta en el archivo `.log`.

### Paso 4: Leer la distancia de enlace optimizada

Párrafo corto. Extracción del parámetro geométrico $R(1,2)$ correspondiente a la longitud de enlace C–O optimizada (en Ångströms) en la tabla final del archivo `.log` o mediante **Results → Optimization**.

### Paso 5: Extraer parámetros vibracionales del .log

Párrafo medio. Localización del bloque `Frequencies --` en el archivo `.log`. Registro de los cuatro parámetros característicos del modo de vibración: frecuencia ($\text{cm}^{-1}$), intensidad infrarroja (`IR Inten`), masa reducida (`Red. masses`) y constante de fuerza armónica (`Frc consts`).

### Paso 6: Visualizar la animación del modo normal

Párrafo corto + figura. Apertura del panel **Results → Vibrations**, activación de la animación tridimensional e inspección del vector de desplazamiento para identificar el movimiento de estiramiento C–O.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Vibrations en GaussView mostrando el modo de estiramiento de CO con vectores de desplazamiento y frecuencia asociada]
```

### Paso 7: Repetir el procedimiento para CO₂

Párrafo medio + tabla + figura. Construcción de dióxido de carbono en disposición lineal (O=C=O), ejecución del cálculo Opt+Freq bajo idénticas condiciones teóricas y caracterización de los 4 modos normales generados.

Clasificación de los modos esperados para CO₂:

| Modo | Tipo de movimiento | Actividad IR esperada |
|:---:|---|:---:|
| 1 | Estiramiento simétrico | Inactivo |
| 2 | Estiramiento asimétrico | Activo |
| 3 | Flexión en el plano | Activo |
| 4 | Flexión fuera del plano | Activo |

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: molécula CO2 lineal en GaussView con la animación de un modo de flexión activada]
```

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
