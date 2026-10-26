# P2-B: Superficie de Energía Potencial

## Introducción

:::{note}
[TEXTO HUMANO: motivación — ¿qué mantiene unidos los átomos en una molécula? La energía
total del sistema depende de la distancia entre los núcleos. Si acercamos demasiado dos
átomos se repelen; si los alejamos demasiado el enlace se rompe. Entre esos extremos hay
un mínimo: la distancia de enlace. En esta práctica calcularemos esa curva de energía para
el H₂ y veremos por qué solo el estado singlete forma enlace. Después aplicaremos el mismo
concepto a una coordenada diferente: el ángulo diedro de un dihaloetano.]
:::

## Objetivos

:::{note}
[TEXTO HUMANO: lista numerada. Propuesta:]

[PROPUESTA:
1. Entender qué es una superficie de energía potencial (PES) y cómo se calcula.
2. Calcular la PES de H₂ en función de la distancia R(H–H) para el estado singlete y el
   triplete, e interpretar la diferencia.
3. Identificar la distancia de equilibrio calculada y compararla con el valor experimental.
4. Calcular la PES del 1,2-dicloroetano en función del ángulo diedro Cl–C–C–Cl e
   identificar los confórmeros estables.
5. Representar gráficamente las curvas de energía obtenidas.
]
:::

---

## Conceptos clave

### ¿Qué es una superficie de energía potencial?

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar la PES como un "paisaje energético". Si movemos los núcleos, la
energía electrónica cambia. Un mínimo en ese paisaje corresponde a una estructura estable
(molécula o confórmero). Una barrera es la energía que hay que superar para pasar de una
estructura a otra. La disociación es el límite cuando los átomos se separan infinitamente.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: diagrama esquemático de una PES en 1D mostrando: zona de repulsión (izquierda),
mínimo (distancia de equilibrio), zona de disociación (derecha) con la energía de
disociación D₀ marcada]
:::

### Singlete y triplete: por qué importa el spin

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: retomar el concepto de multiplicidad de P2-A. En H₂, dos electrones con
spines opuestos (↑↓, singlete) pueden formar un enlace covalente porque su función de
onda puede concentrarse entre los núcleos. Dos electrones con el mismo spin (↑↑, triplete)
no pueden ocupar el mismo orbital — el principio de exclusión de Pauli los repele, y la
curva de energía no tiene mínimo. Por eso el estado fundamental del H₂ es singlete.]
:::

### ¿Qué es un diedro?

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar el ángulo diedro (también llamado ángulo de torsión) como el
ángulo entre dos planos: el plano formado por los átomos A–B–C y el plano formado por
B–C–D. En el 1,2-dicloroetano, el diedro Cl–C–C–Cl describe la rotación alrededor del
enlace C–C. Diferentes valores del diedro corresponden a distintos confórmeros (gauche,
anti, eclipsado). Usar un diagrama de Newman.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: diagrama de Newman del 1,2-dicloroetano mostrando los confórmeros anti
(diedro=180°, más estable) y gauche (diedro=60°), con sus energías relativas]
:::

---

## Parte 1: PES del H₂

En esta primera parte calcularemos cómo varía la energía del H₂ al cambiar la distancia
entre los dos átomos. Lo haremos para el estado **singlete** (multiplicidad 1) y el
**triplete** (multiplicidad 3) y compararemos las dos curvas.

### Paso 1: Dibujar H₂ en GaussView

1. Abre GaussView. En la barra de herramientas selecciona el elemento **H**.
2. Haz clic en el área de dibujo para añadir el primer hidrógeno.
3. Haz clic sobre el átomo para añadir el segundo hidrógeno conectado con un enlace simple.
4. Aparecerán dos átomos H unidos por un enlace. La distancia inicial exacta no importa
   — el scan la variará automáticamente.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: GaussView con la molécula H₂ dibujada — dos átomos H con un enlace]
:::

### Paso 2: Configurar el scan en GaussView

1. Ve a **Calculate → Gaussian Calculation Setup**.
2. Pestaña **Job Type** → selecciona **Relaxed Potential Energy Surface Scan**.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup con Job Type = Relaxed PES Scan]
:::

3. Pestaña **Method**:

| Campo | Valor (singlete) | Valor (triplete) |
|-------|:---:|:---:|
| Method | **HF** | **HF** |
| Basis Set | **STO-3G** | **STO-3G** |
| Charge | **0** | **0** |
| Spin (Multiplicity) | **1** | **3** |

4. Pestaña **Additional Keywords** → escribe: `geom=connectivity`

:::{note}
[TEXTO HUMANO: instrucciones para definir la coordenada de scan dentro de GaussView —
cómo seleccionar el enlace R(H-H) en el panel de la pestaña de scan, y cómo introducir
los parámetros: valor inicial, incremento y número de puntos.]
:::

**Parámetros del scan confirmados en los logs de referencia:**

| Parámetro | Valor |
|-----------|-------|
| Coordenada | R(H₁–H₂) — distancia del enlace |
| Valor inicial | **0.55 Å** |
| Incremento | **0.05 Å** |
| Número de puntos | **21** |
| Valor final | 1.55 Å |

:::{warning}
Introduce los parámetros del scan exactamente como aparecen en la tabla. Un número de
puntos incorrecto o un incremento equivocado producirá una curva incompleta o deformada.
:::

### Paso 3: Lanzar y verificar

1. Haz clic en **Submit**.
2. Guarda el archivo `.gjf` en {{practicas_folder}}`PES/` con el nombre
   `H2_singlete_scan_STO3G.gjf`.
3. El scan tarda más que un cálculo de punto único: calcula 21 geometrías.
   Espera a que la barra de estado indique que ha terminado.

:::{danger}
Verifica la terminación correcta en el `.log` antes de leer cualquier resultado:

{{termination_ok}}
:::

4. Repite los pasos 1–3 para el **triplete** (multiplicidad 3). Guarda el archivo
   como `H2_triplete_scan_STO3G.gjf`.

### Paso 4: Ver la curva en GaussView

:::{tip}
Tras el cálculo, GaussView puede mostrar la curva PES directamente: ve a
**Results → Scan**. Verás un gráfico interactivo con la energía en función de la
coordenada de scan. Haz clic en cada punto para ver la geometría correspondiente.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → Scan de GaussView mostrando la curva PES del H₂ singlete
con el mínimo marcado alrededor de 0.70 Å]
:::

### Paso 5: Extraer la tabla de energías del `.log`

Abre el archivo `.log` con el editor de texto y busca (Ctrl+F): `SCF Done`

Cada aparición corresponde a un punto del scan. Copia el valor de energía de cada
una de las 21 líneas `SCF Done` en tu tabla.

La energía en Hartrees es muy negativa y varía poco entre puntos. Para visualizar mejor
la curva, convierte a **energía relativa** restando el mínimo:

$$
\Delta E(R) = \bigl[E(R) - E_{\min}\bigr] \times {{ha_to_kcal}} \quad [\text{kcal/mol}]
$$

---

## Parte 2: PES diedro de los dihaloetanos

Ahora aplicamos el mismo concepto a una coordinada diferente: la rotación alrededor
del enlace C–C de los 1,2-dihaloetanos (XCH₂–CH₂X). El ángulo diedro X–C–C–X va
de 0° a 360° y describe todos los confórmeros posibles.

Calcularás los tres compuestos siguientes, **en este orden de peso creciente del halógeno**:

| Compuesto | Halógeno | Fórmula | Abreviatura |
|-----------|----------|---------|-------------|
| 1,2-dicloroetano  | Cl | ClCH₂–CH₂Cl | DCE |
| 1,2-dibromoetano  | Br | BrCH₂–CH₂Br | DBE |
| 1,2-diyodoetano   | I  | ICH₂–CH₂I   | DIE |

El procedimiento es idéntico para los tres. Descríbelo una vez (con DCE) y repítelo
cambiando solo el halógeno.

### Paso 1: Dibujar el 1,2-dicloroetano en GaussView

:::{note}
[TEXTO HUMANO: instrucciones para construir ClCH₂–CH₂Cl en GaussView. Sugerencia:
empezar por el esqueleto C–C, añadir los átomos H y Cl sobre cada carbono usando
la tabla periódica, y usar **Edit → Clean** para ajustar la geometría inicial.
Para el DBE y el DIE: mismo procedimiento, solo cambiar el elemento del halógeno.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: GaussView con el 1,2-dicloroetano dibujado en 3D, mostrando los dos átomos Cl]
:::

### Paso 2: Configurar el scan diedro

1. Ve a **Calculate → Gaussian Calculation Setup → Job Type → Relaxed PES Scan**.
2. Pestaña **Method**:

| Campo | Valor |
|-------|-------|
| Method | [CONFIRMAR CON PROFESOR] |
| Basis Set | [CONFIRMAR CON PROFESOR] |
| Charge | **0** |
| Spin (Multiplicity) | **1** |

3. Pestaña **Additional Keywords**:

:::{note}
[TEXTO HUMANO: keywords necesarias para el scan diedro y cualquier otra opción
específica que indique el profesor.]
:::

:::{note}
[TEXTO HUMANO: instrucciones detalladas para seleccionar el diedro X–C–C–X en
GaussView y configurar los parámetros del scan — valor inicial, incremento y número
de puntos indicados por el profesor.]
:::

**Parámetros del scan diedro:**

| Parámetro | Valor |
|-----------|:-----:|
| Coordenada | D(X–C–C–X) — ángulo diedro |
| Valor inicial | [CONFIRMAR] |
| Incremento | [CONFIRMAR] |
| Número de puntos | [CONFIRMAR] |

:::{warning}
El scan diedro de una molécula con halógenos tarda más que el scan de H₂.
Lanza los tres cálculos (DCE, DBE, DIE) seguidos y espera los resultados.
:::

### Paso 3: Lanzar, verificar y leer resultados

1. Guarda los archivos en {{practicas_folder}}`PES/` con nombres descriptivos,
   por ejemplo: `DCE_diedro.gjf`, `DBE_diedro.gjf`, `DIE_diedro.gjf`.
2. Verifica la terminación de cada cálculo: {{termination_ok}}
3. Ve a **Results → Scan** en GaussView para ver la curva de torsión de cada compuesto.

---

## Resultados

### Tabla 1: PES de H₂ — energías calculadas

Completa las columnas de energía copiando los valores de `SCF Done` del `.log`.
La columna ΔE la calculas tú con la fórmula anterior.

| Punto | R (Å) | E singlete (Ha) | E triplete (Ha) | ΔE singlete (kcal/mol) | ΔE triplete (kcal/mol) |
|:-----:|:-----:|:---------------:|:---------------:|:----------------------:|:----------------------:|
| 1  | 0.55 | — | — | — | — |
| 2  | 0.60 | — | — | — | — |
| 3  | 0.65 | — | — | — | — |
| 4  | 0.70 | — | — | — | — |
| 5  | 0.75 | — | — | — | — |
| 6  | 0.80 | — | — | — | — |
| 7  | 0.85 | — | — | — | — |
| 8  | 0.90 | — | — | — | — |
| 9  | 0.95 | — | — | — | — |
| 10 | 1.00 | — | — | — | — |
| 11 | 1.05 | — | — | — | — |
| 12 | 1.10 | — | — | — | — |
| 13 | 1.15 | — | — | — | — |
| 14 | 1.20 | — | — | — | — |
| 15 | 1.25 | — | — | — | — |
| 16 | 1.30 | — | — | — | — |
| 17 | 1.35 | — | — | — | — |
| 18 | 1.40 | — | — | — | — |
| 19 | 1.45 | — | — | — | — |
| 20 | 1.50 | — | — | — | — |
| 21 | 1.55 | — | — | — | — |

### Representación gráfica de la PES del H₂

Una vez rellena la tabla, representa ΔE (kcal/mol) frente a R (Å) para ambas curvas
en el mismo gráfico. Puedes hacerlo con **LibreOffice Calc**:

1. Copia las columnas R, ΔE singlete y ΔE triplete a una hoja de cálculo.
2. Selecciona las tres columnas y ve a **Insertar → Gráfico**.
3. Elige tipo **Línea con puntos**. Pon R (Å) en el eje X y ΔE (kcal/mol) en el eje Y.
4. Añade título y etiquetas de ejes.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: gráfico con las dos curvas PES superpuestas — singlete con mínimo y triplete
monotónicamente creciente (o con asíntota), ambas llegando a un valor similar a R grande]
:::

### Tablas 2–4: PES diedro de los dihaloetanos

Para cada compuesto, extrae las 36 energías del `.log` (una por línea `SCF Done`) y
calcula ΔE restando el mínimo de cada serie. Usa la misma fórmula que en la Parte 1.

**Tabla 2 — 1,2-dicloroetano (DCE, X = Cl)**

| Diedro (°) | E (Ha) | ΔE (kcal/mol) | | Diedro (°) | E (Ha) | ΔE (kcal/mol) |
|:----------:|:------:|:-------------:|-|:----------:|:------:|:-------------:|
| 0   | — | — | | 190 | — | — |
| 10  | — | — | | 200 | — | — |
| 20  | — | — | | 210 | — | — |
| 30  | — | — | | 220 | — | — |
| 40  | — | — | | 230 | — | — |
| 50  | — | — | | 240 | — | — |
| 60  | — | — | | 250 | — | — |
| 70  | — | — | | 260 | — | — |
| 80  | — | — | | 270 | — | — |
| 90  | — | — | | 280 | — | — |
| 100 | — | — | | 290 | — | — |
| 110 | — | — | | 300 | — | — |
| 120 | — | — | | 310 | — | — |
| 130 | — | — | | 320 | — | — |
| 140 | — | — | | 330 | — | — |
| 150 | — | — | | 340 | — | — |
| 160 | — | — | | 350 | — | — |
| 170 | — | — | | | | |
| 180 | — | — | | | | |

**Tabla 3 — 1,2-dibromoetano (DBE, X = Br)** *(misma estructura)*

| Diedro (°) | E (Ha) | ΔE (kcal/mol) | | Diedro (°) | E (Ha) | ΔE (kcal/mol) |
|:----------:|:------:|:-------------:|-|:----------:|:------:|:-------------:|
| 0   | — | — | | 190 | — | — |
| 10  | — | — | | 200 | — | — |
| 20  | — | — | | 210 | — | — |
| 30  | — | — | | 220 | — | — |
| 40  | — | — | | 230 | — | — |
| 50  | — | — | | 240 | — | — |
| 60  | — | — | | 250 | — | — |
| 70  | — | — | | 260 | — | — |
| 80  | — | — | | 270 | — | — |
| 90  | — | — | | 280 | — | — |
| 100 | — | — | | 290 | — | — |
| 110 | — | — | | 300 | — | — |
| 120 | — | — | | 310 | — | — |
| 130 | — | — | | 320 | — | — |
| 140 | — | — | | 330 | — | — |
| 150 | — | — | | 340 | — | — |
| 160 | — | — | | 350 | — | — |
| 170 | — | — | | | | |
| 180 | — | — | | | | |

**Tabla 4 — 1,2-diyodoetano (DIE, X = I)** *(misma estructura)*

| Diedro (°) | E (Ha) | ΔE (kcal/mol) | | Diedro (°) | E (Ha) | ΔE (kcal/mol) |
|:----------:|:------:|:-------------:|-|:----------:|:------:|:-------------:|
| 0   | — | — | | 190 | — | — |
| 10  | — | — | | 200 | — | — |
| 20  | — | — | | 210 | — | — |
| 30  | — | — | | 220 | — | — |
| 40  | — | — | | 230 | — | — |
| 50  | — | — | | 240 | — | — |
| 60  | — | — | | 250 | — | — |
| 70  | — | — | | 260 | — | — |
| 80  | — | — | | 270 | — | — |
| 90  | — | — | | 280 | — | — |
| 100 | — | — | | 290 | — | — |
| 110 | — | — | | 300 | — | — |
| 120 | — | — | | 310 | — | — |
| 130 | — | — | | 320 | — | — |
| 140 | — | — | | 330 | — | — |
| 150 | — | — | | 340 | — | — |
| 160 | — | — | | 350 | — | — |
| 170 | — | — | | | | |
| 180 | — | — | | | | |

:::{tip}
Representa las tres curvas en el **mismo gráfico** en LibreOffice Calc: columna de
diedros en el eje X (0–360°), ΔE de los tres compuestos en el eje Y (kcal/mol).
Usa colores o estilos de línea distintos para cada halógeno. Esto permite comparar
visualmente cómo cambia la barrera de rotación con el tamaño del halógeno.
:::

---

## Preguntas y pruebas

:::{note}
[TEXTO HUMANO: preguntas de reflexión. Propuesta:]

[PROPUESTA:
**Sobre la PES del H₂:**
1. ¿A qué distancia R(H–H) aparece el mínimo de la curva singlete? ¿Coincide con el
   valor experimental de 0.74 Å? ¿Por qué hay diferencia?
2. ¿Por qué la curva triplete no tiene mínimo (o tiene un mínimo muy poco pronunciado)?
   ¿Qué significa físicamente?
3. ¿Qué representa la energía a R muy grande (límite de disociación)? ¿Por qué las dos
   curvas convergen al mismo valor?
4. ¿En qué región de la curva la energía crece más rápidamente? ¿A qué interacción física
   se debe?

**Sobre el diedro de los dihaloetanos:**
5. ¿Cuántos mínimos tiene la curva de torsión del DCE? ¿A qué ángulos aparecen?
   ¿Cómo se llaman esos confórmeros (anti, gauche, eclipsado)?
6. ¿Cuál es el confórmero más estable del DCE? ¿Por qué lo esperas a partir de la
   disposición espacial de los átomos de Cl?
7. Al comparar DCE, DBE y DIE: ¿cómo cambia la altura de la barrera de rotación con
   el tamaño del halógeno? ¿Y la posición del mínimo más estable?
8. ¿Crees que a temperatura ambiente el 1,2-dicloroetano puede rotar libremente
   alrededor del enlace C–C? Estima si la barrera es superable con energía térmica
   (kT ≈ 0.6 kcal/mol a 300 K).
]
:::

---

## Bibliografía

:::{note}
[TEXTO HUMANO: añadir referencia al manual interno de la asignatura si existe.]
:::

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018.
  Cap. 11 (Estructura molecular — superficies de energía potencial).
- Clayden, J.; Greeves, N.; Warren, S. *Organic Chemistry*, 2ª ed.; Oxford University
  Press, 2012. Cap. 18 (Conformational analysis).

---

::::{dropdown} Para ir más lejos *(opcional — solo si terminas antes de tiempo)*
:color: success


Esta sección es completamente **opcional** y no entra en la nota.

### El etano sin halógenos: ¿cuánto vale la barrera de rotación C–C?

Has calculado la barrera de rotación de los dihaloetanos con dos halógenos voluminosos.
¿Cómo es la barrera del **etano** (CH₃–CH₃), que solo tiene hidrógenos?

Repite el scan diedro para el etano usando los mismos parámetros de método y base
que el profesor indique para los dihaloetanos. Compara la altura de la barrera.

:::{note}
[TEXTO HUMANO: preguntas de extensión — ¿por qué la barrera del etano es distinta
a la del DCE? ¿Qué tipo de interacciones dominan en cada caso?]
:::
::::
