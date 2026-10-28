# Prompts para generación de figuras SVG
# Uso: cada bloque es un prompt autocontenido para generar un SVG.
# Cuanta más información tenga el modelo, mejor será el resultado.
# Versión: 1.0.0 | 2026-10-28

---

## FIGURA 01 — Orbital 1s del helio: densidad electrónica
**Archivo destino:** `_static/figures/orbital_1s_he.svg`
**Usado en:** intro-gaussview.md, intro-hartree-fock.md

**Prompt:**
Genera un SVG científico que muestre la representación de la densidad electrónica del orbital 1s del átomo de helio. El SVG debe tener viewBox="0 0 400 400". El fondo debe ser transparente para integrarse en un Jupyter Book con modo claro y oscuro (usa CSS variables o colores que funcionen en ambos). El diagrama debe mostrar: (1) Un conjunto de círculos concéntricos con opacidad decreciente desde el centro hacia el exterior, representando isosuperficies de densidad electrónica; usa tonos azul-morado (por ejemplo stroke="#4a6fa5") con opacidad que va de 0.9 en el centro a 0.1 en el exterior, con 6 o 7 círculos. (2) Un punto o círculo pequeño relleno en el centro representando el núcleo, con etiqueta "He" en texto sans-serif pequeño. (3) Una flecha hacia fuera con la etiqueta "r" indicando la distancia radial. (4) El título de la figura en la parte inferior: "Densidad electrónica del orbital 1s" en fuente sans-serif tamaño 11. El estilo debe ser minimalista, científico, sin decoración innecesaria. No uses imágenes externas ni fuentes externas. Todo inline.

---

## FIGURA 02 — Aproximación gaussiana de un orbital STO: una vs. varias gaussianas
**Archivo destino:** `_static/figures/sto_vs_gaussianas.svg`
**Usado en:** intro-bases.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 500 320", fondo transparente) que muestre en un mismo sistema de ejes coordenados tres curvas superpuestas de la función radial de un orbital tipo s en función de la distancia r (eje x: de 0 a 5 bohrs; eje y: de 0 a 1.2 en unidades relativas). Las tres curvas son: (1) La función STO exacta (Slater Type Orbital): decaimiento exponencial suave, e^(-r), línea continua gruesa color negro o gris oscuro, etiquetada "STO (exacto)". (2) Aproximación con una sola gaussiana: e^(-alpha*r^2), decae más rápido que el STO en la cola y tiene diferente forma en el origen, línea discontinua roja, etiquetada "1 gaussiana". (3) Aproximación con tres gaussianas (STO-3G): combinación lineal de tres gaussianas con distintos exponentes que se aproxima bastante bien al STO, línea de puntos y trazos azul, etiquetada "3 gaussianas (STO-3G)". Incluir ejes con etiquetas: eje x "r (bohrs)", eje y "phi(r) (u.a.)". Leyenda en la esquina superior derecha. Estilo científico limpio, sin rellenos de área. Todo inline, sin fuentes externas.

---

## FIGURA 03 — Diagrama de niveles de orbitales HOMO/LUMO con flecha de ionización
**Archivo destino:** `_static/figures/homo_lumo_ionizacion.svg`
**Usado en:** atomos-koopmans.md

**Diseño de referencia (resultado del prototipo):**
El diagrama tiene viewBox="0 0 320 420", fondo transparente, fuente sans-serif 11px. Estructura de arriba a abajo:

- Eje vertical de energía en x=48, de y=390 a y=22, con flecha en la punta. Etiqueta "E" en cursiva arriba.
- Línea discontinua horizontal en y=50 etiquetada "e⁻ libre (E = 0)" en rojo tenue (#c0392b, stroke-dasharray). Es el cero de referencia.
- Nivel 1s en y=370: línea continua gris (#888), ancho 2. Electrones: dos flechas ↑↓ centradas (x≈130, 148), texto fill #34495e.
- Nivel 2s en y=310: ídem, con ↑↓.
- Nivel 2p en y=255: ídem, con un solo ↑ (ejemplo: átomo de capa abierta).
- Nivel HOMO en y=200: línea azul (#2471a3), ancho 3 (más gruesa que el resto). Etiqueta "HOMO" en negrita azul a la derecha (x=218). Un electrón ↑ centrado. Pequeña etiqueta "ε_HOMO" en cursiva junto a la línea (x=72, tamaño 9).
- Nivel LUMO en y=148: línea naranja (#d35400), ancho 2, stroke-dasharray="7 3". Etiqueta "LUMO" en negrita naranja a la derecha.
- Nivel virtual en y=100: línea gris muy tenue (#ccc), discontinua.
- Corchete en x=57–63 entre y=200 e y=148 con etiqueta "gap" en gris (x=35, centrado verticalmente).
- Flecha roja ascendente desde x=155, y=197 hasta x=155, y=55 con marcador de punta de flecha relleno rojo. Etiqueta "IE" en negrita roja (x=163, y=132) y "≈ −ε_HOMO" debajo (y=144/148, tamaño 9).

**Prompt:**
Genera un SVG científico (viewBox="0 0 320 420", fondo transparente) que muestre un diagrama de niveles de energía orbital para ilustrar el HOMO y el LUMO y su relación con la energía de ionización. Fuente: 'Helvetica Neue', Arial, sans-serif, tamaño base 11px.

Elementos obligatorios, de abajo arriba:
(1) Eje vertical de energía en x=48, desde y=390 hasta y=22, con punta de flecha abierta en el extremo superior. Etiqueta "E" en cursiva tamaño 13 encima de la flecha.
(2) Cuatro niveles de energía ocupados representados como líneas horizontales entre x=72 y x=210, con etiquetas a la derecha (x=218): "1s" (y=370), "2s" (y=310), "2p" (y=255), todos en gris #888, ancho de trazo 2. Sobre cada línea, un par de flechas ↑↓ (texto unicode) centradas, fill #34495e, para representar electrones apareados; en 2p solo una flecha ↑ (electrón desapareado).
(3) Nivel HOMO en y=200: línea azul #2471a3, ancho 3. Etiqueta "HOMO" en negrita azul a la derecha. Un electrón ↑ sobre la línea. Etiqueta pequeña "ε_HOMO" en cursiva junto al extremo izquierdo de la línea.
(4) Nivel LUMO en y=148: línea naranja #d35400, ancho 2, trazo discontinuo stroke-dasharray="7 3". Etiqueta "LUMO" en negrita naranja a la derecha. Sin electrones.
(5) Un nivel virtual adicional en y=100: línea gris #ccc, discontinua, sin etiqueta de nombre.
(6) Línea horizontal roja discontinua en y=50 etiquetada "e⁻ libre (E = 0)" en rojo #c0392b, tamaño 9, centrada. Representa el cero de energía de referencia (electrón libre en el infinito).
(7) Flecha roja vertical ascendente desde (x=155, y=197) hasta (x=155, y=55) con marcador de punta de flecha relleno rojo en la punta superior. Representa la ionización. Etiqueta "IE" en negrita roja tamaño 10 a la derecha de la flecha (x=163, y=132) y "≈ −ε_HOMO" en tamaño 9 debajo (x=163, y=144).
(8) Corchete vertical en x=57–63 entre y=200 e y=148 (indicando el gap HOMO-LUMO). Trazos horizontales en los extremos del corchete. Etiqueta "gap" centrada en x=35, tamaño 8.5, fill #999.

Sin fondos de relleno en los niveles. Sin imágenes externas. Sin fuentes externas. Todo inline. El resultado debe funcionar en modo claro y oscuro (usar colores que contrasten sobre fondo blanco y negro).

---

## FIGURA 04 — Diagrama de flujo del ciclo SCF
**Archivo destino:** `_static/figures/ciclo_scf.svg`
**Usado en:** intro-hartree-fock.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 300 520", fondo transparente) con un diagrama de flujo vertical del ciclo SCF (Self-Consistent Field) de Hartree-Fock. El flujo debe tener exactamente estos nodos en orden vertical: (1) Rectángulo redondeado: "Geometría y base de funciones". (2) Rectángulo redondeado: "Estimación inicial de orbitales (guess)". (3) Rectángulo redondeado: "Construir matriz de Fock F". (4) Rectángulo redondeado: "Resolver FC = SCe". (5) Rombo de decisión: "¿Converge?" con dos salidas: "No" apunta con flecha de vuelta al nodo 3 (por la izquierda), "Sí" continúa hacia abajo. (6) Rectángulo redondeado: "Orbitales y energías finales". Las flechas deben ser negras o gris oscuro. Los nodos deben tener fondo blanco semitransparente con borde gris, o bien usar stroke con fill light. Fuente sans-serif tamaño 10. El bucle de retorno del "No" debe ser una flecha curva o quebrada visible a la izquierda. Todo inline, sin fuentes externas.

---

## FIGURA 05 — Curva de energía potencial 1D con mínimo, barrera y asíntota
**Archivo destino:** `_static/figures/pes_1d_esquema.svg`
**Usado en:** moleculas-pes.md, intro-born-oppenheimer.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 500 340", fondo transparente) que muestre una curva de energía potencial unidimensional esquemática (tipo Morse) en función de la coordenada de reacción o distancia internuclear. El diagrama debe incluir: (1) Ejes cartesianos con eje x etiquetado "Coordenada de reacción" (o "R (distancia internuclear)") y eje y etiquetado "Energía potencial E". (2) La curva principal: en la zona izquierda sube steeply (pared repulsiva), pasa por un mínimo bien pronunciado (pozo de potencial), luego tiene una barrera de activación (un máximo local intermedio si se quiere mostrar una reacción), y finalmente se aplana hacia una asíntota horizontal a la derecha etiquetada "Disociación / reactivos separados". La curva debe ser suave y continua, dibujada con path de SVG, color azul marino o negro. (3) Anotaciones con flechas: "mínimo" señalando el punto más bajo de la curva; "barrera de activación" señalando el máximo; "asíntota de disociación" señalando la parte plana de la derecha. (4) Línea horizontal discontinua a la altura del mínimo para mostrar De (energía de disociación) con una flecha de doble punta vertical etiquetada "De". (5) Tres o cuatro puntos numerados sobre la curva con círculos pequeños, representando pasos sucesivos de optimización de geometría convergiendo al mínimo, etiquetados "1, 2, 3...". Estilo limpio, científico. Todo inline.

---

## FIGURA 06 — Proyección de Newman de un dihaloetano: anti, gauche, eclipsado
**Archivo destino:** `_static/figures/newman_dihaloetano.svg`
**Usado en:** moleculas-pes.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 540 220", fondo transparente) que muestre tres proyecciones de Newman de un 1,2-dihaloetano (por ejemplo, 1,2-dicloroetano con sustituyentes X = Cl) en las tres conformaciones principales, dispuestas horizontalmente de izquierda a derecha con etiquetas debajo. Cada proyección de Newman se dibuja así: un círculo exterior (el carbono trasero), tres líneas desde el borde del círculo hacia el exterior representando los tres sustituyentes del carbono trasero, y tres líneas desde el centro del círculo (el carbono delantero) hacia el exterior o hacia el borde. Los sustituyentes son: cada carbono tiene un X (halógeno) y dos H. Las tres conformaciones son: (1) "Anti" (180°): los dos X están en posiciones opuestas diametralmente. (2) "Gauche" (60°): los dos X forman un ángulo de 60° entre sí. (3) "Eclipsado" (0°): los dos X se superponen exactamente. Cada proyección tiene debajo su etiqueta de conformación y el ángulo diedro entre paréntesis. Los átomos X se dibujan como círculos rellenos verde oliva o amarillo mostaza, los H como texto "H". El estilo debe ser el estándar de química orgánica para proyecciones de Newman. Todo inline, sin fuentes externas.

---

## FIGURA 07 — Diagrama de parámetros geométricos moleculares: distancia, ángulo, diedro
**Archivo destino:** `_static/figures/geometria_molecular.svg`
**Usado en:** intro-born-oppenheimer.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 520 320", fondo transparente) que ilustre los tres parámetros geométricos que definen la estructura de una molécula: distancia de enlace, ángulo de enlace y ángulo diedro. El diagrama debe mostrar una cadena lineal de cuatro átomos A-B-C-D dispuestos en perspectiva ligera (no completamente en línea recta, sino con una ligera curvatura para que el ángulo ABC sea visible). Coordenadas aproximadas: A en (80, 200), B en (200, 150), C en (320, 190), D en (440, 120). Cada átomo es un círculo de radio 18 px con relleno: A y D en #5b8dd9 (azul), B y C en #888888 (gris carbono). Líneas de enlace en negro, stroke-width 2. Etiquetas de los átomos (A, B, C, D) en sans-serif 12 px, color blanco, centradas en el círculo. Anotaciones: (1) DISTANCIA: flecha de doble punta horizontal entre A y B en color #c0392b (rojo), desplazada 25 px por encima de la línea de enlace; etiqueta "d(A-B) [Å]" en #c0392b, tamaño 11. (2) ÁNGULO: arco de arco que representa el ángulo en el vértice B entre los enlaces A-B y B-C; arco en #27ae60 (verde), radio 35 px desde B; etiqueta "θ(ABC) [°]" en #27ae60, tamaño 11, colocada en el interior del arco. (3) DIEDRO: dibuja un arco elíptico alrededor del enlace B-C que sugiera una rotación torsional; usa una flecha curva en #8e44ad (morado) que rodee el enlace B-C, similar a una flecha de rotación en perspectiva; etiqueta "φ(ABCD) [°]" en #8e44ad, tamaño 11. Añade tres pequeñas leyendas en la parte inferior del SVG: "distancia de enlace", "ángulo de enlace", "ángulo diedro", cada una precedida de un cuadrado de color del anotador correspondiente (rojo, verde, morado). Estilo científico, fuente sans-serif, sin rellenos de fondo en las anotaciones. Todo inline, sin fuentes externas.

---

## FIGURA 08 — Diagrama de niveles orbitales del grupo carbonilo: n, pi, pi*
**Archivo destino:** `_static/figures/orbitales_carbonilo.svg`
**Usado en:** espectroscopia-uv.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 380 460", fondo transparente) que muestre el diagrama de niveles de energía orbital del grupo carbonilo (C=O) con énfasis en los orbitales relevantes para espectroscopía UV-Vis. El diagrama debe incluir: (1) Eje vertical de energía a la izquierda, flecha apuntando arriba, etiqueta "E". (2) Los siguientes niveles de energía orbital, de abajo hacia arriba, con líneas horizontales y etiquetas a su derecha: "sigma (C-O)" en la parte más baja (ocupado, dos electrones); "pi (C=O)" en posición media-baja (ocupado, dos electrones); "n (O)" en posición media, justo encima del pi, (ocupado, dos electrones: par solitario del oxígeno); "pi* (C=O)" en posición media-alta (desocupado, línea discontinua); "sigma* (C-O)" en la parte más alta (desocupado, línea discontinua). (3) Dos flechas de transición coloreadas: una flecha roja de trazo fino desde "n (O)" hacia "pi*" etiquetada "n → pi* (~280-300 nm, prohibida)" con símbolo de baja intensidad; una flecha azul gruesa desde "pi (C=O)" hacia "pi*" etiquetada "pi → pi* (<250 nm, permitida)". (4) Los niveles ocupados con electrones dibujados como pares de flechas arriba/abajo siguiendo la convención estándar. (5) Corchete lateral indicando el gap "HOMO-LUMO" entre n y pi*. Estilo científico, fuente sans-serif 10-11. Todo inline.

---

## FIGURA 09 — Pasos de optimización convergiendo a un mínimo sobre una PES 1D
**Archivo destino:** `_static/figures/optimizacion_pasos.svg`
**Usado en:** intro-born-oppenheimer.md

**Prompt:**
Genera un SVG científico (viewBox="0 0 500 300", fondo transparente) que muestre una curva de energía potencial en forma de parábola suave (un único mínimo, sin barrera) con cuatro o cinco puntos numerados sobre la curva que representan pasos sucesivos del algoritmo de optimización de geometría convergiendo al mínimo. El eje x representa la coordenada nuclear (etiqueta "coordenada nuclear Q"), el eje y la energía (etiqueta "E"). Los puntos deben estar distribuidos de modo que el punto 1 esté lejos del mínimo (a la izquierda), los siguientes se aproximen progresivamente, y el último punto esté en o cerca del mínimo. Cada punto va numerado (1, 2, 3...) con pequeños círculos rellenos azules o rojos. Una flecha curva o línea discontinua conecta los puntos en secuencia indicando el camino de optimización. El mínimo está marcado con una estrella pequeña o con la anotación "geometría de equilibrio". Estilo limpio, científico. Todo inline.
