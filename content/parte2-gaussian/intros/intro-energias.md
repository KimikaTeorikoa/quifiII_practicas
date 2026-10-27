# Energías y unidades en Gaussian

## Introducción

Los cálculos de estructura electrónica proporcionan una amplia variedad de valores numéricos asociados a la estabilidad, la reactividad y las vibraciones moleculares. El archivo de salida generado por Gaussian 16 recopila estas magnitudes físicas utilizando convenciones teóricas y unidades atómicas propias del formalismo mecanocuántico. La adecuada lectura de estos resultados requiere diferenciar con claridad entre la energía electrónica total, los autovalores orbitales individuales y las frecuencias vibracionales, aplicando las conversiones correctas hacia electronvoltios o unidades termodinámicas.

---

## La energía total: qué es y por qué es negativa

:::{note}
[TEXTO HUMANO: Qué incluye la energía electrónica total: energía cinética de los electrones, atracción núcleo-electrón, repulsión electrón-electrón, repulsión nuclear. Por qué siempre es negativa para sistemas estables. Dónde aparece en el log: línea `SCF Done` o `E(RHF)=`. (Longitud: 4-5 frases)]
:::

:::{admonition} Nota
:class: note
El convenio mecanocuántico fija el cero de energía en el estado de partículas aisladas en reposo y a distancia infinita ($V = 0$ cuando $r \rightarrow \infty$). En un átomo o molécula estable, la atracción electrostática entre los electrones y los núcleos supera a las repulsiones mutuas, situando la energía total en valores negativos. Un valor de `SCF Done` con mayor magnitud negativa indica una estabilización termodinámica más pronunciada respecto a los componentes infinitamente separados.
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

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
