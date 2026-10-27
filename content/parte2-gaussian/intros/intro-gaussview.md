# Introducción a GaussView

## Introducción

La química computacional moderna requiere traducir geometrías moleculares tridimensionales a instrucciones numéricas precisas que puedan ser procesadas por algoritmos de estructura electrónica. GaussView cumple la función de interfaz gráfica interactiva diseñada para asistir en la preparación de archivos de entrada y en la comunicación fluida con el motor de cálculo Gaussian 16. El uso coordinado de este entorno permite construir modelos atómicos en tres dimensiones, seleccionar los métodos teóricos de cálculo e interpretar de forma directa los resultados energéticos y espectroscópicos generados.

---

## Abrir GaussView

[CONFIRMAR CON PROFESOR: ruta/icono para abrir GaussView en el aula]

:::{note}
[TEXTO HUMANO: Instrucciones para abrir GaussView en el aula. (Longitud: 1-2 frases)]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: escritorio con GaussView abierto, ventana principal vacía]
:::

---

## La interfaz: qué ves al abrir

La interfaz gráfica de GaussView se estructura principalmente en cuatro áreas de trabajo coordinadas. En la parte superior se sitúa la barra de menús principal, que proporciona acceso ordenado a la totalidad de las herramientas de configuración y visualización del programa. Inmediatamente debajo se ubica la barra de herramientas gráficas, donde se agrupan los iconos de acceso directo más frecuentes para seleccionar elementos, ajustar enlaces y manipular fragmentos moleculares. El área central está dominada por la ventana de visualización tridimensional, espacio interactivo en el que se construye, desplaza y rota la estructura bajo estudio mediante el ratón. Finalmente, un panel secundario situado en la región inferior muestra información contextual en tiempo real sobre los átomos seleccionados, distancias interatómicas y estados de los cálculos ejecutados.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana principal anotada con flechas numeradas señalando cada zona]
:::

---

## Construir una molécula

:::{note}
[TEXTO HUMANO: Cómo usar el panel de fragmentos para añadir átomos. Construir H₂O como ejemplo mínimo. Mencionar que GaussView conecta los enlaces automáticamente. (Longitud: 4-5 frases)]
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
[TEXTO HUMANO: Cómo deshacer el último paso (**Edit → Undo** o atajo de teclado). Cómo eliminar un átomo seleccionado (tecla Delete). Cómo limpiar toda la molécula y empezar de cero. Sección pequeña pero importante: los novatos se bloquean aquí. (Longitud: 3-4 frases)]
:::

---

## Añadir hidrógenos automáticamente

:::{note}
[TEXTO HUMANO: GaussView puede completar los hidrógenos implícitos con **Edit → Add Hydrogens**. Útil cuando se dibuja solo el esqueleto pesado. Advertencia: revisar siempre el resultado antes de continuar. (Longitud: 1-2 frases)]
:::

---

## Moverse por la molécula

:::{note}
[TEXTO HUMANO: Rotar (clic + arrastrar), zoom (rueda del ratón), centrar (botón específico o atajo). Solo los tres gestos imprescindibles. (Longitud: 3-4 frases)]
:::

---

## Ver y ajustar geometría

:::{note}
[TEXTO HUMANO: Cómo seleccionar dos átomos para ver la distancia de enlace, tres para el ángulo. Dónde aparece el valor en pantalla. No se pide modificar a mano, solo saber leerlo. (Longitud: 3-4 frases)]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: dos átomos seleccionados con distancia visible en la barra inferior]
:::

---

## Abrir un archivo existente

:::{note}
[TEXTO HUMANO: **File → Open**. Formatos habituales: `.gjf` (input que ya tenían guardado) y `.log` (resultado de un cálculo anterior). Útil para retomar trabajo entre sesiones o abrir los archivos de referencia que proporcione el profesor. (Longitud: 1-2 frases)]
:::

---

## Configurar un cálculo

:::{note}
[TEXTO HUMANO: **Calculate → Gaussian Calculation Setup**. Explicar las pestañas principales: Job Type (qué tipo de cálculo), Method (método y base), Title, Charge/Multiplicity. Para cada campo: qué es en una frase, qué valor poner por defecto. (Longitud: 4-5 frases)]
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
[TEXTO HUMANO: Botón Submit. Qué pasa en pantalla cuando el cálculo empieza. Que puede tardar segundos o minutos según la molécula. (Longitud: 3-4 frases)]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana de output activa con el cálculo corriendo]
:::

---

## Verificar que el cálculo ha terminado bien

:::{note}
[TEXTO HUMANO: Cómo saber si terminó correctamente: buscar {{termination_ok}} en el output. Qué significa "Error termination" (no entrar en detalle, solo avisar al profesor). (Longitud: 3-4 frases)]
:::

:::{danger}
Antes de anotar ningún resultado, comprueba siempre que el cálculo ha terminado correctamente buscando la línea: {{termination_ok}}
:::

---

## Ver los resultados

[CONFIRMAR CON PROFESOR: cómo se llama y dónde aparece el archivo .log en el aula]

:::{note}
[TEXTO HUMANO: Dos vías: (a) en GaussView directamente para geometría y orbitales (**Results → ...** según lo que se busque), (b) abrir el archivo `.log` con el editor de texto para copiar energías a la tabla del guión. (Longitud: 4-5 frases)]
:::

---

## Guardar el trabajo

:::{note}
[TEXTO HUMANO: **File → Save**. Formato `.gjf` para el input, `.log` para los resultados. Recomendación de nombrar los archivos con criterio claro (molécula + método, p. ej. `h2o_hf_sto3g.gjf`). (Longitud: 1-2 frases)]
:::

---

## Bibliografía

- {{gaussian_cite}}

---

::::{dropdown} ⚙️ Personalizar colores y apariencia
:color: success
:icon: gear

:::{note}
[TEXTO HUMANO: Cómo cambiar el color de fondo (negro → blanco, útil para capturas más limpias en el informe), tamaño de átomos, esquema de colores CPK. No es necesario para las prácticas, solo para el alumno que quiera cuidar la presentación. (Longitud: 3-4 frases)]
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: menú de preferencias de color de GaussView]
:::

::::
