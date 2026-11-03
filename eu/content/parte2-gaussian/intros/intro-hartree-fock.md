# Hartree-Fock metodoa

## Sarrera

Schrödinger-en ekuazioak ez du soluzio matematiko zehatzik onartzen elektroi bat baino gehiago duten sistemetan, haien arteko aldarapen elektrostatikoak eragindako akoplamenduaren ondorioz. Hartree-Fock metodoak arazo horri heltzen dio batez besteko eremuaren hurbilketaren bidez, binakako unean uneko elkarrekintzen ordez espazioan batez besteko potentzial bat ezarriz. Sinplifikazio honi esker, Gaussian bezalako programek orbital molekularrak eta energia elektroniko osoa zehaztu ditzakete prozedura iteratibo autokonsistente baten bidez.

## Arazoa: elkar aldarazten duten elektroiak

Bi elektroiko atomo batean, helioan kasu ($Z=2$), hamiltondar eragile zehatzak elektroi bakoitzaren energia zinetikoa, nukleoarekiko erakarpena eta bien arteko aldarapen elektrostatikoa biltzen ditu:

$$\hat{H} = \hat{h}(1) + \hat{h}(2) + \frac{1}{r_{12}}$$

Monoelektroizko $\hat{h}(i)$ eragileak $i$ elektroiaren mugimendua deskribatzen du nukleoaren erakarpen-potentzialaren pean, beste elektroia kontuan hartu gabe:

$$\hat{h}(i) = -\frac{1}{2}\nabla_i^2 - \frac{2}{r_i}$$

$1/r_{12}$ aldarapen coulombiarraren terminoa existituko ez balitz, ekuazioa aldagaiak bananduz ebatziko litzateke, bi atomo hidrogenoideren biderkadura gisa. Hala ere, $1/r_{12}$ terminoak bi elektroien unean uneko posizioak akoplatzen ditu: baten espazio-banaketa zehazteak bestearena une oro ezagutzea eskatzen du. Zailtasun hori edozein sistema polielektronikotara hedatzen da eta egitura elektronikoaren erronka nagusia da.

:::{admonition} Oharra
:class: note
$1/r_{12}$ terminoak elektroien koordenatu espazialak akoplatzen ditu eta eragotzi egiten du Schrödinger-en ekuazioa analitikoki ebaztea bi elektroi edo gehiago dituen edozein atomo edo molekularentzat.
:::

## Hartree-Fock-en ideia: batez besteko eremua

Ekuazioak desakoplatzeko, Hartree-Fock hurbilketak elektroi-bikoteen arteko unean uneko aldarapenak ordezkatzen ditu hodei elektroniko osoak sortutako batez besteko potentzial elektrostatiko baten bidez. Elektroi bakoitza nukleoak eta gainerako elektroien batez besteko dentsitateak sortutako eremuan mugitzen da orduan.

Sinplifikazio horren pean, elektroi bakoitzak Fock-en $\hat{f}$ eragileak gobernatutako monoelektroizko autobalio-ekuazio bat betetzen du:

$$\hat{f} \phi_i = \varepsilon_i \phi_i$$

Helio-atomoarentzat, non bi elektroiek $\phi_1$ espazio-orbital bera okupatzen duten kontrako spinekin, Fock-en eragileak forma hau hartzen du:

$$\hat{f} = \hat{h} + \hat{J}_1$$

non $\hat{J}_1$ eragileak beste elektroiaren hodeiak sortutako batez besteko potentzial elektrostatikoa adierazten duen:

$$\hat{J}_1 \phi_1(\mathbf{r}_1) = \left[\int \frac{|\phi_1(\mathbf{r}_2)|^2}{r_{12}} d\mathbf{r}_2\right] \phi_1(\mathbf{r}_1)$$

:::{admonition} Oharra
:class: note
Elektroien arteko aldarapena batez besteztatzean, ez dira kontuan hartzen elektroien posizioen arteko unean uneko korrelazioak (korrelazio elektronikoa). Bariazio-teoremaren arabera, Hartree-Fock mugan kalkulatutako energia sistemaren energia ez-erlatibista zehatzaren goi-muga bat da beti.
:::

## Orbitalak: oinarri-funtzioen konbinazio lineala (LCAO)

Elektroi bakoitzaren egoera espaziala $\phi_i(\mathbf{r})$ orbital baten bidez deskribatzen da. Helioan, bere oinarrizko egoeran, bi elektroiek $\phi_1$ orbitala okupatzen dute kontrako spinekin ($\alpha$ eta $\beta$).

$\phi_i(\mathbf{r})$ orbitalaren forma matematiko zehatza aldez aurretik ezagutzen ez denez, aurrez definitutako $\{\chi_\mu\}$ oinarri-funtzioen ($K$ funtzio) konbinazio lineal gisa hedatzen da (normalean nukleoetan zentratutako funtzio gaussiarrak):

$$\phi_i(\mathbf{r}) = \sum_{\mu=1}^{K} C_{\mu i} \chi_\mu(\mathbf{r})$$

Problema kuantikoa ebaztea sistemaren energia osoa minimizatzen duten $C_{\mu i}$ zenbakizko koefizienteak zehaztearen baliokidea da. Irudiak helio-atomoarentzat lortutako 1s orbitalaren dentsitate elektronikoa erakusten du.

:::{figure} /_static/figures/eu/orbital_1s_he.svg
:alt: Helio-atomoaren 1s orbitalaren dentsitate elektronikoaren adierazpena gainazal zentrokideen bidez
:width: 50%
:align: center
:::

## Roothaan-Hall ekuazioak: Helioaren adibidea bi orbitalekin

LCAO hedapena Fock-en ekuazioan ordezkatu eta oinarri-funtzio bakoitzaren gainean proiektatzean, ekuazio integrodiferentzialak autobalio-arazo matrizial orokortu bihurtzen dira:

$$\mathbf{F} \mathbf{C} = \mathbf{S} \mathbf{C} \boldsymbol{\varepsilon}$$

Har dezagun bi s motako funtzioko oinarri batekin deskribatutako helio-atomoa ($\chi_1$ eta $\chi_2$), adibidez berretzaile desberdineko bi funtzio gaussiar hodei elektronikoa erradialki hedatu edo uzkurtu ahal izateko. Espazio-orbital bakoitza honela adierazten da:

$$\phi_1 = C_{11}\chi_1 + C_{21}\chi_2 \quad (\text{orbital okupatua, HOMO})$$

$$\phi_2 = C_{12}\chi_1 + C_{22}\chi_2 \quad (\text{orbital birtuala, LUMO})$$

2×2 dimentsioko sistema matrizialak forma esplizitu hau hartzen du:

$$\begin{pmatrix} F_{11} & F_{12} \\ F_{21} & F_{22} \end{pmatrix} \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix} = \begin{pmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{pmatrix} \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix} \begin{pmatrix} \varepsilon_1 & 0 \\ 0 & \varepsilon_2 \end{pmatrix}$$

Matrize bakoitzak esanahi fisiko zuzena du:

**Gainjartze-matrizea $\mathbf{S}$:** Bi oinarri-funtzioen arteko ez-ortogonaltasun espaziala deskribatzen du:

$$\mathbf{S} = \begin{pmatrix} 1 & S_{12} \\ S_{12} & 1 \end{pmatrix}$$

Funtzioak normalizatuta daudenez, diagonaleko elementuek 1 balio dute ($S_{11} = S_{22} = 1$). Elementu gurutzatuak bien arteko gainjartze-integrala adierazten du:

$$S_{12} = \int \chi_1^*(\mathbf{r}) \chi_2(\mathbf{r}) \, d\mathbf{r}$$

**Fock-en matrizea $\mathbf{F}$:** Oinarri-funtzio bakoitzean elektroi baten energia eraginkorra ($F_{11}, F_{22}$) eta elkarrekiko akoplamendua ($F_{12} = F_{21}$) biltzen ditu:

$$\mathbf{F} = \begin{pmatrix} F_{11} & F_{12} \\ F_{21} & F_{22} \end{pmatrix}$$

Bere elementuak Fock-en eragilea oinarriaren gainean integratuz lortzen dira:

$$F_{\mu\nu} = \int \chi_\mu^*(\mathbf{r}) \hat{f} \chi_\nu(\mathbf{r}) \, d\mathbf{r}$$

**Koefizienteen matrizea $\mathbf{C}$:** Zutabe bakoitzak espazio-orbitaletako bat definitzen du:

$$\mathbf{C} = \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix}$$

Lehen zutabeak $\begin{pmatrix} C_{11} \\ C_{21} \end{pmatrix}$ $\chi_1$ eta $\chi_2$ funtzioen pisuak ditu $\phi_1$ orbital okupatuan (HOMO). Bigarren zutabeak $\begin{pmatrix} C_{12} \\ C_{22} \end{pmatrix}$ $\phi_2$ orbital birtualaren koefizienteak ditu (LUMO).

**Orbital-energien matrizea $\boldsymbol{\varepsilon}$:** Autobalio energetikoak biltzen dituen matrize diagonala da:

$$\boldsymbol{\varepsilon} = \begin{pmatrix} \varepsilon_1 & 0 \\ 0 & \varepsilon_2 \end{pmatrix}$$

non $\varepsilon_1 = \varepsilon_{\text{HOMO}}$ orbital lotuaren energia den (negatiboa) eta $\varepsilon_2 = \varepsilon_{\text{LUMO}}$ lehen orbital hutsaren energia den.

:::{note} Helioaren kasua eta benetako sistemak: $K \times K$ dimentsioko matrizeak
Ez da nahastu behar 2×2 eredu hau kalkulu molekularren benetako dimentsioarekin:

1. **Zergatik 2×2 adibide honetan?** Nahita aukeratu dugulako $K = 2$ funtzioko oinarri minimo bat 2 elektroiko atomo baterako. Bi oinarri-funtzio egonda, zehazki 2 orbital lortzen dira: orbital okupatu 1 (bi elektroi parekatuekin) eta orbital birtual huts 1.
2. **Dimentsioak benetako sistemetan:** Edozein kalkulu molekular estandarretan, $K$ oinarri-funtzioen kopurua askoz handiagoa da ($K = 30, 80, 300\dots$). $\mathbf{F}$, $\mathbf{S}$ eta $\mathbf{C}$ matrizeak beti dira **$K \times K$** dimentsioko matrize karratuak.
3. **Orbital okupatuen eta birtualen banaketa:** $N$ elektroiko eta $K$ oinarri-funtzioko geruza itxiko sistema neutro baterako, metodoak beti sortzen ditu $K$ espazio-orbital. $\mathbf{C}$ matrizearen lehen $N/2$ zutabeak bakarrik dagozkie orbital okupatuei ($\phi_{N/2}$ HOMO orbitaleraino); gainerako $K - N/2$ zutabeak orbital birtual hutsei dagozkie ($\phi_{N/2 + 1}$ LUMO orbitaletik hasita).
:::

## SCF zikloa: iterazio bidez ebaztea

Mendekotasun zirkular bat dago: Fock-en $\mathbf{F}$ matrizea kalkulatzeko dentsitate elektronikoa ezagutu behar da ($\mathbf{C}$ koefizienteak), baina $\mathbf{C}$ lortzeko $\mathbf{F}\mathbf{C} = \mathbf{S}\mathbf{C}\boldsymbol{\varepsilon}$ sistema diagonalizatu behar da.

Zirkulartasun hori eremu autokonsistentearen metodoaren bidez ebazten da (SCF, *Self-Consistent Field*):

1. Koefizienten hasierako zenbatespen bat sortzen da (*guess* $\mathbf{C}^{(0)}$).
2. Koefiziente horiekin $\mathbf{F}^{(k)}$ Fock-en matrizea eraikitzen da.
3. $\mathbf{F}^{(k)}\mathbf{C} = \mathbf{S}\mathbf{C}\boldsymbol{\varepsilon}$ sistema diagonalizatzen da $\mathbf{C}^{(k+1)}$ koefiziente berriak eta $\boldsymbol{\varepsilon}^{(k+1)}$ energia berriak lortzeko.
4. Egiaztatzen da ea aurreko urratsarekiko energiaren eta dentsitatearen aldaketa ezarritako tolerantzia baino txikiagoa den (adibidez $10^{-6}$ Ha). Ez badu konbergitu, 2. urratsera itzultzen da.

:::{figure} /_static/figures/eu/ciclo_scf.svg
:alt: SCF zikloaren fluxu-diagrama hasierako hurbilpenetik konbergentziaraino
:width: 55%
:align: center
:::

## Energiak: orbitala vs osoa

Fock-en matrizea diagonalizatzean lortutako $\varepsilon_i$ autobalioak orbital indibidual bakoitzaren energiei dagozkie, ez sistemaren energia osoari.

Helioaren bi elektroientzat $\phi_1$ orbitalean, orbital-energiak $h_{11}$ monoelektroizko energia eta beste elektroiarekiko $J_{11}$ aldarapen elektrostatikoa biltzen ditu:

$$\varepsilon_1 = h_{11} + J_{11}$$

Bi elektroien orbital-energiak zuzenean batuko bagenitu:

$$2\varepsilon_1 = 2h_{11} + 2J_{11}$$

$J_{11}$ elektroien arteko aldarapena bi aldiz kontatuko genuke. Beraz, benetako energia elektronikoak elkarrekintza bikoiztu hori kentzen du:

$$E_{\text{elec}} = 2\varepsilon_1 - J_{11} = 2h_{11} + J_{11}$$

Hainbat nukleo dituen molekula batean, energia osoak gainera $V_{NN}$ nukleoen arteko aldarapen coulombiarra gehitzen du:

$$E_{\text{total}} = E_{\text{elec}} + V_{NN}$$

Balio hori da hain zuzen ere Gaussian-ek `.log` fitxategiaren `SCF Done` lerroan inprimatzen duena.

:::{admonition} Abisua
:class: warning
Gaussian-en log fitxategiko `SCF Done` lerroan agertzen den energia sistemaren energia osoa da $E_{\text{total}}$, ez orbital indibidual baten energia $\varepsilon_i$.
:::

## HF metodoaren mugak: korrelazio elektronikoa

Hartree-Fock metodoak unean uneko elkarrekintzak batez besteko eremu batez ordezkatzen dituenez, puntu batean elektroi bat aurkitzeko probabilitatea bestearen unean uneko posiziotik independentea dela onartzen du. Oinarri infinituko Hartree-Fock energiaren ($E_{\text{HF}}^{\text{limit}}$) eta energia ez-erlatibista zehatzaren ($E_{\text{exacta}}$) arteko diferentziak korrelazio-energia definitzen du:

$$E_{\text{corr}} = E_{\text{exacta}} - E_{\text{HF}}^{\text{limit}}$$

$E_{\text{HF}}^{\text{limit}} \ge E_{\text{exacta}}$ denez bariazio-printzipioagatik, korrelazio-energia negatiboa da beti ($E_{\text{corr}} \le 0$). Energia osoaren % 1 baino gutxiago izan ohi den arren, erabakigarria da lotura-energiak, erreakzio-hesiak eta trantsizio espektroskopikoak zehaztasunez kalkulatzeko.

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} 🚀 Uhin-funtzio antisimetrikoa eta Slater-en determinantea
:color: success
:icon: rocket

Pauliren bazterketa-printzipioak eskatzen du uhin-funtzio elektronikoa antisimetrikoa izatea edozein bi elektroiren trukearen aurrean:

$$\Psi(\mathbf{x}_1, \mathbf{x}_2) = -\Psi(\mathbf{x}_2, \mathbf{x}_1)$$

$\phi_1$ espazio-orbitalean kontrako spinak dituzten bi elektroirentzat, uhin-funtzioa Slater-en determinante gisa adierazten da:

$$\Psi(\mathbf{x}_1, \mathbf{x}_2) = \frac{1}{\sqrt{2}} \begin{vmatrix} \phi_1(\mathbf{r}_1)\alpha(1) & \phi_1(\mathbf{r}_1)\beta(1) \\ \phi_1(\mathbf{r}_2)\alpha(2) & \phi_1(\mathbf{r}_2)\beta(2) \end{vmatrix}$$

Bi elektroien koordenatuak elkarrekin trukatzea determinantearen bi errenkada trukatzearen baliokidea da; horrek zeinua automatikoki alderantzikatzen du eta Pauliren printzipioa bermatzen du.

::::

::::{dropdown} 🚀 Korrelazio-energia eta post-HF metodoak
:color: success
:icon: rocket

Hartree-Fock-en uhin-funtziotik abiatuta hainbat metodo garatu dira korrelazio elektronikoa berreskuratzeko eta batez besteko eremuaren hurbilketa gainditzeko. Møller-Plesset-en bigarren ordenako perturbazio-teoriak (MP2) zuzenketa dinamikoak gehitzen dizkio energiari neurrizko kalkulu-kostuarekin. Bestalde, *Coupled Cluster* metodoek (hala nola CCSD) askoz zehaztasun handiagoa eskaintzen dute kalkulu-ahalegin handiagoaren truke. Eskema hauek xehetasunez aztertzen dira geroko atal teoriko batean (Hartree-Fock-etik haratago).

::::
