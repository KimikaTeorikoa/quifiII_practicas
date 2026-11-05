# Atomoak eta Koopmans-en teorema

## Sarrera

Ionizazio-energiak nukleoak kanpoko elektroiei eragiten dien erakarpen-indarra neurtzen du, eta elementuen erreaktibitate kimikoa eta aldizkako joerak zehazten ditu. Hartree-Fock kalkuluak Gaussian programan eginez, bi hurbilketa osagarri aplikatzen dira propietate hori ebaluatzeko: atomo neutroaren eta bere katioiaren arteko energia osoaren diferentzia zuzena ($\Delta E$), eta energia handieneko orbital okupatutik abiatuta egindako estimazioa, Koopmans-en teorema erabiliz ($-\varepsilon_{\text{HOMO}}$).

## Helburuak

1. Atomo neutroen eta katioi monokargatuen energia elektroniko osoa kalkulatu Hartree-Fock metodoa erabiliz {{gaussian_version}} programan.
2. Ionizazio-energia kalkulatu diferentzia autoegokituaren bidez ($\Delta E$) eta orbitalen estimazioaren bidez, Koopmans-en teorema erabiliz ($-\varepsilon_{\text{HOMO}}$).
3. Kalkulatutako ionizazio-energiak balio esperimentalekin alderatu lehen eta bigarren periodoko elementuetan.
4. Energia handieneko orbital okupatuen (HOMO) banaketa espaziala eta simetria bistaratu GaussView programan.

## Kontzeptu gakoak

### Zergatik dira energiak negatiboak?

Atomo baten energia elektronikoa erreferentzia-egoera batekiko neurtzen da, non nukleoa eta elektroi guztiak pausagunean eta infinituan bananduta dauden, elkarrekintzarik gabe. Atomo lotua erreferentzia-egoera hori baino egonkorragoa denez, bere energia beti negatiboa da. `SCF Done` lerroan agertzen den balioa zenbat eta negatiboagoa izan, orduan eta egonkorragoa da sistema. Energia osoan emaitza positibo batek kalkuluaren konfigurazioan akats bat dagoela adieraziko luke.

### HOMO eta LUMO

Orbital molekularrak energia txikienetik handienera ordenatzen dira. Energia handieneko orbital okupatuari HOMO (ingelesez *Highest Occupied Molecular Orbital*) deritzo, eta elektroiak ateratzeko errazenak ditu. Lehen orbital hutsa, LUMO (*Lowest Unoccupied Molecular Orbital*), elektroiak jasotzeko prest dagoen orbitala da. HOMO mailaren eta hutsune-mailaren arteko aldea sistemak elektroi bat ateratzeko behar den energiaren lehen estimazioa da.

:::{admonition} Oharra
:class: note

Gaussian irteeran `pop=full`, HOMOaren energia azken lerroko `Alpha occ. eigenvalues` azken balio numerikoari dagokio. Hurrengo lerroko lehen balioa `Alpha virt. eigenvalues` LUMOari dagokio.

:::

:::{figure} /_static/figures/eu/homo_lumo_ionizacion.svg
:alt: Diagrama de niveles de orbitales con HOMO y LUMO señalados y flecha de energía de ionización
:width: 60%
:align: center
:::

### Ionizazio-energia eta Koopmans-en teorema

Atomo neutro baten $A$ ionizazio-energia gas-fasean elektroi bat ateratzeko eta $A^+$ katioia sortzeko behar den gutxieneko energia da, $A \rightarrow A^+ + e^-$ prozesuaren arabera. Praktika honetan bi modu independentetan kalkulatzen da. Lehenengoa katioiaren eta atomo neutroaren arteko SCF energien diferentzia zuzena da, eta horretarako bi kalkulu bereizi behar dira. Bigarrena Koopmans-en teoreman oinarritzen da, eta balio hori atomo neutroaren HOMO orbitalaren energiatik abiatuta estimatzeko aukera ematen du, katioia kalkulatu beharrik gabe.

$$\text{IE}_{\Delta E} = E(A^+) - E(A)$$

$$\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}$$

:::{admonition} Oharra
:class: note

Koopmans-en teoremak orbital izoztuen hurbilketa hartzen du, $A^+$ katioiaren orbitalak $A$ atomo neutroaren berdinak direla suposatuz. Ionizazio-prozesu fisiko batean, elektroi baten galerak elektroi arteko aldarapena murrizten du eta geratzen den hodei elektronikoa nukleorantz uzkurtzea eragiten du (orbitalen erlaxazioa). Koopmans-en hurbilketak erlaxazio egonkortzaile hori eta korrelazio-energiaren desberdintasunak alde batera uzten dituenez, $-\varepsilon_{\text{HOMO}}$ balioa diferentzia autoegokituan kalkulatutako balioarekin alderatuta $\text{IE}_{\Delta E}$ desberdina da pixka bat.

:::

### Spin-anizkoiztasuna

Spin-anizkoiztasunak sistemarako eskuragarri dauden spin-egoera kuantiko kopurua adierazten du eta $2S+1$ gisa kalkulatzen da, non $S$ elektroi desparekatuen spinen batura den. Elektroi guztiak parekatuta dituen atomo batek $S=0$ eta anizkoiztasun 1 (singletea) ditu. Elektroi desparekatu batek $S=1/2$ eta anizkoiztasun 2 (dobletea) ematen ditu. Anizkoiztasun-balio oker bat esleitzeak Gaussianek orbitalen artean elektroiak gaizki banatzea eragiten du $\alpha$ eta $\beta$, eta horrek emaitza baliogabetzen du edo SCF zikloaren konbergentzia eragozten du.

:::{admonition} Abisua
:class: warning

Egiaztatu beti spin-anizkoiztasunaren balioa kalkulua bidali aurretik: balio oker batek emaitzak baliogabetzen ditu edo SCF konbergentzia eragozten du.

:::

## Prozedura

:::{admonition} Adi
:class: danger

Kalkulu bakoitzaren ondorengo nahitaezko egiaztapena: ireki `.log` fitxategia testu-editorearekin eta egiaztatu azken lerro zehatza dagoela:
{{termination_ok}}

:::

### 1. urratsa: GaussView ireki eta atomoa marraztu

1. Ireki GaussView aplikazioen menutik edo sistemaren abiarazletik.
2. Ireki atomo-zatien paleta **View → Element Fragments** sakatuz (edo goiko tresna-barrako taula periodikoaren ikonoa sakatuz).
3. Hautatu kalkulatu nahi den elementu kimikoa (adibidez, karbonoa, **C**).
4. Egin klik bakarra ezkerreko botoiarekin marrazketa-leiho nagusian. Erdigune atomiko isolatu bat agertuko da, loturarik gabe.

### 2. urratsa: Atomo neutroaren kalkulua konfiguratu

1. Sartu **Calculate → Gaussian Calculation Setup** menura.
2. **Job Type** fitxan, hautatu **Energy**.
3. **Method** fitxan, konfiguratu kalkuluaren parametroak:

| Eremua | Balioa |
|---|---|
| Metodoa | **HF** |
| Oinarri-multzoa | **STO-3G** |
| Karga | **0** |
| Spin (Anizkoiztasuna) | Kontsultatu anizkoiztasunen taula atomo neutro bakoitzerako |

4. **Title** fitxan, idatzi deskribapen identifikatzaile bat (adibidez, `C neutro HF STO-3G`).
5. **Additional Keywords** fitxan, idatzi zehazki: `pop=full`. Instrukzio honek orbital molekular guztien energiak irteera-fitxategian sartzen ditu.

Erreferentziako anizkoiztasunen taula ($2S+1$):

| Atomoa | $Z$ | Konfigurazioa | Anizkoiztasuna |
|---|:---:|---|:---:|
| H | 1 | 1s¹ | 2 |
| He | 2 | 1s² | 1 |
| Li | 3 | [He] 2s¹ | 2 |
| Be | 4 | [He] 2s² | 1 |
| B | 5 | [He] 2s² 2p¹ | 2 |
| C | 6 | [He] 2s² 2p² | 3 |
| N | 7 | [He] 2s² 2p³ | 4 |
| O | 8 | [He] 2s² 2p⁴ | 3 |
| F | 9 | [He] 2s² 2p⁵ | 2 |
| Ne | 10 | [He] 2s² 2p⁶ | 1 |

:::{figure} /_static/capturas/07_koopmans_setup_c_popfull.png
:alt: Configuración del cálculo de Hartree-Fock con pop=full para el átomo de carbono
:width: 85%
:align: center
:::

### 3. urratsa: Kalkulua abiarazi eta fitxategia gorde

1. Sakatu **Bidali** botoia **Gaussian Calculation Setup** leihoaren behealdean.
2. Gorde fitxategia elkarrizketa-koadroan, adierazi sarrera-fitxategiaren izena `.gjf` (adibidez, `C_neutro_HF_STO3G.gjf`) eta gorde laborategiko laneko direktorioan: `__PROTECTED_BLOCK_36__`.
3. Berretsi elkarrizketa-koadroa **Save** sakatuz eta ondoren **Bidali**.
4. Ikusi exekuzio-egoera GaussView-ren beheko barran, kalkulua amaitu arte (segundo gutxi batzuk elementu arinentzat).

### 4. urratsa: Amaiera zuzena egiaztatu

1. Ireki sortutako `.log` fitxategia (`C_neutro_HF_STO3G.log`) testu-editorearekin (**File → Open** editorean edo eskuineko botoiarekin fitxategian klik eginez).
2. Joan fitxategiaren amaierara **Ctrl + Amaiera** sakatuz.
3. Egiaztatu fitxategiaren azken lerroa zehazki bat datorrela: `__PROTECTED_BLOCK_37__`. Ez bada agertzen, kalkulua huts egin du eta ez dira datuak erabili behar.

:::{figure} /_static/capturas/08_koopmans_log_terminacion_normal.png
:alt: Terminación normal de Gaussian 16 al final del archivo de salida .log
:width: 85%
:align: center
:::

### 5. urratsa: Irakurri guztizko energia E(N)

1. Testu-editorean irekitako `.log` fitxategian, sakatu **Ctrl + B** bilaketa aktibatzeko.
2. Idatzi bilaketa-testua: `SCF Done`.
3. Aurkitu guztizko energia `SCF Done:  E(RHF) = ...` lerroan (geruza itxiko sistema multiplicitate 1ekin) edo `SCF Done:  E(ROHF) = ...` lerroan (geruza irekiko sistema multiplicitate desberdinarekin).
4. Kopiatu balio numerikoa unitate atomikoetan (A.U. / Hartree) eta itsatsi emaitzen taulako $E(N)$ zutabean.

### 6. urratsa: Irakurri HOMO orbitalaren energia eta bistaratu orbitala

1. **Irakurketa numerikoa `.log` fitxategian:**
   - Irekitako `.log` fitxategian, bilatu **Ctrl + B**-rekin testu hau: `Alpha occ. eigenvalues`.
   - Aurkitu azken lerroko azken zenbakia `Alpha occ. eigenvalues --`. Balio numeriko hori energia handieneko betetako orbitalari dagokio, $\varepsilon_{\text{HOMO}}$ (Hartree-etan).
   - Aurkitu hurrengo lerroko lehen zenbakia `Alpha virt. eigenvalues --`, energia txikieneko hutsik dagoen orbitalari dagokiona ($\varepsilon_{\text{LUMO}}$).
   - Kopiatu $\varepsilon_{\text{HOMO}}$ balioa (Hartree-etan) emaitzen taulako dagokion zutabean.

2. **Egiaztapena eta bistaratzea GaussView-n:**
   - GaussView-n, ireki kalkuluaren ondoriozko `.chk` fitxategia eta sartu **Results → MOs** menura.
   - **New Gaussian MOs** fitxan, ikusi energia-mailen diagrama eta spin $\alpha$ eta $\beta$-ren orbitalen okupazioa. Karbono neutroaren triplete egoeran, energia handieneko betetako orbitalak ($\alpha$, 4. orbitala) $-0.32803\text{ Ha}$ energia du.

:::{figure} /_static/capturas/07b_koopmans_gv_orbitales_c.png
:alt: Diagrama de niveles de energía y ocupación de orbitales Alpha y Beta en Results MOs
:width: 85%
:align: center
:::

- Orbitalaren hiru dimentsioko banaketa sortzeko, leiho horren barruan **Visualize** fitxa hautatzen dugu. 4. orbitala (HOMO) hautatzen dugu, **Isovalue** eremua `0.01` ezartzen dugu eta **Update** sakatzen dugu. Ezkerreko azpileihoan $2p$ orbital atomikoaren bi lobuluak agertuko dira.

:::{figure} /_static/capturas/09_koopmans_gv_orbital_homo.png
:alt: Generación de la isosuperficie 3D del orbital HOMO (2p) con isovalor 0.01 en la pestaña Visualize
:width: 85%
:align: center
:::

### 7. urratsa: Konfiguratu eta kalkulatu A⁺ katioia

1. Itzuli GaussView-ra pantailan dagoen atomo-zentro berarekin.
2. Ireki berriro **Calculate → Gaussian Calculation Setup** panela.
3. ****Method**** fitxan, aldatu parametro hauek:
   - **Charge**: aldatu `0`-tik `1`-ra.
   - **Spin**: doitu katioi-espezieari dagokion multiplicitatera (ikusi beheko taula). HOMOtik elektroi bat kenduta, desparekatutako elektroien kopurua aldatu egiten da.
4. Mantendu **Job Type** `Energy`-n, **Method** `HF`-n, **Basis Set** `STO-3G`-n eta **Additional Keywords**-en `pop=full` gako-hitza.
5. ****Title**** fitxan, idatzi: `C cation HF STO-3G`.
6. Sakatu **Bidali**, gorde izen adierazgarri batekin (adibidez, `C_cation_HF_STO3G.gjf`) `{{practicas_folder}}`-n eta berretsi bidalketa.
7. Egiaztatu amaiera zuzena `.log` berrian eta atera guztizko energia $E(A^+)$ `SCF Done` lerroan.

| Eremua | Neutroa | Katioia |
|---|:---:|:---:|
| Charge | 0 | +1 |
| Spin | Multiplicitate neutroa | Multiplicitate katioia |

### 8. urratsa: Kalkulatu ionizazio-energiak

1. Kalkulatu ionizazio-energia zuzeneko diferentziaren bidez ($\text{IE}_{\Delta E}$):

$$\text{IE}_{\Delta E} = \bigl[E(A^+) - E(A)\bigr] \times 27.2114 \quad [\text{eV}]$$

2. Kalkulatu Koopmans-en teoremaren estimazioa ($\text{IE}_{\text{Koopmans}}$):

$$\text{IE}_{\text{Koopmans}} = -\varepsilon_{\text{HOMO}} \times 27.2114 \quad [\text{eV}]$$

3. Erregistratu bi balioak elektronvoltetan datuen taulan eta kalkulatu desbiderapen portzentuala erreferentziako balio esperimentalarekiko.

## Emaitzak eta analisia

Kalkulatutako atomo bakoitzerako, `.log` fitxategitik ateratako bi energiak erregistratzen ditugu eta ionizazio-energiaren bi estimazioak kalkulatzen ditugu. Ondorengo taulak Hartree-etan jasotzen ditu balioak eta emaitzak eV-ra bihurtuta. Erreferentziako balio esperimentalak sartzen dira errore portzentuala kalkulatzeko.

---

## Bibliografia

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Kimika Fisikoa*, 10. ed.; Editorial Médica Panamericana, 2018. 9. kap. (Egitura elektroniko atomikoa).
- NIST Chemistry WebBook, https://webbook.nist.gov (ionizazio-energiaren datu esperimentalak).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} Urrutirago joateko (aukerakoa)
:color: success

Esplorazio honek aztertzen du nola aldatzen den emaitzaren kalitatea oinarri-funtzioen multzoa handitzean. Karbono atomo neutroaren kalkulua errepikatzen dugu hiru oinarri desberdinekin eta HOMOren energia eta Koopmans-en estimatutako ionizazio-energia alderatzen ditugu balio esperimentalarekin. Prozedura praktika nagusiaren berdina da: **Basis Set** eremua bakarrik aldatzen dugu **Gaussian Calculation Setup → Method**-en.

| Oinarria | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Errorea (%) |
|:---:|:---:|:---:|:---:|:---:|
| STO-3G | −0.328 | 8.93 | 11.26 | 20.7 |
| 3-21G | (kalkulatzeko) | (kalkulatzeko) | 11.26 | (kalkulatzeko) |
| 6-311G | (kalkulatzeko) | (kalkulatzeko) | 11.26 | (kalkulatzeko) |

:::{note} Zein zentzutan aldatzen da __PROTECTED_BLOCK_73__ oinarriaren tamaina handitzean? Txikitzen al da errorea balio esperimentalarekiko modu monotonoan, edo ba al dago kasurik oinarri handiago batek emaitza hobetzen ez duena? Lotu desberdintasunak oinarri bakoitzak balentzia-elektroien dentsitatea deskribatzeko duen gaitasunarekin.

:::

::::
