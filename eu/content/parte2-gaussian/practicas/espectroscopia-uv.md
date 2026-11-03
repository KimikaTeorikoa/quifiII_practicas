# Zetonen UV-Vis espektroskopia

## Sarrera

Erradiazio ultramore-ikusgaiaren xurgapenak trantsizio elektronikoak eragiten ditu molekula organikoetan, balentziako orbital okupatuetatik energia handiagoko orbital birtualetara elektroiak sustatzean. Gaussian-en denboraren menpeko dentsitatearen funtzionalaren teoriaren (TD-DFT) bidez, kitzikapen hauek simulatu daitezke dentsitate elektronikoaren berrantolaketa kontuan hartuta. Praktika honetan xurgapen-uhin-luzerak eta osziladore-indarrak kalkulatzen dira zetonetako $n \rightarrow \pi^*$ eta $\pi \rightarrow \pi^*$ trantsizioetarako, eta disolbatzailearen polaritateak espektroaren bandak nola desplazatzen dituen aztertzen da.

## Helburuak

1. Atariko xurgapen-uhin-luzera zenbatestea orbital-energien arteko diferentziatik abiatuta ($\Delta E_{\text{gap}}$ HOMO-LUMO).
2. Singlete egoeretarako eszitazio bertikaleko energiak kalkulatzea TD-DFT metodologia eta B3LYP/6-311G erabiliz.
3. $n \rightarrow \pi^*$ eta $\pi \rightarrow \pi^*$ trantsizio elektronikoak esleitzea haien energiaren eta osziladore-indarraren ($f$) arabera.
4. Uretan dagoen azetonaren desplazamendu solbatokromikoa kuantifikatzea disolbatzailearen polarizazio-eredu jarraituaren bidez (PCM).
5. Kalkulatutako xurgapen-espektroak balio esperimentalekin alderatzea ingurunearen polaritatearen eta alkilo-ordezkatzaileen arabera.

## Kontzeptu nagusiak

### Trantsizio elektronikoak konposatu karbonilikoetan

C=O taldean, bi trantsizio esanguratsuak hauek dira: $n \rightarrow \pi^*$, non oxigenoaren lotura gabeko bikote bakartiko elektroi bat karboniloaren $\pi^*$ orbital antilotzailera igarotzen den, eta $\pi \rightarrow \pi^*$, non elektroia lotura bikoitzaren $\pi$ orbital lotzailetik abiatzen den. $n \rightarrow \pi^*$ trantsizioa 280–300 nm inguruan agertzen da eta intentsitate baxua du; $\pi \rightarrow \pi^*$ trantsizioa, berriz, 250 nm-tik behera kokatzen da eta askoz biziagoa da. Intentsitate-alde hori $f$ osziladore-indarrean islatzen da: zerotik gertuko balioak $n \rightarrow \pi^*$ trantsiziorako eta 0.1–1 ordenakoak $\pi \rightarrow \pi^*$ trantsiziorako.

:::{figure} /_static/figures/eu/orbitales_carbonilo.svg
:alt: Karbonilo taldearen orbital-energia mailen diagrama n→π* eta π→π* trantsizioekin
:width: 55%
:align: center
:::

### HOMO-LUMO gap-a atariko zenbatespen gisa

HOMOaren eta LUMOaren energien arteko aldeak gutxieneko eszitazio-energiaren zenbatespen zuzena ematen du. Elektroi-voltetara eta uhin-luzerara bihurtuta, xurgapenaren eskualde espektrala aurreikusten du kalkulu osoa exekutatu aurretik. Zenbatespen honek trantsizio-energia sistematikoki gainestimatzen du, ez baitu kontuan hartzen egoera kitzikatuaren erlaxazioa.

$$\Delta E_{\text{gap}}\text{ (eV)} = (\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}) \times 27.2114$$

$$\lambda_{\text{zenbatetsia}}\text{ (nm)} = \frac{1239.8}{\Delta E_{\text{gap}}\text{ (eV)}}$$

### Disolbatzailearen efektua: solbatokromismoa

$n \rightarrow \pi^*$ trantsizioan, karboniloaren oinarrizko egoera polaragoa da egoera kitzikatua baino. Disolbatzaile polar batek oinarrizko egoera hobesten eta egonkortzen du, bi egoeren arteko energia-aldea handituz eta banda uhin-luzera txikiagoetarantz desplazatuz (efektu hipsokromikoa edo urdineranzko desplazamendua). Gaussian-ek efektu hau PCM polarizazio-eredu jarraituaren bidez modelatzen du; eredu honek disolbatzailea ingurune dielektriko homogeneo gisa adierazten du, bere konstante dielektrikoaren bidez bereiztua. Hau zehazteko, `scrf=(solvent=izena)` gako-hitza gehitzen da **Additional Keywords** eremuan.

Azetonarentzako erreferentziazko balio esperimentalak:

| Disolbatzailea | $\lambda\ (n \rightarrow \pi^*)$ esperimentala (nm) |
|---|:---:|
| Ziklohexanoa (apolarra) | 279 |
| Ura (oso polarra) | 264 |
| Aldakuntza ($\Delta \lambda$) | −15 nm (urdineranzko desplazamendua) |

:::{admonition} Oharra
:class: note
$n \rightarrow \pi^*$ trantsizioan gertatzen den urdineranzko desplazamendu solbatokromikoa (hipsokromikoa) inplikatutako egoera elektronikoen polaritate desberdinetik dator. Oinarrizko egoeran ($S_0$), karbonilo taldeak une dipolar handia du eta oxigenoaren bikote bakartiek hidrogeno-loturak eratzen dituzte ur bezalako disolbatzaile polar protikoekin. Trantsizio elektronikoan zehar, kargaren birbanaketak $\pi^*$ sistemarantz une dipolarra txikitzen du egoera kitzikatuan ($S_1$); horrek solbatazio bidezko egonkortzea murrizten du eta eszitazio bertikalerako behar den energia handitzen du.
:::

## Prozedura

### A Zatia: Atariko zenbatespena HOMO-LUMO gap-arekin

#### A1 Urratsa: Geometria disolbatzailean optimizatu

1. Eraiki azetona GaussView-n eta aplikatu **Edit → Clean**.
2. Ireki **Calculate → Gaussian Calculation Setup**, hautatu **Job Type → Optimization** eta sartu parametroak:

| Eremua | Balioa |
|---|---|
| Method | `B3LYP` |
| Basis Set | `6-311G` |
| Charge | **0** |
| Spin | **1** |
| Additional Keywords | `scrf=(solvent=acetonitrile)` |

3. Gorde `acetona_MeCN_opt.gjf` gisa `{{practicas_folder}}EspectroscopiaUV/` karpetan eta abiarazi.

#### A2 Urratsa: HOMO eta LUMO autobalioak atera

1. Optimizazioaren `.log` fitxategian (`acetona_MeCN_opt.log`), bilatu **Ctrl + F** bidez: `Alpha  occ. eigenvalues`.
2. Identifikatu `Alpha occ.` azken lerroko azken zenbakizko balioa, HOMO orbitalaren energiari dagokiona ($\varepsilon_{\text{HOMO}}$ hartree-tan).
3. Identifikatu hurrengo `Alpha virt. eigenvalues` lerroko lehen zenbakizko balioa, LUMO orbitalaren energiari dagokiona ($\varepsilon_{\text{LUMO}}$ hartree-tan).
4. Kalkulatu energia-diferentzia $\Delta E_{\text{gap}} = (\varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}) \times 27.2114$ eV-etan.
5. Zenbatetsi xurgapen-uhin-luzera: $\lambda_{\text{zenbatetsia}} = 1239.8 / \Delta E_{\text{gap}}\text{ (eV)}$ nm-tan.
6. Erregistratu lortutako zenbakizko balioak emaitzen A Taulan.

### B Zatia: Xurgapen-espektroaren TD-DFT kalkulua

#### B1 Urratsa: TD-DFT kalkulua konfiguratu

1. GaussView-n, ireki aurreko geometria optimizatuaren fitxategia (`acetona_MeCN_opt.log` edo dagokion `.chk`) **File → Open** bidez.
2. Joan **Calculate → Gaussian Calculation Setup** menura.
3. **Job Type** fitxan, hautatu **Energy** (puntu bakarreko kalkulua oreka-egituraren gainean).
4. **Method** fitxan, mantendu Method **B3LYP**, Basis Set **6-311G**, Charge **0**, Spin **1**.
5. **Title** fitxan, idatzi: `Acetona TD-DFT B3LYP 6-311G MeCN`.
6. Beheko **Additional Keywords** eremuan, idatzi: `td scrf=(solvent=acetonitrile) geom=connectivity`.
7. Sakatu **Submit**, gorde `acetona_MeCN_td.gjf` gisa `{{practicas_folder}}EspectroscopiaUV/` karpetan eta berretsi kalkulua **Save** eta **Submit** bidez.
8. Egiaztatu `{{termination_ok}}` azken lerroa agertzen dela `.log` fitxategian.

#### B2 Urratsa: Egoera kitzikatuen datuak atera .log fitxategitik

1. Ireki `.log` fitxategia (`acetona_MeCN_td.log`) testu-editorean.
2. Bilatu **Ctrl + F** bidez: `Excited State   1`.
3. Atera lehen singlete egoera kitzikatuaren datu kuantitatiboak:
   - Kalkulatutako uhin-luzera ($\lambda$) nanometrotan (nm).
   - Eszitazio-energia elektroi-voltetan (eV).
   - Osziladore-indarra ($f$).
4. Behatu trantsizioari lotutako orbital-lerroak (jatorria eta helmuga) kitzikapen-mota berresteko.
5. Identifikatu 270–300 nm inguruko osziladore-indar txikieneko banda $n \rightarrow \pi^*$ trantsizio gisa.

#### B3 Urratsa: Espektroa GaussView-n bistaratu

1. GaussView-n, ireki `acetona_MeCN_td.log` fitxategia **File → Open** bidez.
2. Joan **Results → UV-Vis** menura.
3. Aztertu sortutako espektro elektroniko sintetikoa:
   - Barra bertikalek trantsizio diskretuak adierazten dituzte, $f$ osziladore-indarrarekiko proportzionala den altuerarekin.
   - Kurba jarraituak profil konboluzionatua erakusten du.
4. Identifikatu $n \rightarrow \pi^*$ banda ahula 250 nm-tik beherako uhin-luzeretan agertzen den $\pi \rightarrow \pi^*$ banda intentsoaren aurrean.

### C Zatia: Disolbatzaile-saila eta solbatokromismoa

Errepikatu azetonaren TD-DFT kalkulua dagoeneko optimizatutako geometriaren gainean, disolbatzailearen gako-hitza bakarrik aldatuz **Additional Keywords** eremuan:

| Disolbatzailea | Additional Keywords |
|---|---|
| Hutsunea (gasa) | `td` |
| Ziklohexanoa | `td scrf=(solvent=cyclohexane)` |
| Kloroformoa | `td scrf=(solvent=chloroform)` |
| Etanola | `td scrf=(solvent=ethanol)` |
| Azetonitriloa | `td scrf=(solvent=acetonitrile)` |
| Ura | `td scrf=(solvent=water)` |

Gorde fitxategi bakoitza izen deskribatzaile batekin `{{practicas_folder}}EspectroscopiaUV/` karpetan eta atera `Excited State 1` ataleko $\lambda$ eta $f$ `.log` bakoitzean.

### D Zatia: Zetona ordezkatuen saila

Errepikatu prozedura osoa (optimizazioa + TD-DFT azetonitrilean) ondorengo lau konposatuentzat:

| Konposatua | Egitura |
|---|---|
| Azetil kloruroa | CH₃–CO–Cl |
| Azetofenona | CH₃–CO–C₆H₅ |
| Azido azetikoa | CH₃–CO–OH |
| Metil etil zetona | CH₃–CO–CH₂CH₃ |

Bakoitzarentzat, atera `Excited State 1` ataleko $\lambda$ eta $f$ eta alderatu $n \rightarrow \pi^*$ bandaren desplazamendua azetonarekiko.

---

## Bibliografia

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. 13. kap. (Espektroskopia elektronikoa).
- Casida, M. E. *Time-Dependent Density Functional Theory for Molecules*. In *Recent Advances in Density Functional Methods*; World Scientific, 1995.
- NIST Chemistry WebBook, https://webbook.nist.gov (erreferentziako xurgapen ultramore-ikusgaiaren espektroak).

---

::::{dropdown} 🚀 Aurrerago joateko (hautazkoa)
:color: success
:icon: rocket

GaussView-k kalkulatutako trantsizio bakoitza barra diskretu gisa erakusten du, $f$-rekiko proportzionala den altuerarekin. Espektro esperimentalarekin alderagarria den profil jarraitu bat lortzeko, barra horiek zabalera egokiko funtzio gaussiarrekin konboluzionatzen ditugu. `.log` fitxategiko egoera kitzikatuen zerrenda kalkulu-orri batera esportatuz eta konboluzioa aplikatuz, bandaren forma erreproduzi dezakegu eta maximoen posizioa NIST Chemistry WebBook-eko datuekin alderatu.
::::
