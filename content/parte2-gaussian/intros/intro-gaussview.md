# Introducción a GaussView

## Introducción

La química computacional requiere transformar geometrías moleculares tridimensionales en coordenadas e instrucciones numéricas procesables por algoritmos de estructura electrónica. GaussView es la interfaz gráfica que facilita preparar los archivos de entrada y comunicarse con el motor de cálculo Gaussian 16. Con este entorno se pueden construir modelos atómicos en tres dimensiones, seleccionar el método teórico adecuado e interpretar directamente los resultados energéticos y espectroscópicos obtenidos.

## Abrir GaussView

GaussView se abre desde el escritorio del ordenador del aula o desde el menú de aplicaciones del sistema. [CONFIRMAR CON PROFESOR: ruta o icono exacto en el equipo del aula]

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: escritorio con GaussView abierto, ventana principal vacía]
:::

## La interfaz: qué ves al abrir

La interfaz de GaussView consta de cuatro áreas principales de trabajo. En la parte superior se encuentra la barra de menús, que da acceso a las herramientas de configuración y visualización. Debajo se sitúa la barra de herramientas, con iconos de acceso rápido para seleccionar elementos, modificar enlaces y manipular fragmentos. El área central contiene la ventana de visualización tridimensional, donde se construye, desplaza y rota la molécula con el ratón. Por último, un panel inferior muestra información en tiempo real sobre los átomos seleccionados, distancias interatómicas y el estado de los cálculos.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana principal anotada con flechas numeradas señalando cada zona]
:::

## Construir una molécula

Para construir una molécula en GaussView, primero se selecciona el elemento químico en el panel de fragmentos y se hace clic con el botón izquierdo en la ventana central para situar el átomo. Al añadir átomos adicionales cerca de los existentes, el programa genera los enlaces de forma automática a partir de los radios covalentes estándar. Para el agua ($\text{H}_2\text{O}$), basta con colocar un átomo de oxígeno central y enlazar dos átomos de hidrógeno en posiciones angulares aproximadas. La estructura definitiva y las distancias exactas se ajustarán durante la optimización de geometría en Gaussian, por lo que el dibujo inicial solo necesita representar la conectividad química del sistema sin exigir precisión métrica rigurosa.

:::{admonition} Advertencia
:class: warning
No hacer doble clic accidental sobre el fondo: duplica átomos sin avisar.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: H₂O construida en la ventana 3D]
:::

## Corregir errores y deshacer

Para deshacer la última acción realizada se utiliza el menú **Edit → Undo** o el atajo de teclado Ctrl+Z. Si se desea eliminar un átomo o fragmento específico, basta con seleccionarlo con el ratón y pulsar la tecla Supr (o Delete). Para limpiar la ventana por completo y reiniciar el modelo, se puede recurrir a **Edit → Select All** seguido de Supr, o bien abrir un área de trabajo nueva desde **File → New**.

## Añadir hidrógenos automáticamente

La opción de menú **Edit → Add Hydrogens** completa automáticamente los átomos de hidrógeno implícitos necesarios para saturar la valencia del esqueleto atómico dibujado. Se recomienda revisar siempre la estructura tridimensional resultante, ya que la asignación automática puede diferir del estado de protonación o la distribución de valencias deseada.

## Moverse por la molécula

Para inspeccionar la estructura molecular, la vista se rota manteniendo presionado el botón izquierdo del ratón mientras se desplaza el cursor. El zoom se ajusta de forma directa con la rueda del ratón. Si se pierde de vista la molécula o se necesita centrar el modelo en la ventana, se utiliza el botón de centrado en la barra de herramientas o su atajo correspondiente. El manejo de estos tres movimientos permite orientar la geometría con soltura durante el modelado y la inspección de resultados.

## Ver y ajustar geometría

Para medir una distancia de enlace en GaussView se seleccionan los dos átomos implicados manteniendo pulsada la tecla Ctrl. La distancia interatómica en ángstroms ($\text{Å}$) aparece de inmediato en la barra de estado, en el borde inferior de la ventana. Al seleccionar tres átomos consecutivos se visualiza el ángulo de enlace en grados, y con cuatro átomos se obtiene el ángulo diedro correspondiente. Esta función opera exclusivamente en modo de lectura para verificar las dimensiones de la estructura, por lo que no es necesario modificar estos parámetros manualmente.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: dos átomos seleccionados con distancia visible en la barra inferior]
:::

## Abrir un archivo existente

Para abrir un archivo existente se accede al menú **File → Open**. Los formatos habituales son `.gjf`, correspondiente a archivos de entrada de cálculo, y `.log`, que contiene las salidas generadas por Gaussian. Esto permite retomar el trabajo entre sesiones de laboratorio o analizar estructuras de referencia.

## Configurar un cálculo

El panel de configuración del cálculo se abre desde **Calculate → Gaussian Calculation Setup**. En la pestaña **Job Type** se selecciona la tarea a ejecutar: una energía puntual (*Energy* o *Single Point*), una optimización de geometría (*Optimization*) o el cálculo de modos vibracionales (*Frequency*). La pestaña **Method** permite definir el nivel de teoría especificando el método mecanocuántico (como Hartree-Fock o B3LYP) y la base de funciones asignada en cada práctica. En **Title Card** se introduce una breve descripción identificativa del cálculo sin caracteres especiales. Por último, en **Charge & Multiplicity** se establece la carga neta del sistema (cero en especies neutras) y su multiplicidad de espín (uno en sistemas de capa cerrada).

:::{admonition} Advertencia
:class: warning
Revisar siempre la carga y la multiplicidad antes de pulsar Submit. Un error aquí invalida todo el cálculo.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup, pestaña Method con HF/STO-3G seleccionado]
:::

## Lanzar el cálculo

[CONFIRMAR CON PROFESOR: el cálculo se lanza en local o se envía a un servidor?]

Una vez configurados los parámetros, el cálculo se lanza pulsando el botón **Submit** en la parte inferior de la ventana. GaussView abre entonces una ventana de seguimiento que muestra las líneas de salida generadas por Gaussian en tiempo real. La duración del proceso oscila entre unos segundos para moléculas sencillas con bases mínimas y varios minutos cuando se tratan sistemas más extensos o métodos con correlación electrónica. Durante este tiempo no es necesario realizar ninguna acción adicional hasta que el cálculo finalice.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana de output activa con el cálculo corriendo]
:::

## Verificar que el cálculo ha terminado bien

Al terminar el cálculo, la última línea del archivo de salida debe contener {{termination_ok}}. Si en su lugar aparece `Error termination`, el cálculo no ha terminado correctamente. Las causas más habituales son una geometría inicial inadecuada, una configuración incompatible o haber superado el límite de memoria asignado.

:::{admonition} Atención
:class: danger
Antes de anotar ningún resultado, comprueba siempre que el cálculo ha terminado correctamente buscando la línea: {{termination_ok}}
:::

## Ver los resultados

[CONFIRMAR CON PROFESOR: cómo se llama y dónde aparece el archivo .log en el aula]

Los resultados se consultan por dos vías según la información que se necesite. Para visualizar la geometría optimizada, la densidad electrónica o los orbitales moleculares, se utiliza el menú **Results** de GaussView. Para extraer valores numéricos como la energía total o las frecuencias vibracionales y anotarlos en el cuaderno de trabajo, es más directo abrir el archivo `.log` con un editor de texto y localizar las líneas pertinentes. En el guión de cada práctica se indica qué término buscar y cómo anotar cada valor.

## Guardar el trabajo

El archivo de entrada se guarda desde **File → Save** con la extensión `.gjf`. Se recomienda utilizar una nomenclatura clara que identifique la molécula y el nivel de teoría empleado (por ejemplo, `h2o_b3lyp_6311g.gjf`), lo que evita pérdidas de datos y facilita organizar los cálculos durante la sesión.

---

## Bibliografía

- {{gaussian_cite}}

---

::::{dropdown} Personalizar colores y apariencia
:color: success
:icon: gear

El color de fondo del espacio tridimensional se modifica desde **View → Display Format → Background Color**. En esta misma ventana se puede personalizar el tamaño de las esferas atómicas y su esquema de colores en los apartados **Atom Size** y **Atom Colors**. Estos ajustes no alteran los cálculos ni son obligatorios, pero usar un fondo blanco facilita obtener capturas nítidas para la memoria de prácticas.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: menú de preferencias de color de GaussView]
:::

::::
