---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Resolución numérica de la Ecuación de Schrödinger
En nuestra primera práctica vamos a trabajar con un método
numérico para resolver la ecuación de Schrödinger. Se 
trata de el método de diferencias finitas. Tratándose de un
método numérico, el cambio más importante es que en lugar
de trabajar con soluciones analíticas de la Ecuación
de Schrödinger,
```{math}
\hat{H}\Psi(\mathbf{r})=E\Psi(\mathbf{r})
```
vamos a trabajar con una versión discreta de esta ecuación. 
En el caso de un sistema en una sola dimensión, el eje $x$
pasa a estar discretizado en una serie de posiciones 
$\mathbf{x}=\{x_1, x_2, x_3, ..., x_n\}$ y la función de onda pasa a tener
una serie de valores
$\boldsymbol{\psi}=\{\psi_1, \psi_2, \psi_3,..., \psi_n\}$.

Para derivar las expresiones correspondientes a la versión
discreta del hamiltoniano, es importante que recordemos primero
 cómo se aproxima el valor de una función en un punto $x+h$ usando 
 una serie de Taylor
```{math}
f(x+h) = f(x) + h\cdot f'(x) + \frac{1}{2}h^2\cdot f''(x)
```
Si esta expansión la realizamos tanto hacia atrás en $x$, entonces
obtendremos
```{math}
f(x-h) = f(x) - h\cdot f'(x) + \frac{1}{2}h^2\cdot f''(x)
```
Podemos sumar ambas expresiones  y reorganizar términos para 
obtener una expresión compacta para la segunda derivada 
```{math}
f''(x) = \frac{f(x+h) + f(x-h) - 2f(x)}{h^2}
```

A continuación, repararemos en que en la ecuación de Schrödinger,
el término de energía cinética del operador hamiltoniano 
incorpora precisamente una segunda derivada de la función de
onda. Usando la expresión que acabamos de obtener, podemos definir
la segunda derivada de la función de onda para un determinado valor
de $x$ como 
```{math}
\psi''(x) = \frac{\psi(x+h) + \psi(x-h) - 2\psi(x)}{h^2}
```
Y dado que $x$ está ahora discretizado en un número finito de posiciones,
podemos escribir que para una posición $i$,
```{math}
\psi''(x_i) = \frac{\psi(x_{i+1}) + \psi(x_{i-1}) - 2\psi(x_i)}{\Delta x^2}
```

Usando esta expresión para la segunda derivada, podemos escribir la 
forma matricial del operador que, para un vector 
$\boldsymbol{\psi}=\{\psi_1, \psi_2, \psi_3,..., \psi_n\}$
nos permitirá obtener exactamente esta expresión para la segunda
derivada
```{math}
\frac{-\hbar^2}{2m}
\frac{1}{\Delta x^2 }
\begin{bmatrix}
-2 & 1&  0  & 0  &\cdots &\cdots & \cdots & \cdots & 0\\
1  & -2  & 1  & 0  & &  &  & & 0\\
0  & 1  &  -2 & 1 &  &  &  & & 0\\
\vdots & \vdots & \vdots  & & & &  & & \vdots\\
0  &   &   &  & -2 &1 & 0 & \cdots & 0\\
0  &   &    &  &1 & -2  & 1 &\cdots  & 0\\
0  &   &    &  &0 & 1 & -2 & \cdots & 0\\
\vdots  &  &  &   & &  &  & & \vdots\\
0  & 0  & 0 & \cdots  & & & &  1 & -2 \\
\end{bmatrix}
\begin{bmatrix}
\psi_1\\
\psi_2\\
\psi_3\\
\vdots\\
\psi_{n-1}\\
\psi_n \\
\psi_{n+1} \\
\vdots\\
\psi_L
\end{bmatrix}= 
E
\begin{bmatrix}
\psi_1\\
\psi_2\\
\psi_3\\
\vdots\\
\psi_{n-1}\\
\psi_n \\
\psi_{n+1} \\
\vdots\\
\psi_L
\end{bmatrix}
```

Hasta ahora sólo nos hemos ocupado del término de energía cinética del
hamiltoniano. En el caso de que el sistema que nos concierna también
esté sometido a un potencial externo, habrá que añadir la correspondiente
versión discretizada del operador energía potencial
```{math}
\frac{-\hbar^2}{2m}
\frac{1}{\Delta x^2 }
\begin{bmatrix}
-2 & 1&  0  & 0  &\cdots &\cdots & \cdots & \cdots & 0\\
1  & -2  & 1  & 0  & &  &  & & 0\\
0  & 1  &  -2 & 1 &  &  &  & & 0\\
\vdots & \vdots & \vdots  & & & &  & & \vdots\\
0  &   &   &  & -2 &1 & 0 & \cdots & 0\\
0  &   &    &  &1 & -2  & 1 &\cdots  & 0\\
0  &   &    &  &0 & 1 & -2 & \cdots & 0\\
\vdots  &  &  &   & &  &  & & \vdots\\
0  & 0  & 0 & \cdots  & & & &  1 & -2 \\
\end{bmatrix}
\begin{bmatrix}
\psi_1\\
\psi_2\\
\psi_3\\
\vdots\\
\psi_{n-1}\\
\psi_n \\
\psi_{n+1} \\
\vdots\\
\psi_L
\end{bmatrix}
+  \\
\begin{bmatrix}
V_1 & 0 &  0  & 0  &\cdots &\cdots & \cdots & \cdots & 0\\
0  & V_2  & 0 & 0  & &  &  & & 0\\
0  & 0 &  V_3 & 0 &  &  &  & & 0\\
\vdots & \vdots & \vdots  & & & &  & & \vdots\\
0  &   &   &  & V_{n-1} & 0 & 0 & \cdots & 0\\
0  &   &    &  & 0 & V_n & 0 &\cdots  & 0\\
0  &   &    &  &0 & 0 & V_{n+1} & \cdots & 0\\
\vdots  &  &  &   & &  &  & & \vdots\\
0  & 0  & 0 & \cdots  & & & & 0 & V_L \\
\end{bmatrix}
\begin{bmatrix}
\psi_1\\
\psi_2\\
\psi_3\\
\vdots\\
\psi_{n-1}\\
\psi_n \\
\psi_{n+1} \\
\vdots\\
\psi_L
\end{bmatrix}= 
E
\begin{bmatrix}
\psi_1\\
\psi_2\\
\psi_3\\
\vdots\\
\psi_{n-1}\\
\psi_n \\
\psi_{n+1} \\
\vdots\\
\psi_L
\end{bmatrix}
```

Las soluciones del hamiltoniano serán las funciones propias de 
esta matriz y sus autovalores serán las energías asociadas a
las funciones propias. En lugar de resolver nosotros mismos
este problema, en estas prácticas dejaremos que el ordenador
haga este trabajo por nosotros.