# P2-A: Átomos y el Teorema de Koopmans

## Introducción

:::{note}
[TEXTO HUMANO: motivación química — ¿por qué nos interesa la energía de ionización?
Conectar con las tendencias periódicas que el alumno ya conoce de Química General: la IE
aumenta a lo largo de un período y disminuye al bajar un grupo. Explicar que en esta práctica
comprobaremos si un modelo teórico sencillo (Hartree-Fock) reproduce esas tendencias, y
aprenderemos a interpretar qué nos dice el orbital más alto ocupado (HOMO) sobre la
reactividad del átomo.]
:::

## Objetivos

:::{note}
[TEXTO HUMANO: lista numerada de objetivos de aprendizaje. Propuesta:]

[PROPUESTA:
1. Aprender a realizar cálculos de energía de átomos con GaussView y {{gaussian_version}}.
2. Calcular la energía de ionización por dos métodos: diferencia de energías totales y
   teorema de Koopmans.
3. Comparar los valores calculados con los experimentales e identificar las tendencias
   periódicas.
4. Visualizar los orbitales atómicos HOMO en GaussView e interpretar su forma.
]
:::

---

:::{note}
Antes de empezar, asegúrate de haber leído la introducción a GaussView.
:::

---

## Conceptos clave

### ¿Por qué las energías son negativas?

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar en 3-4 frases, sin fórmulas, que un sistema ligado tiene menos
energía que sus partes separadas — de ahí el signo negativo. Analogía: una pelota en el
fondo de un pozo tiene menos energía que fuera del pozo. Gaussian siempre devuelve
energías negativas para sistemas estables; si ves un número positivo, algo ha ido mal.]
:::

### El HOMO y el LUMO

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que en un átomo o molécula, los electrones ocupan "pisos" de
energía llamados orbitales. El HOMO (Highest Occupied Molecular Orbital) es el piso más
alto que tiene electrones — y por tanto el electrón más fácil de arrancar. El LUMO
(Lowest Unoccupied Molecular Orbital) es el primer piso vacío, y determina dónde irían
nuevos electrones.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: diagrama esquemático de niveles de energía con HOMO y LUMO señalados,
y flecha indicando IE = energía necesaria para sacar el electrón del HOMO]
:::

### La energía de ionización

La energía de ionización (IE) es la energía mínima necesaria para arrancar un electrón
de un átomo neutro en estado gaseoso:

$$
\text{A} \rightarrow \text{A}^+ + e^-
$$

En esta práctica la calcularemos de **dos formas**:

**Vía 1 — Diferencia de energías totales:**

$$
\text{IE}_{\Delta E} = E(\text{A}^+) - E(\text{A})
$$

Hacemos dos cálculos separados: el átomo neutro A y el catión A⁺. La diferencia,
convertida a eV, es la IE.

**Vía 2 — Teorema de Koopmans:**

$$
\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}
$$

Con un único cálculo (el del átomo neutro) obtenemos una estimación de la IE.

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar por qué las dos vías no dan exactamente el mismo resultado.
El teorema de Koopmans asume que los orbitales del catión son idénticos a los del neutro,
lo cual no es del todo cierto porque al quitar un electrón los demás se reorganizan.
Además, el método Hartree-Fock no incluye la correlación entre electrones. Mencionar que
aun así la aproximación es sorprendentemente buena.]
:::

### La multiplicidad

:::{admonition} Intuición física
:class: intuicion
[TEXTO HUMANO: explicar en términos sencillos qué es el spin del electrón (↑ y ↓) y
cómo se cuenta la multiplicidad: 2S+1, donde S es la suma de los spines no apareados.
Ejemplos: H tiene 1 electrón desapareado → S=1/2 → mult=2. He tiene 2 electrones con
spines opuestos → S=0 → mult=1. Si la multiplicidad es incorrecta, Gaussian calculará
un estado excitado o devolverá un error.]
:::

**Unidades de energía:** Gaussian trabaja en Hartrees (Ha). Para convertir a eV:

$$
1 \text{ Ha} = {{ha_to_ev}} \text{ eV}
$$

---

## Procedimiento

:::{danger}
**Verificación obligatoria tras cada cálculo.**
Antes de anotar ningún resultado, abre el archivo `.log` con el editor de texto y
comprueba que la última línea dice exactamente:

{{termination_ok}}

Si no aparece esa línea, el cálculo ha fallado. No uses los resultados. Avisa al
profesor.
:::

### Paso 1: Abrir GaussView y dibujar el átomo

1. Abre GaussView desde el escritorio o el menú de aplicaciones.
2. En la barra de herramientas superior, haz clic en el icono de la **tabla periódica**
   (o ve a **View → Element Fragments**).
3. Selecciona el elemento que quieres calcular (por ejemplo, **C** para carbono).
4. Haz clic **una sola vez** en el área de dibujo central. Aparecerá el átomo.
5. No añadas ningún enlace ni ningún otro átomo.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: GaussView con un único átomo de carbono en el área de dibujo, sin enlaces]
:::

:::{tip}
Un átomo aislado es simplemente una "molécula" de un solo centro. GaussView lo trata
exactamente igual que cualquier molécula — no hay que hacer nada especial.
:::

### Paso 2: Configurar el cálculo del átomo neutro

1. Ve a **Calculate → Gaussian Calculation Setup**. Se abre una ventana con pestañas.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup con las pestañas Job Type, Method,
Title y Additional Keywords visibles]
:::

2. Pestaña **Job Type** → selecciona **Energy**.
3. Pestaña **Method** → configura:

| Campo | Valor |
|-------|-------|
| Method | **HF** |
| Basis Set | **STO-3G** |
| Charge | **0** |
| Spin (Multiplicity) | ver tabla de multiplicidades |

4. Pestaña **Additional Keywords** → escribe: `pop=full`

:::{admonition} ¿Para qué sirve `pop=full`?
:class: intuicion
Esta keyword le indica a Gaussian que incluya en el archivo `.log` las energías de
**todos** los orbitales moleculares. Sin ella, solo aparecen los datos de la energía
total y no podríamos leer $\varepsilon_{\text{HOMO}}$.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: pestaña Method con HF/STO-3G seleccionado, Charge=0, y la multiplicidad
correcta para el carbono (3)]
:::

**Multiplicidades (2S+1) para los tres primeros períodos:**

| Átomo | Z | Configuración electrónica | Multiplicidad |
|-------|---|--------------------------|:---:|
| H  | 1  | 1s¹              | 2 |
| He | 2  | 1s²              | 1 |
| Li | 3  | [He] 2s¹         | 2 |
| Be | 4  | [He] 2s²         | 1 |
| B  | 5  | [He] 2s² 2p¹     | 2 |
| C  | 6  | [He] 2s² 2p²     | 3 |
| N  | 7  | [He] 2s² 2p³     | 4 |
| O  | 8  | [He] 2s² 2p⁴     | 3 |
| F  | 9  | [He] 2s² 2p⁵     | 2 |
| Ne | 10 | [He] 2s² 2p⁶     | 1 |
| Na | 11 | [Ne] 3s¹         | 2 |
| Mg | 12 | [Ne] 3s²         | 1 |
| Al | 13 | [Ne] 3s² 3p¹     | 2 |
| Si | 14 | [Ne] 3s² 3p²     | 3 |
| P  | 15 | [Ne] 3s² 3p³     | 4 |
| S  | 16 | [Ne] 3s² 3p⁴     | 3 |
| Cl | 17 | [Ne] 3s² 3p⁵     | 2 |
| Ar | 18 | [Ne] 3s² 3p⁶     | 1 |

:::{warning}
La multiplicidad incorrecta es el error más frecuente en esta práctica. Consúltala
en la tabla antes de lanzar cada cálculo.
:::

### Paso 3: Lanzar el cálculo y guardar el archivo

1. Haz clic en **Submit** en la ventana de configuración.
2. GaussView te pedirá guardar el archivo `.gjf`. Guárdalo en
   {{practicas_folder}}`Koopmans/` con un nombre como `C_neutro_HF_STO3G.gjf`.
3. El cálculo comenzará; la barra de estado de GaussView lo indicará.
4. Tiempo aproximado: átomos del 1er y 2º período → **segundos**;
   3er período → menos de un minuto.

:::{note}
[TEXTO HUMANO: instrucciones específicas del laboratorio si el lanzamiento difiere
del descrito — por ejemplo, si hay que usar un servidor remoto.]
:::

### Paso 4: Verificar la terminación correcta

1. Abre el archivo `.log` con el editor de texto
   (clic derecho sobre el archivo → **Abrir con → Editor de texto**).
2. Ve al final del archivo con **Ctrl + Fin**.
3. La última línea debe ser exactamente: {{termination_ok}}

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: final de un archivo .log mostrando la línea "Normal termination of Gaussian 16"]
:::

### Paso 5: Leer la energía total E(N)

Con el `.log` abierto, busca con **Ctrl + F** el texto: `SCF Done`

Verás una línea como esta:

```
SCF Done:  E(ROHF) =  -37.19864000     A.U. after    8 cycles
```

El número después de `E(RHF) =` o `E(ROHF) =` es la energía total en **Hartrees**.
Cópialo y pégalo en tu tabla de resultados.

:::{tip}
Usa `E(RHF)` para átomos con multiplicidad 1 (capa cerrada) y `E(ROHF)` para el
resto. Ambos son energías totales — el nombre solo indica el tipo de cálculo HF.
:::

### Paso 6: Leer ε_HOMO

En el mismo `.log`, busca: `Alpha occ. eigenvalues`

```
Alpha  occ. eigenvalues --  -11.32466  -0.82007  -0.45085  -0.45085  -0.45085
Alpha virt. eigenvalues --    0.55445   0.60267
```

- Línea `occ.` → orbitales **ocupados**. El **último valor** es ε_HOMO.
  En el ejemplo: ε_HOMO = −0.45085 Ha.
- Línea `virt.` → orbitales **virtuales**. El **primer valor** es ε_LUMO.

:::{tip}
Anota también ε_LUMO — lo necesitarás en las preguntas.
:::

### Paso 7: Calcular el catión A⁺

Repite los pasos 1–5 para el mismo átomo, cambiando solo en **Method**:

| Campo | Neutro | Catión |
|-------|:------:|:------:|
| Charge | 0 | **+1** |
| Spin (Multiplicity) | ver tabla | **multiplicidad del catión** |

:::{note}
[TEXTO HUMANO: explicar cómo obtener la multiplicidad del catión. Al quitar el electrón
HOMO cambia el número de electrones desapareados. Ejemplo: C neutro → [He]2s²2p²,
mult=3. C⁺ → [He]2s²2p¹, mult=2.]
:::

Guarda con nombre distinto (p. ej. `C_cation_HF_STO3G.gjf`) y lee E(A⁺) igual que
en el Paso 5.

### Paso 8: Calcular las energías de ionización

**Vía ΔE:**

$$
\text{IE}_{\Delta E} = \bigl[E(\text{A}^+) - E(\text{A})\bigr] \times {{ha_to_ev}}
\quad [\text{eV}]
$$

**Vía Koopmans:**

$$
\text{IE}_{\text{Koopmans}} = -\varepsilon_{\text{HOMO}} \times {{ha_to_ev}}
\quad [\text{eV}]
$$

---

## Resultados

Completa la tabla. Las tres primeras columnas de datos se copian del `.log`.
Las dos IE las calculas con las fórmulas del Paso 8.

| Átomo | $E(N)$ (Ha) | $E(\text{A}^+)$ (Ha) | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\Delta E}$ (eV) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:-----:|:-----------:|:--------------------:|:---:|:---:|:---:|:---:|:---:|
| H  | — | — | — | — | — | 13.60 | — |
| He | — | — | — | — | — | 24.59 | — |
| Li | — | — | — | — | — | 5.39  | — |
| Be | — | — | — | — | — | 9.32  | — |
| B  | — | — | — | — | — | 8.30  | — |
| C  | — | — | — | — | — | 11.26 | — |
| N  | — | — | — | — | — | 14.53 | — |
| O  | — | — | — | — | — | 13.62 | — |
| F  | — | — | — | — | — | 17.42 | — |
| Ne | — | — | — | — | — | 21.56 | — |
| Na | — | — | — | — | — | 5.14  | — |
| Mg | — | — | — | — | — | 7.65  | — |
| Al | — | — | — | — | — | 5.99  | — |
| Si | — | — | — | — | — | 8.15  | — |
| P  | — | — | — | — | — | 10.49 | — |
| S  | — | — | — | — | — | 10.36 | — |
| Cl | — | — | — | — | — | 12.97 | — |
| Ar | — | — | — | — | — | 15.76 | — |

:::{tip}
Estrategia eficiente: lanza primero todos los cálculos de átomos neutros (columnas
$E(N)$ y $\varepsilon_{\text{HOMO}}$), luego todos los cationes ($E(\text{A}^+)$).
Así maximizas el tiempo que Gaussian está trabajando mientras tú preparas el siguiente.
:::

## Visualización de orbitales

:::{tip}
Tras el cálculo del átomo neutro, ve a **Results → MOs** en GaussView. Verás un diagrama
de niveles. Haz **doble clic** sobre el HOMO (el ocupado de mayor energía) para verlo
en 3D. Ajusta **Isovalue = 0.02** a.u. en el panel lateral para una buena visualización.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → MOs con el HOMO del carbono visualizado como isosuperficie
3D — dos lóbulos de orbital p, uno rojo y otro azul]
:::

:::{note}
[TEXTO HUMANO: instrucciones para visualizar el HOMO de al menos tres átomos (H, C, Ne)
y describir cómo cambia la forma a lo largo del período. ¿Es esférico o tiene lóbulos?]
:::

---

## Preguntas y pruebas

:::{note}
[TEXTO HUMANO: preguntas de reflexión. Propuesta:]

[PROPUESTA:
1. ¿En qué átomos coinciden mejor IE$_{\Delta E}$ e IE$_{\text{Koopmans}}$?
   ¿En cuáles difieren más? ¿Qué suposición del teorema de Koopmans se viola en esos casos?
2. ¿Se reproduce la tendencia periódica esperada? ¿Hay algún átomo que rompe la tendencia?
   Explícalo con la configuración electrónica.
3. La IE del O es menor que la del N. ¿Cómo lo explica la regla de Hund?
4. ¿Qué forma tiene el HOMO del hidrógeno? ¿Y el del carbono? ¿Por qué son distintos?
5. ¿Cuál de las dos vías (ΔE o Koopmans) da mayor error? Propón una razón.
6. ¿Qué le pasaría al resultado si introdujeras una multiplicidad incorrecta?
   ¿Cómo detectarías el error sin conocer el resultado experimental?
]
:::

---

## Bibliografía

:::{note}
[TEXTO HUMANO: añadir referencia al manual interno de la asignatura si existe.]
:::

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018.
  Cap. 9 (Estructura electrónica atómica).

[PROPUESTA: Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*, Dover, 1996, cap. 1–3,
como lectura opcional para alumnos con más curiosidad matemática.]

---

::::{dropdown} Para ir más lejos *(opcional — solo si terminas antes de tiempo)*
:color: success

Esta sección es completamente **opcional** y no entra en la nota. Si has terminado
todo lo anterior y te queda tiempo, prueba el siguiente ejercicio.

### Efecto del tamaño de la base

Hasta ahora hemos usado **STO-3G**, la base más sencilla disponible. Repite el cálculo
del **carbono neutro** cambiando únicamente el campo **Basis Set** en
**Calculate → Gaussian Calculation Setup → Method**:

| Base | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:----:|:---:|:---:|:---:|:---:|
| STO-3G  | — *(ya lo tienes)* | — | 11.26 | — |
| 3-21G   | — | — | 11.26 | — |
| 6-311G  | — | — | 11.26 | — |

:::{note}
[TEXTO HUMANO: preguntas para esta subsección — ¿mejora el acuerdo con el experimento
al ampliar la base? ¿A partir de qué base el error se estabiliza? No hace falta entender
qué significa cada base — basta con observar la tendencia numérica.]
:::
::::
