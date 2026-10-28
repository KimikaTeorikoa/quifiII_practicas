# P2-D: Espectroscopía UV-Vis de Cetonas

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA - NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

La absorción de radiación ultravioleta-visible induce transiciones electrónicas en las moléculas orgánicas al promover electrones desde orbitales ocupados de valencia hacia orbitales virtuales de mayor energía. Mediante la teoría del funcional de la densidad dependiente del tiempo (TD-DFT) en Gaussian, es posible simular estas excitaciones teniendo en cuenta la reorganización de la densidad electrónica. En esta práctica se calculan las longitudes de onda de absorción y las fuerzas de oscilador para las transiciones $n \rightarrow \pi^*$ y $\pi \rightarrow \pi^*$ en cetonas, analizando además cómo la polaridad del disolvente desplaza las bandas del espectro.

---

## Objetivos

1. Estimar la longitud de onda de absorción preliminar a partir de la diferencia de energías orbitales ($\Delta E_{\text{gap}}$ HOMO-LUMO).
2. Calcular las energías de excitación vertical hacia estados singlete empleando la metodología TD-DFT con B3LYP/6-311G.
3. Asignar las transiciones electrónicas $n \rightarrow \pi^*$ y $\pi \rightarrow \pi^*$ en función de su energía y su fuerza del oscilador ($f$).
4. Cuantificar el desplazamiento solvatocrómico de la acetona en agua mediante el modelo de polarización continua del disolvente (PCM).
5. Comparar los espectros de absorción calculados frente a valores experimentales en función de la polaridad del medio y los sustituyentes alquílicos.

---

## ¿Qué software vamos a usar?

Párrafo muy corto. Referencia al uso combinado de GaussView para la parametrización de cálculos de estados excitados y solvatación continua, y {{gaussian_version}} para la resolución de las ecuaciones TD-DFT y PCM.

---

## Conceptos clave

### Transiciones electrónicas en compuestos carbonílicos

Párrafo medio + figura. Promoción de electrones de valencia desde orbitales ocupados a orbitales virtuales desocupados. Distinción entre la transición $n \rightarrow \pi^*$ (electrón no enlazante del oxígeno al orbital antienlazante $\pi^*$ del carbonilo, prohibida por simetría, baja fuerza de oscilador, $\lambda \approx 280-300\text{ nm}$) y la transición $\pi \rightarrow \pi^*$ (orbital enlazante $\pi$ al antienlazante $\pi^*$, permitida, alta fuerza de oscilador, $\lambda < 250\text{ nm}$).

```{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: diagrama de niveles de orbitales moleculares del grupo carbonilo con flechas de transición n a pi* y pi a pi*]
```

### El gap HOMO-LUMO como estimación preliminar

Párrafo medio + tabla. Relación directa entre la diferencia de energías orbitales y la energía de excitación elemental. Expresiones de conversión de unidades atómicas a electronvoltios y longitud de onda en nanómetros. Discusión de aproximaciones implícitas (orbitales no relajados e ignorancia de repulsión entre estados excitados).

$$\Delta E_{\text{gap}}\text{ (eV)} = (\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}) \times {{ha_to_ev}}$$

$$\lambda_{\text{estimada}}\text{ (nm)} = \frac{1239.8}{\Delta E_{\text{gap}}\text{ (eV)}}$$

Ejemplo metodológico de referencia con autovalores del formaldehído en acetonitrilo:

| Nivel | Energía (Ha) |
|---|:---:|
| HOMO | −0.27636 |
| LUMO | −0.06005 |
| Gap (Ha) | 0.21631 |
| Gap (eV) | 5.89 |
| $\lambda$ estimada (nm) | 210 |

### Fundamento del método TD-DFT

Párrafo medio. Descripción del formalismo de DFT dependiente del tiempo para evaluar respuestas a perturbaciones electromagnéticas dinámicas. Concepto de fuerza del oscilador ($f$) como magnitud proporcional a la probabilidad de transición y a la intensidad de la banda observada.

:::{admonition} Nota
:class: note
La fuerza del oscilador ($f$) es una magnitud adimensional proporcional al cuadrado del momento dipolar de transición que cuantifica la probabilidad de absorción y la intensidad de la banda observada. En la transición $n \rightarrow \pi^*$, el orbital no enlazante del oxígeno reside en el plano molecular mientras que el orbital $\pi^*$ es perpendicular a dicho plano; esta ortogonalidad espacial hace que la integral de transición sea casi nula, lo que produce un valor de $f$ muy reducido. En cambio, las transiciones con marcado solapamiento espacial entre orbitales de simetría compatible presentan valores de $f$ varios órdenes de magnitud mayores.
:::

### Efecto del disolvente: solvatocromismo

Párrafo medio + tabla. Modelo de polarización continua (PCM) para el disolvente. Mecanismo de estabilización diferencial del estado fundamental dipolar frente al estado excitado menos polar en la transición $n \rightarrow \pi^*$, con el consiguiente ensanchamiento del gap energético y desplazamiento hacia longitudes de onda menores (desplazamiento al azul o hipsocrómico).

Valores experimentales de referencia para acetona:

| Disolvente | $\lambda\ (n \rightarrow \pi^*)$ experimental (nm) |
|---|:---:|
| Ciclohexano (apolar) | 279 |
| Agua (muy polar) | 264 |
| Variación ($\Delta \lambda$) | −15 nm (desplazamiento al azul) |

:::{admonition} Nota
:class: note
El desplazamiento solvatocrómico al azul (hipsocrómico) en la transición $n \rightarrow \pi^*$ deriva de la diferente polaridad de los estados electrónicos implicados. En el estado fundamental ($S_0$), el grupo carbonilo posee un momento dipolar elevado y los pares solitarios del oxígeno forman enlaces de hidrógeno con disolventes polares próticos como el agua. Durante la transición electrónica, la redistribución de carga hacia el sistema $\pi^*$ disminuye el momento dipolar en el estado excitado ($S_1$), lo que reduce la estabilización por solvatación y aumenta la energía necesaria para la excitación vertical.
:::

---

## Procedimiento

:::{danger}
Verificación obligatoria tras cada cálculo: abrir el archivo `.log` con el editor de texto y confirmar la presencia de la línea final exacta:
{{termination_ok}}
:::

### Parte A: Estimación preliminar con el gap HOMO-LUMO

#### Paso A1: Optimizar la geometría en disolvente

1. Iniciar GaussView desde el menú de aplicaciones o lanzador del sistema.
2. Dibujar la molécula de acetona (CH₃–CO–CH₃): seleccionar el fragmento de carbonilo o añadir sucesivamente los átomos de C, O e hidrógenos.
3. Aplicar **Edit → Clean** (o hacer clic en el icono de escoba) para obtener una geometría inicial razonable.
4. Acceder al menú **Calculate → Gaussian Calculation Setup**.
5. En la pestaña **Job Type**, seleccionar **Optimization**.
6. En la pestaña **Method**, configurar los parámetros de cálculo:

| Campo | Valor |
|---|---|
| Job Type | Optimization |
| Method | **B3LYP** |
| Basis Set | **6-311G** |
| Charge | **0** |
| Spin (Multiplicity) | **1** |
| Additional Keywords | `scrf=(solvent=acetonitrile) geom=connectivity` |

7. En la pestaña **Title**, escribir: `Acetona opt B3LYP 6-311G MeCN`.
8. En el campo inferior **Additional Keywords**, escribir: `scrf=(solvent=acetonitrile) geom=connectivity`.
9. Pulsar **Submit**, guardar el archivo como `acetona_MeCN_opt.gjf` en el directorio `{{practicas_folder}}EspectroscopiaUV/` y confirmar el cálculo con **Save** y **Submit**.
10. Abrir el archivo de salida `.log` (`acetona_MeCN_opt.log`) en el editor de texto y comprobar la línea final: `{{termination_ok}}`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup con Job Type Optimization y Additional Keywords scrf=(solvent=acetonitrile)]
:::

#### Paso A2: Extraer autovalores HOMO y LUMO

1. En el archivo `.log` de la optimización (`acetona_MeCN_opt.log`), buscar con **Ctrl + F** el texto: `Alpha  occ. eigenvalues`.
2. Identificar el último valor numérico de la última fila `Alpha occ.` correspondiente a la energía del orbital HOMO ($\varepsilon_{\text{HOMO}}$ en hartrees).
3. Identificar el primer valor numérico de la fila siguiente `Alpha virt. eigenvalues` correspondiente a la energía del orbital LUMO ($\varepsilon_{\text{LUMO}}$ en hartrees).
4. Calcular la diferencia energética $\Delta E_{\text{gap}} = (\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}) \times {{ha_to_ev}}$ en eV.
5. Estimar la longitud de onda de absorción: $\lambda_{\text{estimada}} = 1239.8 / \Delta E_{\text{gap}}\text{ (eV)}$ en nm.
6. Anotar los valores numéricos obtenidos en la Tabla A de resultados.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: fragmento del archivo .log mostrando las lineas Alpha occ. y Alpha virt. con las energias orbitales de HOMO y LUMO destacadas]
:::

---

### Parte B: Cálculo TD-DFT del espectro de absorción

#### Paso B1: Configurar el cálculo TD-DFT

1. En GaussView, abrir el archivo de geometría optimizada anterior (`acetona_MeCN_opt.log` o el correspondiente `.chk`) mediante **File → Open**.
2. Acceder al menú **Calculate → Gaussian Calculation Setup**.
3. En la pestaña **Job Type**, seleccionar **Energy** (cálculo de punto único sobre la estructura de equilibrio).
4. En la pestaña **Method**, mantener Method **B3LYP**, Basis Set **6-311G**, Charge **0**, Spin **1**.
5. En la pestaña **Title**, escribir: `Acetona TD-DFT B3LYP 6-311G MeCN`.
6. En el campo inferior **Additional Keywords**, escribir: `td scrf=(solvent=acetonitrile) geom=connectivity`.
7. Pulsar **Submit**, guardar como `acetona_MeCN_td.gjf` en `{{practicas_folder}}EspectroscopiaUV/` y confirmar el cálculo con **Save** y **Submit**.
8. Verificar la presencia de la línea final `{{termination_ok}}` en el archivo `.log`.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Calculate → Gaussian Calculation Setup en pestana Additional Keywords con las opciones td y scrf introducidas para TD-DFT]
:::

#### Paso B2: Extraer datos de los estados excitados del .log

1. Abrir el archivo `.log` (`acetona_MeCN_td.log`) en el editor de texto.
2. Buscar con **Ctrl + F** la cadena: `Excited State   1`.
3. Extraer los datos cuantitativos del primer estado excitado singlete:
   - Longitud de onda calculada ($\lambda$) en nanómetros (nm).
   - Energía de excitación en electronvoltios (eV).
   - Fuerza del oscilador ($f$).
4. Observar las líneas de orbitales asociadas a la transición (origen y destino) para confirmar el tipo de excitación.
5. Comprobar que la fuerza del oscilador es reducida ($f < 0.01$) y la longitud de onda se sitúa en el rango 270–300 nm, correspondiente a la banda prohibida por simetría $n \rightarrow \pi^*$.

Campos del bloque de estado excitado:

| Campo | Significado físico |
|---|---|
| Simetría de estado | Representación irreducible del estado excitado |
| Energía (eV) | Diferencia energética entre estado fundamental y excitado |
| Longitud de onda (nm) | Posición del máximo de absorción en el espectro |
| Fuerza del oscilador ($f$) | Intensidad relativa de la banda espectral |
| Contribución orbital | Índices de los orbitales ocupados y virtuales implicados |

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: fragmento del archivo .log mostrando el bloque de Excited State 1 con valores de longitud de onda, energia y fuerza de oscilador]
:::

#### Paso B3: Visualizar el espectro en GaussView

1. En GaussView, abrir el archivo `acetona_MeCN_td.log` mediante **File → Open**.
2. Acceder al menú **Results → UV-Vis**.
3. Examinar el espectro electrónico sintético generado:
   - Las barras verticales indican las transiciones discretas, con altura proporcional a la fuerza del oscilador $f$.
   - La curva continua muestra el perfil convolucionado.
4. Identificar la banda débil $n \rightarrow \pi^*$ frente a la banda intensa $\pi \rightarrow \pi^*$ a longitudes de onda inferiores a 250 nm.

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana Results → UV-Vis en GaussView mostrando el espectro electronico de acetona con las bandas n a pi* y pi a pi* senaladas]
:::

---

### Parte C: Serie de disolventes y solvatocromismo

1. En GaussView, abrir nuevamente la geometría optimizada de la acetona.
2. Configurar el cálculo TD-DFT mediante **Calculate → Gaussian Calculation Setup** (Job Type **Energy**, Method **B3LYP/6-311G**, Charge **0**, Spin **1**).
3. Modificar la palabra clave en el campo **Additional Keywords** para cada disolvente de la serie:
   - Vacío (gas): `td geom=connectivity` (sin palabra clave `scrf`)
   - Ciclohexano: `td scrf=(solvent=cyclohexane) geom=connectivity`
   - Cloroformo: `td scrf=(solvent=chloroform) geom=connectivity`
   - Etanol: `td scrf=(solvent=ethanol) geom=connectivity`
   - Acetonitrilo: `td scrf=(solvent=acetonitrile) geom=connectivity`
   - Agua: `td scrf=(solvent=water) geom=connectivity`
4. Guardar cada archivo con nombre descriptivo en `{{practicas_folder}}EspectroscopiaUV/` (por ejemplo, `acetona_ciclohexano_td.gjf`, `acetona_agua_td.gjf`).
5. Ejecutar cada cálculo y verificar la línea `{{termination_ok}}` en los archivos `.log`.
6. Extraer los valores de $\lambda$ y de fuerza de oscilador $f$ para `Excited State 1` en cada `.log` y anotarlos en la Tabla B de resultados.
7. Comparar la posición de la banda en ciclohexano ($\lambda \approx 279\text{ nm}$) con la observada en agua ($\lambda \approx 264\text{ nm}$) para cuantificar el desplazamiento hipsocrómico (al azul).

| Disolvente | Constante dieléctrica ($\varepsilon$) | Palabra clave en Additional Keywords |
|---|:---:|---|
| Vacío (gas) | 1.0 | *(sin palabra clave scrf)* |
| Ciclohexano | 2.0 | `scrf=(solvent=cyclohexane)` |
| Cloroformo | 4.8 | `scrf=(solvent=chloroform)` |
| Etanol | 24.9 | `scrf=(solvent=ethanol)` |
| Acetonitrilo | 37.5 | `scrf=(solvent=acetonitrile)` |
| Agua | 78.4 | `scrf=(solvent=water)` |

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: comparacion de espectros en Results → UV-Vis o de lineas Excited State 1 en el .log mostrando el desplazamiento al azul de la banda n a pi* de acetona al pasar de ciclohexano a agua]
:::

---

### Parte D: Serie de cetonas sustituidas

1. Construir en GaussView las cuatro moléculas carbonílicas complementarias:
   - Cloruro de acetilo (CH₃–CO–Cl)
   - Acetofenona (CH₃–CO–C₆H₅)
   - Ácido acético (CH₃–CO–OH)
   - Metil-etil-cetona (CH₃–CO–CH₂CH₃)
2. Para cada compuesto, realizar primero la optimización de geometría en acetonitrilo:
   - Menú **Calculate → Gaussian Calculation Setup** → Job Type **Optimization**, Method **B3LYP/6-311G**, Charge **0**, Spin **1**.
   - Additional Keywords: `scrf=(solvent=acetonitrile) geom=connectivity`.
   - Guardar como `[molecula]_MeCN_opt.gjf` y verificar terminación normal.
3. Sobre cada estructura optimizada, configurar y ejecutar el cálculo TD-DFT:
   - Menú **Calculate → Gaussian Calculation Setup** → Job Type **Energy**, Method **B3LYP/6-311G**, Charge **0**, Spin **1**.
   - Campo **Additional Keywords**: `td scrf=(solvent=acetonitrile) geom=connectivity`.
   - Guardar como `[molecula]_MeCN_td.gjf` y verificar terminación normal.
4. Organizar los archivos en subcarpetas específicas dentro de `{{practicas_folder}}EspectroscopiaUV/` para facilitar la gestión.
5. Localizar el bloque `Excited State 1` en el archivo `.log` de cada derivado, extraer $\lambda$ y la fuerza de oscilador $f$, y anotar los valores en la Tabla C de resultados para evaluar el efecto electrónico del sustituyente.

| Compuesto | Estructura química | Denominación |
|---|---|---|
| Acetona | CH₃–CO–CH₃ | Propanona |
| Cloruro de acetilo | CH₃–CO–Cl | Cloruro de etanoilo |
| Acetofenona | CH₃–CO–C₆H₅ | 1-feniletanona |
| Ácido acético | CH₃–CO–OH | Ácido etanoico |
| Metil-etil-cetona | CH₃–CO–CH₂CH₃ | Butanona |

:::{warning}
Cada molécula requiere una optimización geométrica previa en disolvente antes de ejecutar el cálculo TD-DFT correspondiente.
:::

:::{admonition} Captura de pantalla
:class: captura
[CAPTURA: ventana principal de GaussView con la estructura tridimensional de una cetona sustituida (como acetofenona) y su correspondiente espectro en Results → UV-Vis]
:::

---

## Resultados y análisis

### Tabla A: Estimación del gap HOMO-LUMO para acetona

Párrafo corto + tabla. Registro de autovalores de energía orbital y cálculo de longitud de onda estimada para acetona en los diferentes disolventes.

| Disolvente | HOMO (Ha) | LUMO (Ha) | Gap (Ha) | Gap (eV) | $\lambda$ estimada (nm) |
|---|:---:|:---:|:---:|:---:|:---:|
| Vacío | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Ciclohexano | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Acetonitrilo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Agua | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Tabla B: Solvatocromismo de acetona por TD-DFT

Párrafo corto + tabla. Vaciado de longitudes de onda calculadas por TD-DFT y fuerzas de oscilador frente a datos experimentales disponibles.

| Disolvente | $\lambda$ calculada (nm) | $f$ calculada | $\lambda$ experimental (nm) | Desviación (nm) |
|---|:---:|:---:|:---:|:---:|
| Ciclohexano | [TEXTO HUMANO] | [TEXTO HUMANO] | 279 | [TEXTO HUMANO] |
| Agua | [TEXTO HUMANO] | [TEXTO HUMANO] | 264 | [TEXTO HUMANO] |
| Acetonitrilo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Etanol | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Cloroformo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Tabla C: Efecto del sustituyente en la banda n a pi*

Párrafo corto + tabla. Comparación sistemática de longitudes de onda y fuerzas de oscilador para las cinco cetonas evaluadas en medio acetonitrilo.

| Compuesto | $\lambda$ calculada (nm) | $f$ calculada | Comentario sobre el desplazamiento |
|---|:---:|:---:|---|
| Acetona | [TEXTO HUMANO] | [TEXTO HUMANO] | Referencia |
| Cloruro de acetilo | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Acetofenona | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Ácido acético | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |
| Metil-etil-cetona | [TEXTO HUMANO] | [TEXTO HUMANO] | [TEXTO HUMANO] |

### Directrices de recogida de datos

Párrafo corto. Pautas metodológicas para transferir con exactitud los valores de $\lambda$ y $f$ desde el archivo `.log` o desde el panel de visualización espectral de GaussView hacia las tablas del informe.

---

## Preguntas

1. ¿Qué valor de energía de excitación en eV, longitud de onda en nm y fuerza de oscilador $f$ reporta la línea `Excited State 1` en el archivo `.log` de la acetona? Comparar dicha energía vertical con la diferencia estática de autovalores de frontera $\Delta \varepsilon = \varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}$ e indicar la desviación numérica entre ambas aproximaciones.
2. La transición electrónica $n \rightarrow \pi^*$ en la acetona presenta una fuerza de oscilador muy baja ($f \approx 0.0001$), mientras que las transiciones $\pi \rightarrow \pi^*$ muestran típicamente $f > 0.1$. Justificar esta marcada diferencia a partir del solapamiento espacial entre el orbital del par solitario no enlazante del oxígeno y el orbital antienlazante $\pi^*$.
3. El cálculo TD-DFT en disolución mediante el modelo continuo PCM predice un desplazamiento hipsocrómico (hacia el azul) de la banda $n \rightarrow \pi^*$ en agua menor que el medido experimentalmente. Justificar por qué la aproximación de medio dieléctrico homogéneo no reproduce con exactitud la estabilización producida por enlaces de hidrógeno discretos soluto-disolvente.
4. Comparar la longitud de onda de absorción máxima ($\lambda_{\text{max}}$) calculada para la acetona en fase gas con la obtenida en disolución acuosa mediante PCM. Deducir el signo y la magnitud del desplazamiento solvatocrómico ($\Delta \lambda$) y explicar si corresponde a un efecto batocrómico o hipsocrómico.
5. Al comparar el espectro de la acetona con el de la acetofenona, el grupo carbonilo experimenta un desplazamiento hacia el rojo ($\lambda_{\text{max}}$ mayor). Explicar cómo la deslocalización electrónica entre el grupo carbonilo y los orbitales $\pi$ del anillo aromático reduce la separación energética entre los estados electrónicos fundamental y excitado.

---

## Bibliografía

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. Cap. 13 (Espectroscopía electrónica).
- Casida, M. E. *Time-Dependent Density Functional Theory for Molecules*. In *Recent Advances in Density Functional Methods*; World Scientific, 1995.
- NIST Chemistry WebBook, https://webbook.nist.gov (espectros de absorción ultravioleta-visible de referencia).

---

::::{dropdown} Para ir más lejos (opcional)
:color: success

Párrafo medio. Ejercicio opcional sobre la simulación de espectros UV-Vis continuos mediante convolución gaussiana de los estados discretos calculados, y contraste gráfico entre la aproximación estática de gap y TD-DFT para la serie de cetonas.

:::{note}
[TEXTO HUMANO: instrucciones para exportar estados excitados y generar el perfil de absorbancia espectral convolucionado]
:::
::::
