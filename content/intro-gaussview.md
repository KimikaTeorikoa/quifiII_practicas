# Introducción a GaussView

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA — NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto (3-4 líneas). Qué es GaussView (interfaz gráfica) y qué es Gaussian
(motor de cálculo). Que son dos programas distintos pero que trabajan juntos. Sin esto
los alumnos confunden los dos nombres durante toda la asignatura.

---

## Abrir GaussView

Párrafo muy corto + figura.
`[CONFIRMAR CON PROFESOR: ruta/icono para abrir GaussView en el aula]`

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: escritorio con GaussView abierto, ventana principal vacía]
```

---

## La interfaz: qué ves al abrir

Párrafo medio + figura anotada. Descripción de las 3-4 zonas principales: barra de
menús, barra de herramientas, ventana de visualización 3D, panel de resultados (si
existe). Sin entrar en cada botón — solo orientación espacial.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana principal anotada con flechas numeradas señalando cada zona]
```

---

## Construir una molécula

Párrafo medio + figura. Cómo usar el panel de fragmentos para añadir átomos. Construir
H₂O como ejemplo mínimo. Mencionar que GaussView conecta los enlaces automáticamente.

```{warning}
No hacer doble clic accidental sobre el fondo: duplica átomos sin avisar.
```

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: H₂O construida en la ventana 3D]
```

---

## Corregir errores y deshacer

Párrafo corto. Cómo deshacer el último paso (**Edit → Undo** o atajo de teclado).
Cómo eliminar un átomo seleccionado (tecla Delete). Cómo limpiar toda la molécula y
empezar de cero. Sección pequeña pero crítica: los novatos se bloquean aquí.

---

## Añadir hidrógenos automáticamente

Párrafo muy corto. GaussView puede completar los hidrógenos implícitos con
**Edit → Add Hydrogens**. Útil cuando se dibuja solo el esqueleto pesado. Advertencia:
revisar siempre el resultado antes de continuar.

---

## Moverse por la molécula

Párrafo corto. Rotar (clic + arrastrar), zoom (rueda del ratón), centrar (botón
específico o atajo). Solo los tres gestos imprescindibles.

---

## Ver y ajustar geometría

Párrafo corto + figura. Cómo seleccionar dos átomos para ver la distancia de enlace,
tres para el ángulo. Dónde aparece el valor en pantalla. No se pide modificar a mano —
solo saber leerlo.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: dos átomos seleccionados con distancia visible en la barra inferior]
```

---

## Abrir un archivo existente

Párrafo muy corto. **File → Open**. Formatos habituales: `.gjf` (input que ya tenían
guardado) y `.log` (resultado de un cálculo anterior). Útil para retomar trabajo entre
sesiones o abrir los archivos de referencia que proporcione el profesor.

---

## Configurar un cálculo

Párrafo medio + figura. **Calculate → Gaussian Calculation Setup**. Explicar las
pestañas principales: Job Type (qué tipo de cálculo), Method (método y base), Title,
Charge/Multiplicity. Para cada campo: qué es en una frase, qué valor poner por defecto.

```{warning}
Revisar siempre la carga y la multiplicidad antes de pulsar Submit. Un error aquí
invalida todo el cálculo.
```

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Gaussian Calculation Setup, pestaña Method con HF/STO-3G seleccionado]
```

---

## Lanzar el cálculo

Párrafo corto. Botón Submit. Qué pasa en pantalla cuando el cálculo empieza. Que puede
tardar segundos o minutos según la molécula. `[CONFIRMAR CON PROFESOR: el cálculo se
lanza en local o se envía a un servidor?]`

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana de output activa con el cálculo corriendo]
```

---

## Verificar que el cálculo ha terminado bien

Párrafo corto + bloque danger. Cómo saber si terminó correctamente: buscar
{{termination_ok}} en el output. Qué significa "Error termination" (no entrar en
detalle — solo avisar al profesor).

```{danger}
Antes de anotar ningún resultado, comprueba siempre que el cálculo ha terminado
correctamente buscando la línea: {{termination_ok}}
```

---

## Ver los resultados

Párrafo medio. Dos vías: (a) en GaussView directamente para geometría y orbitales
(**Results → ...** según lo que se busque), (b) abrir el archivo `.log` con el editor
de texto para copiar energías a la tabla del guión.
`[CONFIRMAR CON PROFESOR: cómo se llama y dónde aparece el archivo .log en el aula]`

---

## Guardar el trabajo

Párrafo muy corto. **File → Save**. Formato `.gjf` para el input, `.log` para los
resultados. Recomendación de nombrar los archivos con criterio claro (molécula +
método, p. ej. `h2o_hf_sto3g.gjf`).

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional — manual oficial de GaussView o equivalente]`

---

::::{dropdown} ⚙️ Personalizar colores y apariencia
:color: success
:icon: gear

Párrafo corto + figura. Cómo cambiar el color de fondo (negro → blanco, útil para
capturas más limpias en el informe), tamaño de átomos, esquema de colores CPK. No es
necesario para las prácticas — solo para el alumno que quiera cuidar la presentación.

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: menú de preferencias de color de GaussView]
```

::::
