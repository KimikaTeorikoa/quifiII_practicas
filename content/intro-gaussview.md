# Introducción a GaussView

## Introducción

:::{note}
[TEXTO HUMANO: Explicar qué es GaussView como interfaz gráfica y qué es Gaussian como motor de cálculo independiente, aclarando que colaboran estrechamente pero son programas distintos para evitar confusiones de terminología en el laboratorio. Longitud: 3-4 frases.]
:::

---

## Abrir GaussView

[CONFIRMAR CON PROFESOR: ruta/icono para abrir GaussView en el aula]

:::{note}
[TEXTO HUMANO: Procedimiento para iniciar GaussView en las estaciones de trabajo del aula informática. Longitud: 1-2 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: escritorio con GaussView abierto, ventana principal vacía]
:::

---

## La interfaz: qué ves al abrir

:::{note}
[TEXTO HUMANO: Descripción de orientación espacial de las zonas principales: barra de menús, barra de herramientas, ventana de visualización 3D y panel de resultados sin detallar cada botón. Longitud: 4-5 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana principal anotada con flechas numeradas señalando cada zona]
:::

---

## Construir una molécula

:::{note}
[TEXTO HUMANO: Utilización del panel de fragmentos para seleccionar elementos y añadir átomos, construyendo una molécula de agua como ejemplo elemental y destacando la conexión automática de enlaces. Longitud: 4-5 frases.]
:::

:::{warning}
No hacer doble clic accidental sobre el fondo: duplica átomos sin avisar.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: H₂O construida en la ventana 3D]
:::

---

## Corregir errores y deshacer

:::{note}
[TEXTO HUMANO: Indicaciones para deshacer la última acción mediante Edit → Undo, suprimir átomos seleccionados con la tecla Delete y reiniciar el espacio de trabajo para evitar bloqueos operativos iniciales. Longitud: 3-4 frases.]
:::

---

## Añadir hidrógenos automáticamente

:::{note}
[TEXTO HUMANO: Uso de la función Edit → Add Hydrogens para saturar valencias sobre un esqueleto atómico pesado, con la advertencia de revisar siempre la estructura resultante. Longitud: 2-3 frases.]
:::

---

## Moverse por la molécula

:::{note}
[TEXTO HUMANO: Tres gestos esenciales de navegación en la ventana 3D: rotación con clic y arrastre, variación de zoom con la rueda del ratón y recentrado de la vista mediante atajo o botón. Longitud: 3-4 frases.]
:::

---

## Ver y ajustar geometría

:::{note}
[TEXTO HUMANO: Selección de pares de átomos para medir distancias de enlace y tríos para ángulos, indicando la ubicación de lectura del valor en la barra de estado inferior sin alteración manual. Longitud: 3-4 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: dos átomos seleccionados con distancia visible en la barra inferior]
:::

---

## Abrir un archivo existente

:::{note}
[TEXTO HUMANO: Apertura de archivos mediante File → Open, distinguiendo entre archivos de entrada .gjf y archivos de salida .log para reanudar sesiones o consultar referencias. Longitud: 2-3 frases.]
:::

---

## Configurar un cálculo

:::{note}
[TEXTO HUMANO: Acceso a Calculate → Gaussian Calculation Setup y descripción sucinta de las pestañas principales (Job Type, Method, Title y Charge/Multiplicity) con sus valores recomendados por defecto. Longitud: 4-5 frases.]
:::

:::{warning}
Revisar siempre la carga y la multiplicidad antes de pulsar Submit. Un error aquí invalida todo el cálculo.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup, pestaña Method con HF/STO-3G seleccionado]
:::

---

## Lanzar el cálculo

[CONFIRMAR CON PROFESOR: el cálculo se lanza en local o se envía a un servidor?]

:::{note}
[TEXTO HUMANO: Ejecución mediante el botón Submit, visualización del estado de avance en la interfaz y estimación orientativa de tiempos según la complejidad del sistema molecular. Longitud: 3-4 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana de output activa con el cálculo corriendo]
:::

---

## Verificar que el cálculo ha terminado bien

:::{note}
[TEXTO HUMANO: Comprobación sistemática de la terminación en el archivo de salida buscando la línea estándar de cierre correcto y pauta de actuación ante un mensaje de terminación con error. Longitud: 3-4 frases.]
:::

:::{danger}
Antes de anotar ningún resultado, comprueba siempre que el cálculo ha terminado correctamente buscando la línea: {{termination_ok}}
:::

---

## Ver los resultados

[CONFIRMAR CON PROFESOR: cómo se llama y dónde aparece el archivo .log en el aula]

:::{note}
[TEXTO HUMANO: Dos vías complementarias de análisis: visualización gráfica de geometrías y orbitales en los menús Results de GaussView y extracción cuantitativa de energías desde el archivo .log en el editor de texto. Longitud: 4-5 frases.]
:::

---

## Guardar el trabajo

:::{note}
[TEXTO HUMANO: Procedimiento de guardado con File → Save diferenciando .gjf de entrada y .log de resultados, junto con criterios de nomenclatura clara y reproducible. Longitud: 2-3 frases.]
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional : manual oficial de GaussView o equivalente)]`

---

::::{dropdown} ⚙️ Personalizar colores y apariencia
:color: success
:icon: gear

:::{note}
[TEXTO HUMANO: Configuración opcional de preferencias estéticas como el fondo blanco para exportar figuras nítidas, escalas de radios atómicos y esquemas cromáticos CPK. Longitud: 3-4 frases.]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: menú de preferencias de color de GaussView]
:::

::::
