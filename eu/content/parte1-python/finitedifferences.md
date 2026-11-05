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
# Schrödinger-en Ekuazioaren Ebazpen Numerikoa
Gure lehen praktikan, Schrödinger-en ekuazioa ebazteko metodo numeriko batekin lan egingo dugu. Metodo hori diferentzia finituen metodoa da. Metodo numerikoa denez, aldaketarik garrantzitsuena da Schrödinger-en ekuazioaren soluzio analitikoekin lan egin beharrean,
```{math}
\hat{H}\Psi(\mathbf{r})=E\Psi(\mathbf{r})
```
ekuazio honen bertsio diskretu batekin lan egingo dugula. Dimentsio bakarreko sistema baten kasuan, $x$ ardatza posizio-serie batean diskretizatuta dago
$\mathbf{x}=\{x_1, x_2, x_3, ..., x_n\}$, eta uhin-funtzioak balio-serie bat du
$\boldsymbol{\psi}=\{\psi_1, \psi_2, \psi_3,..., \psi_n\}$.

Hamiltondarren bertsio diskretuari dagozkion adierazpenak eratorzeko, garrantzitsua da lehenik gogoratzea nola hurbiltzen den funtzio baten balioa puntu batean $x+h$ Taylor serie bat erabiliz
```{math}
f(x+h) = f(x) + h\cdot f'(x) + \frac{1}{2}h^2\cdot f''(x)
```
Hedapen hau atzerantz egiten badugu $x$, orduan
lortuko dugu
```{math}
f(x-h) = f(x) - h\cdot f'(x) + \frac{1}{2}h^2\cdot f''(x)
```
Bi adierazpenak batu eta terminoak berrantolatu ditzakegu bigarren deribatuaren adierazpen trinko bat lortzeko
```{math}
f''(x) = \frac{f(x+h) + f(x-h) - 2f(x)}{h^2}
```

Jarraian, Schrödinger-en ekuazioan, energia zinetikoaren terminoak, hamiltondar operadorearen barruan, uhin-funtzioaren bigarren deribatua barne hartzen duela ikusiko dugu. Lortu berri dugun adierazpena erabiliz, uhin-funtzioaren bigarren deribatua defini dezakegu $x$ balio jakin baterako
```{math}
\psi''(x) = \frac{\psi(x+h) + \psi(x-h) - 2\psi(x)}{h^2}
```
Eta $x$ orain posizio kopuru finitu batean diskretizatuta dagoenez, idatz dezakegu posizio baterako $i$,
```{math}
\psi''(x_i) = \frac{\psi(x_{i+1}) + \psi(x_{i-1}) - 2\psi(x_i)}{\Delta x^2}
```

Bigarren deribatuaren adierazpen hau erabiliz, operadorearen forma matrizeala idatz dezakegu, bektore baterako
$\boldsymbol{\psi}=\{\psi_1, \psi_2, \psi_3,..., \psi_n\}$
bigarren deribatuaren adierazpen hau lortzeko aukera emango diguna
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

Orain arte, hamiltondarren energia zinetikoaren terminoaz bakarrik arduratu gara. Aztertzen ari garen sistema kanpoko potentzial baten eraginpean badago ere, energia potentzialaren operadorearen bertsio diskretizatua gehitu beharko da
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

Hamiltondarren soluzioak matrize honen funtzio propioak izango dira, eta autobalioak funtzio propioei lotutako energiak izango dira. Arazo hau guk geuk ebatzi beharrean, praktika hauetan ordenagailuari utziko diogu lan hori egiten.
