# Energías y unidades en Gaussian

## Introducción

:::{note}
[TEXTO HUMANO: Gaussian devuelve varios números: energías, frecuencias, energías orbitales. Este archivo explica qué es cada uno, en qué unidades viene y cuándo se usa. Sin esto los alumnos copian el número equivocado. (Longitud: 3-4 frases)]
:::

---

## La energía total: qué es y por qué es negativa

:::{note}
[TEXTO HUMANO: Qué incluye la energía electrónica total: energía cinética de los electrones, atracción núcleo-electrón, repulsión electrón-electrón, repulsión nuclear. Por qué siempre es negativa para sistemas estables. Dónde aparece en el log: línea `SCF Done` o `E(RHF)=`. (Longitud: 4-5 frases)]
:::

:::{admonition} Intuición
:class: intuicion  [revisar de nuevo]
Imagina una pelota que rueda hacia el interior de un pozo seco: si tomas el nivel del suelo como altura cero, la pelota tendrá una cota negativa mientras permanezca atrapada en el fondo. En química cuántica el cero de referencia corresponde a núcleos y electrones completamente separados e inmóviles a distancia infinita, de modo que cualquier enlace o atracción los sitúa por debajo de ese umbral. Por esta razón, la energía de `SCF Done` en tu archivo `.log` siempre llevará un signo negativo delante. Cuanto mayor sea su valor absoluto, más hondo será el pozo energético y más estable resultará la molécula que acabas de calcular.
:::

---

## Unidades: Hartrees, eV y kcal/mol

:::{note}
[TEXTO HUMANO: Gaussian trabaja en Hartrees. Para comparar con experimento o con otras disciplinas hay que convertir. Cuándo usar cada una: eV para propiedades electrónicas (IE, HOMO/LUMO), kcal/mol para barreras y diferencias de energía, Ha en el log de Gaussian. (Longitud: 4-5 frases)]
:::

| De | A | Factor |
|----|---|--------|
| Ha | eV | × {{ha_to_ev}} |
| Ha | kcal/mol | × {{ha_to_kcal}} |

:::{warning}
Nunca comparar dos energías en unidades distintas. Convertir siempre antes de restar.
:::

---

## Diferencias de energía: lo que realmente importa

:::{note}
[TEXTO HUMANO: La energía absoluta en Ha no tiene significado físico directo, lo que importa es la diferencia entre dos geometrías o dos estados. Por eso en las prácticas siempre se trabaja con ΔE respecto a un punto de referencia. (Longitud: 3-4 frases)]
:::

---

## Energías orbitales: no confundir con la energía total

:::{note}
[TEXTO HUMANO: Los autovalores de Fock (energías del HOMO, LUMO...) son distintos de la energía total. Aparecen en una sección diferente del log. Unidades: también Hartrees. La energía total no es la suma de las energías orbitales. (Longitud: 3-4 frases)]
:::

---

## Frecuencias vibracionales: un resultado distinto

:::{note}
[TEXTO HUMANO: Los cálculos `freq` devuelven frecuencias en cm⁻¹, no en Ha. Son un tipo de resultado completamente distinto, no son energías sino modos de vibración. Dónde aparecen en el log: líneas `Frequencies --`. Un valor negativo (frecuencia imaginaria) indica que la geometría no es un mínimo real. (Longitud: 4-5 frases)]
:::

:::{warning}
Si ves frecuencias negativas en el log, la geometría no ha convergido correctamente. Avisar al profesor.
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional (libro de texto de química cuántica o equivalente)]`
