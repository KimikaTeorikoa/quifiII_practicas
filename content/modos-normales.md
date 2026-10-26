# P2-C: Modos Normales de Vibración

## Introducción

:::{note}
[TEXTO HUMANO: motivación — la espectroscopía IR como herramienta analítica cotidiana.
¿Qué mide un espectrómetro de IR? Conectar con que los átomos de una molécula no están
quietos: vibran alrededor de sus posiciones de equilibrio. En esta práctica calcularemos
esas vibraciones para el CO y el CO₂ y compararemos con los espectros experimentales.]
:::

## Objetivos

:::{note}
[TEXTO HUMANO: lista numerada. Propuesta:]

[PROPUESTA:
1. Entender qué es un modo normal de vibración y cuántos tiene cada molécula.
2. Calcular la geometría optimizada y las frecuencias vibracionales del CO con
   B3LYP/6-311G.
3. Visualizar los modos normales en GaussView e identificar su tipo (estiramiento,
   flexión).
4. Aplicar las reglas de selección IR para determinar qué modos son activos.
5. Comparar las frecuencias calculadas con los valores experimentales.
6. Repetir el análisis para el CO₂ y contrastar el número de modos activos.
]
:::

---

## Conceptos clave

### Las moléculas vibran

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que los átomos de una molécula no están quietos aunque la
molécula esté "optimizada". Vibran alrededor del mínimo de energía como masas unidas
por muelles. La frecuencia de vibración depende de la rigidez del enlace (constante de
fuerza) y de la masa de los átomos. Un enlace rígido y átomos ligeros → frecuencia alta.
Un enlace blando y átomos pesados → frecuencia baja.]
:::

### Modos normales

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que una molécula con N átomos tiene muchos movimientos posibles,
pero todos se pueden descomponer en combinaciones de movimientos más simples llamados
"modos normales", en los que todos los átomos oscilan en fase con la misma frecuencia.
Número de modos: 3N−5 para moléculas lineales, 3N−6 para no lineales. Dar ejemplos:
CO (N=2, lineal) → 1 modo; CO₂ (N=3, lineal) → 4 modos.]
:::

**Número de modos normales para las moléculas de esta práctica:**

| Molécula | N | Lineal | Fórmula | Modos vibracionales |
|----------|---|:------:|---------|:-------------------:|
| CO       | 2 | Sí  | 3N − 5 | **1** |
| CO₂      | 3 | Sí  | 3N − 5 | **4** |

### Reglas de selección IR

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que no todos los modos normales absorben luz infrarroja. Solo
los modos que cambian el momento dipolar de la molécula son "activos en IR". Ejemplo:
el estiramiento simétrico del CO₂ no cambia el dipolo (los dos extremos se mueven igual
y opuesto) → inactivo IR. El estiramiento asimétrico sí lo cambia → activo IR.
Esta regla permite identificar la simetría molecular a partir del espectro.]
:::

### Primer paso obligatorio: optimizar la geometría

:::{warning}
**Siempre hay que optimizar la geometría antes de calcular frecuencias.**
Si calculas frecuencias sobre una geometría no optimizada, obtendrás frecuencias
imaginarias (valores negativos) que no tienen significado físico. En esta práctica
usaremos `opt freq` para hacer los dos pasos en un solo cálculo.
:::

---

## Procedimiento

### Paso 1: Dibujar el CO en GaussView

1. Abre GaussView. Selecciona **C** (carbono) en la tabla periódica y haz clic en el
   área de dibujo.
2. Selecciona **O** (oxígeno) y haz clic sobre el carbono para añadirlo con un enlace.
3. La distancia inicial no importa — la optimización la ajustará.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: GaussView con la molécula CO dibujada — dos átomos con un enlace]
:::

### Paso 2: Configurar el cálculo opt+freq

1. Ve a **Calculate → Gaussian Calculation Setup**.
2. Pestaña **Job Type** → selecciona **Opt+Freq**.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: pestaña Job Type con Opt+Freq seleccionado]
:::

3. Pestaña **Method** (valores confirmados en los logs de referencia):

| Campo | Valor |
|-------|-------|
| Method | **B3LYP** |
| Basis Set | **6-311G** |
| Charge | **0** |
| Spin (Multiplicity) | **1** |

4. Pestaña **Additional Keywords** → escribe: `geom=connectivity`

:::{tip}
`Opt+Freq` realiza primero la optimización de geometría y luego, sobre la geometría
optimizada, calcula las frecuencias vibracionales. Es más eficiente que hacerlo en dos
cálculos separados — y garantiza que las frecuencias se calculan siempre en el mínimo.
:::

### Paso 3: Lanzar y verificar

1. Haz clic en **Submit**. Guarda como `CO_opt_freq_B3LYP_6311G.gjf` en
   {{practicas_folder}}`ModoNormales/`.
2. Este cálculo tarda más que un simple `Energy`: primero optimiza y luego calcula las
   derivadas segundas. Espera a que termine.

:::{danger}
Verifica la terminación correcta: {{termination_ok}}

Un cálculo `opt+freq` con terminación incorrecta puede haber completado la optimización
pero fallado en el paso de frecuencias. Comprueba que la sección de frecuencias esté
presente en el `.log` (busca `Frequencies --`).
:::

### Paso 4: Leer la geometría optimizada

Abre el `.log` y busca (Ctrl+F): `R1    R(1,2)`

Encontrarás una línea como:

```
! R1    R(1,2)                  1.1473         -DE/DX =    0.0                 !
```

El valor `1.1473` es la distancia C–O optimizada en **Ångströms**.

:::{tip}
También puedes ver la geometría optimizada en GaussView: ve a **Results → Optimization**
y haz clic en el último fotograma de la animación para ver la estructura final.
:::

### Paso 5: Leer la frecuencia vibracional

En el mismo `.log`, busca: `Frequencies --`

Verás un bloque como este (datos reales del log de referencia):

```
 Frequencies --   2063.3674
 Red. masses --     13.4388
 Frc consts  --     33.7103
 IR Inten    --     70.1641
```

- `Frequencies --` → frecuencia en **cm⁻¹**
- `IR Inten` → intensidad IR (proporcional a la absorbancia). Si es cero o muy pequeña,
  el modo es inactivo en IR.
- `Red. masses` → masa reducida del oscilador (en uma)
- `Frc consts` → constante de fuerza del enlace (en mdyne/Å)

:::{tip}
Para el CO (1 modo), habrá un único bloque `Frequencies --`. Para el CO₂ (4 modos),
habrá cuatro.
:::

### Paso 6: Visualizar el modo normal en GaussView

:::{tip}
Ve a **Results → Vibrations**. Verás una lista de los modos normales con sus frecuencias.
Haz clic sobre un modo para ver la animación: los átomos se moverán mostrando el patrón
de vibración. Identifica si el movimiento es un **estiramiento** (los átomos se acercan
y alejan a lo largo del enlace) o una **flexión** (el ángulo cambia).
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Vibrations de GaussView mostrando el único modo del CO
con la animación de estiramiento C–O y la frecuencia 2063 cm⁻¹ visible]
:::

### Paso 7: Repetir para el CO₂

:::{note}
[TEXTO HUMANO: instrucciones para dibujar CO₂ en GaussView (O=C=O lineal) y configurar
el mismo tipo de cálculo opt+freq con B3LYP/6-311G, multiplicidad 1.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: GaussView con la molécula CO₂ dibujada en su geometría lineal]
:::

El CO₂ tiene **4 modos normales**. Búscalos en el `.log` y clasifícalos:

| Modo | Descripción esperada | IR activo |
|:----:|---------------------|:---------:|
| 1 | Estiramiento simétrico (O←C→O) | No |
| 2 | Estiramiento asimétrico (O←C–O) | Sí |
| 3 | Flexión en el plano | Sí |
| 4 | Flexión fuera del plano | Sí |

:::{note}
[TEXTO HUMANO: guiar al alumno a identificar qué modo corresponde a qué número en el
output de Gaussian. Los modos degenerados (flexión ×2) aparecen con la misma frecuencia.]
:::

---

## Resultados

### Tabla de frecuencias: CO

| Magnitud | Calculado (B3LYP/6-311G) | Experimental | Error (%) |
|----------|:------------------------:|:------------:|:---------:|
| R(C–O) (Å) | — | 1.128 | — |
| ν̃ CO (cm⁻¹) | — | 2143 | — |

### Tabla de frecuencias: CO₂

Completa la tabla con los valores que obtengas del `.log`:

| Modo | Tipo | ν̃ calculada (cm⁻¹) | ν̃ experimental (cm⁻¹) | IR activo | Error (%) |
|:----:|------|:-------------------:|:---------------------:|:---------:|:---------:|
| 1 | Estiramiento simétrico | — | 1388 | No | — |
| 2 | Estiramiento asimétrico | — | 2349 | Sí | — |
| 3 | Flexión (×2) | — | 667 | Sí | — |

:::{note}
[TEXTO HUMANO: preguntas guiadas para interpretar las tablas — ¿en qué porcentaje difiere
la frecuencia calculada de la experimental? ¿Es el error sistemático (siempre en el mismo
sentido)? ¿Qué aproximación del cálculo explica esa diferencia?]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Vibrations del CO₂ mostrando los 4 modos listados con sus
frecuencias, con uno de los modos de flexión animado]
:::

---

## Preguntas y pruebas

:::{note}
[TEXTO HUMANO: preguntas de reflexión. Propuesta:]

[PROPUESTA:
1. ¿Cuántos modos normales tiene el CO? ¿Y el CO₂? ¿Coincide con la fórmula 3N−5?
2. ¿Por qué el estiramiento simétrico del CO₂ no es activo en IR? Explícalo en términos
   del momento dipolar.
3. La frecuencia calculada del CO es 2063 cm⁻¹ y la experimental es 2143 cm⁻¹.
   ¿En qué sentido se equivoca el cálculo? ¿Qué aproximación es responsable de ese error?
4. ¿Qué significaría encontrar una frecuencia imaginaria (negativa) en el output?
   ¿Cómo lo interpretarías?
5. Mira los vectores de desplazamiento del modo de estiramiento del CO en GaussView.
   ¿Cuál de los dos átomos se desplaza más? ¿Tiene sentido en términos de su masa?
]
:::

---

## Bibliografía

:::{note}
[TEXTO HUMANO: añadir referencia al manual interno de la asignatura si existe.]
:::

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018.
  Cap. 12 (Espectroscopía vibracional).
- NIST Chemistry WebBook, https://webbook.nist.gov — valores experimentales de
  frecuencias vibracionales de CO y CO₂.

---

::::{dropdown} Para ir más lejos *(opcional — solo si terminas antes de tiempo)*
:color: success


Esta sección es completamente **opcional** y no entra en la nota.

### Espectro rovibracional del CO

El CO no solo vibra — también rota. El espectro IR real del CO muestra una estructura
fina formada por las transiciones rotacionales superpuestas a la vibracional: son las
**ramas P y R** del espectro rovibracional.

:::{note}
[TEXTO HUMANO: instrucciones para esta extensión — qué datos adicionales hay que extraer
del log (constante rotacional B), cómo se calculan las posiciones de las líneas P y R,
y cómo comparar con el espectro experimental del NIST. Si el laboratorio dispone del
script `TheoEspRotBib.py`, indicar cómo usarlo.]
:::
::::
