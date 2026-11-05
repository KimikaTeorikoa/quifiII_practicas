# Referencia de ecuaciones — M_QUIFIS2

Fuente de verdad para todas las expresiones matemáticas del libro.
Versión: 1.0.0 | 2026-10-25

Las prácticas copian estas ecuaciones tal cual. Si cambia un factor de conversión o
una definición, se corrige aquí y se propaga.

---

## 1. Conversiones de unidades

### 1.1 Hartree a electronvoltio

$$
1 \, \text{Ha} = {{ha_to_ev}} \, \text{eV}
$$

### 1.2 Hartree a kcal/mol

$$
1 \, \text{Ha} = {{ha_to_kcal}} \, \text{kcal mol}^{-1}
$$

### 1.3 Hartree a kJ/mol

$$
1 \, \text{Ha} = 2625.50 \, \text{kJ mol}^{-1}
$$

### 1.4 Número de onda a electronvoltio

$$
1 \, \text{cm}^{-1} = 1.23984 \times 10^{-4} \, \text{eV}
$$

### 1.5 Longitud de onda a energía (relación de Planck-Einstein)

$$
E \, (\text{eV}) = \frac{1239.8}{\lambda \, (\text{nm})}
$$

Equivalentemente:

$$
\lambda \, (\text{nm}) = \frac{1239.8}{E \, (\text{eV})}
$$

---

## 2. Energía de ionización (P2-A)

### 2.1 Método de diferencia de energías totales

Sea $E(N)$ la energía total del átomo neutro y $E(N-1)$ la del catión (un electrón menos):

$$
\text{IE} = E(N-1) - E(N)
$$

El resultado en Hartrees se convierte a eV multiplicando por ${{ha_to_ev}}$.

### 2.2 Teorema de Koopmans

En el marco Hartree-Fock, la energía de ionización del orbital $i$ es igual a la
energía orbital cambiada de signo:

$$
\text{IE}_i \approx -\varepsilon_i
$$

Para el electrón más débilmente ligado (HOMO):

$$
\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}
$$

:::{warning}
El teorema de Koopmans ignora la relajación orbital tras la ionización y la correlación
electrónica. Da valores sistemáticamente superiores a los experimentales en un 10–20 %.
:::

---

## 3. Gap HOMO-LUMO y longitud de onda estimada (P2-D)

### 3.1 Gap en electronvoltios

$$
\Delta E_{\text{gap}} \, (\text{eV})
  = \bigl(\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}\bigr)
    \times {{ha_to_ev}}
$$

Los valores de $\varepsilon$ se leen del `.log` en Hartrees (ambos negativos para
sistemas estables; el LUMO tiene mayor energía, es decir, es menos negativo).

### 3.2 Longitud de onda estimada

$$
\lambda_{\text{estimada}} \, (\text{nm}) = \frac{1239.8}{\Delta E_{\text{gap}} \, (\text{eV})}
$$

:::{note}
Esta estimación asume que la primera transición electrónica corresponde directamente
al gap HOMO-LUMO. TD-DFT es más preciso porque incluye la respuesta del sistema al
campo oscilante.
:::

---

## 4. Modos normales de vibración (P2-C)

### 4.1 Número de modos normales

Para una molécula no lineal de $N$ átomos:

$$
\text{modos normales} = 3N - 6
$$

Para una molécula lineal:

$$
\text{modos normales} = 3N - 5
$$

### 4.2 Modelo armónico: frecuencia de un oscilador diatómico

$$
\tilde{\nu} = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}}
$$

donde $k$ es la constante de fuerza (N m$^{-1}$), $c$ la velocidad de la luz
($2.998 \times 10^{10}$ cm s$^{-1}$) y $\mu$ la masa reducida:

$$
\mu = \frac{m_1 \, m_2}{m_1 + m_2}
$$

:::{note}
Los alumnos no calculan $k$ ni $\mu$ a mano. Gaussian devuelve las frecuencias
directamente en cm$^{-1}$. Esta ecuación explica por qué un enlace más rígido o
átomos más ligeros vibran a mayor frecuencia.
:::

### 4.3 Regla de selección IR (criterio cualitativo)

Un modo normal es activo en IR si durante la vibración cambia el momento dipolar
eléctrico de la molécula:

$$
\left(\frac{\partial \boldsymbol{\mu}}{\partial Q_k}\right)_0 \neq \mathbf{0}
$$

donde $Q_k$ es la coordenada normal del modo $k$.

---

## 5. Superficie de energía potencial (P2-B)

### 5.1 Energía relativa en una exploración de coordenada

Para comparar puntos de la PES, se toma como referencia el mínimo calculado $E_0$:

$$
\Delta E \, (\text{kcal mol}^{-1})
  = \bigl(E_i - E_0\bigr) \times {{ha_to_kcal}}
$$

:::{warning}
P2-B está pendiente de confirmación del método y base para dihaloetanos.
No usar estas ecuaciones hasta desbloquear esa práctica.
:::
