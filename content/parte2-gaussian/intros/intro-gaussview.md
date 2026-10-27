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

Para construir una molécula en GaussView, se selecciona en primer lugar el elemento químico correspondiente en el panel interactivo de fragmentos y se pulsa con el botón izquierdo sobre la ventana de visualización central para colocar el átomo. Al incorporar átomos adicionales en la proximidad de los existentes, el programa genera automáticamente los enlaces químicos correspondientes según los radios covalentes estándar. En el caso del agua ($\text{H}_2\text{O}$), el procedimiento consiste en situar un átomo de oxígeno central y acoplar a continuación dos átomos de hidrógeno en posiciones angulares aproximadas. La estructura espacial definitiva y las distancias exactas se ajustarán numéricamente durante el cálculo de optimización de geometría en Gaussian. Por este motivo, el dibujo inicial en pantalla solo requiere reproducir de forma orientativa la conectividad química del sistema sin necesidad de una precisión métrica estricta.

:::{warning}
No hacer doble clic accidental sobre el fondo: duplica átomos sin avisar.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: H₂O construida en la ventana 3D]
:::

---

## Corregir errores y deshacer

Para revertir la última acción realizada sobre el espacio de trabajo se emplea la ruta de menú **Edit → Undo** o el atajo de teclado estándar Ctrl+Z. En caso de requerir la eliminación de un átomo o fragmento específico, basta con pulsar sobre él con el ratón para seleccionarlo y presionar a continuación la tecla Supr (o Delete). Si resulta necesario limpiar la ventana por completo y reiniciar el modelado desde cero, se puede utilizar la opción **Edit → Select All** seguida de la tecla Supr. De forma alternativa, es posible generar un espacio de trabajo limpio acudiendo a **File → New** para abrir una nueva ventana interactiva vacía.

---

## Añadir hidrógenos automáticamente

La opción de menú **Edit → Add Hydrogens** permite completar de forma automática los átomos de hidrógeno implícitos necesarios para saturar la valencia del esqueleto atómico dibujado. Conviene revisar siempre la estructura tridimensional resultante tras aplicar esta acción, ya que la asignación automática puede no coincidir con el estado de protonación o la distribución de valencias deseada.

---

## Moverse por la molécula

Para inspeccionar la estructura molecular se rota la vista manteniendo presionado el botón izquierdo del ratón mientras se desplaza el cursor sobre el espacio de trabajo. El acercamiento o alejamiento visual (zoom) se gradúa de forma directa mediante la rueda de desplazamiento del ratón. En caso de perder de vista el objeto o desear reencuadrar el modelo en la ventana central, se recurre al botón de centrado situado en la barra de herramientas principal o al atajo de teclado correspondiente. El dominio coordinado de estos tres movimientos básicos basta para orientar la geometría con soltura durante las etapas de modelado e interpretación de resultados.

---

## Ver y ajustar geometría

Para medir una distancia de enlace en GaussView se seleccionan secuencialmente los dos átomos implicados haciendo clic sobre ellos mientras se mantiene pulsada la tecla Ctrl. El valor numérico de la separación interatómica calculada en ángstroms ($\text{Å}$) se muestra de inmediato en la barra de estado situada en el borde inferior de la ventana. Si se seleccionan tres átomos consecutivos se visualiza el ángulo de enlace en grados sexagesimales, y con cuatro átomos se obtiene el ángulo diedro correspondiente. Esta funcionalidad opera exclusivamente en modalidad de lectura para comprobar las dimensiones de la estructura, por lo que no se requiere modificar manualmente ninguno de estos parámetros.

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
