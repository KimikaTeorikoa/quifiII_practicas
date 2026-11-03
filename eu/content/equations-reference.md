# Ekuazioen erreferentzia — M_QUIFIS2

Liburuko adierazpen matematiko guztien erreferentzia nagusia (SSOT).
Bertsioa: 1.0.0 | 2026-10-25

Praktikek ekuazio hauek beren horretan kopiatzen dituzte. Bihurketa-faktore edo definizioren bat aldatzen bada, hemen zuzendu eta gainerakoetara hedatzen da.

---

## 1. Unitate-bihurketak

### 1.1 Hartree-tik elektroi-voltera

$$
1 \, \text{Ha} = {{ha_to_ev}} \, \text{eV}
$$

### 1.2 Hartree-tik kcal/mol-era

$$
1 \, \text{Ha} = {{ha_to_kcal}} \, \text{kcal mol}^{-1}
$$

### 1.3 Hartree-tik kJ/mol-era

$$
1 \, \text{Ha} = 2625.50 \, \text{kJ mol}^{-1}
$$

### 1.4 Uhin-zenbakitik elektroi-voltera

$$
1 \, \text{cm}^{-1} = 1.23984 \times 10^{-4} \, \text{eV}
$$

### 1.5 Uhin-luzeratik energiara (Planck-Einstein erlazioa)

$$
E \, (\text{eV}) = \frac{1239.8}{\lambda \, (\text{nm})}
$$

Baliokideki:

$$
\lambda \, (\text{nm}) = \frac{1239.8}{E \, (\text{eV})}
$$

---

## 2. Ionizazio-energia (P2-A)

### 2.1 Energia osoen kenduraren metodoa

Izan bitez $E(N)$ atomo neutroaren energia osoa eta $E(N-1)$ katioiarena (elektron bat gutxiago):

$$
\text{IE} = E(N-1) - E(N)
$$

Hartree-tan lortutako emaitza eV-etara bihurtzeko, ${{ha_to_ev}}$ balioaz biderkatzen da.

### 2.2 Koopmans-en teorema

Hartree-Fock esparruan, $i$ orbitalaren ionizazio-energia orbital-energiaren balio negatiboaren berdina da:

$$
\text{IE}_i \approx -\varepsilon_i
$$

Lotura ahuleneko elektroiarentzat (HOMO):

$$
\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}
$$

:::{warning}
Koopmans-en teoremak ez ditu kontuan hartzen ionizazioaren ondorengo orbital-erlaxazioa ezta korrelazio elektronikoa ere. Balio esperimentalak baino % 10–20 handiagoak diren emaitzak ematen ditu sistematikoki.
:::

---

## 3. HOMO-LUMO gap-a eta zenbatetsitako uhin-luzera (P2-D)

### 3.1 Gap-a elektroi-voltetan

$$
\Delta E_{\text{gap}} \, (\text{eV})
  = \bigl(\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}\bigr)
    \times {{ha_to_ev}}
$$

$\varepsilon$ balioak `.log` fitxategitik irakurtzen dira Hartree-tan (biak negatiboak sistema egonkorretan; LUMOaren energia handiagoa da, hots, ez hain negatiboa).

### 3.2 Zenbatetsitako uhin-luzera

$$
\lambda_{\text{zenbatetsia}} \, (\text{nm}) = \frac{1239.8}{\Delta E_{\text{gap}} \, (\text{eV})}
$$

:::{note}
Hurbilketa honek lehen trantsizio elektronikoa HOMO-LUMO gap-ari zuzenean dagokiola onartzen du. TD-DFT zehatzagoa da, eremu oszilakorrarekiko sistemaren erantzuna barne hartzen baitu.
:::

---

## 4. Bibrazio-modu normalak (P2-C)

### 4.1 Modu normalen kopurua

$N$ atomoko molekula ez-lineal baterako:

$$
\text{modu normalak} = 3N - 6
$$

Molekula lineal baterako:

$$
\text{modu normalak} = 3N - 5
$$

### 4.2 Eredu harmonikoa: osziladore diatomiko baten maiztasuna

$$
\tilde{\nu} = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}}
$$

non $k$ indar-konstantea den (N m$^{-1}$), $c$ argiaren abiadura ($2.998 \times 10^{10}$ cm s$^{-1}$) eta $\mu$ masa laburtua:

$$
\mu = \frac{m_1 \, m_2}{m_1 + m_2}
$$

:::{note}
Ikasleek ez dituzte $k$ eta $\mu$ eskuz kalkulatzen. Gaussian-ek maiztasunak zuzenean cm$^{-1}$ unitatetan ematen ditu. Ekuazio honek azaltzen du zergatik lotura zurrunagoek edo atomo arinagoek maiztasun handiagoan bibratzen duten.
:::

### 4.3 IR hautaketa-araua (irizpide kualitatiboa)

Modu normal bat aktiboa da infragorrian bibrazioan zehar molekularen une dipolar elektrikoa aldatzen bada:

$$
\left(\frac{\partial \boldsymbol{\mu}}{\partial Q_k}\right)_0 \neq \mathbf{0}
$$

non $Q_k$ $k$ moduaren koordenatu normala den.

---

## 5. Potentzial-energiaren gainazala (P2-B)

### 5.1 Energia erlatiboa koordenatu-esplorazio batean

PEG-aren puntuak elkarrekin alderatzeko, kalkulatutako $E_0$ minimoa hartzen da erreferentzia gisa:

$$
\Delta E \, (\text{kcal mol}^{-1})
  = \bigl(E_i - E_0\bigr) \times {{ha_to_kcal}}
$$
