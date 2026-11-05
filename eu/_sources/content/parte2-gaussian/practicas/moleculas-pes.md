# Energia potentzialaren gainazala

## Sarrera

Lotura kimikoaren egonkortasuna eta molekulen lehentasun konformazionalak nukleoen posizioak aldatzean energia elektronikoa nola aldatzen denaren araberakoak dira. Born-Oppenheimerren hurbilketari esker, aldaketa horiek energia potentzialaren gainazal gisa irudika daitezke, Gaussianen bidez kalkulatutako miaketa geometriko sistematikoen bidez. Praktika honetan, hidrogeno-molekularen disoziazio-kurba aztertzen da, spin-egoera desberdinetarako, eta etanoaren deribatu halogenatuen angelu diedroaren errotazio-profila.

## Helburuak

1. $\text{H}_2$ molekularen energia potentzialaren kurba eraiki, HF/STO-3G-rekin kalkulatutako nukleoarteko distantziaren ($R(\text{H–H})$) miaketa baten bidez, singlete eta triplete egoeretarako.
2. Oreka nuklearreko distantzia ($R_{\text{eq}}$) eta $\text{H}_2$-ren disoziazio-energia zehaztu, kalkulatutako balioak datu esperimentalekin alderatuz.
3. Dihaloetanoen angelu diedroaren miaketa konformazionala egin, anti eta gauche konformeroak identifikatzeko energia potentzialaren gainazalean.
4. Errotazio konformazionalaren oztopoak kuantifikatu, konformazio eklipsatuekiko energia-diferentzia ebaluatuz.

## Kontzeptu gakoak

### Zer da energia potentzialaren gainazal bat?

Born-Oppenheimerren hurbilketaren arabera, energia elektronikoa koordenatu nuklearren funtzio jarraitua da, sistema baten energia potentzialaren gainazala (EPG) definitzen duena:

$$
E = E(\mathbf{R})
$$

Gainazal honen minimoak oreka geometrietako egonkorrei dagozkie, non nukleo bakoitzaren gaineko indarrak nuluak diren eta edozein deformaziok energia handitzen duen. Lehen mailako zela-puntuek ondoko minimoak lotzen dituzte eta erreakzio kimikoen edo aldaketa konformazionalen trantsizio-egoerak adierazten dituzte. Nukleoarteko distantzia handietan, energia potentzialak disoziazio-muga lortzen du, non atomoek elkarri eragiteari uzten dioten.

:::{figure} /_static/figures/eu/pes_1d_esquema.svg
:alt: Curva unidimensional de energía potencial con mínimo de equilibrio, barrera y asíntota de disociación
:width: 60%
:align: center
:::

### Singletea eta tripletea: zergatik da garrantzitsua spina

Singlete egoeran, H₂-ren bi elektroiek spin antiparaleloak dituzte (multiplicitatea 1). Horri esker, espazioaren eskualde bera partekatu eta dentsitate elektronikoa bi nukleoen artean kontzentratu dezakete, elkarren arteko aldarapena pantailatuz eta lotura kobalentea egonkortuz energia-minimo batean oreka-distantzian. Triplete egoeran, berriz, spinak paraleloak dira (multiplicitatea 3) eta Pauliren bazterketa-printzipioak eragozten du bi elektroiak aldi berean nukleoarteko eskualdean egotea. Horregatik, tripletearen energia potentzialaren kurba erabat aldaragarria da ibilbide osoan, eta ez du lotura-minimorik aurkezten.

:::{admonition} Oharra
:class: note

Ikuspegi mekanokuantikotik, singletearen uhin-funtzio espaziala ($^1\Sigma_g^+$) simetrikoa da elektroien permutazioarekiko, eta horrek nukleoarteko karga pilatzea bultzatzen du. Tripletean ($^3\Sigma_u^+$), funtzio espaziala antisimetrikoa da eta nukleoarteko plano nodal bat aurkezten du, non probabilitate-dentsitatea nulua den. Elektroi-dentsitaterik ez dagoenez protoiak pantailatzeko, nukleoarteko aldarapenak distantzia orotan nagusitzen da.

:::

### Angelu diedroa eta analisi konformazionala

Angelu diedroak lotura sinple zentral baten bidez lotutako bi talderen errotazio erlatiboa deskribatzen du, eta X–C–C–X sekuentzia osatzen duten lau atomoen bidez definitzen da, 0° eta 360° arteko tartean. Newmanen proiekzio batean, konformazio bakoitza angelu horrek zehazten du. Anti konformazioak (180°) ordezkatzaile bolumentsuenak posizio kontrajarrietan jartzen ditu, aldarapen esterikoak minimizatuz eta energia-minimo globala konfiguratuz. Gauche konformeroek (60° eta 300°) minimo lokalak osatzen dituzte, elkarrekiko aldarapen handiagoarekin. Kurban maximoak konformazio eklipsatuei dagozkie, eta horien gainjartzeak barne-errotazioko oztopoa zehazten du.

:::{figure} /_static/figures/eu/newman_dihaloetano.svg
:alt: Proyección de Newman de un dihaloetano con las conformaciones anti, gauche y eclipsada anotadas
:width: 70%
:align: center
:::

## Prozedura

### 1. zatia: H₂ molekularen EPG

#### 1. urratsa: H₂ GaussView-n marraztu

1. GaussView ireki.
2. Zatiki-paleta flotagarrian, hidrogeno-atomoa (H) hautatu.
3. Erdiko 3D leihoan klik egin, lehen hidrogeno-atomoa jartzeko.
4. Sortutako atomoaren gainean bigarren klik bat egin, $\text{H}_2$ molekula diatomikoa sortzeko, lotura sinplearekin.

#### 2. urratsa: Miaketa-kalkulua konfiguratu (Scan)

1. GaussView-ko menu-barran, sartu **Calculate → Gaussian Calculation Setup**.
2. **Job Type** fitxan, hautatu **Scan** aukera eta beheko goitibeherako menuan hautatu **Relaxed (Redundant Coord)**.
3. Eskaneatze-koordenatua definitzeko, sartu **Edit → Redundant Coordinates** (edo sakatu koordenatu erredundanteen edizio-botoia).
4. **Redundant Coordinate Editor** elkarrizketa-koadroan:
   - Sakatu **Add** botoia.
   - Goitibeherako menuan hautatu **Bond** eta adierazi **Coordinate** atalean 1 eta 2 atomoak.
   - Hautatu **Scan Coordinate** ekintza motan eta finkatu eskaneatze-parametroak (adibidez, 40 urrats 0.1 Å-ko tamainakoak).
   - Sakatu **Ok** koordenatua baliozkotzeko.
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
| Metodoa | HF | HF (ROHF) |
| Oinarri-multzoa | STO-3G | STO-3G |
| Karga | 0 | 0 |
| Multiplicitatea | 1 | 3 |
| Distantzien tartea | 0,5 Å-tik 4,0 Å-ra | 0,5 Å-tik 4,0 Å-ra |
| Urratsaren gehikuntza | 0,1 Å (35-40 urrats) | 0,1 Å (35-40 urrats) |

:::{figure} /_static/capturas/11_pes_setup_scan_h2.png
:alt: Configuración del barrido de potencial (Scan) para H2 en Gaussian Calculation Setup
:width: 85%
:align: center
:::

:::{figure} /_static/capturas/11a_pes_redundant_coord_h2.png
:alt: Definición de la coordenada de enlace y pasos del barrido en el editor de coordenadas redundantes
:width: 85%
:align: center
:::

#### 3. urratsa: Kalkuluak gorde eta abiarazi

1. **Gaussian Calculation Setup** leihoan, sakatu **Submit** botoia.
2. Gorde singletearen fitxategia izen honekin: `H2_singlete_scan.gjf` `__PROTECTED_BLOCK_24__PES/` karpetan.
3. Berretsi kalkulua hasteko elkarrizketa-koadroa.
4. Errepikatu prozesua multiplicitatea 3ra aldatuz eta gorde izen honekin: `H2_triplete_scan.gjf`.
5. Egiaztatu bi kalkuluak aurrera doazela exekuzio-barran.

#### 4. urratsa: EPG GaussView-n bistaratu

1. GaussView-n, ireki `H2_singlete_scan.log` fitxategia **File → Open** bidez.
2. Sartu **Results → Scan** menuan.
3. Bi dimentsioko grafiko interaktibo bat agertuko da, energia $R(\text{H–H})$ distantziaren aurka erakusten duena.
4. Ireki aldi berean `H2_triplete_scan.log` fitxategia, tripletearen kurba singletearen kurbaren gainean jartzeko ikusteko leiho berean.
5. Behatu singletearen kurbako potentzial-zuloaren forma eta tripletearen kurbako zulo eza.

### 2. zatia: Dihaloetanoaren angelu diedroaren EPG

Konformazio-eskaneatzea egingo da ondorengo hiru dihaloetanoentzat: 1,2-dikloroetanoa, 1,2-dibromoetanoa eta 1,2-diiodoetanoa. Prozedura berdina da hirurentzat; errepikatu, molekula eraikitzeko urratsean halogenoa bakarrik aldatuz.

#### 1. urratsa: Dihaloetanoa marraztu GaussView-n

1. Ireki leiho berri bat GaussView-n (**File → New → Molecule Group**).
2. Eraiki dihaloetanoaren molekula, karbono-katea hautatuz eta bi hidrogeno atomo halogenoz ordezkatuz alboko karbonoetan.
3. Aplikatu aurreko garbiketa geometrikoa **Edit → Clean** bidez.

#### 2. urratsa: Eskaneatze diedroaren kalkulua konfiguratu

1. Sartu **Calculate → Gaussian Calculation Setup** menuan.
2. **Job Type** fitxan, hautatu **Scan**.
3. Definitu barne-koordenatua **Dihedral** motakoa, lotutako lau atomoak hautatuz: $\text{X–C–C–X}$.
4. Zehaztu eskaneatzearen angelu-parametroak:
   - Koordenatua: diedro $\text{X–C–C–X}$.
   - Angelu-tartea: 0°-tik 360°-ra (10° edo 15°-ko urratsetan).
5. **Method** fitxan, konfiguratu:
   - Metodoa: **HF**.
   - Oinarri-multzoa: **STO-3G**.
   - Karga: `0`.
   - Multiplicitatea: `1` (Singlete).
6. **Title** fitxan, idatzi: `Dihaloetano diedro scan HF STO-3G`.

#### 3. urratsa: Gorde, abiarazi eta egiaztatu

1. Gorde fitxategia izen honekin: `dihaloetano_scan.gjf` `__PROTECTED_BLOCK_25__PES/` karpetan.
2. Berretsi kalkulua bidaltzeko **Submit** botoia sakatuz.

#### 4. urratsa: Diedro-kurba ikusi GaussView-n

1. GaussView-n, ireki eskaneatzearen irteera-fitxategia **File → Open** bidez.
2. Sartu **Results → Scan** menuan.
3. Identifikatu gutxieneko lokalak (gauche konformeroa) eta gutxieneko globala (anti konformeroa 180°-tan), baita tarteko errotazio-hesiak ere.

---

## Bibliografia

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10. ed.; Editorial Médica Panamericana, 2018. 11. kap. (Egitura molekularra eta energia potentzialaren gainazalak).
- Clayden, J.; Greeves, N.; Warren, S. *Organic Chemistry*, 2. ed.; Oxford University Press, 2012. 18. kap. (Konformazio-analisia).
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.



::::{dropdown} Urrunago joateko (aukerakoa)
:color: success

:icon: rocket

Aukerako jarduera gisa, errepikatu etanoaren konformazio-eskaneatzea ($\text{CH}_3\text{-CH}_3$) teoria-maila berarekin. Kalkulatutako errotazio-hesia, 3 kcal/mol ingurukoa, nabarmen txikiagoa da dihaloetanoarena baino. Bi profilen konparazio zuzenak erakusten du nola ordezkatzailearen bolumenak, C–X loturaren polaritateak eta halogenoaren elektronegatibotasunak energia-minimoak desplazatzen dituzten eta errotazio-hesia igotzen duten.

::::
