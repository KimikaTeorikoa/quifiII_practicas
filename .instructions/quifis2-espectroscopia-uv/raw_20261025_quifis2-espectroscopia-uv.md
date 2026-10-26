# P2-D: Espectroscopía UV-Vis de Cetonas

## Introducción

:::{note}
[TEXTO HUMANO: motivación — la espectroscopía UV-Vis como herramienta de identificación
de cromóforos orgánicos. Conectar con el color de compuestos orgánicos cotidianos.
Las cetonas son un ejemplo modelo porque tienen dos tipos de transiciones electrónicas
bien separadas y responden de forma característica al disolvente.]
:::

## Objetivos

:::{note}
[TEXTO HUMANO: lista numerada. Propuesta:]

[PROPUESTA:
1. Calcular el espectro UV-Vis de la acetona y otras cetonas mediante TD-DFT.
2. Identificar las transiciones n→π* y π→π* en el output de Gaussian.
3. Estimar la primera transición a partir del gap HOMO-LUMO y comparar con TD-DFT.
4. Estudiar el efecto del disolvente (solvatocromismo) sobre la banda n→π*.
5. Comparar los resultados calculados con los valores experimentales.
]
:::

---

## Conceptos clave

### Transiciones electrónicas en cetonas

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que cuando una molécula absorbe luz UV-Vis, un electrón "salta"
de un orbital ocupado a un orbital vacío. En las cetonas (grupo C=O) hay dos saltos
importantes: el n→π* (electrón no enlazante del oxígeno al π* del carbonilo, banda débil
alrededor de 280-300 nm) y el π→π* (del enlace π del carbonilo al π*, banda intensa
por debajo de 250 nm). La longitud de onda de absorción nos dice qué energía separa
esos orbitales — y eso depende del entorno químico.]
:::

### El gap HOMO-LUMO como primera aproximación

:::{admonition} 💡 Intuición física
:class: intuicion
La diferencia de energía entre el HOMO y el LUMO da una idea aproximada de la energía
de la primera transición electrónica. Si esa diferencia es grande → el compuesto absorbe
en el UV lejano (aparece incoloro). Si es pequeña → absorbe en el visible (aparece
coloreado).

La conversión es:
- ΔE (Ha) × {{ha_to_ev}} = ΔE en eV
- λ (nm) = 1239.8 / ΔE (eV)

Esta estimación es solo orientativa: el TD-DFT es más preciso.
:::

**Ejemplo con los datos del log de referencia (formaldehído, CH₂O, en MeCN):**

:::{note}
El log de referencia disponible corresponde al **formaldehído** (un aldehído, no una cetona),
pero el procedimiento de cálculo e interpretación es idéntico. Los alumnos obtendrán sus
propios valores para las cetonas de la práctica.
:::

| Orbital | Energía (Ha) |
|---------|:------------:|
| HOMO    | −0.27636 |
| LUMO    | −0.06005 |
| Gap     | 0.21631 |
| Gap (eV) | 5.89 |
| λ estimada (nm) | 210 |

### TD-DFT: cálculo de estados excitados

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que el DFT normal solo describe el estado fundamental. Para
calcular las energías de los estados excitados (los que absorben luz), se usa una
extensión llamada TD-DFT (DFT dependiente del tiempo). Gaussian la activa con la
palabra clave `td`. El resultado es una lista de estados excitados con su energía
en eV y en nm, y una "fuerza del oscilador" f que indica qué tan intensa es esa
absorción (f ≈ 0 → banda débil; f > 0.1 → banda intensa).]
:::

### Efecto del disolvente: solvatocromismo

:::{admonition} 💡 Intuición física
:class: intuicion
[TEXTO HUMANO: explicar que el disolvente estabiliza o desestabiliza de forma distinta
el estado fundamental y el estado excitado. Para la banda n→π*: en disolventes polares,
el estado fundamental (con el par no enlazante del O) se estabiliza más que el excitado
→ el gap aumenta → la banda se desplaza hacia longitudes de onda menores (blue shift).
Para la banda π→π* ocurre lo contrario (red shift). Este fenómeno se llama
solvatocromismo y es muy útil para identificar el tipo de transición.]
:::

**Efecto experimental conocido para la acetona:**

| Disolvente | λ n→π* experimental (nm) |
|-----------|:------------------------:|
| Ciclohexano | 279 |
| Agua | 264 |
| Δ (blue shift) | −15 nm |

El modelo PCM de Gaussian (`scrf=`) simula este efecto.

---

## Procedimiento

La práctica tiene **dos partes**: (A) estimar el gap HOMO-LUMO y (B) calcular el espectro TD-DFT.

### Parte A: Estimación por gap HOMO-LUMO

#### Paso A1: Calcular la geometría optimizada

1. Dibuja la acetona en GaussView (CH₃-CO-CH₃).
2. Ve a **Calculate → Gaussian Calculation Setup**.
3. Pestaña **Job Type** → **Optimization**.
4. Pestaña **Method**:

| Campo | Valor |
|-------|-------|
| Method | **B3LYP** |
| Basis Set | **6-311G** |
| Charge | **0** |
| Spin (Multiplicity) | **1** |

5. En **Additional Keywords** escribe: `scrf=(solvent=acetonitrile)`

:::{tip}
`scrf=(solvent=acetonitrile)` activa el modelo PCM para simular el disolvente
acetonitrilo. Gaussian elige automáticamente los parámetros dieléctricos del disolvente.
Para estudiar otro disolvente, basta con cambiar el nombre: `solvent=water`,
`solvent=cyclohexane`, etc.
:::

6. Haz clic en **Submit**. Guarda como `acetona_MeCN_opt.gjf` en
   {{practicas_folder}}`EspectroscopiaUV/`.

:::{danger}
Verifica la terminación correcta: {{termination_ok}}
:::

#### Paso A2: Leer el HOMO y el LUMO

Abre el `.log` y busca (Ctrl+F): `Alpha  occ. eigenvalues`

Verás algo como:

```
 Alpha  occ. eigenvalues --  ...   -0.27636
 Alpha virt. eigenvalues --   -0.06005   ...
```

- El **último número** de la última línea `Alpha  occ.` → **HOMO** (energía en Ha)
- El **primer número** de la primera línea `Alpha virt.` → **LUMO** (energía en Ha)

:::{warning}
Los valores de energía orbital en Ha son negativos para orbitales enlazantes.
El HOMO y el LUMO de la acetona en MeCN son ambos negativos — el LUMO también puede
serlo si el método incluye efectos de correlación (como B3LYP). Esto es normal.
:::

Anota los valores y calcula el gap:

$$\Delta E_\text{gap} \text{ (eV)} = (\varepsilon_\text{LUMO} - \varepsilon_\text{HOMO}) \times \text{{{ha_to_ev}}}$$

$$\lambda_\text{estimada} \text{ (nm)} = \frac{1239.8}{\Delta E_\text{gap} \text{ (eV)}}$$

:::{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: fragmento del log mostrando las líneas Alpha occ. y Alpha virt. con el HOMO
y LUMO marcados]
:::

---

### Parte B: Cálculo TD-DFT del espectro UV

#### Paso B1: Configurar el cálculo TD-DFT

Sobre la geometría ya optimizada (o partir del archivo `.chk`):

1. En GaussView: **File → Open** → abre el `.log` de la optimización.
2. Ve a **Calculate → Gaussian Calculation Setup**.
3. Pestaña **Job Type** → **Energy**.
4. Pestaña **Method** (mismo que antes: B3LYP/6-311G, mult=1).
5. En **Additional Keywords** escribe: `td scrf=(solvent=acetonitrile) geom=connectivity`

:::{tip}
La keyword `td` es todo lo que necesitas para activar TD-DFT. Gaussian calcula
automáticamente los primeros 3 estados excitados. Si necesitas más, escribe `td=(nstates=10)`.
:::

:::{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: pestaña Additional Keywords del Gaussian Calculation Setup con `td
scrf=(solvent=acetonitrile)` escrito]
:::

6. Guarda como `acetona_MeCN_td.gjf` y lanza.

#### Paso B2: Leer los estados excitados

En el `.log`, busca: `Excited State`

Verás un bloque como este (ejemplo del log de referencia procesado):

```
 Excited State   1:      Singlet-A"     4.2871 eV  289.23 nm  f=0.0003
       8 -> 9         0.70711
```

| Campo | Significado |
|-------|-------------|
| `Singlet-A"` | Simetría del estado excitado |
| `4.2871 eV` | Energía de la transición |
| `289.23 nm` | Longitud de onda de absorción |
| `f=0.0003` | Fuerza del oscilador (intensidad relativa) |
| `8 -> 9` | Orbital de origen → orbital de destino |

:::{tip}
Para identificar si es n→π* o π→π*, visualiza los orbitales 8 y 9 en GaussView:
**Results → MOs**. Si el orbital de origen tiene forma de par solitario en el oxígeno →
transición n→π*.
:::

:::{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: fragmento del log mostrando los primeros estados excitados con sus energías,
longitudes de onda y fuerzas del oscilador]
:::

#### Paso B3: Visualizar el espectro en GaussView

:::{tip}
Ve a **Results → UV-Vis**. GaussView representa el espectro calculado como barras
(una por cada estado excitado, con altura proporcional a f) y como una envolvente
gaussiana. Identifica la banda n→π* (f muy pequeño, ~290 nm) y la π→π* (f mayor,
<250 nm).
:::

:::{admonition} 📸 Captura de pantalla
:class: captura
[CAPTURA: ventana Results → UV-Vis de GaussView mostrando el espectro de la acetona
en MeCN con las dos bandas identificadas]
:::

---

### Parte C: Efecto del disolvente (5 disolventes)

Repite el cálculo TD-DFT cambiando únicamente el disolvente en `scrf=`:

| Disolvente | Keyword |
|-----------|---------|
| Vacío | *(no escribir `scrf=`)* |
| Ciclohexano | `scrf=(solvent=cyclohexane)` |
| Cloroformo | `scrf=(solvent=chloroform)` |
| Etanol | `scrf=(solvent=ethanol)` |
| Acetonitrilo | `scrf=(solvent=acetonitrile)` |
| Agua | `scrf=(solvent=water)` |

Guarda cada cálculo con un nombre diferente:
`acetona_vacio_td.gjf`, `acetona_ciclohexano_td.gjf`, etc.

### Parte D: Otras cetonas (5 cetonas)

Repite el procedimiento completo (opt + TD-DFT) para cada cetona:

| Cetona | Fórmula |
|--------|---------|
| Acetona | CH₃-CO-CH₃ |
| Cloruro de acetilo | CH₃-CO-Cl |
| Acetofenona | CH₃-CO-C₆H₅ |
| Ácido acético | CH₃-CO-OH |
| Metil-etil-cetona | CH₃-CO-CH₂CH₃ |

:::{warning}
Cada cetona debe optimizarse en cada disolvente antes del cálculo TD-DFT.
En total son 25 cálculos de optimización + 25 TD-DFT = 50 cálculos.
Organiza los archivos en subcarpetas por cetona para no confundirlos.
:::

---

## Resultados

### Tabla A: Gap HOMO-LUMO (acetona)

| Disolvente | HOMO (Ha) | LUMO (Ha) | Gap (Ha) | Gap (eV) | λ estimada (nm) |
|-----------|:---------:|:---------:|:--------:|:--------:|:---------------:|
| Vacío | — | — | — | — | — |
| Ciclohexano | — | — | — | — | — |
| Acetonitrilo | — | — | — | — | — |
| Agua | — | — | — | — | — |

### Tabla B: λ n→π* calculada por TD-DFT vs. experimental (acetona)

| Disolvente | λ calculada (nm) | f | λ experimental (nm) | Error (nm) |
|-----------|:----------------:|:---:|:-------------------:|:----------:|
| Ciclohexano | — | — | 279 | — |
| Agua | — | — | 264 | — |
| Acetonitrilo | — | — | — | — |
| Etanol | — | — | — | — |
| Cloroformo | — | — | — | — |

### Tabla C: λ n→π* por cetona (en acetonitrilo)

| Cetona | λ calculada (nm) | f | Comentario |
|--------|:----------------:|:---:|------------|
| Acetona | — | — | |
| Cloruro de acetilo | — | — | |
| Acetofenona | — | — | |
| Ácido acético | — | — | |
| Metil-etil-cetona | — | — | |

:::{note}
[TEXTO HUMANO: instrucciones de recogida de datos — dónde copiar los valores de λ y f
desde el log o desde la ventana Results → UV-Vis de GaussView.]
:::

---

## Preguntas y pruebas

:::{note}
[TEXTO HUMANO: preguntas de reflexión. Propuesta:]

[PROPUESTA:
1. ¿Cuál es la diferencia entre la λ estimada por el gap HOMO-LUMO y la obtenida por
   TD-DFT? ¿En qué sentido falla la estimación del gap?
2. ¿Cómo cambia la λ de la banda n→π* al pasar de ciclohexano a agua? ¿Es un
   desplazamiento al azul o al rojo? ¿Por qué?
3. ¿Qué sustituyente en R produce el mayor desplazamiento de λ respecto a la acetona?
   ¿Lo puedes relacionar con la capacidad de ese sustituyente para extender la
   conjugación o estabilizar el par solitario?
4. La banda n→π* tiene f ≈ 0.0003 y la π→π* tiene f > 0.1. ¿Qué significa esto para
   la intensidad observada en un espectro real?
5. Si mides el espectro UV de la acetona en etanol y observas que la banda n→π*
   aparece a 268 nm, ¿está de acuerdo con tu cálculo TD-DFT?
]
:::

---

## Bibliografía

:::{note}
[TEXTO HUMANO: añadir referencia al manual interno de la asignatura si existe.]
:::

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018.
  Cap. 13 (Espectroscopía electrónica).
- Casida, M. E. *Time-Dependent Density Functional Theory for Molecules*. In *Recent
  Advances in Density Functional Methods*; World Scientific, 1995.
- NIST Chemistry WebBook, https://webbook.nist.gov — espectros UV-Vis experimentales.

---

::::{dropdown} 🚀 Para ir más lejos *(opcional — solo si terminas antes de tiempo)*
:color: success
:icon: rocket

Esta sección es completamente **opcional** y no entra en la nota.

### Simular el espectro UV con ensanchamiento gaussiano

El espectro que muestra GaussView usa barras discretas (una por estado excitado).
Un espectro experimental muestra bandas anchas porque cada transición está ensanchada
por las vibraciones moleculares. Podemos simular este efecto aplicando una función
gaussiana centrada en cada λ calculada y sumándolas todas.

:::{note}
[TEXTO HUMANO: instrucciones para esta extensión — cómo exportar la lista de estados
excitados desde el log (tabla λ, f), cómo representar el espectro convolucionado en
LibreOffice Calc o Python, y cómo comparar visualmente con el espectro experimental
del NIST.]
:::

### Comparar gap HOMO-LUMO vs. TD-DFT para las 5 cetonas

Representa en un gráfico el λ estimado por HOMO-LUMO vs. el λ calculado por TD-DFT
para las 5 cetonas en acetonitrilo. ¿Es la desviación sistemática? ¿Hay alguna cetona
donde el gap HOMO-LUMO sea una buena aproximación?
::::
