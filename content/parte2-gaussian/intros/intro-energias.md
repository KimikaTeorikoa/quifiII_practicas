# Energías y unidades en Gaussian

## Introducción

Los cálculos de estructura electrónica proporcionan una amplia variedad de valores numéricos asociados a la estabilidad, la reactividad y las vibraciones moleculares. El archivo de salida generado por Gaussian 16 recopila estas magnitudes físicas utilizando convenciones teóricas y unidades atómicas propias del formalismo mecanocuántico. La adecuada lectura de estos resultados requiere diferenciar con claridad entre la energía electrónica total, los autovalores orbitales individuales y las frecuencias vibracionales, aplicando las conversiones correctas hacia electronvoltios o unidades termodinámicas.

---

## La energía total: qué es y por qué es negativa

La energía total reportada por Gaussian agrupa cuatro contribuciones físicas: la energía cinética de los electrones, la atracción electrostática entre los electrones y los núcleos, la repulsión coulómbica entre pares de electrones y la repulsión electrostática entre los núcleos. En sistemas atómicos y moleculares estables, la magnitud de las interacciones atractivas supera a la de los términos repulsivos, por lo que la energía electrónica total adopta valores negativos respecto al estado de partículas aisladas en reposo. Este valor global se notifica en el archivo de salida bajo la línea `SCF Done` en cálculos Hartree-Fock y DFT, o en el encabezado correspondiente al método correlacionado ejecutado. En todos los casos, la magnitud se expresa numéricamente en unidades atómicas de energía (hartrees).

:::{admonition} Nota
:class: note
El convenio mecanocuántico fija el cero de energía en el estado de partículas aisladas en reposo y a distancia infinita ($V = 0$ cuando $r \rightarrow \infty$). En un átomo o molécula estable, la atracción electrostática entre los electrones y los núcleos supera a las repulsiones mutuas, situando la energía total en valores negativos. Un valor de `SCF Done` con mayor magnitud negativa indica una estabilización termodinámica más pronunciada respecto a los componentes infinitamente separados.
:::

---

## Unidades: Hartrees, eV y kcal/mol

El motor de cálculo de Gaussian reporta de manera sistemática todas las energías electrónicas en unidades atómicas denominadas hartrees (Ha). Para conectar estos autovalores teóricos con la escala de las medidas de laboratorio es imprescindible aplicar factores de conversión estándar: un hartree equivale a 27,21 electronvoltios, 627,51 kilocalorías por mol o 2625,5 kilojulios por mol. En el análisis químico, los electronvoltios se emplean de forma preferente para expresar potenciales de ionización, afinidades electrónicas y diferencias energéticas entre orbitales HOMO y LUMO. Por su parte, las kilocalorías por mol y los kilojulios por mol constituyen las unidades estándar para cuantificar barreras de activación, calores de reacción y diferencias termodinámicas de estabilidad entre confórmeros. Conocer el orden de magnitud de cada propiedad evita errores numéricos graves al transferir los datos del archivo de salida hacia los informes de prácticas.

| De | A | Factor |
|----|---|--------|
| Ha | eV | × {{ha_to_ev}} |
| Ha | kcal/mol | × {{ha_to_kcal}} |

:::{warning}
Nunca comparar dos energías en unidades distintas. Convertir siempre antes de restar.
:::

---

## Diferencias de energía: lo que realmente importa

El valor numérico absoluto de la energía total reportado en hartrees depende del convenio de referencia adoptado ($V = 0$ a separación infinita) y carece de un significado experimental directo. Por este motivo, no resulta válido comparar valores absolutos obtenidos con métodos mecanocuánticos o conjuntos de base diferentes. La magnitud observable relevante en química es siempre la diferencia relativa de energía ($\Delta E$) entre dos estados o dos disposiciones geométricas del mismo sistema calculadas con idéntico nivel de teoría. En las sesiones del curso, todos los análisis termodinámicos, alturas de barrera o curvas de potencial se expresan sistemáticamente como incrementos $\Delta E$ calculados respecto a una estructura de referencia.

---

## Energías orbitales: no confundir con la energía total

Los autovalores calculados al diagonalizar la matriz de Fock corresponden a las energías orbitales monoelectrónicas, tabuladas en el archivo de salida bajo los epígrafes `Alpha occ. eigenvalues` para los niveles ocupados y `Alpha virt. eigenvalues` para los desocupados. Estos autovalores no representan la energía total del sistema bajo estudio. Sumar directamente las energías de todos los orbitales ocupados generaría una sobreestimación física grave de la energía electrónica, debido a que el término de repulsión coulómbica entre cada par de electrones se computaría por duplicado. Por esta razón termodinámica, la energía electrónica total del sistema se evalúa mediante una expresión independiente y se notifica de forma separada en la línea `SCF Done` del archivo `.log`.

---

## Frecuencias vibracionales: un resultado distinto

Los cálculos de frecuencias vibracionales (`freq`) reportan los valores correspondientes a los modos normales de vibración molecular expresados en centímetros inversos ($\text{cm}^{-1}$), magnitud física y dimensionalmente distinta a los hartrees de la energía total. Estos valores se localizan en el archivo de salida `.log` bajo los encabezados identificados como `Frequencies --`. La presencia de una frecuencia imaginaria, indicada en Gaussian como un valor numérico negativo, señala que la estructura optimizada no corresponde a un mínimo real en la superficie de energía potencial, sino a un punto de silla. En esa situación, la geometría molecular debe revisarse y reoptimizarse antes de extraer o analizar cualquier otra propiedad fisicoquímica.

:::{warning}
Si ves frecuencias negativas en el log, la geometría no ha convergido correctamente. Avisar al profesor.
:::

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
