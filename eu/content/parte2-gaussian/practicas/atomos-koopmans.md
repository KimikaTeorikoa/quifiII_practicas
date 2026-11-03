# Atomoak eta Koopmans-en teorema

## Sarrera

Ionizazio-energiak neurtzen du nukleoak kanpokoeneko elektroien gainean eragiten duen erakarpen-indarra, eta elementuen erreaktibotasun kimikoa zein joera periodikoak finkatzen ditu. Gaussian-en egindako Hartree-Fock kalkuluen bidez, bi hurbilketa osagarri aplikatuko ditugu propietate hau ebaluatzeko: atomo neutroaren eta bere katioiaren arteko energia osoaren kendura zuzena ($\Delta E$), eta energia goreneko orbital okupatutik abiatutako zenbatespena Koopmans-en teoremaren bidez ($-\varepsilon_{\text{HOMO}}$).

## Helburuak

1. Atomo neutroen eta katioi monokargatuen energia elektroniko osoa kalkulatzea Hartree-Fock metodoaren bidez {{gaussian_version}} erabiliz.
2. Ionizazio-energia zehaztea diferentzia autokonsistentearen bidez ($\Delta E$) eta orbital-zenbatespenaren bidez Koopmans-en teoremari jarraituz ($-\varepsilon_{\text{HOMO}}$).
3. Kalkulatutako ionizazio-energiak lehen eta bigarren periodoko balio esperimentalekin alderatzea.
4. Energia goreneko orbital atomiko okupatuen (HOMO) banaketa espaziala eta simetria bistaratzea GaussView-n.

## Kontzeptu nagusiak

### Zergatik dira energiak negatiboak?

Atomo baten energia elektronikoa erreferentzia-egoera batekiko neurtzen da: nukleoa eta elektroi guztiak pausagunean eta infinituan bananduta daudenean, elkarrekintzarik gabe. Atomo lotua erreferentzia-egoera hori baino egonkorragoa denez, bere energia beti da negatiboa. `SCF Done` lerroan agertzen den balioa zenbat eta negatiboagoa izan, orduan eta handiagoa da sistemaren egonkortasuna. Energia osoan emaitza positibo bat lortzeak kalkuluaren konfigurazioan errore bat dagoela adieraziko luke.

### HOMO eta LUMO

Orbital molekularrak energiarik txikienetik handienera ordenatzen dira. Energia goreneko orbital okupatuak HOMO izena jasotzen du (ingelesezko *Highest Occupied Molecular Orbital*) eta erauzteko errazenak diren elektroiak ditu. Lehen orbital hutsak, LUMO izenekoak (*Lowest Unoccupied Molecular Orbital*), elektroiak jasotzeko prest dagoen orbitala adierazten du. HOMO mailaren eta hutsaren mailaren arteko aldeak sistematik elektroi bat erauzteko behar den energiaren lehen zenbatespena ematen du.

:::{admonition} Oharra
:class: note
`pop=full` aukera duen Gaussian-en irteeran, HOMOaren energia `Alpha occ. eigenvalues` lerroko azken zenbakizko balioari dagokio. Hurrengo `Alpha virt. eigenvalues` lerroko lehen balioa LUMOari dagokio.
:::

:::{figure} /_static/figures/eu/homo_lumo_ionizacion.svg
:alt: Orbital-mailen diagrama HOMO eta LUMO orbitalak adierazita eta ionizazio-energiaren geziarekin
:width: 60%
:align: center
:::

### Ionizazio-energia eta Koopmans-en teorema

Gas-fasean dagoen $A$ atomo neutro baten ionizazio-energia elektroi bat erauzi eta $A^+$ katioia sortzeko behar den gutxieneko energia da, $A \rightarrow A^+ + e^-$ prozesuaren arabera. Praktika honetan bi bide independentetatik kalkulatzen dugu. Lehena katioiaren eta atomo neutroaren arteko SCF energien kendura zuzena da, eta bi kalkulu bereizi eskatzen ditu. Bigarrena Koopmans-en teoreman oinarritzen da; horri esker, balio hori atomo neutroaren HOMO orbitalaren energiatik soilik zenbatets daiteke, katioia kalkulatu beharrik gabe.

$$\text{IE}_{\Delta E} = E(A^+) - E(A)$$

$$\text{IE}_{\text{Koopmans}} \approx -\varepsilon_{\text{HOMO}}$$

:::{admonition} Oharra
:class: note
Koopmans-en teoremak orbital izoztuen hurbilketa onartzen du, $A^+$ katioiaren orbitalak $A$ atomo neutroaren orbitalen berdinak direla suposatuz. Benetako ionizazio-prozesu fisiko batean, elektroi bat galtzeak elektroien arteko aldarapen orokorra murrizten du eta geratzen den hodei elektronikoa nukleorantz uzkurtzea eragiten du (orbital-erlaxazioa). Koopmans-en hurbilketak ez dituenez kontuan hartzen ez erlaxazio egonkortzaile hori ezta korrelazio-energiaren aldeak ere, $-\varepsilon_{\text{HOMO}}$ apur bat aldentzen da $\text{IE}_{\Delta E}$ kendura autokonsistentearen bidez kalkulatutako baliotik.
:::

### Spin-anizkoiztasuna

Spin-anizkoiztasunak sistemarentzat eskuragarri dauden spin-egoera kuantikoen kopurua adierazten du, eta $2S+1$ gisa kalkulatzen da, non $S$ elektroi parekatu gabeen spinen batura den. Elektroi guztiak parekatuta dituen atomo batek $S=0$ du eta 1eko anizkoiztasuna (singletea). Parekatu gabeko elektroi bakar batek $S=1/2$ eta 2ko anizkoiztasuna ematen du (bikoiztea edo dobletea). Anizkoiztasun-balio oker bat esleitzeak Gaussian-ek elektroiak $\alpha$ eta $\beta$ orbitalen artean gaizki banatzea eragiten du; horrek emaitza baliogabetzen du edo SCF zikloaren konbergentzia eragozten du.

:::{admonition} Abisua
:class: warning
Egiaztatu beti spin-anizkoiztasunaren balioa kalkulua bidali aurretik: balio oker batek emaitzak baliogabetzen ditu edo SCF konbergentzia eragozten du.
:::

## Prozedura

:::{admonition} Adi
:class: danger
Derrigorrezko egiaztapena kalkulu bakoitzaren ondoren: ireki `.log` fitxategia testu-editorearekin eta ziurtatu amaierako lerro zehatz hau agertzen dela:
{{termination_ok}}
:::

### 1. urratsa: GaussView ireki eta atomoa marraztu

1. Ireki GaussView aplikazioen menutik edo sistemaren abiarazletik.
2. Ireki elementuen zatien paleta **View → Element Fragments** bidez (edo goiko tresna-barrako taula periodikoaren ikonoa sakatuz).
3. Hautatu kalkulatu nahi den elementu kimikoa (adibidez, karbonoa, **C**).
4. Egin klik bakar bat ezkerreko botoiarekin erdiko marrazketa-leihoan. Loturarik gabeko zentro atomiko isolatu bat agertuko da.

### 2. urratsa: Atomo neutroaren kalkulua konfiguratu

1. Joan **Calculate → Gaussian Calculation Setup** menura.
2. **Job Type** fitxan, hautatu **Energy**.
3. **Method** fitxan, konfiguratu kalkuluaren parametroak:

| Eremua | Balioa |
|---|---|
| Method | **HF** |
| Basis Set | **STO-3G** |
| Charge | **0** |
| Spin (Multiplicity) | Kontsultatu atomo neutro bakoitzaren anizkoiztasun-taula |

4. **Title** fitxan, idatzi deskribapen identifikatzaile bat (adibidez, `C neutro HF STO-3G`).
5. **Additional Keywords** fitxan, idatzi zehatz-mehatz: `pop=full`. Argibide honek orbital molekular guztien energiak sartzen ditu irteera-fitxategian.

Erreferentziazko anizkoiztasun-taula ($2S+1$):

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
:alt: Hartree-Fock kalkuluaren konfigurazioa pop=full aukerarekin karbono-atomoarentzat
:width: 85%
:align: center
:::

### 3. urratsa: Kalkulua abiarazi eta fitxategia gorde

1. Sakatu **Submit** botoia **Gaussian Calculation Setup** leihoaren behealdean.
2. Gordetzeko elkarrizketa-koadroan, zehaztu `.gjf` sarrera-fitxategiaren izena (adibidez, `C_neutro_HF_STO3G.gjf`) eta gorde laborategiko lan-direktorioan: `{{practicas_folder}}`.
3. Berretsi elkarrizketa-koadroa lehenik **Save** eta ondoren **Submit** sakatuz.
4. Begiratu exekuzio-egoera GaussView-ren beheko barran kalkulua amaitu arte (segundo gutxi batzuk elementu arinentzat).

### 4. urratsa: Amaiera zuzena egiaztatu

1. Ireki sortutako `.log` fitxategia (`C_neutro_HF_STO3G.log`) sistemako testu-editorearekin (**File → Open** editorean edo eskuineko klik fitxategiaren gainean).
2. Joan fitxategiaren amaierara **Ctrl + Fin** (edo Ctrl + End) sakatuz.
3. Egiaztatu fitxategiaren azken lerroa zehazki bat datorrela honekin: `{{termination_ok}}`. Agertzen ez bada, kalkuluak huts egin du eta haren datuak ezin dira erabili.

:::{figure} /_static/capturas/08_koopmans_log_terminacion_normal.png
:alt: Gaussian 16-ren amaiera normala .log irteera-fitxategiaren amaieran
:width: 85%
:align: center
:::

### 5. urratsa: E(N) energia osoa irakurri

1. Testu-editorean irekitako `.log` fitxategian, sakatu **Ctrl + F** bilaketa aktibatzeko.
2. Idatzi bilaketa-testua: `SCF Done`.
3. Kokatu energia osoa `SCF Done:  E(RHF) = ...` lerroan (1eko anizkoiztasuna duten geruza itxiko sistemetan) edo `SCF Done:  E(ROHF) = ...` lerroan (1 ez den anizkoiztasuna duten geruza irekikoetan).
4. Kopiatu zenbakizko balioa unitate atomikoetan (A.U. / Hartrees) eta itsatsi emaitzen taulako $E(N)$ zutabean.

### 6. urratsa: HOMOaren orbital-energia irakurri eta orbitala bistaratu

1. **Zenbakizko irakurketa `.log` fitxategian:**
   - Editorean irekitako `.log` fitxategian, bilatu **Ctrl + F** bidez testu hau: `Alpha occ. eigenvalues`.
   - Kokatu `Alpha occ. eigenvalues --` azken lerroko azken zenbakia. Zenbakizko balio hori energia goreneko orbital okupatuaren energiari dagokio, $\varepsilon_{\text{HOMO}}$ (Hartree-tan).
   - Kokatu berehalako hurrengo `Alpha virt. eigenvalues --` lerroko lehen zenbakia, energia baxueneko orbital hutsari dagokiona ($\varepsilon_{\text{LUMO}}$).
   - Kopiatu $\varepsilon_{\text{HOMO}}$ balioa (Hartree-tan) emaitzen taulako dagokion zutabean.

2. **Egiaztapena eta bistaratzea GaussView-n:**
   - GaussView-n, kalkulutik sortutako `.chk` fitxategia ireki eta **Results → MOs** menura joko dugu.
   - **New Gaussian MOs** fitxan energia-mailen diagrama eta orbitalen okupazioa ikusiko ditugu $\alpha$ eta $\beta$ spinetarako. Karbono neutroaren kasuan (triplete egoeran), energia goreneko orbital okupatuak ($\alpha$, 4. orbitala) $-0.32803\text{ Ha}$-ko energia du.

:::{figure} /_static/capturas/07b_koopmans_gv_orbitales_c.png
:alt: Energia-mailen diagrama eta Alpha zein Beta orbitalen okupazioa Results MOs leihoan
:width: 85%
:align: center
:::

   - Orbitalaren hiru dimentsioko banaketa sortzeko, leiho horren barruko **Visualize** fitxara joko dugu. 4. orbitala (HOMO) hautatuko dugu, **Isovalue** eremuan `0.01` ezarri eta **Update** sakatuko dugu. Ezkerreko azpileihoan $2p$ orbital atomikoaren bi lobuluak agertuko dira.

:::{figure} /_static/capturas/09_koopmans_gv_orbital_homo.png
:alt: HOMO orbitalaren (2p) 3D gainazala sortzea 0.01 isobalioarekin Visualize fitxan
:width: 85%
:align: center
:::

### 7. urratsa: A⁺ katioia konfiguratu eta kalkulatu

1. Itzuli GaussView-ra zentro atomiko bera pantailan duzula.
2. Ireki berriro **Calculate → Gaussian Calculation Setup** panela.
3. **Method** fitxan, aldatu ondorengo parametroak:
   - **Charge**: aldatu `0`tik `1`era.
   - **Spin**: egokitu espezie kationikoari dagokion anizkoiztasunera (ikus beheko taula). HOMO orbitalean elektroi bat erauztean, parekatu gabeko elektroien kopurua aldatu egiten da.
4. Mantendu **Job Type** `Energy` moduan, **Method** `HF` moduan, **Basis Set** `STO-3G` moduan eta `pop=full` gako-hitza **Additional Keywords** eremuan.
5. **Title** fitxan, idatzi: `C cation HF STO-3G`.
6. Sakatu **Submit**, gorde izen adierazgarri batekin (adibidez, `C_cation_HF_STO3G.gjf`) `{{practicas_folder}}` karpetan eta berretsi bidalketa.
7. Egiaztatu amaiera zuzena `.log` berrian eta atera $E(A^+)$ energia osoa `SCF Done` lerrotik.

| Eremua | Neutroa | Katioia |
|---|:---:|:---:|
| Charge | 0 | +1 |
| Spin | Neutroaren anizkoiztasuna | Katioiaren anizkoiztasuna |

### 8. urratsa: Ionizazio-energiak kalkulatu

1. Kalkulatu ionizazio-energia diferentzia zuzenaren bidez ($\text{IE}_{\Delta E}$):

   $$\text{IE}_{\Delta E} = \bigl[E(A^+) - E(A)\bigr] \times 27.2114 \quad [\text{eV}]$$

2. Kalkulatu Koopmans-en teoremaren zenbatespena ($\text{IE}_{\text{Koopmans}}$):

   $$\text{IE}_{\text{Koopmans}} = -\varepsilon_{\text{HOMO}} \times 27.2114 \quad [\text{eV}]$$

3. Erregistratu bi balioak elektroi-voltetan datu-taulan eta kalkulatu ehuneko desbiderapena erreferentziazko balio esperimentalarekiko.

## Emaitzak eta analisia

Kalkulatutako atomo bakoitzeko, `.log` fitxategitik ateratako bi energiak erregistratuko ditugu eta ionizazio-energiaren bi zenbatespenak kalkulatuko ditugu. Ondorengo taulak balioak Hartree-tan eta dagoeneko eV-etara bihurtutako emaitzak biltzen ditu. Erreferentziako balio esperimentalak ere sartzen dira ehuneko errorea kalkulatzeko.

---

## Bibliografia

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. 9. kap. (Egitura elektroniko atomikoa).
- NIST Chemistry WebBook, https://webbook.nist.gov (ionizazio-energien datu esperimentalak).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} 🚀 Aurrerago joateko (hautazkoa)
:color: success
:icon: rocket

Esplorazio honek oinarri-funtzioen multzoa zabaltzean emaitzaren kalitatea nola aldatzen den aztertzen du. Karbono-atomo neutroaren kalkulua tamaina desberdineko hiru oinarrirekin errepikatuko dugu, eta HOMOaren energia zein Koopmans-ek zenbatetsitako ionizazio-energia balio esperimentalarekin alderatuko ditugu. Prozedura praktika nagusiaren berdina da: **Gaussian Calculation Setup → Method** leihoan **Basis Set** eremua bakarrik aldatuko dugu.

| Oinarria | $\varepsilon_{\text{HOMO}}$ (Ha) | IE$_{\text{Koopmans}}$ (eV) | IE exp. (eV) | Errorea (%) |
|:---:|:---:|:---:|:---:|:---:|
| STO-3G | −0.328 | 8.93 | 11.26 | 20.7 |
| 3-21G | (kalkulatzeke) | (kalkulatzeke) | 11.26 | (kalkulatzeke) |
| 6-311G | (kalkulatzeke) | (kalkulatzeke) | 11.26 | (kalkulatzeke) |

:::{note}
Zer zentzutan aldatzen da $\varepsilon_{\text{HOMO}}$ oinarriaren tamaina handitzean? Gutxitzen al da balio esperimentalarekiko errorea modu monotonoan, ala ba al dago kasurik non oinarri handiago batek ez duen emaitza hobetzen? Erlazionatu desberdintasunak oinarri bakoitzak balentzia-eskualdean dentsitate elektronikoa deskribatzeko duen ahalmenarekin.
:::
::::
