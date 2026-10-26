# Energías y unidades en Gaussian

<!-- ============================================================
     VERSIÓN ESQUEMÁTICA — NO ES TEXTO FINAL
     Este archivo contiene el esqueleto de contenidos párrafo a
     párrafo. Cada sección indica qué debe contener, longitud
     orientativa y dónde van figuras. NO editar como texto final
     hasta que el esquema esté aprobado por el supervisor.
     ============================================================ -->

## Introducción

Párrafo corto. Gaussian devuelve varios números: energías, frecuencias, energías
orbitales. Este archivo explica qué es cada uno, en qué unidades viene y cuándo se
usa. Sin esto los alumnos copian el número equivocado.

---

## La energía total: qué es y por qué es negativa

Párrafo medio. Qué incluye la energía electrónica total: energía cinética de los
electrones, atracción núcleo-electrón, repulsión electrón-electrón, repulsión nuclear.
Por qué siempre es negativa para sistemas estables. Dónde aparece en el log: línea
`SCF Done` o `E(RHF)=`.

:::{admonition} Intuición
:class: intuicion
[TEXTO HUMANO: analogía — una bola en un pozo tiene menos energía que fuera; cuanto
más profundo el pozo, más negativa la energía]
:::

---

## Unidades: Hartrees, eV y kcal/mol

Párrafo medio + tabla. Gaussian trabaja en Hartrees. Para comparar con experimento o
con otras disciplinas hay que convertir.

| De | A | Factor |
|----|---|--------|
| Ha | eV | × {{ha_to_ev}} |
| Ha | kcal/mol | × {{ha_to_kcal}} |

Cuándo usar cada una: eV para propiedades electrónicas (IE, HOMO/LUMO), kcal/mol para
barreras y diferencias de energía, Ha en el log de Gaussian.

:::{warning}
Nunca comparar dos energías en unidades distintas. Convertir siempre antes de restar.
:::

---

## Diferencias de energía: lo que realmente importa

Párrafo corto. La energía absoluta en Ha no tiene significado físico directo — lo que
importa es la diferencia entre dos geometrías o dos estados. Por eso en las prácticas
siempre se trabaja con ΔE respecto a un punto de referencia.

---

## Energías orbitales: no confundir con la energía total

Párrafo corto. Los autovalores de Fock (energías del HOMO, LUMO...) son distintos de
la energía total. Aparecen en una sección diferente del log. Unidades: también
Hartrees. La energía total no es la suma de las energías orbitales.

---

## Frecuencias vibracionales: un resultado distinto

Párrafo corto. Los cálculos `freq` devuelven frecuencias en cm⁻¹, no en Ha. Son un
tipo de resultado completamente distinto — no son energías sino modos de vibración.
Dónde aparecen en el log: líneas `Frequencies --`. Un valor negativo (frecuencia
imaginaria) indica que la geometría no es un mínimo real.

:::{warning}
Si ves frecuencias negativas en el log, la geometría no ha convergido correctamente.
Avisar al profesor.
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional — libro de texto de química cuántica o equivalente]`
