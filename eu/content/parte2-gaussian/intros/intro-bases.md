# Oinarri-funtzioak

## Sarrera

Sistema polielektronikoen orbital atomiko eta molekularrek forma espazial jarraituak dituzte, eta ez dute soluzio analitiko sinplerik onartzen. Konputazionalki adierazteko, oinarri-funtzio deritzen funtzio matematiko ezagunen multzoak erabiltzen ditugu (orokorrean gaussiarren konbinazioak). Gaussian-en oinarria aukeratzeak hodei elektronikoa modelatzeko zenbakizko malgutasuna finkatzen du, eta eragin zuzena du bai emaitzaren zehaztasun fisikoan bai behar den kalkulu-denboran.

## Ideia nagusia: orbitalak funtzio ezagunen bidez hurbiltzea

Kimika kuantiko konputazionalean, orbital molekularrak oinarri-funtzio deritzen funtzio ezagunen multzo finitu baten konbinazio lineal gisa adierazten dira. Funtzio gaussiarrak estandarrak dira Gaussian bezalako programetan, erakarpen- eta aldaratze-integralak azkartasun analitiko handiz kalkulatzea ahalbidetzen baitute. Multzoko funtzio-kopurua handitzean, dentsitate elektronikoa zehaztasunez deskribatzeko zenbakizko gaitasuna hobetzen da. Horregatik, oinarri-multzoa aukeratzeak etengabeko oreka eskatzen du lortu nahi den zehaztasun fisikoaren eta eskura dagoen kalkulu-kostuaren artean.

:::{figure} /_static/figures/eu/sto_vs_gaussianas.svg
:alt: 1s orbital zehatzaren eta STO hurbilketaren konparazioa gaussiar baten eta hainbaten bidez
:width: 65%
:align: center
:::

## Zehaztasuna vs kalkulu-kostua

Oinarri-multzoaren tamainak finkatzen du kalkulu batek lor dezakeen zehaztasun fisikoaren muga. Atomo bakoitzeko funtzio-kopurua handitzean banaketa elektronikoa fideltasun handiagoz deskribatzen da, baina kalkulu-denbora eta memoria-kontsumoa nabarmen handitzen dira. Ondorengo taulak joera kualitatibo hori erakusten du maiz erabiltzen diren bi oinarriren bidez: STO-3G (oinarri minimoa, azkarra baina hurbildua) eta 6-311G (oinarri hedatua, zehatzagoa eta garestiagoa). Praktika bakoitzaren gidoian zehazten dugu zein oinarri-multzo erabili GaussView-n.

| Oinarria | Tamaina erlatiboa | Kostu erlatiboa |
|----------|-------------------|-----------------|
| STO-3G   | Txikia            | Baxua           |
| 6-311G   | Handiagoa         | Handiagoa       |

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.

---

::::{dropdown} 🚀 Zer esan nahi du notazioak: 6-31G, 6-311G eta polarizazio-funtzioak
:color: success
:icon: rocket

Pople-ren balentzia zatituko oinarrien notazioan, digituek adierazten dute zenbat funtzio gaussiar primitibok osatzen duten barne- eta balentzia-orbital bakoitza. Adibidez, 6-311G oinarrian sei gaussiar uzkurtzen dira barne-geruzetako orbital bakoitzerako; balentzia-geruza, berriz, hiru, bat eta bat gaussiarrez osatutako hiru funtziotan banatzen da. Izartxoak edo `*` atzizkiak polarizazio-funtzioak gehitu direla adierazten du (d motakoak hidrogenoa ez diren atomoen gainean); hauek malgutasun angeluarra ematen dute lotura kimikoa eratzean dentsitate elektronikoak pairatzen dituen deformazioak deskribatzeko. GaussView-n, multzo osoa **Method** fitxako goitibeherako menuan hautatzen da.

::::
