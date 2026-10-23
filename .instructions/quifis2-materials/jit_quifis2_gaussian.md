# JIT Guide: Gaussian 16 — Convenciones para QUIFIS2

> Cargado al inicio de sesiones que involucran scaffolds de prácticas (T012–T015).
> Extraído de: logs de referencia (`reference_files/extracted/Gaussian/*.log.txt`) y manual original.

---

## 1. Versión confirmada

Los archivos de log de referencia muestran:
```
Gaussian 16, Revision A.03  (25-Dec-2016)
Link 0=g16
/usr/local/g16/l1.exe
```
**La versión en uso en los ordenadores del laboratorio es Gaussian 16 (g16)**, no g03 como indica el manual antiguo.  
El comando de ejecución es:
```bash
$ g16 nombre_calculo.gjf > nombre_calculo.log &
```
(o equivalente según la instalación local — confirmar con T003)

---

## 2. Anatomía del archivo de input (.gjf o .com)

```
%chk=nombre.chk          ← checkpoint (para GaussView, opcional)
# método/base keywords   ← línea de ruta (route section)
[línea en blanco]
Título del cálculo       ← comentario libre
[línea en blanco]
carga multiplicidad      ← p.ej. "0 1" (neutro singlete)
COORDENADAS              ← z-matrix o coordenadas cartesianas
[línea en blanco]        ← línea en blanco final OBLIGATORIA
```

### Ejemplos reales de route sections (extraídos de logs)

| Cálculo | Route section |
|---------|---------------|
| H₂ singlete SP | `# rohf/sto-3g geom=connectivity` |
| CO optimización+frecuencias | `# opt freq rob3lyp/6-311g geom=connectivity` |
| Acetona en acetonitrilo opt+freq | `# opt freq b3lyp/6-311g scrf=(solvent=acetonitrile) geom=connectivity` |

### Keywords más usados en estas prácticas

| Keyword | Función |
|---------|---------|
| `rohf` | Restricted Open-shell Hartree-Fock |
| `rhf` | Restricted Hartree-Fock (capa cerrada) |
| `uhf` | Unrestricted HF (uso en átomos con spines desapareados) |
| `b3lyp` / `rob3lyp` | DFT híbrido B3LYP (cerrada / abierta) |
| `sto-3g` | Base mínima (usada en P2-A Koopmans y en H₂) |
| `6-311g` | Base triple-zeta (usada en CO y acetona) |
| `opt` | Optimización de geometría (minimización en PES) |
| `freq` | Cálculo de frecuencias (hessiana, modos normales) |
| `td` | Time-Dependent DFT (estados excitados, espectro UV) |
| `scrf=(solvent=X)` | Modelo de solvatación implícita (PCM) |
| `geom=connectivity` | Incluir tabla de conectividad (para GaussView) |
| `scan` | Barrido de coordenada interna (vía ModRedundant) |
| `pop=full` | Análisis de población completo (cargos Mulliken, orbitales) |

### Multiplicidades comunes

| Sistema | Carga | Multiplicidad | Método |
|---------|-------|---------------|--------|
| H (átomo) | 0 | 2 | ROHF |
| H₂ singlete | 0 | 1 | ROHF |
| H₂ triplete | 0 | 3 | ROHF |
| CO singlete | 0 | 1 | ROHF/B3LYP |
| CO doblete (N-1e) | +1 | 2 | usado para Koopmans |
| Átomo Li–Ne | 0 | ver tabla periódica | UHF/3-21G |
| Acetona | 0 | 1 | B3LYP |

---

## 3. Anatomía del archivo de output (.log)

### Sección de encabezado
```
Entering Gaussian System, Link 0=g16
Input=ruta/al/archivo.gjf
Output=ruta/al/archivo.log
Gaussian 16:  ES64L-G16RevA.03  25-Dec-2016
```

### Verificar terminación correcta
**Siempre** buscar al final del .log:
```
Normal termination of Gaussian 16 at [fecha y hora].
```
Si no aparece, el cálculo falló o fue interrumpido.

### Resumen archivado (archive entry)
Unas líneas antes del `Normal termination`, aparece el bloque `\\@` que resume el cálculo:
```
1\1\GINC-...\SP\ROHF\STO-3G\H2\IKASLE\...\0\\
# rohf/sto-3g geom=connectivity\\Title...\\0,1\H,...\\
Version=ES64L-G16RevA.03\State=1-SGG\HF=-1.1011282\
RMSD=0.000e+00\Dipole=0.,0.,0.\PG=D*H\\@
```
Aquí se puede leer directamente la energía HF (en Hartrees).

### Energía SCF (línea principal)
```
SCF Done:  E(ROHF) =  -1.10112824196     A.U. after    1 cycles
SCF Done:  E(ROB3LYP) =  -113.296812140  A.U. after    6 cycles
SCF Done:  E(RB3LYP) =  -114.501579454   A.U. after    8 cycles
```

### Energías orbitales (eigenvalues)
```
Alpha  occ. eigenvalues --  -19.24711 -10.31547  -1.20216  -0.57634  -0.48510
Alpha  occ. eigenvalues --   -0.48510  -0.38412         ← el último negativo = HOMO
Alpha virt. eigenvalues --   -0.04879  -0.04879  ...    ← el primero = LUMO
```
**Koopmans:** IE = −ε_HOMO (en Hartrees) × 27.2114 eV/Ha

### Geometría optimizada
```
                       !   Optimized Parameters   !
                       ! (Angstroms and Degrees)  !
! R1    R(1,2)         1.1473         -DE/DX =    0.0   !
```

### Frecuencias de vibración
```
Frequencies --   2063.3674          ← CO (1 modo, molécula diatómica lineal: 3N-5=1)
Frequencies --   1225.5178    1279.0043    1542.3808   ← acetona (múltiples)
Zero-point correction=   0.004701 (Hartree/Particle)
```
- Frecuencia positiva → mínimo en la PES
- Frecuencia imaginaria (negativa) → punto de silla / estructura de transición

### Momento dipolar
```
Dipole moment (field-independent basis, Debye):
   X=  0.0000   Y=  0.0000   Z=  0.0000   Tot=  0.0000
```

### Cargas Mulliken
```
Mulliken charges and spin densities:
   1  O   -0.xxx
   2  C   +0.xxx
```

### Estados excitados (TD-DFT)
Aparece con keyword `td` en la route section:
```
Excited State   1:  Singlet-A"    4.2871 eV  289.23 nm  f=0.0003
   8 -> 9         0.70711
```
- `eV` y `nm` son la energía y longitud de onda de la transición
- `f=` es la fuerza del oscilador (intensidad)
- `8 -> 9` indica qué orbital→qué orbital (HOMO→LUMO, etc.)

### Scan de PES (barrido de coordenada)
```
The following ModRedundant input section has been read:
   R1   R(1,2)   0.55   Scan
Step number  1 out of a maximum of  20 on scan point  1 out of  21
SCF Done:  E(ROHF) =  -1.07905...
```
Cada `scan point` es un punto de la PES a una geometría distinta.

---

## 4. GaussView como interfaz principal del estudiante

**Los estudiantes usan GaussView exclusivamente** — no escriben inputs ni lanzan comandos Bash.

### Flujo completo en GaussView
1. **Abrir GaussView** (icono en escritorio o `gaussview &` en terminal)
2. **Dibujar la molécula:**
   - `File → New → Molecule Group` → editor gráfico con tabla periódica
   - Usar `Builder` para añadir átomos y enlaces; GaussView ajusta geometría inicial
   - Alternativamente: `File → Open` para cargar una geometría desde un `.log` anterior
3. **Configurar el cálculo:**
   - `Calculate → Gaussian Calculation Setup`
   - Pestaña `Method`: seleccionar Job Type (Energy / Opt / Freq / ...), Method (HF/B3LYP/...), Basis Set (STO-3G / 3-21G / 6-311G / ...)
   - Pestaña `Additional Keywords`: para añadir `scrf=(solvent=X)`, `td`, `pop=full` etc.
   - Pestaña `Link 0`: para añadir `%chk=` si se quiere checkpoint
4. **Lanzar:** botón `Submit` → GaussView genera el `.gjf` y llama a Gaussian en segundo plano
5. **Ver resultados cuando termina:**
   - `Results → Optimization` → ver convergencia y geometría final animada
   - `Results → Vibrations` → animación de cada modo normal
   - `Results → MOs` → visualizar orbitales moleculares (HOMO, LUMO, ...)
   - `Results → NMR`, `Results → UV-Vis` → si se calcularon
6. **Leer el .log para extraer datos numéricos:**
   - `File → Open` el archivo `.log` → GaussView lo renderiza
   - Para datos exactos (eigenvalues, frecuencias) → abrir el `.log` con un editor de texto o usar `Results → Summary`

### MOLDEN (alternativa para visualizar .log)
```bash
$ molden nombre.log
```
- Menu `Density mode` → ver densidad electrónica y orbitales
- Menu `Freq` → ver modos normales de vibración

### MOLDEN
```bash
$ molden nombre.log
```
- Menu `Density mode` → ver densidad electrónica y orbitales
- Menu `Freq` → ver modos normales de vibración
- Menu `Read` → cargar otro archivo .log

---

## 5. Convenciones de nomenclatura de archivos

Del laboratorio de referencia (directorio `/home/ikasle/Documentos/Practicas/`):
```
h2.gjf / h2.log          ← H₂ singlete, SP
h2_triplet.gjf / .log    ← H₂ triplete
h2_scan.gjf / .log       ← PES scan H₂ singlete
h2_scan_triplet.gjf/.log ← PES scan H₂ triplete
h_scan2.gjf / .log       ← scan alternativo
co_b3lyp.gjf / .log      ← CO, solo SP B3LYP
co_b3lyp_opt.gjf / .log  ← CO, opt+freq B3LYP (R_CO opt = 1.1473 Å)
co_doublet.gjf / .log    ← CO catión (+1), doblete
acetone_acetonitrile.gjf/.log ← acetona en acetonitrilo, opt+freq
```
Convención sugerida para nuevos archivos: `molecula_metodo_tarea.gjf`

---

## 6. Unidades y factores de conversión

| Magnitud | Unidad Gaussian | Conversión |
|----------|-----------------|-----------|
| Energía | Hartree (a.u.) | 1 Ha = 27.2114 eV = 627.509 kcal/mol |
| Distancia | Angström (Å) | 1 Å = 0.529177 a₀ (Bohr) |
| Frecuencia | cm⁻¹ | — |
| Dipolo | Debye | — |

---

## 7. Notas pedagógicas para los scaffolds

- **P2-A (Koopmans):** usar `uhf/3-21g` (como en el artículo de referencia) o `rohf/sto-3g`; leer HOMO eigenvalue; convertir a eV; comparar con tabla NIST.
- **P2-B (PES scan):** keyword `scan` en ModRedundant; leer energía en cada `scan point`; construir tabla R vs E.
- **P2-C (Modos normales):** keyword `opt freq`; leer `Frequencies --`; comparar con valores experimentales CO (~2143 cm⁻¹ exp, 2063 calc); 3N-5 modos para lineal, 3N-6 para no lineal.
- **P2-D (UV):** keyword `td` + `scrf`; leer `Excited State` lines; identificar n→π* (~289 nm acetona) vs π→π*; estudiar efecto del disolvente sobre λ_max.
