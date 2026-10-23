# Notas de Contenido por Práctica — QUIFIS2

> Extraído de: Manual_Practicas_Teoria.pdf, slides_quifi_practicas.pdf,
> Modeling_of_Ionization_Energy_of_Element.pdf, logs Gaussian de referencia.
> Estas notas informan los scaffolds T012–T015. El texto final es SIEMPRE escrito por humano.

---

## P2-A · Átomos y Teorema de Koopmans

### Concepto central
El teorema de Koopmans establece que la energía de ionización (IE) de un átomo o molécula puede
aproximarse como el negativo de la energía del orbital HOMO (Highest Occupied Molecular Orbital):

**IE ≈ −ε_HOMO**

Esta aproximación es válida dentro del método Hartree-Fock y asume que los orbitales no se
reordenan al eliminar un electrón (approximación de "orbitales congelados").

### Contenidos a cubrir
1. Introducción al método Hartree-Fock (HF) — campo medio, intercambio, correlación.
2. Concepto de orbital atómico y energía orbital.
3. Teorema de Koopmans: derivación cualitativa y limitaciones.
4. Cómo leer energías orbitales del output de Gaussian (`Alpha occ. eigenvalues`).
5. Conversión de unidades: Hartree → eV (×27.2114).
6. Comparación con valores experimentales (tabla NIST).

### Sistemas de referencia (de los logs y del artículo de referencia)
- Átomo H: ROHF/STO-3G → E = −0.64088 Ha (HOMO); IE(Koopmans) = 17.44 eV
- Átomo Mg: UHF/3-21G → HOMO = −0.25189 Ha → IE = 6.85 eV (exp: 7.65 eV, discrepancia ~11%)
- Artículo: cálculos UHF/3-21G para H→Xe; tabla completa disponible en referencia

### Input Gaussian tipo (UHF/3-21G para átomos, según artículo)
```
# UHF/3-21G

Calcul IE atomo X

0 multiplicidad_correcta
X  0.00000  0.00000  0.00000
```
Multiplicidades: H→2, He→1, Li→2, Be→1, B→2, C→3, N→4, O→3, F→2, Ne→1, Na→2, Mg→1...

### Input Gaussian tipo (ROHF/STO-3G para H, según manual de laboratorio)
```
%nproc=1
%Chk=h
# ROHF/STO-3G gfinput pop=full

Calculo del atomo de hidrogeno

0 2
H
```

### Preguntas/Actividades (del manual y las slides)
- Calcular IE de átomos de los 3 primeros períodos.
- Visualizar orbitales ocupados y vacíos con GaussView/MOLDEN.
- Comparar IE calculada (Koopmans) vs. experimental.
- Discutir por qué el método HF sobrestima o subestima la IE según el átomo.

### Resultados esperados de referencia
| Átomo | Exp IE (eV) | HF/3-21G IE (eV) |
|-------|-------------|------------------|
| H | 13.60 | 13.68 |
| He | 24.59 | 24.98 |
| Li | 5.39 | 5.34 |
| Mg | 7.65 | 6.85 |
(tabla completa en `reference_files/extracted/Modeling_of_Ionization_Energy_of_Element.pdf`)

---

## P2-B · Superficie de Energía Potencial (Scan de coordenada interna)

### Concepto central
La Superficie de Energía Potencial (PES, Potential Energy Surface) describe cómo varía la energía
electrónica del sistema al cambiar la geometría nuclear. Un barrido ("scan") calcula energías a lo
largo de una coordenada interna (distancia de enlace, ángulo, diedro) sin optimizar el resto de la
geometría.

### Contenidos a cubrir
1. Aproximación de Born-Oppenheimer: separación de movimientos nuclear y electrónico.
2. Concepto de PES: mínimos (estructuras estables), puntos de silla (estados de transición), barreras.
3. Coordenadas internas: distancias R, ángulos θ, diedros φ.
4. El keyword `scan` en Gaussian con `ModRedundant`.
5. Cómo extraer energías por punto del log y construir la curva PES.
6. Interpretación: disociación, isomerización, barreras de rotación.

### Sistemas de referencia (del manual y de los logs h2_scan.log.txt)
- **H₂ singlete y triplete:** scan de distancia R(H-H) → curva de disociación del enlace
  - Singlete: mínimo en R ≈ 0.74 Å (experimental), barreras hacia disociación
  - Triplete: sin mínimo → no forma enlace estable
- **Diedro en H₂XC-CXH₂ (X = halógeno):** scan de ángulo diedro → barrera de rotación conformacional
  - Práctica real: calcular la barrera para distintos X (F, Cl, Br)

### Input Gaussian tipo (scan R(H-H), ROHF/STO-3G)
```
%chk=h2_scan.chk
# ROHF/STO-3G geom=connectivity

Scan PES H2

0 1
H
H 1 R1
[línea en blanco]
R1=0.55    ← distancia inicial en Å
[línea en blanco]
ModRedundant
R1 R(1,2) 0.55 Scan    ← 21 puntos, paso de 0.05 Å (infered: 0.55 to 1.55 Å)
```

### Cómo leer los resultados del scan
En el log, cada punto del scan tiene:
```
Step number  1 out of a maximum of 20 on scan point  1 out of 21
SCF Done:  E(ROHF) =  -1.07905...  A.U.
```
Extraer: número de punto + energía SCF → tabla R vs E(Ha) → convertir a kcal/mol relativa al mínimo.

### Preguntas/Actividades (del manual)
- Construir PES H₂ singlete y triplete en el mismo gráfico.
- Identificar el mínimo y la longitud de enlace de equilibrio.
- Comparar el triplete con el singlete; interpretar físicamente.
- Para moléculas de tipo H₂XC-CXH₂: identificar los confórmeros estable y las barreras.
- ¿Cuál halógeno produce la mayor barrera de rotación? Justificar.

---

## P2-C · Modos Normales de Vibración

### Concepto central
Las vibraciones moleculares se describen como combinaciones lineales de "modos normales",
en los que todos los átomos oscilan en fase con la misma frecuencia. Una molécula no lineal con
N átomos tiene 3N-6 modos de vibración; una lineal, 3N-5.

### Contenidos a cubrir
1. Aproximación armónica: la PES se aproxima como parábola cerca del mínimo.
2. Concepto de modo normal: coordenadas normales, frecuencias propias.
3. Reglas de selección IR (el modo debe cambiar el momento dipolar).
4. Número de modos activos: 3N-5 (lineal) vs 3N-6 (no lineal).
5. El keyword `freq` en Gaussian: output de frecuencias y desplazamientos atómicos.
6. Visualización de modos normales con GaussView o MOLDEN.
7. Comparación con espectros experimentales NIST.
8. (Avanzado) Espectroscopia rotacional-vibracional de CO (script TheoEspRotBib.py).

### Sistemas de referencia (de los logs Gaussian y del manual)
- **CO (diatómica lineal):** 3×2-5 = 1 modo vibracional
  - Calculado B3LYP/6-311G: ν̃ = 2063.37 cm⁻¹ (exp: ~2143 cm⁻¹; escala ×1.04 aprox.)
  - R(C-O) optimizado = 1.1473 Å (exp: 1.128 Å)
  - HOMO = −0.38412 Ha, LUMO = −0.04879 Ha → gap = 9.11 eV
- **CO₂ (lineal, 3 átomos):** 3×3-5 = 4 modos (pero 2 son dobletes degenerados: estiramiento sim., asim., flexión×2)
- **Acetona (no lineal, 10 átomos):** 3×10-6 = 24 modos normales
  - Frecuencias de referencia (B3LYP/6-311G en MeCN): 1225, 1279, 1542, 1715, 2962, 3044 cm⁻¹

### Input Gaussian tipo (CO opt+freq, B3LYP/6-311G)
```
%chk=co_b3lyp_opt.chk
# opt freq rob3lyp/6-311g geom=connectivity

CO optimizacion y frecuencias

0 1
C
O 1 R1
[línea en blanco]
R1=1.20
```

### Cómo leer las frecuencias del log
```
Frequencies --   2063.3674
Red. masses --     6.8584
Frc consts  --     0.1719
IR Intensities --   4.5083
Zero-point correction=   0.004701 (Hartree/Particle)
```

### Espectro rovibracional de CO (capítulo 6 del manual)
- Combinación de vibración (ν̃ = 2169.86 cm⁻¹ exp.) y rotación (B = 1.9369 cm⁻¹)
- Ramas P (ΔJ=−1) y R (ΔJ=+1); no hay rama Q para ΔJ=0 en CO
- Posiciones de líneas: F(J) = B×J×(J+1); ν̃_PR = ν̃_vib ± 2B×(m+1)
- Script TheoEspRotBib.py: genera espectro teórico (frecuencias + intensidades Boltzmann)
- XMGRACE: para graficar y comparar teórico vs. experimental

### Preguntas/Actividades
- Calcular el número de modos normales esperado para CO, CO₂, H₂O.
- Visualizar cada modo normal en GaussView: ¿es estiramiento o flexión? ¿IR activo?
- Comparar frecuencias calculadas vs. experimentales (NIST); discutir el factor de escala.
- (Opcional avanzado) Simular espectro rovibracional de CO y comparar con experimental.

---

## P2-D · Espectroscopía UV-Vis de Cetonas

### Concepto central
Las cetonas absorben luz UV-Vis principalmente por dos tipos de transiciones electrónicas:
- **n→π*:** electrón no enlazante del O al orbital π* del C=O. Banda débil (~280-300 nm, f<0.001, prohibida por simetría).
- **π→π*:** electrón del orbital π enlazante al π*. Banda intensa (<250 nm, f>0.1, permitida).

El solvente desplaza las bandas ("solvatocromismo"): el n→π* se desplaza al azul en disolventes polares (blue shift), el π→π* se desplaza al rojo.

### Contenidos a cubrir
1. Introducción a la espectroscopía UV-Vis: cromóforos, transiciones electrónicas.
2. HOMO-LUMO gap como estimación de la primera transición (limitaciones).
3. TD-DFT: método para calcular estados excitados con mayor precisión.
4. Keyword `td` en Gaussian; interpretación del output (`Excited State N`).
5. Solvatación implícita: modelo PCM, keyword `scrf=(solvent=X)`.
6. Efecto del sustituyente R en H₃C-C(=O)-R sobre λ_max.
7. Efecto del disolvente sobre n→π*.

### Sistemas de referencia (del manual y de los logs)
**Disolventes a estudiar:** ciclohexano, acetonitrilo, cloroformo, etanol, agua
**Cetonas a estudiar:**
- Acetona (H₃C-CO-CH₃)
- Cloruro de acetilo (H₃C-CO-Cl)
- Acetofenona (H₃C-CO-Ph)
- Ácido acético (H₃C-CO-OH)
- Metil-etil-cetona (H₃C-CO-CH₂CH₃)

**Valores de referencia (acetona):**
- En vacío: banda n→π* calculada ~289 nm (TD-DFT)
- Experimental: 279 nm (ciclohexano), 264 nm (agua) → blue shift en disolvente polar
- HOMO = −0.27636 Ha (acetona en MeCN), LUMO = −0.06005 Ha → gap estimado ~5.9 eV (~210 nm)

### Input Gaussian tipo (acetona en acetonitrilo, TD-DFT)
```
%chk=acetona_mecn_td.chk
# td b3lyp/6-311g scrf=(solvent=acetonitrile) geom=connectivity

Acetona TD-DFT en acetonitrilo

0 1
[coordenadas de acetona]
```

### Cómo leer los estados excitados del log
```
Excited State   1:  Singlet-A"    4.2871 eV  289.23 nm  f=0.0003
    8 -> 9         0.70711
```
- `Singlet-A"` → simetría del estado excitado
- `4.2871 eV` / `289.23 nm` → energía / longitud de onda de la transición
- `f=0.0003` → fuerza del oscilador (proporcional a intensidad absorbancia); f<0.01 = banda débil
- `8 -> 9` → contribución principal: MO #8 (HOMO) → MO #9 (LUMO)

### Estimación previa vía HOMO-LUMO gap
Antes de TD-DFT, se puede estimar λ_max con el gap HOMO-LUMO:
- ΔE_gap (Ha) → ΔE (eV) = ΔE_gap × 27.2114
- λ (nm) = hc/ΔE → λ (nm) ≈ 1239.8 / ΔE(eV)
- Para CO en B3LYP/6-311G: ΔE = 0.33533 Ha × 27.2114 = 9.12 eV → λ ≈ 136 nm
- Esta estimación suele subestimar λ (sobreestima el gap); TD-DFT es más preciso.

### Preguntas/Actividades (del manual)
- Calcular el espectro UV de las 5 cetonas en los 5 disolventes (25 cálculos).
- Para cada cetona: tabla λ_max (n→π*) vs. disolvente; identificar blue/red shift.
- Discutir la relación entre polaridad del disolvente (constante dieléctrica) y el desplazamiento.
- Comparar la λ_max estimada por HOMO-LUMO gap vs. TD-DFT.
- Identificar qué sustituyente R produce el mayor desplazamiento respecto a acetona pura.

---

## Notas transversales para todos los scaffolds

### Filosofía pedagógica (del manual y slides)
- El objetivo NO es aprender a usar Gaussian, sino entender la química/física subyacente.
- Los cálculos son un medio; la interpretación es el fin.
- Cada práctica debe incluir: (1) introducción teórica, (2) instrucciones de cálculo paso a paso, (3) preguntas de análisis e interpretación.

### Errores frecuentes de estudiantes (inferido del manual)
- Confundir multiplicidad de espín con carga (multiplicidad = 2S+1, NO la carga).
- No dejar la línea en blanco final en el .gjf → error de Gaussian.
- Confundir g03 con g16 (el manual usa g03 pero el laboratorio tiene g16).
- No verificar `Normal termination` antes de analizar resultados.
- Usar extensión `.com` en vez de `.gjf` (convención actual del laboratorio).

### Software disponible en el laboratorio
- Gaussian 16 (g16) — cálculos quantum
- GaussView — visualización y preparación de inputs
- MOLDEN — visualización alternativa de orbitales y frecuencias
- Python / Jupyter Notebook — análisis de datos y espectros
- XMGRACE — gráficos científicos (especialmente para espectros rovibracional CO)
