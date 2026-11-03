# GaussView-rako sarrera

## Sarrera

Gaussian-en kalkulu bat egiteko, lehenik eta behin molekula espazioan nola kokatuta dagoen adierazi behar zaio programari. GaussView zeregin hori errazten duen interfaze grafikoa da: haren bidez eredu molekularra eraikitzen dugu, kalkulua konfiguratzen dugu eta emaitzak bistaratzen ditugu, fitxategiak eskuz editatu beharrik gabe.

## GaussView ireki

GaussView gelako ordenagailuaren mahaigainetik edo sistemako aplikazioen menutik irekitzen da.

## Interfazea: zer ikusten den irekitzean

GaussView-ren interfazeak lau lan-eremu nagusi ditu. Goialdean menu-barra aurkituko dugu, konfigurazio- eta bistaratze-tresnekin. Azpian tresna-barra dago, sarbide azkarreko ikonoekin. Erdiko eremua hiru dimentsioko bistaratze-leihoa da; bertan molekula eraiki, desplazatu eta biratzen dugu saguarekin. Beheko panel batek hautatutako atomoei, atomo arteko distantziei eta kalkuluaren egoerari buruzko denbora errealeko informazioa erakusten du.

:::{figure} /_static/capturas/01_gv_interfaz_principal.png
:alt: GaussView-ren interfaze nagusia
:width: 85%
:align: center
:::

## Molekula bat eraiki

GaussView-n molekula bat eraikitzeko, tresna-barran atomoaren ikonoa sakatuko dugu (**Builder palette**, **View → Builder** bidetik ere eskura daitekeena) elementu kimikoen eta zatien panela irekitzeko. Nahi dugun elementua hautatu eta saguaren ezkerreko botoiarekin klik egingo dugu erdiko leihoan atomoa kokatzeko. Dauden atomoen ondoan atomo gehigarriak gehitzean, programak loturak automatikoki sortzen ditu erradio kobalente estandarretatik abiatuta. Uraren kasuan ($\text{H}_2\text{O}$), nahikoa da erdiko oxigeno-atomo bat jartzea eta bi hidrogeno lotzea gutxi gorabeherako posizio angeluarretan. Distantzia zehatzak Gaussian-en geometria-optimizazioan zehar doituko dira; beraz, hasierako marrazkiak konektibitate kimikoa adieraztea besterik ez du behar.

:::{figure} /_static/capturas/02_gv_construccion_h2o_fragmentos.png
:alt: Ur-molekularen eraikuntza eta zatien paleta
:width: 85%
:align: center
:::

:::{admonition} Abisua
:class: warning
Ez egin ustekabeko klik bikoitzik atzeko planoaren gainean: atomoak bikoizten ditu ohartarazi gabe.
:::

## Erroreak zuzendu eta desegin

Azken ekintza desegiteko **Edit → Undo** edo Ctrl+Z erabiliko dugu. Atomo edo zati zehatz bat ezabatu nahi badugu, saguarekin hautatu eta Ezabatu (Supr) tekla sakatuko dugu. Leihoa erabat garbitzeko **Edit → Select All** eta ondoren Ezabatu erabil ditzakegu, edo lan-eremu berri bat ireki **File → New** menutik.

## Hidrogenoak automatikoki gehitu

**Edit → Add Hydrogens** aukerak automatikoki osatzen ditu marraztutako hezurduraren balentzia asetzeko beharrezkoak diren hidrogeno inplizituak. Emaitza beti berrikustea komeni da, esleipen automatikoa nahi den protonazio-egoeratik desberdina izan baitaiteke.

## Molekulan zehar mugitu

Egitura ikuskatzeko, bista biratuko dugu ezkerreko botoia sakatuta mantenduz kurtsorea mugitzen dugun bitartean. Zooma saguaren gurpiltxoarekin doitzen dugu. Molekula bistatik galtzen badugu, tresna-barrako zentratze-botoia erabiliko dugu. Hiru mugimendu hauekin geometria erraz bideratzen dugu modelatzean eta emaitzen berrikuspenean.

## Geometria ikusi eta doitu

Lotura-distantzia bat kontsultatzeko edo doitzeko, lotura-tresna (**Modify Bond**, tresna-barran bi esfera lotuta dituen ikonoa) edo kontsulta-tresna (**Inquire**, galdera-ikurra **`?`** duen ikonoa) hautatuko dugu eta 3D ikuspegian bi atomoen gainean klik egingo dugu. Leiho gainerakorrak uneko distantzia erakusten du angstrometan eta konektibitatea egiaztatzeko aukera ematen du kalkulua abiarazi aurretik.

:::{figure} /_static/capturas/03_gv_medicion_distancia.png
:alt: Lotura-distantziaren neurketa GaussView-n
:width: 85%
:align: center
:::

## Lehendik dagoen fitxategi bat ireki

Lehendik dagoen fitxategi bat irekitzeko **File → Open** menura joko dugu. Ohiko formatuak `.gjf` (sarrera-fitxategiak) eta `.log` (Gaussian-ek sortutako irteerak) dira; horri esker, saio batetik bestera lana berreskura dezakegu edo erreferentziazko egiturak azter ditzakegu.

## Kalkulu bat konfiguratu

Konfigurazio-panela **Calculate → Gaussian Calculation Setup** menutik irekiko dugu. **Job Type** fitxan kalkulu-mota hautatuko dugu: energia puntuala (*Energy*), geometria-optimizazioa (*Optimization*) edo maiztasunen kalkulua (*Frequency*). **Method** fitxak teoria-maila definitzeko aukera ematen digu: metodo mekanokuantikoa (Hartree-Fock, B3LYP...) eta praktika bakoitzean adierazitako oinarri-funtzioak. **Title Card** atalean deskribapen labur bat sartuko dugu karaktere berezirik gabe. Azkenik, **Charge & Multiplicity** atalean karga garbia eta spin-anizkoiztasuna ezarriko ditugu.

:::{admonition} Abisua
:class: warning
Egiaztatu beti karga eta anizkoiztasuna Submit sakatu aurretik. Hemen egindako errore batek kalkulu osoa baliogabetzen du.
:::

:::{figure} /_static/capturas/04_gv_setup_method_hf.png
:alt: Kalkuluaren konfigurazioa Gaussian Calculation Setup leihoan
:width: 85%
:align: center
:::

## Kalkulua abiarazi

Parametroak konfiguratu ondoren, kalkulua lokalean abiaraziko dugu **Submit** sakatuz. GaussView-k jarraipen-leiho bat irekitzen du denbora errealeko irteera-lerroekin. Iraupena oinarri minimoak dituzten molekula sinpleen kasuan segundo gutxi batzuetakoa da, eta molekula handiagoen edo korrelazio elektronikoko metodoen kasuan minutu batzuetakoa. Ez dago beste ezer egin beharrik kalkulua amaitu arte.

## Kalkulua ondo amaitu dela egiaztatu

Kalkulua amaitzean, irteera-fitxategiaren azken lerroak {{termination_ok}} eduki behar du. Horren ordez `Error termination` agertzen bada, kalkulua ez da behar bezala amaitu. Arrazoi ohikoenak hasierako geometria desegokia, konfigurazio bateraezina edo esleitutako memoria-muga gainditu izana dira.

:::{admonition} Adi
:class: danger
Emaitzarik idatzi aurretik, egiaztatu beti kalkulua ondo amaitu dela lerro hau bilatuz: {{termination_ok}}
:::

## Emaitzak ikusi

Emaitzak bi bidetatik kontsultatzen ditugu. Optimizatutako geometria, dentsitate elektronikoa edo orbital molekularrak bistaratzeko, GaussView-ren **Results** menua erabiliko dugu. **Results → Summary** aukerak laburpen-taula bat aurkezten du metodoarekin, oinarriarekin, kalkulatutako energia elektroniko osoarekin eta une dipolarra bezalako magnitudeekin. Zenbakizko balioak xehetasun osoz ateratzeko, zuzenagoa da `.log` fitxategia testu-editore batekin irekitzea eta lerro garrantzitsuak bilatzea. Praktika bakoitzaren gidoian adierazten dugu zein termino bilatu eta nola erregistratu balio bakoitza.

:::{figure} /_static/capturas/05_gv_summary_resultados.png
:alt: Kalkuluaren laburpena GaussView-ren Gaussian Calculation Summary leihoan
:width: 85%
:align: center
:::

## Lana gorde

Sarrera-fitxategia **File → Save** bidez gordetzen dugu `.gjf` luzapenarekin. Komeni da molekula eta teoria-maila argi identifikatzen dituen nomenklatura erabiltzea (adibidez, `h2o_b3lyp_6311g.gjf`); horrek kalkuluak antolatzea errazten du saioan zehar.

---

## Bibliografia

- {{gaussian_cite}}

---

::::{dropdown} 🚀 Koloreak eta itxura pertsonalizatu
:color: success
:icon: gear

Atzeko planoaren kolorea **View → Display Format** menutik aldatzen dugu. **General** fitxan, klik egingo dugu **Background Color** ondoan dagoen laukitxoan eta kolore zuria hautatuko dugu. Leiho berean atomo-esferen tamaina pertsonaliza dezakegu **Atom Size** atalean eta haien kolore-eskema **Atom Colors** atalean. Doikuntza hauek ez dituzte kalkuluak aldatzen, baina atzeko plano zuria erabiltzeak praktika-txostenerako irudi garbiak lortzea errazten du.

:::{figure} /_static/capturas/06_gv_display_background_blanco.png
:alt: Atzeko plano zuriari dagozkion doikuntzak Display Format atalean
:width: 85%
:align: center
:::

::::
