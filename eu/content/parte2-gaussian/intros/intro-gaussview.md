# GaussView-ren sarrera

## Sarrera

Gaussian-en kalkulu bat egiteko, lehenik eta behin, programari esan behar zaio molekula nola dagoen espazioan kokatuta. GaussView zeregin hori errazten duen interfaze grafikoa da: molekula-eredua eraikitzen dugu, kalkulua konfiguratzen dugu eta emaitzak bistaratzen ditugu eskuz fitxategiak editatu beharrik gabe.

## GaussView irekitzea

GaussView ikasgelako ordenagailuaren mahaigainetik edo sistemaren aplikazioen menutik irekitzen da.

## Interfazea: zer ikusten duzu irekitzean

GaussView-ren interfazeak lau lan-eremu ditu. Goiko aldean menu-barra dago, konfigurazio- eta bistaratze-tresnekin. Azpian tresna-barra dago, sarbide azkarreko ikonoekin. Erdiko eremua hiru dimentsioko bistaratze-leihoa da, non molekula eraiki, mugitu eta biratzen dugun saguarekin. Beheko panel batek denbora errealean hautatutako atomoen, atomoen arteko distantzien eta kalkuluaren egoerari buruzko informazioa erakusten du.

:::{figure} /_static/capturas/01_gv_interfaz_principal.png
:alt: Interfaz principal de GaussView
:width: 85%
:align: center
:::

## Molekula bat eraikitzea

GaussView-n molekula bat eraikitzeko, tresna-barrako atomoaren ikonoa sakatzen dugu (**Builder palette**, **View → Builder**-tik ere eskuragarri) zatiak eta elementu kimikoak dituen panela irekitzeko. Nahi dugun elementua hautatzen dugu eta ezkerreko botoiarekin klik egiten dugu erdiko leihoan atomoa kokatzeko. Atomo gehigarriak lehendik dauden atomoetatik gertu gehitzean, programak loturak automatikoki sortzen ditu erradio kobalente estandarretatik abiatuta. Urarentzat ($\text{H}_2\text{O}$), oxigeno-atomo zentral bat jartzea eta bi hidrogeno angelu-posizioetan lotzea nahikoa da. Distantzia zehatzak Gaussian-en geometria optimizatzean doituko dira; beraz, hasierako marrazkiak konektibitate kimikoa soilik irudikatu behar du.

:::{figure} /_static/capturas/02_gv_construccion_h2o_fragmentos.png
:alt: Construcción de la molécula de agua y paleta de fragmentos
:width: 85%
:align: center
:::

:::{admonition} Abisua
:class: warning

Ez egin klik bikoitza ustekabean atzeko planoan: atomoak bikoizten ditu abisatu gabe.

:::

## Akatsak zuzentzea eta desegitea

Azken ekintza desegiteko, **Edit → Undo** edo Ctrl+Z erabiltzen dugu. Atomo edo zati zehatz bat ezabatu nahi badugu, saguarekin hautatzen dugu eta Supr sakatzen dugu. Leihoa guztiz garbitzeko, **Edit → Select All** erabil dezakegu Supr sakatuta, edo lan-eremu berri bat ireki dezakegu **File → New**-tik.

## Hidrogenoak automatikoki gehitzea

**Edit → Add Hydrogens** aukerak marraztutako eskeletoa asetzeko beharrezkoak diren hidrogeno inplizituak automatikoki osatzen ditu. Emaaitzazko egitura beti berrikustea komeni da, esleipen automatikoa nahi den protonazio-egoerarekin bat ez etortzea gerta baitaiteke.

## Molekularen inguruan mugitzea

Egitura ikuskatzeko, bista biratzen dugu ezkerreko botoia sakatuta mantenduz eta kurtsorea mugituz. Zooma saguaren gurpilarekin doitzen dugu. Molekula bistatik galtzen badugu, tresna-barrako zentratze-botoia erabiltzen dugu. Hiru mugimendu horiekin, geometria erraz orientatzen dugu modelatzean eta emaitzak berrikustean.

## Geometria ikustea eta doitzea

Lotura-distantzia bat kontsultatzeko edo doitzeko, lotura-tresna (**Modify Bond**, bi esfera lotuta dituen ikonoa tresna-barran) edo kontsulta-tresna (**Inquire**, **`?`** galdera-ikurra duen ikonoa) hautatzen dugu eta 3D ikuspegian bi atomoetan klik egiten dugu. Agertzen den leihoak uneko distantzia angstrometan erakusten du eta konektibitatea egiaztatzeko aukera ematen du kalkulua abiarazi aurretik.

:::{figure} /_static/capturas/03_gv_medicion_distancia.png
:alt: Medición de distancia de enlace en GaussView
:width: 85%
:align: center
:::

## Fitxategi bat ireki

Fitxategi bat irekitzeko, **File → Open** menura jo behar dugu. Formatu ohikoenak `.gjf` (sarrerako fitxategiak) eta `.log` (Gaussianek sortutako irteerak) dira. Horri esker, saioen artean lanarekin jarraitu edo erreferentziazko egiturak aztertu ditzakegu.

## Kalkulu bat konfiguratu

Konfigurazio-panela **Calculate → Gaussian Calculation Setup** tik irekitzen dugu. **Job Type** fitxan, ataza hautatzen dugu: energia puntuala (*Energy*), geometriaren optimizazioa (*Optimization*) edo maiztasunen kalkulua (*Frequency*). **Method** fitxan, teoria-maila definitu dezakegu: metodo mekanokuantikoa (Hartree-Fock, B3LYP...) eta praktika bakoitzean adierazitako funtzio-basea. **Title Card** atalean, deskribapen labur bat sartzen dugu karaktere berezirik gabe. Azkenik, **Charge & Multiplicity** atalean, karga garbia eta spin-anizkoiztasuna ezartzen ditugu.

:::{admonition} Abisua
:class: warning

Karga eta anizkoiztasuna beti berrikusi Submit sakatu aurretik. Akats batek kalkulu osoa baliogabetzen du.

:::

:::{figure} /_static/capturas/04_gv_setup_method_hf.png
:alt: Configuración del cálculo en Gaussian Calculation Setup
:width: 85%
:align: center
:::

## Kalkulua abiarazi

Parametroak konfiguratu ondoren, kalkulua lokalean abiarazten dugu **Submit** sakatuz. GaussViewek jarraipen-leiho bat irekitzen du denbora errealeko irteera-lerroekin. Iraupena segundo batzuetatik (molekula sinpleak eta gutxieneko baseak) minutu batzuetara (sistema handiagoak edo elektroi-korrelazioko metodoak) alda daiteke. Ez dago ezer gehiago egin beharrik kalkulua amaitu arte.

## Kalkulua ondo amaitu dela egiaztatu

Kalkulua amaitzean, irteera-fitxategiko azken lerroak {{termination_ok}} eduki behar du. Horren ordez `Error termination` agertzen bada, kalkulua ez da behar bezala amaitu. Arrazoi ohikoenak hasierako geometria desegokia, konfigurazio bateraezina edo esleitutako memoria-muga gainditzea dira.

:::{admonition} Adi
:class: danger

Emaitzarik idatzi aurretik, beti egiaztatu kalkulua behar bezala amaitu dela, lerro hau bilatuz: {{termination_ok}}

:::

## Emaitzak ikusi

Emaitzak bi modutan kontsultatzen ditugu. Geometria optimizatua, dentsitate elektronikoa edo orbital molekularrak ikusteko, GaussViewen **Results** menua erabiltzen dugu. **Results → Summary** aukerak laburpen-koadro bat aurkezten du, metodoa, basea, kalkulatutako energia elektroniko osoa eta momentu dipolarra bezalako magnitudeekin. Balio numerikoak xehetasun guztiekin ateratzeko, zuzenagoa da `.log` fitxategia testu-editore batekin irekitzea eta dagozkion lerroak bilatzea. Praktika bakoitzaren gidoian adierazten dugu zein termino bilatu eta nola idatzi balio bakoitza.

:::{figure} /_static/capturas/05_gv_summary_resultados.png
:alt: Resumen del cálculo en la ventana Gaussian Calculation Summary de GaussView
:width: 85%
:align: center
:::

## Lana gorde

Sarrerako fitxategia **File → Save** tik gordetzen dugu `.gjf` luzapenarekin. Komeni da nomenklatura argia erabiltzea, molekula eta teoria-maila identifikatzeko (adibidez, `h2o_b3lyp_6311g.gjf`), horrek saioan zehar kalkuluak antolatzea errazten baitu.

---

## Bibliografia

- {{gaussian_cite}}

---

::::{dropdown} Koloreak eta itxura pertsonalizatu
:color: success

:icon: gear

Atzeko kolorea **View → Display Format** menutik aldatzen dugu. **General** fitxan, **Background Color** ondoan dagoen laukian klik egiten dugu eta kolore zuria hautatzen dugu. Leiho horretan bertan, atomo-esferen tamaina pertsonaliza dezakegu **Atom Size** atalean, eta haien kolore-eskema **Atom Colors** atalean. Doikuntza horiek ez dituzte kalkuluak aldatzen, baina atzeko plano zuria erabiltzeak praktiken memoriarentzako kaptura garbiak lortzea errazten du.

:::{figure} /_static/capturas/06_gv_display_background_blanco.png
:alt: Personalización del color de fondo blanco en Display Format
:width: 85%
:align: center
:::

::::
