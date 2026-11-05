# Oinarri-funtzioak

## Sarrera

Sistema polielektronikoen orbital atomiko eta molekularrak forma espazial jarraituak dituzte, eta ez dute soluzio analitiko sinplerik onartzen. Horiek konputazionalki irudikatzeko, funtzio matematiko ezagunen multzoak erabiltzen ditugu (normalean gaussiarren konbinazioak), oinarri-funtzioak deiturikoak. Gaussianen oinarria aukeratzeak eragin zuzena du elektroi-hodeia modelizatzeko malgutasun numerikoan, baita emaitzaren zehaztasun fisikoan eta beharrezko kalkulu-denboran ere.

## Ideia nagusia: orbitalak funtzio ezagunekin hurbiltzea

Kimika kuantiko konputazionalean, orbital molekularrak oinarri-funtzioen konbinazio lineal gisa irudikatzen dira. Funtzio gaussiarrak estandarra dira Gaussian bezalako programetan, erakarpen- eta aldarapen-integralak azkar kalkulatzeko aukera ematen baitute. Multzoko funtzio kopurua handitzean, elektroi-dentsitatea zehaztasunez deskribatzeko gaitasun numerikoa hobetzen da. Beraz, oinarri-multzoa aukeratzeak oreka etengabea eskatzen du nahi den zehaztasun fisikoaren eta eskuragarri dagoen kostu konputazionalaren artean.

:::{figure} /_static/figures/eu/sto_vs_gaussianas.svg
:alt: Comparación del orbital 1s exacto con la aproximación STO por una y varias gaussianas
:width: 65%
:align: center
:::

## Zehaztasuna vs kostu konputazionala

Oinarri-multzoaren tamainak kalkulu batek lor dezakeen zehaztasun fisikoaren muga finkatzen du. Atomo bakoitzeko funtzio kopurua handitzean, elektroi-banaketa fideltasun handiagoz deskribatzen da, baina kalkulu-denbora eta memoria-kontsumoa nabarmen handitzen dira. Ondorengo taulak joera kualitatibo hau ilustratzen du bi oinarri ohikoren bidez: STO-3G (oinarri minimoa, azkarra baina hurbildua) eta 6-311G (oinarri hedatua, zehatzagoa eta garestiagoa). Praktika bakoitzaren gidoian adierazten dugu zein oinarri-multzo erabili GaussView-n.

| Oinarria | Tamaina erlatiboa | Kostu erlatiboa |
|----------|------------------|----------------|
| STO-3G   | Txikia           | Baxua          |
| 6-311G   | Handiagoa        | Handiagoa      |

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} Zer esan nahi du notazioak: 6-31G, 6-311G eta polarizazio-funtzioak
:color: success

Pople-ren balentzia banatuko oinarrien notazioan, zenbakiek adierazten dute zenbat funtzio gaussiar primitibok osatzen duten barne-orbital eta balentzia-orbital bakoitza. Adibidez, 6-311G oinarrian, sei gaussiar kontrajartzen dira barne-geruza bakoitzerako, eta balentzia-geruza hiru funtziotan banatzen da, hiru, bat eta gaussiar baten kontrakzioz osatuak. Izartxoak edo `*` atzizkiak polarizazio-funtzioen gehikuntza adierazten du (d motakoak hidrogenoa ez diren atomoetan), angelu-malgutasuna ematen dutenak elektroi-dentsitatearen deformazioak deskribatzeko lotura kimikoa eratzean. GaussView-n, multzo osoa **Method** fitxako goitibeherako menuan hautatzen da.

::::
