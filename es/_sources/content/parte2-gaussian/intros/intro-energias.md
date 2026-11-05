# Energías y unidades en Gaussian

## Introducción

Los cálculos de estructura electrónica proporcionan diversas magnitudes numéricas relativas a la estabilidad, la reactividad y las vibraciones moleculares. El archivo de salida de Gaussian recopila estos datos utilizando convenciones y unidades atómicas propias de la mecánica cuántica. Interpretar adecuadamente estos resultados exige distinguir entre la energía total, las energías de los orbitales individuales y las frecuencias vibracionales, aplicando las conversiones necesarias a electronvoltios o unidades termodinámicas.

## La energía total: qué es y por qué es negativa

La energía total calculada por Gaussian comprende cuatro contribuciones físicas: la energía cinética de los electrones, la atracción electrostática entre electrones y núcleos, la repulsión coulómbica entre electrones y la repulsión electrostática internuclear. En sistemas atómicos y moleculares estables, las fuerzas atractivas predominan sobre las repulsivas, por lo que la energía total es negativa respecto al estado de partículas aisladas en reposo. Este valor se muestra en la línea `SCF Done` del archivo `.log` (o en el encabezado del método correlacionado correspondiente) y se expresa siempre en unidades atómicas (hartrees).

:::{admonition} Nota
:class: note
En mecánica cuántica molecular, el cero de energía se sitúa en el estado de núcleos y electrones infinitamente separados y en reposo ($V = 0$ cuando $r \rightarrow \infty$). La formación de un enlace o de un átomo ligado libera energía, lo que sitúa el valor de `SCF Done` en números negativos. Cuanto más negativo sea este valor, mayor es la estabilidad del sistema frente a sus componentes aislados.
:::

## Unidades: Hartrees, eV y kcal/mol

Gaussian expresa las energías electrónicas en unidades atómicas denominadas hartrees (Ha). Para relacionar estos valores con datos experimentales o termodinámicos empleamos factores de conversión estándar: un hartree equivale a 27.21 electronvoltios, 627.51 kilocalorías por mol o 2625.5 kilojulios por mol. En química, los electronvoltios (eV) se usan habitualmente para potenciales de ionización, afinidades electrónicas y diferencias HOMO–LUMO. Las kilocalorías por mol (kcal/mol) y los kilojulios por mol (kJ/mol) son las unidades de referencia para barreras de activación, calores de reacción y diferencias de energía entre confórmeros.

| De | A | Factor |
|----|---|--------|
| Ha | eV | × {{ha_to_ev}} |
| Ha | kcal/mol | × {{ha_to_kcal}} |

:::{admonition} Advertencia
:class: warning
Nunca comparar dos energías en unidades distintas. Convertir siempre antes de restar.
:::

## Diferencias de energía: lo que realmente importa

La energía absoluta en hartrees depende del convenio de referencia (partículas separadas en el infinito) y no se mide directamente en el laboratorio. Por ello, nunca deben compararse energías absolutas obtenidas con métodos o bases distintas. La magnitud físicamente relevante en química es siempre la diferencia relativa de energía ($\Delta E$) entre dos estados o geometrías del mismo sistema calculadas al mismo nivel de teoría. En estas prácticas, cualquier análisis termodinámico, barrera de rotación o curva de potencial lo expresamos como un incremento relativo respecto a una estructura de referencia.

## Energías orbitales: no confundir con la energía total

Los autovalores obtenidos al diagonalizar la matriz de Fock corresponden a las energías de los orbitales individuales, tabuladas en el archivo `.log` bajo las etiquetas `Alpha occ. eigenvalues` (orbitales ocupados) y `Alpha virt. eigenvalues` (orbitales virtuales o desocupados). Estos valores no representan la energía total del sistema. Sumar las energías de todos los orbitales ocupados generaría una sobreestimación física grave de la energía real, ya que la repulsión entre electrones se contabilizaría dos veces. Por este motivo, la energía total se calcula mediante una expresión independiente y se muestra por separado en la línea `SCF Done`.

## Frecuencias vibracionales: un resultado distinto

El cálculo de frecuencias (`freq`) determina los modos normales de vibración molecular expresados en centímetros inversos ($\text{cm}^{-1}$), una magnitud física con dimensiones distintas a los hartrees de la energía total. Estos valores aparecen en el archivo `.log` en las líneas `Frequencies --`. La presencia de una frecuencia imaginaria (que Gaussian muestra como un número negativo) indica que la estructura optimizada no corresponde a un mínimo real en la superficie de energía potencial, sino a un estado de transición o punto de silla. En ese caso, la geometría debe corregirse y reoptimizarse antes de analizar cualquier otra propiedad fisicoquímica.

:::{admonition} Advertencia
:class: warning
Si aparecen frecuencias negativas en el log, la geometría no ha convergido a un mínimo real. Hay que reoptimizar antes de continuar.
:::

---

## Bibliografía

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
