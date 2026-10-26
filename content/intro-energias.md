# Energías y unidades en Gaussian

## Introducción

:::{note}
[TEXTO HUMANO: Explicar la variedad de magnitudes que devuelve Gaussian (energía total, autovalores orbitales, frecuencias) y la importancia de identificar las unidades correspondientes para prevenir confusiones numéricas en el informe. Longitud: 3-4 frases.]
:::

---

## La energía total: qué es y por qué es negativa

:::{note}
[TEXTO HUMANO: Desglosar las contribuciones que integran la energía total (cinética electrónica, atracción núcleo-electrón, repulsión electrón-electrón y repulsión internuclear), justificando el signo negativo como indicador de estabilidad cuántica respecto a partículas separadas e indicando la etiqueta de búsqueda en el log. Longitud: 4-5 frases.]
[ECUACIÓN: componentes de la energía molecular total, $E_{\text{total}} = \langle\hat{T}_e\rangle + \langle\hat{V}_{Ne}\rangle + \langle\hat{V}_{ee}\rangle + V_{NN}$]
:::

:::{admonition} 💡 Intuición
:class: intuicion
[TEXTO HUMANO: Analogía de una esfera en el fondo de un pozo gravitatorio, cuya energía disminuye por debajo de cero a medida que el pozo se hace más profundo y estable. Longitud: 2-3 frases.]
:::

---

## Unidades: Hartrees, eV y kcal/mol

:::{note}
[TEXTO HUMANO: Presentar las unidades atómicas (Hartrees) propias del motor de cálculo de Gaussian y definir los factores de conversión necesarios para comparar con datos espectroscópicos o termodinámicos. Longitud: 3-4 frases.]
:::

| De | A | Factor |
|---|---|---|
| Ha | eV | × {{ha_to_ev}} |
| Ha | kcal/mol | × {{ha_to_kcal}} |

:::{note}
[TEXTO HUMANO: Pautas de asignación de unidades según el contexto: eV para potenciales de ionización y transiciones ópticas, kcal/mol para barreras de activación y diferencias energéticas relativas, y Ha para lectura directa del archivo de salida. Longitud: 2-3 frases.]
:::

:::{warning}
Nunca comparar dos energías en unidades distintas. Convertir siempre antes de restar.
:::

---

## Diferencias de energía: lo que realmente importa

:::{note}
[TEXTO HUMANO: Subrayar que los valores absolutos de energía carecen de significación termodinámica directa y que la magnitud observable corresponde invariablemente a diferencias energéticas respecto a un estado o geometría de referencia. Longitud: 3-4 frases.]
[ECUACIÓN: energía potencial relativa respecto a una referencia, $\Delta E = E - E_{\text{ref}}$]
:::

---

## Energías orbitales: no confundir con la energía total

:::{note}
[TEXTO HUMANO: Diferenciar los autovalores monoelectrónicos de Fock (HOMO, LUMO) frente a la energía total del sistema, recordando que la suma de energías orbitales no reproduce la energía molecular global por contar doblemente la repulsión coulómbica. Longitud: 3-4 frases.]
:::

---

## Frecuencias vibracionales: un resultado distinto

:::{note}
[TEXTO HUMANO: Aclarar que las frecuencias reportadas en cm⁻¹ en cálculos de tipo freq corresponden al movimiento vibracional y no a energías electrónicas, alertando sobre el significado de frecuencias imaginarias como indicio de geometrías no estacionarias o estados de transición. Longitud: 4-5 frases.]
[ECUACIÓN: frecuencia armónica de vibración molecular, $\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}$]
:::

:::{warning}
Si ves frecuencias negativas en el log, la geometría no ha convergido correctamente. Avisar al profesor.
:::

---

## Bibliografía

- `[TEXTO HUMANO: manual de la asignatura si existe]`
- Gaussian 16, Revision A.03, M. J. Frisch et al., Gaussian, Inc., Wallingford CT, 2016.
- `[TEXTO HUMANO: referencia adicional : libro de texto de química cuántica o equivalente)]`
