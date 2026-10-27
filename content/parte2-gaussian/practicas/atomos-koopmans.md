# P2-A: Átomos y el Teorema de Koopmans

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA - NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto (3-4 líneas). Motivación química sobre la energía de ionización y su relación con las tendencias periódicas en la tabla periódica. Contraste del modelo teórico Hartree-Fock frente a datos experimentales e interpretación física del orbital más alto ocupado (HOMO).

:::{note}
[TEXTO HUMANO: introducción y motivación química sobre tendencias periódicas de energía de ionización]
:::

---

## Objetivos

Párrafo corto (lista numerada). Objetivos de aprendizaje de la sesión práctica:
1. Realización de cálculos de energía electrónica en átomos aislados mediante GaussView y {{gaussian_version}}.
2. Determinación de la energía de ionización por dos métodos: diferencia de energías totales ($\Delta E$) y teorema de Koopmans.
3. Comparación sistemática de los valores calculados con datos experimentales para los elementos del primer y segundo período.
4. Visualización tridimensional e interpretación de la simetría de los orbitales atómicos HOMO.

:::{note}
[TEXTO HUMANO: lista de objetivos formativos adaptada al guion del curso]
:::

---

## ¿Qué software vamos a usar?

Párrafo muy corto. Referencia al uso combinado de GaussView como entorno gráfico interactivo y {{gaussian_version}} como motor de cálculo de estructura electrónica. Consulta previa obligatoria de la guía de introducción a GaussView.

---

## Conceptos clave

### ¿Por qué las energías son negativas?

Párrafo corto. Explicación cualitativa del origen del signo negativo en sistemas ligados frente a partículas en reposo separadas en el infinito. Interpretación del pozo de potencial atractivo núcleo-electrón y comprobación de coherencia física en la salida del cálculo.

:::{admonition} 💡 Intuición física 
:class: intuicion
Piensa en una canica atrapada en el fondo de un cuenco hondo: necesitas empujarla y gastar energía para sacarla a la mesa, donde su energía relativa sería cero. En un átomo estable ocurre lo mismo, porque la atracción del núcleo crea una trampa energética que mantiene a los electrones confinados en un estado ligado. Por eso verás que el valor de `SCF Done` en tu archivo `.log` aparece precedido de un signo menos. Cuanto más negativo sea ese número, más fuertemente retenidos estarán los electrones y más estable será el átomo.
:::

### El HOMO y el LUMO

Párrafo corto + figura. Definición de orbitales frontera: orbital ocupado de mayor energía (HOMO) y primer orbital desocupado (LUMO). Relación entre el nivel energético del electrón más externo y la energía necesaria para su remoción.

:::{admonition} 💡 Intuición física
:class: intuicion
Imagina una estantería vertical donde vas colocando libros desde la balda inferior hasta que llenas las baldas intermedias. Si alguien quiere llevarse un libro con el menor esfuerzo posible, tirará del que descansa en la balda más alta alcanzada, que equivale exactamente a tu orbital HOMO. En tu cálculo, ese autovalor HOMO es el último número que aparece en la línea `Alpha occ. eigenvalues`. Ese nivel energético determina directamente la energía mínima necesaria para arrancar el primer electrón del átomo.
:::

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: diagrama de niveles de orbitales con HOMO y LUMO señalados y flecha indicando energía de ionización]
```

### La energía de ionización y el Teorema de Koopmans

Párrafo medio. Definición de energía de ionización para un átomo neutro en fase gas ($A \rightarrow A^+ + e^-$). Formulación de las dos vías metodológicas de evaluación cuántica: cálculo autoconsistente del catión (vía $\Delta E$) y aproximación por energía orbital (teorema de Koopmans).

$$\text{IE}_{\Delta E} = E(A^+) - E(A)$$

$$\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}$$

:::{admonition} 💡 Intuición física
:class: intuicion
Es como hacer una foto de grupo en un autobús lleno y asumir que, si una persona se baja de golpe, nadie cambiará de asiento para ponerse más cómodo. El teorema de Koopmans congela la distribución espacial del resto de partículas, olvidando que al perder una carga negativa las demás se reacomodan y relajan su energía. Por esta razón, comprobarás que el valor de $\text{IE}_{\text{Koopmans}}$ no coincide de forma exacta con la diferencia directa $\text{IE}_{\Delta E}$. Aunque ambas aproximaciones difieren ligeramente, los dos números siguen la misma tendencia ascendente a lo largo de la tabla periódica.
:::

### La multiplicidad de espín

Párrafo corto + tabla. Regla $2S+1$ para la multiplicidad a partir de electrones desapareados. Importancia de la asignación exacta en capas abiertas para evitar estados de espín erróneos o fallos de convergencia SCF.

:::{admonition} 💡 Intuición física
:class: intuicion
Piensa en los asientos dobles de un tren de cercanías: los pasajeros prefieren sentarse solos en filas libres antes de compartir asiento con un desconocido. La multiplicidad refleja ese ordenamiento natural de la regla de Hund, distinguiendo si quedan flechas de espín desapareadas en orbitales independientes o si viajan forzosamente en parejas opuestas. Si calculas el átomo de carbono con multiplicidad 1 en lugar de 3, obligarás a dos electrones a ocupar el mismo espacio innecesariamente. En tu archivo `.log` verás de inmediato que esa configuración forzada dispara la energía total hacia valores mucho menos estables.
:::

:::{warning}
Verificar siempre el valor de multiplicidad de espín antes de enviar el cálculo: un valor incorrecto invalida los resultados o impide la convergencia SCF.
:::

### Unidades de energía

Párrafo muy corto. Uso de unidades atómicas (Hartrees) en el motor de cálculo y factor de conversión a electronvoltios (eV) para la comparación experimental.

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
4. Hacer un único clic sobre la ventana central de dibujo. Aparece un único centro atómico sin enlaces.

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
5. En la pestaña **Additional Keywords**, escribir exactamente: `pop=full`. Esta instrucción vuelca las energías de la totalidad de orbitales moleculares en el archivo de salida.

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
3. Localizar el autovalor de energía total en la línea `SCF Done:  E(RHF) = ...` (para sistemas de capa cerrada con multiplicidad 1) o `SCF Done:  E(ROHF) = ...` (para capa abierta con multiplicidad distinta de 1).
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

Párrafo corto + tabla. Recopilación de los datos extraídos de los archivos `.log` y cálculo de las desviaciones porcentuales respecto a los valores experimentales tabulados.

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

Párrafo corto + figura. Procedimiento en GaussView para acceder al menú **Results → MOs**, selección de isosuperficie tridimensional del orbital HOMO y ajuste del valor de contorno para examinar simetrías tipo s frente a lóbulos nodales p.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: isosuperficie tridimensional del orbital HOMO del carbono en GaussView Results → MOs]
:::

:::{note}
[TEXTO HUMANO: descripción comparativa de la morfología del HOMO a lo largo del período y presencia de planos nodales]
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

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 9 (Estructura electrónica atómica).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Párrafo medio + tabla. Exploración voluntaria sobre el efecto del conjunto de base en el átomo de carbono neutro. Comparación sistemática de la energía del HOMO y la IE calculada al ampliar la base desde STO-3G hacia 3-21G y 6-311G.

| Base | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Error (%) |
|:---:|:---:|:---:|:---:|:---:|
| STO-3G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| 3-21G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |
| 6-311G | [TEXTO HUMANO] | [TEXTO HUMANO] | 11.26 | [TEXTO HUMANO] |

:::{note}
[TEXTO HUMANO: preguntas de profundización sobre la convergencia del error respecto al tamaño de la base]
:::
::::
