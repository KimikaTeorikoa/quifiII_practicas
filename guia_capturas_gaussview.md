# Guía de Capturas de Pantalla (GaussView y Prácticas)

Esta guía organiza las capturas poniendo el peso visual principal en el capítulo de **Introducción a GaussView** ([intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md)), que es donde el alumno aprende a manejar la interfaz gráfica desde cero. Los capítulos de prácticas contienen únicamente los detalles específicos de cada cálculo.

Todas las capturas se guardan en formato PNG dentro del directorio:
`_static/capturas/`

---

## 1. Ajustes iniciales de calidad en GaussView

Para que todas las capturas queden nítidas y listas para imprenta o web:

1. **Fondo blanco:**
   * Abre GaussView.
   * Ve a **View → Display Format**.
   * En la pestaña **Background**, marca color sólido y selecciona **blanco** (`#FFFFFF`).
   * Pulsa **Apply to All**.
2. **Estilo molecular:**
   * En la pestaña **Molecule**, usa representación **Ball & Stick** o **Tubes**.
3. **Recorte en el sistema operativo:**
   * Para ventanas y menús: captura únicamente la ventana activa (`Alt + Impr Pant` en Linux).
   * Para fragmentos de texto `.log`: abre el archivo en un editor de texto (gedit, Pluma o VS Code con fondo claro) y recorta el bloque exacto.

---

## 2. Catálogo completo de capturas

### Bloque A: Introducción a GaussView (Núcleo tutorial del programa)

| ID | Archivo | Sección en `intro-gaussview.md` | Qué muestra |
|:---:|---|---|---|
| **01** | `01_gv_interfaz_principal.png` | [La interfaz: qué ves al abrir](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L11) | Ventana principal con menús, barra de herramientas, visor 3D y barra de estado. |
| **02** | `02_gv_construccion_h2o_fragmentos.png` | [Construir una molécula](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L20) | Molécula de $\text{H}_2\text{O}$ en el visor 3D junto con la paleta de elementos/fragmentos. |
| **03** | `03_gv_medicion_distancia.png` | [Ver y ajustar geometría](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L41) | Dos átomos seleccionados en $\text{H}_2\text{O}$ con la distancia visible en la barra inferior. |
| **04** | `04_gv_setup_method_hf.png` | [Configurar un cálculo](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L49) | Ventana *Gaussian Calculation Setup*, pestaña **Method** con HF/STO-3G. |
| **05** | `05_gv_monitor_output.png` | [Lanzar el cálculo](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L63) | Ventana de seguimiento en tiempo real tras pulsar **Submit** con el cálculo en marcha. |
| **06** | `06_gv_display_background_blanco.png` | [Personalizar colores y apariencia](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L92) | Ventana **View → Display Format**, pestaña **Background** con el color blanco seleccionado. |

---

### Bloque B: Prácticas (Detalles específicos de cada experimento)

| ID | Archivo | Práctica y sección | Qué muestra |
|:---:|---|---|---|
| **07** | `07_koopmans_setup_c_popfull.png` | [atomos-koopmans.md (Paso 2)](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#paso-2-configurar-el-cálculo-de-hartree-fock) | Calculation Setup del átomo C neutro: triplete y `pop=full`. |
| **07b** | `07b_koopmans_gv_orbitales_c.png` | [atomos-koopmans.md (Paso 6)](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#paso-6-leer-la-energía-orbital-del-homo-y-visualizar-el-orbital) | Diagrama de niveles y ocupación de orbitales Alpha y Beta en **Results → MOs**. |
| **08** | `08_koopmans_log_terminacion_normal.png` | [atomos-koopmans.md (Paso 4)](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#paso-4-verificar-la-terminación-correcta) | Editor de texto: líneas finales del `.log` con `Normal termination`. |
| **09** | `09_koopmans_gv_orbital_homo.png` | [atomos-koopmans.md (Paso 6)](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#paso-6-leer-la-energía-orbital-del-homo-y-visualizar-el-orbital) | Isosuperficie 3D del orbital HOMO (2p) con isovalor 0.01 en **Results → MOs (Visualize)**. |
| **11** | `11_pes_setup_scan_h2.png` / `11a_pes_redundant_coord_h2.png` | [moleculas-pes.md (Paso 2)](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/moleculas-pes.md#paso-2-configurar-el-barrido-de-potencial-scan) | Calculation Setup (Job Type Scan) y Redundant Coordinate Editor para H–H. |
| **12** | *(Omitida)* | [moleculas-pes.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/moleculas-pes.md) | Omitida por decisión de autor (procedimiento análogo al paso 11). |
| **13** | *(Omitida)* | [moleculas-pes.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/moleculas-pes.md) | Omitida por decisión de autor. |
| **14** | `14_vibraciones_gv_modos_co2.png` / `14b_vibraciones_gv_visor_co2.png` | [modos-normales.md (Paso 7)](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/modos-normales.md#paso-7-repetir-el-procedimiento-para-co₂) | Diálogo Vibrations con los 4 modos normales de $\text{CO}_2$ e intensidades IR, y visor 3D. |
| **15** | *(Omitida)* | [modos-normales.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/modos-normales.md) | Omitida por decisión de autor. |
| **16** | *(Omitida)* | [espectroscopia-uv.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/espectroscopia-uv.md) | Omitida por decisión de autor. |

---

## 3. Instrucciones paso a paso

### Captura 01: Interfaz principal de GaussView
* **Archivo:** `_static/capturas/01_gv_interfaz_principal.png`
* **Capítulo:** [intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L11)
* **Qué preparar:** Abre GaussView y maximiza o centra la ventana con fondo blanco.
* **Qué debe verse:** La barra superior de menús (**File**, **Edit**, **View**, **Calculate**, **Results**), la barra de iconos de herramientas, el visor 3D central despejado y la barra de estado inferior.
* **Encuadre:** Ventana completa de GaussView.

---

### Captura 02: Construcción molecular y paleta de fragmentos
* **Archivo:** `_static/capturas/02_gv_construccion_h2o_fragmentos.png`
* **Capítulo:** [intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L20)
* **Qué preparar:** Dibuja la molécula de agua ($\text{H}_2\text{O}$) en el visor 3D. Abre la paleta de elementos periódicos o fragmentos haciendo clic en el icono del átomo de la barra de herramientas.
* **Qué debe verse:** El visor 3D con el agua orientada y, junto a ella, la ventana flotante de selección de elementos químicos.
* **Encuadre:** Visor 3D con la paleta de elementos superpuesta o adyacente.

---

### Captura 03: Medición de distancia de enlace
* **Archivo:** `_static/capturas/03_gv_medicion_distancia.png`
* **Capítulo:** [intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L41)
* **Qué preparar:** En la barra de herramientas, activa la herramienta **Inquire** (icono **`?`**). En la molécula de $\text{H}_2\text{O}$, haz clic primero en el átomo de oxígeno y a continuación en uno de los hidrógenos (sin mantener pulsada ninguna tecla).
* **Qué debe verse:** Los dos átomos seleccionados numerados y, en la barra de estado inferior de la ventana, la distancia de enlace en ángstroms (por ejemplo, `O1 - H2 = 0.96... Å`).
* **Encuadre:** Visor con los átomos seleccionados y la barra inferior legible.

---

### Captura 04: Configuración general del cálculo (Method HF/STO-3G)
* **Archivo:** `_static/capturas/04_gv_setup_method_hf.png`
* **Capítulo:** [intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L49)
* **Qué preparar:** Abre **Calculate → Gaussian Calculation Setup** y pulsa en la pestaña **Method**. Selecciona Method: `Hartree-Fock` (o `HF`), Basis Set: `STO-3G`, Charge: `0`, Spin: `Singlet`.
* **Qué debe verse:** El diálogo completo de Calculation Setup mostrando las pestañas superiores, los campos configurados y los botones inferiores (**Submit**, **Cancel**).
* **Encuadre:** Ventana emergente del Calculation Setup recortada sin escritorio.

---

### Captura 05: Ventana de monitorización del cálculo en ejecución
* **Archivo:** `_static/capturas/05_gv_monitor_output.png`
* **Capítulo:** [intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L63)
* **Qué preparar:** Tras pulsar **Submit** en el cálculo de prueba de $\text{H}_2\text{O}$, confirma el guardado. GaussView abre una ventana de seguimiento (*Stream Output* o monitor del trabajo).
* **Qué debe verse:** La ventana con las líneas de salida de Gaussian avanzando o finalizadas.
* **Encuadre:** Ventana de seguimiento del cálculo.

---

### Captura 06: Diálogo de configuración del color de fondo blanco
* **Archivo:** `_static/capturas/06_gv_display_background_blanco.png`
* **Capítulo:** [intro-gaussview.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/intros/intro-gaussview.md#L92)
* **Qué preparar:** Accede a **View → Display Format** y pulsa en la pestaña **Background**.
* **Qué debe verse:** El diálogo con la casilla de color sólido y el cuadro blanco seleccionado.
* **Encuadre:** Diálogo emergente de Display Format.

---

### Captura 07: Setup del átomo de Carbono neutro con `pop=full`
* **Archivo:** `_static/capturas/07_koopmans_setup_c_popfull.png`
* **Capítulo:** [atomos-koopmans.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#L105)
* **Qué preparar:** Con un único átomo de C, abre **Calculate → Gaussian Calculation Setup**. En **Method**: Method `HF`, Basis `STO-3G`, Charge `0`, Spin `Triplet (3)`. En **Additional Keywords** (o pestaña General): escribe `pop=full`.
* **Qué debe verse:** La ventana de configuración con la multiplicidad 3 y el texto `pop=full` visible.
* **Encuadre:** Ventana del Calculation Setup.

---

### Captura 08: Verificación de terminación normal en el `.log`
* **Archivo:** `_static/capturas/08_koopmans_log_terminacion_normal.png`
* **Capítulo:** [atomos-koopmans.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#L123)
* **Qué preparar:** Abre el archivo `.log` en un editor de texto claro y ve al final.
* **Qué debe verse:** Las últimas líneas con `Normal termination of Gaussian 16 at <fecha>`.
* **Encuadre:** Recuadro del editor centrado en las últimas 8 líneas.

---

### Captura 09: Autovalores orbitales HOMO y LUMO en el `.log`
* **Archivo:** `_static/capturas/09_koopmans_log_homo_lumo.png`
* **Capítulo:** [atomos-koopmans.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#L142)
* **Qué preparar:** En el mismo `.log`, busca `Alpha occ. eigenvalues`.
* **Qué debe verse:** Las filas con `Alpha occ. eigenvalues` y `Alpha virt. eigenvalues`, donde se distingue el último ocupado (HOMO) y el primer desocupado (LUMO).
* **Encuadre:** Fragmento de 4 a 6 líneas en el editor de texto.

---

### Captura 10: Visualización 3D del HOMO del Carbono
* **Archivo:** `_static/capturas/10_koopmans_gv_orbital_homo.png`
* **Capítulo:** [atomos-koopmans.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/atomos-koopmans.md#L115)
* **Qué preparar:** Abre el log o chk del carbono en GaussView. Accede a **Results → MOs**, selecciona el orbital HOMO y genera la superficie (isovalor 0.02).
* **Qué debe verse:** El orbital atómico 2p en 3D sobre el núcleo de carbono con fondo blanco.
* **Encuadre:** Visor 3D con el lóbulo del orbital.

---

### Captura 11: Configuración del barrido 1D en $\text{H}_2$ (Scan)
* **Archivo:** `_static/capturas/11_pes_setup_scan_h2.png`
* **Capítulo:** [moleculas-pes.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/moleculas-pes.md#L93)
* **Qué preparar:** Molécula $\text{H}_2$ en pantalla. Abre Calculation Setup, pestaña **Job Type**, selecciona **Scan**. Configura la coordenada de enlace entre 1 y 2 con valor inicial 0.50 Å, 20 o 30 pasos e incremento de 0.05 o 0.10 Å.
* **Qué debe verse:** Ventana con el Job Type Scan y los parámetros numéricos del barrido visibles.
* **Encuadre:** Ventana emergente del Calculation Setup.

---

### Captura 12: Configuración del barrido diedro en dihaloetano
* **Archivo:** `_static/capturas/12_pes_setup_scan_diedro.png`
* **Capítulo:** [moleculas-pes.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/moleculas-pes.md#L139)
* **Qué preparar:** Dihaloetano en pantalla. Calculation Setup en **Job Type: Scan**. Coordenada interna **Dihedral** seleccionando los 4 átomos $\text{Cl–C–C–Cl}$ con rotación de 0° a 360°.
* **Qué debe verse:** Los 4 átomos seleccionados y los campos del barrido angular completos.
* **Encuadre:** Ventana emergente del Calculation Setup.

---

### Captura 13: Gráfica de la PES en GaussView
* **Archivo:** `_static/capturas/13_pes_gv_curva_scan.png`
* **Capítulo:** [moleculas-pes.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/moleculas-pes.md#L150)
* **Qué preparar:** Abre el log del barrido de $\text{H}_2$ o del dihaloetano y accede a **Results → Scan**.
* **Qué debe verse:** La ventana interactiva con la curva de energía frente a la coordenada.
* **Encuadre:** Ventana emergente de Results Scan.

---

### Captura 14: Bloque de frecuencias vibracionales en el `.log`
* **Archivo:** `_static/capturas/14_vibraciones_log_frequencies.png`
* **Capítulo:** [modos-normales.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/modos-normales.md#L110)
* **Qué preparar:** Abre el `.log` de CO en editor de texto y busca `Frequencies --`.
* **Qué debe verse:** El bloque con `Frequencies`, `Red. masses`, `Frc consts` e `IR Inten`.
* **Encuadre:** Recuadro del editor centrado en esas 4 filas.

---

### Captura 15: Animación del modo de estiramiento de CO con vectores
* **Archivo:** `_static/capturas/15_vibraciones_gv_vectores_co.png`
* **Capítulo:** [modos-normales.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/modos-normales.md#L123)
* **Qué preparar:** Abre el log de frecuencias de CO en GaussView. Accede a **Results → Vibrations**, selecciona el modo de ~2063 cm⁻¹ y marca la casilla **Show Vectors**.
* **Qué debe verse:** El diálogo Display Vibrations con la frecuencia y la molécula con los vectores verdes de desplazamiento nuclear.
* **Encuadre:** Diálogo Display Vibrations y molécula adyacente.

---

### Captura 16: Configuración TD-DFT y modelo de disolvente implícito
* **Archivo:** `_static/capturas/16_uv_setup_tddft_scrf.png`
* **Capítulo:** [espectroscopia-uv.md](file:///home/javi/ORGANIZED/PHD/M_QUIFIS2/content/parte2-gaussian/practicas/espectroscopia-uv.md#L95)
* **Qué preparar:** Acetona optimizada en pantalla. Calculation Setup: **Job Type: Energy**, **Method: B3LYP/6-311G**. En **Additional Keywords**: `td scrf=(solvent=acetonitrile) geom=connectivity`.
* **Qué debe verse:** Ventana con las palabras clave adicionales legibles.
* **Encuadre:** Ventana emergente del Calculation Setup.
