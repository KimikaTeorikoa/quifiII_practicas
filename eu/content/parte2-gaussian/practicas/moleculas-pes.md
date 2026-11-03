# Potentzial-energiaren gainazala

## Sarrera

Lotura kimikoaren egonkortasuna eta molekulen lehentasun konformazionalak energia elektronikoa nukleoen posizioak aldatzean nola aldatzen den menpe daude. Born-Oppenheimer-en hurbilketari esker, aldaketa hauek Gaussian-en egindako miaketa geometriko sistematikoen bidez kalkulatutako potentzial-energiaren gainazal gisa adieraz daitezke. Praktika honetan hidrogeno-molekularen disoziazio-kurba aztertzen dugu spin-egoera desberdinetarako, baita etanoaren deribatu halogenatuen angelu diedroaren biraketa-profil energetikoa ere.

## Helburuak

1. $\text{H}_2$ molekularen potentzial-energiaren kurba eraikitzea $R(\text{H–H})$ nukleo arteko distantziaren miaketa baten bidez singlete eta triplete egoeretarako HF/STO-3G mailan.
2. $\text{H}_2$-ren nukleo arteko oreka-distantzia ($R_{\text{eq}}$) eta disoziazio-energia zehaztea, kalkulatutako balioak datu esperimentalekin alderatuz.
3. Dihaloetanoetan angelu diedroaren miaketa konformazionala egitea potentzial-energiaren gainazalean anti eta gauche konformeroak identifikatzeko.
4. Biraketa-hesi konformazionalak kuantifikatzea konformazio eklipsatuekiko energia-diferentzia ebaluatuz.

## Kontzeptu nagusiak

### Zer da potentzial-energiaren gainazal bat?

Born-Oppenheimer-en hurbilketaren pean, energia elektronikoa nukleo-koordenatuen funtzio jarraitu bat da, sistemaren potentzial-energiaren gainazala (PEG) definitzen duena:

$$
E = E(\mathbf{R})
$$

Gainazal honen minimoak oreka-geometria egonkorrei dagozkie, non nukleo bakoitzaren gaineko indarrak nuluak diren eta edozein deformaziok energia handitzen duen. Lehen ordenako zela-puntuek ondoko minimoak lotzen dituzte eta erreakzio kimikoen edo aldaketa konformazionalen trantsizio-egoerak adierazten dituzte. Nukleo arteko distantzia handietan, potentzial-energiak disoziazio-muga lortzen du, non atomoek elkarrekintza izateari uzten dioten.

:::{figure} /_static/figures/eu/pes_1d_esquema.svg
:alt: Dimentsio bakarreko potentzial-energiaren kurba oreka-minimoarekin, hesiarekin eta disoziazio-asintotarekin
:width: 60%
:align: center
:::

### Singletea eta tripletea: zergatik duen garrantzia spinak

Singlete egoeran, H₂-ren bi elektroiek spin antiparaleloak dituzte (1eko anizkoiztasuna). Horri esker espazio-eskualde bera parteka dezakete eta dentsitate elektronikoa bi nukleoen artean kontzentratu, haien elkarrekiko aldarapena pantailaratuz eta lotura kobalentea energia-minimo batean egonkortuz oreka-distantzian. Aldiz, triplete egoeran spinak paraleloak dira (3ko anizkoiztasuna) eta Pauliren bazterketa-printzipioak eragotzi egiten du bi elektroiak nukleo arteko eskualdean aldi berean kokatzea. Hori dela eta, tripletearen potentzial-energiaren kurba erabat aldaratzailea da ibilbide osoan eta ez du inolako lotura-minimorik agertzen.

:::{admonition} Oharra
:class: note
Ikuspegi mekanokuantikotik, singletearen uhin-funtzio espaziala ($^1\Sigma_g^+$) simetrikoa da elektroien permutazioaren aurrean; horrek nukleo arteko karga-metaketa bultzatzen du. Tripletean ($^3\Sigma_u^+$), funtzio espaziala antisimetrikoa da eta nukleo arteko plano nodal bat du, non probabilitate-dentsitatea nulua den. Protoiak pantailaratuko dituen dentsitate elektronikorik ez dagoenez, nukleo arteko aldarapena nagusitzen da edozein distantziatan.
:::

### Angelu diedroa eta analisi konformazionala

Angelu diedroak erdiko lotura bakun batez lotutako bi talderen arteko errotazio erlatiboa deskribatzen du, eta X–C–C–X sekuentzia osatzen duten lau atomoen bidez definitzen da 0° eta 360° arteko tartean. Newman-en proiekzio batean, konformazio bakoitza angelu horren bidez finkatzen da. *Anti* konformazioak (180°) kontrako posizioetan kokatzen ditu ordezkatzaile handienak, aldarapen esterikoak minimizatuz eta energiaren minimo globala osatuz. *Gauche* konformeroek (60° eta 300°) aldarapen handiagoko minimo lokalak osatzen dituzte. Kurbaren maximoak konformazio eklipsatuei dagozkie, eta haien gainjartzeak barne-biraketaren hesi energetikoa finkatzen du.

:::{figure} /_static/figures/eu/newman_dihaloetano.svg
:alt: Dihaloetano baten Newman-en proiekzioa anti, gauche eta eklipsatu konformazioak adierazita
:width: 70%
:align: center
:::

## Prozedura

### 1. Zatia: H₂ molekularen PEG-a

#### 1. urratsa: H₂ marraztu GaussView-n

1. Ireki GaussView.
2. Zatien paleta flotagarrian, hautatu hidrogeno-atomoa (**H**).
3. Egin klik erdiko 3D leihoan lehen hidrogeno-atomoa kokatzeko.
4. Egin bigarren klik bat sortutako atomoaren gainean lotura bakuna duen $\text{H}_2$ molekula diatomikoa sortzeko.

#### 2. urratsa: Miaketa-kalkulua konfiguratu (Scan)

1. GaussView-ren menu-barran, joan **Calculate → Gaussian Calculation Setup** menura.
2. **Job Type** fitxan, hautatu **Scan** aukera eta aukeratu beheko goitibeherako menuan **Relaxed (Redundant Coord)**.
3. Miaketa-koordenatua definitzeko, joan **Edit → Redundant Coordinates** menura (edo sakatu koordenatu erredundanteak editatzeko botoia).
4. **Redundant Coordinate Editor** elkarrizketa-koadroan:
   - Sakatu **Add** botoia.
   - Goitibeherako menuan hautatu **Bond** eta adierazi **Coordinate** atalean **1** eta **2** atomoak.
   - Hautatu **Scan Coordinate** ekintza-motan eta finkatu miaketaren parametroak (adibidez, 40 urrats 0.1 Å-ko tamainarekin).
   - Sakatu **Ok** koordenatua balidatzeko.
5. **Gaussian Calculation Setup** leihora itzulita, **Method** fitxan hautatu:
   - Metodoa: **HF** (Hartree-Fock).
   - Oinarri-multzoa: **STO-3G**.
   - Karga: `0`.
   - Singlete egoerarako: **Spin = Singlet** (Multiplicity = `1`).
   - Triplete egoerarako: **Spin = Triplet** (Multiplicity = `3`).
6. **Title** fitxan, idatzi: `H2 scan HF STO-3G`.
7. **Additional Keywords** fitxan, idatzi: `scan`.

| Parametroa | Singlete egoera | Triplete egoera |
|---|:---:|:---:|
| Method | HF | HF (ROHF) |
| Basis Set | STO-3G | STO-3G |
| Charge | 0 | 0 |
| Multiplicity | 1 | 3 |
| Distantzia-tartea | 0.5etik 4.0 Å-ra | 0.5etik 4.0 Å-ra |
| Urrats-hazkundea | 0.1 Å (35–40 urrats) | 0.1 Å (35–40 urrats) |

:::{figure} /_static/capturas/11_pes_setup_scan_h2.png
:alt: H2-ren potentzial-miaketaren konfigurazioa (Scan) Gaussian Calculation Setup leihoan
:width: 85%
:align: center
:::

:::{figure} /_static/capturas/11a_pes_redundant_coord_h2.png
:alt: Lotura-koordenatuaren eta miaketa-urratsen definizioa koordenatu erredundanteen editorean
:width: 85%
:align: center
:::

#### 3. urratsa: Gorde eta kalkuluak abiarazi

1. **Gaussian Calculation Setup** leihoan, sakatu **Submit** botoia.
2. Gorde singletearen fitxategia izen honekin: `H2_singlete_scan.gjf` lan-direktorioan: `{{practicas_folder}}PES/`.
3. Berretsi elkarrizketa-koadroa kalkulua hasteko.
4. Errepikatu prozesua anizkoiztasuna 3ra aldatuz eta gorde honela: `H2_triplete_scan.gjf`.
5. Egiaztatu bi kalkuluek aurrera egiten dutela exekuzio-barran.

#### 4. urratsa: PEG-a bistaratu GaussView-n

1. GaussView-n, ireki `H2_singlete_scan.log` fitxategia **File → Open** bidez.
2. Joan **Results → Scan** menura.
3. Bi dimentsioko grafiko interaktibo bat agertuko da, energia $R(\text{H–H})$ distantziaren aurrean erakusten duena.
4. Ireki aldi berean `H2_triplete_scan.log` fitxategia tripletearen kurba singletearenaren gainean gainjartzeko bistaratze-leiho berean.
5. Behatu potentzial-putzuaren forma singletearen kurban eta putzurik eza tripletearen kurban.

### 2. Zatia: Dihaloetanoaren diedro-PEG-a

Miaketa konformazionala ondorengo hiru dihaloetanoentzat egingo da: 1,2-dikloroetanoa, 1,2-dibromoetanoa eta 1,2-diyodoetanoa. Prozedura berdina da hirurentzat; errepikatu halogenoa bakarrik aldatuz molekula eraikitzeko urratsean.

#### 1. urratsa: Dihaloetanoa marraztu GaussView-n

1. Ireki leiho berri bat GaussView-n (**File → New → Molecule Group**).
2. Eraiki dihaloetanoaren molekula karbono-katea hautatuz eta bi hidrogeno-atomo halogenoengatik ordezkatuz ondoko karbonoetan.
3. Aplikatu atariko garbiketa geometrikoa **Edit → Clean** bidez.

#### 2. urratsa: Diedro-miaketaren kalkulua konfiguratu

1. Joan **Calculate → Gaussian Calculation Setup** menura.
2. **Job Type** fitxan, hautatu **Scan**.
3. Definitu **Dihedral** motako barne-koordenatua lotutako lau atomoak hautatuz: $\text{X–C–C–X}$.
4. Zehaztu miaketaren angelu-parametroak:
   - Koordenatua: $\text{X–C–C–X}$ diedroa.
   - Angelu-tartea: 0°tik 360°ra (10° edo 15°-ko urratsak).
5. **Method** fitxan, konfiguratu:
   - Metodoa: **HF**.
   - Oinarri-multzoa: **STO-3G**.
   - Karga: `0`.
   - Anizkoiztasuna: `1` (Singletea).
6. **Title** fitxan, idatzi: `Dihaloetano diedro scan HF STO-3G`.

#### 3. urratsa: Gorde, abiarazi eta egiaztatu

1. Gorde fitxategia `dihaloetano_scan.gjf` gisa `{{practicas_folder}}PES/` karpetan.
2. Berretsi kalkulua bidaltzea **Submit** sakatuz.

#### 4. urratsa: Diedro-kurba bistaratu GaussView-n

1. GaussView-n, ireki miaketaren irteera-fitxategia **File → Open** bidez.
2. Joan **Results → Scan** menura.
3. Identifikatu minimo lokalak (gauche konformeroa) eta minimo globala (anti konformeroa 180°-tan), baita tarteko errotazio-hesiak ere.

---

## Bibliografia

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. 11. kap. (Egitura molekularra eta potentzial-energiaren gainazalak).
- Clayden, J.; Greeves, N.; Warren, S. *Organic Chemistry*, 2ª ed.; Oxford University Press, 2012. 18. kap. (Conformational analysis).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} 🚀 Aurrerago joateko (hautazkoa)
:color: success
:icon: rocket

Aukerako jarduera gisa, etanoaren ($\text{CH}_3\text{-CH}_3$) miaketa konformazionala errepikatuko dugu teoria-maila berarekin. Kalkulatutako biraketa-hesia, 3 kcal/mol-etik gertukoa, dihaloetanoarena baino nabarmen txikiagoa da. Bi profilen arteko konparazio zuzenak erakusten du nola ordezkatzailearen bolumenak, C–X loturaren polaritateak eta halogenoaren elektronegatibotasunak energia-minimoak desplazatzen dituzten eta errotazio-hesia igotzen duten.

::::
