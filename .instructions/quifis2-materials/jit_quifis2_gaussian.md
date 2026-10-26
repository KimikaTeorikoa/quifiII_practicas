# JIT Guide: Gaussian 16 y GaussView — Convenciones M_QUIFIS2
# Cargado por Claude al inicio de cada chat de scaffold de práctica.
# Versión: 1.0.0 | 2026-10-24
# Fuente: logs de referencia en reference_files/extracted/Gaussian/

---

## 1. Entorno de laboratorio (confirmado en logs de referencia)

| Parámetro | Valor confirmado |
|-----------|-----------------|
| Software | **Gaussian 16, Revision A.03** |
| Ruta ejecutable | `/usr/local/g16/` |
| Usuario de laboratorio | `ikasle` |
| Carpeta de trabajo | `/home/ikasle/Documentos/Practicas/` |
| Scratch | `/scratch/ikasle/` |
| Línea de terminación correcta | `Normal termination of Gaussian 16` |

Los scaffolds usan estos valores. Si el laboratorio cambia de versión, actualizar este archivo.

---

## 2. Anatomía de un archivo de input (`.gjf`)

Los alumnos NUNCA escriben inputs a mano. GaussView los genera. Pero el scaffold puede
mostrar el input generado como referencia, con este formato:

```
%chk=nombre.chk
# HF/STO-3G pop=full

Título descriptivo

0 1
C   0.000   0.000   0.000

```

**Campos clave:**
- `%chk=` — guarda el checkpoint (no obligatorio para lectura básica)
- `# método/base keywords` — la línea de ruta (route section)
- `0 1` — carga y multiplicidad
- Bloque de coordenadas (generado automáticamente por GaussView)
- **Línea en blanco final** — OBLIGATORIA; sin ella, el cálculo falla

---

## 3. Líneas clave del archivo de output (`.log`)

Estas son las líneas que los alumnos deben buscar y copiar. Incluir el texto exacto
en cada práctica.

### Terminación correcta

```
Normal termination of Gaussian 16
```

Si la última línea NO es esta, el cálculo falló.

### Versión y fecha (primeras líneas del log)

```
Entering Gaussian System, Link 0=g16
...
Gaussian 16:  ES64L-G16RevA.03 25-Dec-2016
```

### Energía total (SCF Done)

```
SCF Done:  E(RHF) =  -1.11750479741     A.U. after    6 cycles
```

- `E(RHF)` para sistemas de capa cerrada (multiplicidad 1)
- `E(ROHF)` para sistemas de capa abierta (multiplicidad ≠ 1)
- El número en `A.U.` son **Hartrees**

### Energías orbitales (con `pop=full`)

```
Alpha  occ. eigenvalues --  -20.55676  -1.34630  -0.71460  -0.57108  -0.49787
Alpha virt. eigenvalues --    0.21434   0.30393
```

- `occ.` = orbitales ocupados; `virt.` = orbitales virtuales (vacíos)
- El **último valor de la última línea `occ.`** es $\varepsilon_{\text{HOMO}}$
- El **primer valor de la primera línea `virt.`** es $\varepsilon_{\text{LUMO}}$
- Todos los valores están en **Hartrees**

### Frecuencias de vibración (cálculos `freq`)

```
 Frequencies --    1027.1259              3161.7916
```

- Valores en cm⁻¹
- Una frecuencia imaginaria (negativa) indica que la geometría NO es un mínimo

---

## 4. Configuración GaussView: pestaña por pestaña

### Gaussian Calculation Setup — pestaña **Job Type**

| Tipo | Cuándo usarlo |
|------|--------------|
| Energy | Calcular la energía en una geometría fija (SP) |
| Optimization | Optimizar la geometría hasta encontrar un mínimo |
| Frequency | Calcular modos normales (requiere geometría optimizada) |
| Opt+Freq | Optimizar y calcular frecuencias en un solo paso |
| Scan | Barrer una coordenada (PES) |

### Gaussian Calculation Setup — pestaña **Method**

| Campo | Descripción |
|-------|-------------|
| Method | Método QM: HF, B3LYP, MP2, etc. |
| Basis Set | Base: STO-3G, 3-21G, 6-31G, 6-311G, etc. |
| Charge | Carga total de la molécula/átomo (0 = neutro, +1 = catión) |
| Spin | Multiplicidad (2S+1): 1 = singlete, 2 = doblete, 3 = triplete, 4 = cuartete |

### Gaussian Calculation Setup — pestaña **Additional Keywords**

Campo de texto libre para keywords que no tienen opción gráfica:
- `pop=full` — muestra todas las energías orbitales en el `.log`
- `scrf=(solvent=water)` — modelo de solvatación implícita
- `td` — cálculo de estados excitados (TD-DFT)

---

## 5. Rutas de menú GaussView para resultados

| Resultado | Ruta de menú |
|-----------|-------------|
| Energías orbitales y HOMO/LUMO | **Results → MOs** |
| Resumen de la energía total | **Results → Summary** |
| Modos de vibración animados | **Results → Vibrations** |
| Geometría optimizada animada | **Results → Optimization** |
| Curva de barrido (PES) | **Results → Scan** |
| Espectro IR (con intensidades) | **Results → Vibrations → IR Spectrum** |

---

## 6. Convenciones de nombrado de archivos en el laboratorio

Usar siempre nombres descriptivos. Patrón recomendado:

```
{átomo_o_molécula}_{estado}_{método}_{base}.gjf
```

Ejemplos:
- `C_neutro_HF_STO3G.gjf`
- `C_cation_HF_STO3G.gjf`
- `H2_singlete_HF_STO3G.gjf`
- `CO_opt_B3LYP_6311G.gjf`

Los archivos `.log` se generan automáticamente con el mismo nombre base.

---

## 7. Errores frecuentes y cómo identificarlos en el `.log`

| Error | Síntoma en el `.log` | Causa más probable |
|-------|----------------------|-------------------|
| Multiplicidad incorrecta | `The combination of multiplicity X and N electrons is impossible` | Carga o multiplicidad equivocada |
| No converge SCF | `Convergence failure -- run terminated` | Geometría inicial muy mala o multiplicidad errónea |
| Falta línea en blanco | `End of file in ZSymb` o similar | El input no termina con línea en blanco |
| Frecuencia imaginaria | Valor negativo en `Frequencies --` | Geometría no optimizada antes del freq |

---

## 8. Conversiones de unidades (para incluir en las prácticas)

| Conversión | Factor |
|-----------|--------|
| Hartree → eV | × 27.2114 |
| Hartree → kcal/mol | × 627.509 |
| Hartree → kJ/mol | × 2625.50 |
| cm⁻¹ → eV | × 0.000124 |
| Å → Bohr | × 1.88973 |
