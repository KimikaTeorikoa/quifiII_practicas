# Introducción a GaussView

## Introducción

La química computacional moderna requiere traducir geometrías moleculares tridimensionales a instrucciones numéricas precisas que puedan ser procesadas por algoritmos de estructura electrónica. GaussView cumple la función de interfaz gráfica interactiva diseñada para asistir en la preparación de archivos de entrada y en la comunicación fluida con el motor de cálculo Gaussian 16. El uso coordinado de este entorno permite construir modelos atómicos en tres dimensiones, seleccionar los métodos teóricos de cálculo e interpretar de forma directa los resultados energéticos y espectroscópicos generados.

---

## Abrir GaussView

GaussView se abre desde el escritorio del ordenador del aula o desde el menú de aplicaciones del sistema. [CONFIRMAR CON PROFESOR: ruta o icono exacto en el equipo del aula]

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

Para abrir un archivo existente en el entorno de trabajo se utiliza la ruta de menú **File → Open**. Los formatos habituales de trabajo son `.gjf` para cargar archivos de entrada de cálculo previamente guardados y `.log` para examinar salidas generadas por Gaussian, facilitando la reanudación del trabajo entre sesiones de laboratorio o el análisis de estructuras de referencia.

---

## Configurar un cálculo

El panel de configuración del cálculo se abre acudiendo a **Calculate → Gaussian Calculation Setup**. En la pestaña **Job Type** se selecciona la tarea computacional que se desea ejecutar, tal como una energía puntual (*Energy* o *Single Point*), una optimización de geometría (*Optimization*) o el cálculo de modos vibracionales (*Frequency*). La pestaña **Method** permite definir el nivel de aproximación electrónica especificando tanto el método mecanocuántico (como Hartree-Fock o B3LYP) como el conjunto de funciones de base asignado en cada práctica. En la sección **Title Card** se introduce una breve descripción identificativa del cálculo sin caracteres especiales. Finalmente, el apartado **Charge & Multiplicity** fija la carga neta del sistema molecular (cero en especies neutras) y su multiplicidad de espín (uno en sistemas de capa cerrada).

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

Tras completar los parámetros de configuración se inicia la ejecución del cálculo pulsando el botón **Submit** situado en la parte inferior de la ventana. A continuación, GaussView despliega un panel de monitorización que reporta las líneas de texto generadas por Gaussian en tiempo real. La duración del proceso oscila entre unos pocos segundos en moléculas sencillas tratadas con bases mínimas y varios minutos cuando se abordan sistemas moleculares más extensos o métodos correlacionados. Durante este intervalo de cómputo el usuario solo debe esperar a que el proceso culmine de forma automática.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana de output activa con el cálculo corriendo]
:::

---

## Verificar que el cálculo ha terminado bien

Al culminar la ejecución computacional, la última línea del archivo de salida debe contener {{termination_ok}}. Si en su lugar aparece el mensaje `Error termination`, el programa no ha completado el cálculo con éxito. En tal circunstancia se debe notificar la incidencia al profesor de prácticas, puesto que los motivos del fallo pueden originarse en una geometría inicial defectuosa, una parametrización incompatible o la superación de los límites de memoria asignados.

:::{danger}
Antes de anotar ningún resultado, comprueba siempre que el cálculo ha terminado correctamente buscando la línea: {{termination_ok}}
:::

---

## Ver los resultados

[CONFIRMAR CON PROFESOR: cómo se llama y dónde aparece el archivo .log en el aula]

La inspección de los resultados se realiza a través de dos procedimientos complementarios según el tipo de información requerida. Para visualizar la geometría de equilibrio final, las superficies de densidad electrónica o los orbitales moleculares, se recurre a la interfaz de GaussView mediante las opciones del menú **Results**. Por el contrario, para extraer datos cuantitativos como energías electrónicas o frecuencias vibracionales e incluirlos en el cuaderno de trabajo, resulta más directo abrir el archivo `.log` con un editor de texto convencional y localizar los epígrafes pertinentes. En el protocolo de cada práctica se especifica el término exacto de búsqueda y el formato en que deben transcribirse los valores numéricos.

---

## Guardar el trabajo

Las instrucciones de cálculo y las estructuras moleculares se guardan accediendo a **File → Save** bajo la extensión `.gjf`. Conviene emplear una nomenclatura estructurada que identifique la molécula y el nivel de teoría seleccionado (por ejemplo, `h2o_b3lyp_6311g.gjf`), evitando pérdidas de datos y facilitando la organización de los cálculos generados a lo largo de la sesión.

---

## Bibliografía

- {{gaussian_cite}}

---

::::{dropdown} ⚙️ Personalizar colores y apariencia
:color: success
:icon: gear

La tonalidad de fondo del espacio tridimensional se modifica en la ruta **View → Display Format → Background Color**. En esta misma ventana de configuración es posible personalizar el tamaño relativo de las esferas atómicas y su esquema de colores en los apartados **Atom Size** y **Atom Colors**. Estos ajustes visuales no alteran los cálculos mecanocuánticos ni son obligatorios para el seguimiento de la asignatura, pero la selección de un fondo blanco facilita la obtención de capturas nítidas y legibles para su inserción en las memorias de prácticas.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: menú de preferencias de color de GaussView]
:::

::::
