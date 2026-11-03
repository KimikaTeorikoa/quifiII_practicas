# Bibrazio-modu normalak

## Sarrera

Erradiazio infragorriaren xurgapena eremu elektromagnetikoaren eta nukleoen bibrazioen arteko elkarrekintzatik sortzen da. Fenomeno hau modelatzeko, Gaussian-ek bibrazio-maiztasunak kalkulatzen ditu potentzial-energiaren matrize hessiarra diagonalizatuz; horrek mugimendu molekularra oszilazio harmoniko independenteetan deskonposatzen du. Lortutako modu normalen analisiak maiztasun teorikoak ematen ditu, desplazamendu atomikoak GaussView-n bistaratzea ahalbidetzen du eta infragorri-espektroan duten jarduera zehazten du simetria molekularraren arauen arabera.

## Helburuak

1. Ereduzko molekula linealen ($\text{CO}$ eta $\text{CO}_2$) bibrazio-askatasun gradu independenteak kalkulatzea.
2. Geometria molekularra optimizatzea eta maiztasun harmonikoak kalkulatzea B3LYP/6-311G mailako `Opt+Freq` metodo konbinatuaren bidez.
3. Luzapen- eta tolestura-moduei dagozkien desplazamendu atomikoak bistaratzea eta sailkatzea GaussView-ren animazioen bidez.
4. Jarduera espektrala infragorrian ebaluatzea molekularen une dipolarraren aldakuntza ($\partial \vec{\mu}/\partial Q$) eta kalkulatutako intentsitate-balioa (`IR Inten`) egiaztatuz.
5. Maiztasun harmoniko teorikoak xurgapen-banda esperimentalekin alderatzea ez-harmoniotasunaren efektua kuantifikatzeko.

## Kontzeptu nagusiak

### Molekulek bibratu egiten dute: osziladore harmonikoaren eredua

Hurbilketa harmonikoan, nukleoek oreka-geometriaren inguruan oszilatzen dute osziladore mekaniko baten moduan. Lotura zenbat eta zurrunagoa izan (indar-konstante $k$ handiagoa) eta inplikatutako atomoen masa laburtua $\mu$ zenbat eta txikiagoa izan, orduan eta handiagoa da bibrazioaren maiztasuna:

$$\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}$$

$m_1$ eta $m_2$ masaz osatutako molekula diatomiko baterako, masa laburtua honela definitzen da:

$$\mu = \frac{m_1 m_2}{m_1 + m_2}$$

Gaussian-ek indar-konstanteak lortzen ditu PEG-aren minimoan nukleo-desplazamenduekiko energiaren bigarren deribatuak kalkulatuz.

:::{admonition} Oharra
:class: note
Gaussian-ek indar-konstanteak kalkulatzen ditu optimizatutako geometrian nukleo-desplazamenduekiko potentzial-energiaren bigarren deribatuen bidez (matrize hessiarra). Hurbilketa honek Taylor-en serie-garapena termino koadratikoan mozten du eta potentzial harmoniko ideala onartzen du. Benetako lotura molekularrek ez-harmoniotasuna agertzen dutenez nukleo arteko distantzia handiagoetan, kalkulatutako maiztasunek espektroskopia infragorriaren bidez lortutako balio esperimentalak gainestimatzen dituzte modu sistematikoan.
:::

### Modu normalak eta bibrazio-askatasuneko graduak

Modu normal bakoitzean, molekulako nukleo guztiek fasean eta maiztasun bereizgarri bakar batean oszilatzen dute. Masa-zentroaren translazioko 3 graduak eta errotaziokoak deskontatuta (2 molekula linealetan eta 3 ez-linealetan), $N$ atomorentzat posible diren oinarrizko bibrazioen kopurua honela ematen da:

$$\text{Modu normalak} = \begin{cases} 3N - 5 & (\text{molekula lineala, adib. } \text{CO}_2: 3(3)-5 = 4) \\ 3N - 6 & (\text{molekula ez-lineala, adib. } \text{H}_2\text{O}: 3(3)-6 = 3) \end{cases}$$

Masa haztatuko koordenatuetan hessiarra diagonalizatzeak zuzenean ematen ditu maiztasun horiek eta modu bakoitzari lotutako nukleo-desplazamenduen bektoreak.

### Hautaketa-arauak espektroskopia infragorrian

Bibrazio-modu batek erradiazio infragorria xurgatzen du baldin eta soilik baldin nukleoen mugimenduak molekularen une dipolar garbiaren aldakuntza bat eragiten badu orekaren inguruan:

$$\left(\frac{\partial \vec{\mu}}{\partial Q}\right)_0 \neq \mathbf{0}$$

Molekula simetrikoetan, modu batzuek inbertsio-simetria mantentzen dute bibrazioan zehar eta ez dute dipoloa aldatzen: IR-inaktiboak diren moduak dira. Muturreko kasuan, $\text{H}_2$ molekulak ez du inolako IR banda aktiborik: bere dipolo iraunkorra nulua da eta luzapen-bibrazioak ere ez du aldatzen; beraz, espektro infragorria erabat isila da. `.log` fitxategian, modu bakoitzaren jarduera `IR Inten` eremuan biltzen da: balio nulu batek inaktibitatea adierazten du.

:::{admonition} Oharra
:class: note
Erradiazio infragorriaren xurgapenak bibrazio-mugimenduak une dipolar molekularra aldatzea eskatzen du ($\partial \vec{\mu}/\partial Q \neq 0$). $\text{CO}_2$-ren luzapen simetrikoan, inbertsio-simetria mantentzen da eta dipoloaren aldakuntza garbia nulua da; beraz, modua ez da eremu elektromagnetiko intzidentearekin akoplatzen. `.log` fitxategian, inaktibitate hori 0.0000-ko intentsitate infragorriaren balioarekin (`IR Inten`) agertzen da.
:::

### Baldintza operatiboa: geometriaren aldez aurreko optimizazioa

Maiztasunen kalkuluak hasierako geometria PEG-aren benetako minimo bat izatea eskatzen du, bigarren deribatuek puntu geldikor batean bakarrik baitute esanahi fisikoa. Geometria optimizatu gabe badago, hessiarraren autobalio batzuk negatiboak suertatzen dira eta maiztasun irudikariak agertzen dira `.log` fitxategian, baliozko interpretazio bibrazionalik gabe.

:::{admonition} Abisua
:class: warning
Ezinbestekoa da geometria optimizatzea maiztasunak kalkulatu aurretik. Puntu ez-geldikorretan egindako kalkuluak esanahi fisikorik gabeko maiztasun irudikariak sortzen ditu. Praktika honetan `Opt+Freq` aukera konbinatua erabiltzen dugu bibrazio-kalkulua minimo zehatzetik abiatzen dela bermatzeko.
:::

## Prozedura

### 1. urratsa: CO eraiki GaussView-n

Eraiki CO molekula eta aplikatu **Edit → Clean** hasierako geometria arrazoizko bat lortzeko.

### 2. urratsa: Opt+Freq kalkulu konbinatua konfiguratu

1. Joan **Calculate → Gaussian Calculation Setup** menura.
2. **Job Type** fitxan, hautatu **Opt+Freq** aukera. Egiaztatu behealdean geometria-optimizazioaren eta indar-konstante harmonikoen kalkuluaren zereginak aldi berean aktibatuta geratzen direla.
3. **Method** fitxan, konfiguratu kalkulu-parametroak:

| Eremua | Balioa |
|---|---|
| Job Type | Opt+Freq |
| Method | `B3LYP` |
| Basis Set | `6-311G` |
| Charge | **0** |
| Spin (Multiplicity) | **1** |

4. **Title** fitxan, idatzi deskribapen identifikatzaile bat.

### 3. urratsa: Gorde eta abiarazi

1. Sakatu **Submit**, gorde fitxategia `CO_opt_freq.gjf` gisa `{{practicas_folder}}ModoNormales/` karpetan eta berretsi bidalketa.

### 4. urratsa: Optimizatutako lotura-distantzia irakurri

1. GaussView-n, ireki sortutako `.log` fitxategia **File → Open** bidez eta joan **Results → Optimization** atalera azken fotograman kokatzeko.
2. Hautatu bi atomoak beheko barran C–O distantzia irakurtzeko, edo bilatu `! R1    R(1,2)` `.log` fitxategian **Ctrl + F** bidez.

:::{admonition} Oharra
:class: note
B3LYP/6-311G kalkuluak zehaztasun onez erreproduzitzen du CO-ren distantzia esperimentala. Kalkulatutako erreferentziazko balioa $R(\text{C-O}) = 1.1473$ Å da, 1.128 Å-ko balio esperimentalaren aurrean; aldeak oinarri moderatuekin DFT funtzionalek lotura-distantziak gainestimatzeko duten joera sistematikoa islatzen du.
:::

### 5. urratsa: Bibrazio-parametroak atera .log fitxategitik

Bilatu `Frequencies --` `.log` fitxategian **Ctrl + F** bidez. Modu bakoitzerako, idatzi:
- `Frequencies --`: bibrazio-maiztasuna $\text{cm}^{-1}$ unitatetan.
- `Red. masses --`: masa laburtua uma unitatetan.
- `Frc consts  --`: indar-konstantea mdyne/Å unitatetan.
- `IR Inten    --`: xurgapen-intentsitatea km/mol unitatetan.

### 6. urratsa: Modu normalaren animazioa bistaratu

1. GaussView-n, `CO_opt_freq_B3LYP_6311G.log` fitxategia irekita dagoela, joan **Results → Vibrations** menura.
2. Modu normalen zerrendan, hautatu kalkulatutako maiztasunari dagokion errenkada (2063 $\text{cm}^{-1}$).
3. Aktibatu **Start Animation** laukitxoa nukleoen oszilazio-mugimendua ikusteko.
4. Markatu **Show Vectors** laukitxoa nukleo-desplazamenduen geziak bistaratzeko eta atomoak loturaren ardatzean zehar mugitzen direla egiaztatzeko (luzapen-modua).
5. Egiaztatu gezien anplitude erlatiboa: karbono-atomoak, arinagoa denez, oxigenoak baino desplazamendu handiagoa pairatzen du.

### 7. urratsa: Prozedura errepikatu CO₂-rako

1. Eraiki CO₂ GaussView-n eta aplikatu **Edit → Clean** O=C=O geometria lineala lortzeko.
2. Konfiguratu kalkulua parametro berberekin (B3LYP/6-311G, Opt+Freq, karga 0, anizkoiztasuna 1). Gorde `CO2_opt_freq.gjf` gisa eta abiarazi.
3. Behin amaituta, ireki `.chk` edo `.log` fitxategia GaussView-n eta joan **Results → Vibrations** menura.
4. Animatu lau modu normaletako bakoitza eta erregistratu haien maiztasunak eta intentsitateak. Erlazionatu modu bakoitzaren IR jarduera bibrazioak eragiten duen une dipolarraren aldakuntzarekin.

:::{figure} /_static/capturas/14_vibraciones_gv_modos_co2.png
:alt: Vibrations elkarrizketa-koadroa GaussView-n CO2-ren 4 modu normalen zerrendarekin eta haien intentsitate infragorriekin
:width: 85%
:align: center
:::

:::{figure} /_static/capturas/14b_vibraciones_gv_visor_co2.png
:alt: CO2 molekula GaussView-ren 3D ikuspegian
:width: 65%
:align: center
:::

---

## Bibliografia

- {{gaussian_cite}}
- Atkins, P.; De Paula, J. *Química Física*, 10ª ed.; Editorial Médica Panamericana, 2018. 12. kap. (Bibrazio-espektroskopia).
- NIST Chemistry WebBook, https://webbook.nist.gov (CO eta CO₂ molekulen bibrazio-maiztasunen datu esperimentalak).

---

::::{dropdown} 🚀 Aurrerago joateko (hautazkoa)
:color: success
:icon: rocket

Gas-faseko CO-ren infragorri-espektroak, oinarrizko bandaz gain, lerro meheen egitura bat erakusten du bibrazioaren eta errotazioaren arteko akoplamenduaren ondorioz. P eta R adarretako ondoko lerroen arteko banaketa neurtuz ($\Delta\tilde{\nu} \approx 2B$) molekularen inertzia-unea zehaztu dezakegu eta, horretatik abiatuta, C–O oreka-distantzia zehaztasun espektroskopikoarekin kalkulatu. Erreferentziako datuak NIST Chemistry WebBook-en daude.
::::
