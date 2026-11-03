# Geometria molekularra eta Born-Oppenheimer-en hurbilketa

## Sarrera

Molekula baten edozein propietate fisikokimiko zehazteko beharrezkoa da bere atomoen koordenatu espazialak zehaztasunez ezagutzea. Born-Oppenheimer-en hurbilketak nukleoen eta elektroien masen arteko alde handia aprobetxatzen du haien mugimenduak banantzeko; horri esker, banaketa elektronikoa nukleo finkoen gainean ebatzi daiteke. Esparru teoriko honek oinarritzen du koordenatu konstanteetan egindako energia puntualeko kalkuluen eta energia-minimo egonkorrak bilatzera bideratutako geometria-optimizazioen arteko bereizketa.

## Born-Oppenheimer-en hurbilketa

Protoi baten masa elektroiarena baino 1836 aldiz handiagoa da gutxi gorabehera; horregatik, atomoen nukleoak askoz motelago mugitzen dira. Born-Oppenheimer-en hurbilketak denbora-desberdintasun hori baliatzen du nukleoak karga-zentro gelditzat hartuz mugimendu elektronikoa ebazten den bitartean. Horrela, energia elektronikoa aukeratutako nukleo-posizioen menpe parametrikoki dagoen magnitude gisa lortzen da. Banantze hori gabe, edozein molekularen ebazpen mekanokuantikoa konputazionalki bideraezina litzateke.

:::{admonition} Oharra
:class: note
Nukleoak espazio-antolamendu desberdinetan finkatuz eta bakoitzarentzat energia elektronikoa kalkulatuz, potentzial-energiaren gainazala lortzen dugu (PEG, *Potential Energy Surface*). Gainazal hiperdimentsional horren gainean deskribatzen dira nukleoen dinamika, bibrazio molekularra eta erreakzio kimikoen garapena.
:::

## Geometria molekularra: distantziak, angeluak eta diedroak

Molekula baten geometria hiru parametrok definitzen dute: lotura-distantziek (angstrometan, Å), lotura-angeluek (gradutan) eta bihurdura-angelu diedroek (gradutan). Distantziek eta angeluek ondoko atomoen arteko tokiko konektibitatea finkatzen dute; diedroek, berriz, erdiko lotura partekatzen duten planoen arteko errotazio espaziala deskribatzen dute. Gaussian-ek barne-koordenatu hauek erabiltzen ditu gradienteak kalkulatzeko eta geometriak optimizatzeko. GaussView-n hiru parametroak zuzenean neurtu eta bistara ditzakegu ereduaren gainean.

:::{figure} /_static/figures/eu/geometria_molecular.svg
:alt: Lau atomoko kate baten diagrama, lotura-distantzia, lotura-angelua eta angelu diedroa adierazita
:width: 70%
:align: center
:::

## Energia puntuala: mugitu gabe kalkulatzea

Energia puntualeko kalkulu batean (*Single Point*), nukleoen posizioak finko mantentzen dira sarrera-fitxategiko koordenatuen arabera. Geometria konstante horrekin, Gaussian-ek egitura elektronikoa ebazten du atomorik mugitu gabe. Emaitza konformazio horren energia elektroniko osoa da hartree-tan. GaussView-n kalkulu hau **Job Type → Single Point** bidez hautatzen dugu (normalean *Energy* etiketatua).

## Geometria-optimizazioa: minimoa aurkitzea

Geometria-optimizazio batean, Gaussian-ek hasierako egituraren energia kalkulatzen du eta bere deribatuak ebaluatzen ditu nukleo-koordenatuekiko (energiaren gradientea). $A$ nukleo bakoitzaren gainean eragiten duten indar elektrostatikoak kontrako zeinua duen gradienteari dagozkio:

$$\mathbf{F}_A = -\nabla_{\mathbf{R}_A} E(\mathbf{R})$$

Indar horietatik abiatuta, algoritmoak nukleoak desplazatzen ditu energia murrizten den norabidean gertueneko minimorantz. Geometria berri bakoitzean uhin-funtzioa eta indarrak birkalkulatzen ditu. Prozesua errepikatzen da gradientea zero bihurtzen den arte tolerantzia numerikoaren barruan:

$$\nabla_{\mathbf{R}} E \approx \mathbf{0}$$

GaussView-n kalkulu hau **Job Type → Optimization** bidez hautatzen dugu. Ondorengo irudiak potentzial-putzura konbergitzen duen algoritmoaren urratsak erakusten ditu.

:::{figure} /_static/figures/eu/optimizacion_pasos.svg
:alt: Geometria-optimizazioko algoritmoaren segidako urratsak potentzial-energiaren kurbako energia-minimorantz konbergituz
:width: 65%
:align: center
:::

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} 🚀 Zer gertatzen da hasierako geometria oso txarra bada?
:color: success
:icon: rocket

Hasierako geometria oreka-egituratik oso urrun badago, algoritmoak urrats gehiegi beharko ditu agian, minimo lokal batean harrapatuta gera daiteke edo ez du konbergituko. `.log` fitxategian egoera hau identifikatzen da optimizazio-zikloen mugara iristen denean konbergentzia-irizpideak bete gabe. Hori saihesteko, komeni da molekulak GaussView-ren fragmentu estandarrak erabiliz eraikitzea, kimikoki arrazoizkoak diren hasierako distantziak eta angeluak ematen baitituzte.

::::

::::{dropdown} 🚀 Gehiago gradienteei eta optimizazio-algoritmoei buruz
:color: success
:icon: rocket

Gaussian-en optimizazio-algoritmo lehenetsiek (hala nola Berny metodoak) quasi-Newton motako teknikak erabiltzen dituzte, hessiarraren (bigarren deribatuen matrizearen) hurbilketa iteratiboki eguneratzen dutenak minimorantz egin beharreko desplazamendua proiektatzeko. Ziklo bakoitzak uhin-funtzioa eta gradiente osoa kalkulatzea eskatzen duenez, molekula handiak edo konformazionalki malguak optimizatzeak kalkulu-kostu handia eta dozenaka optimizazio-urrats eska ditzake.

::::
