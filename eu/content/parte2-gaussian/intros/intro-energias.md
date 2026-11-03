# Energiak eta unitateak Gaussian-en

## Sarrera

Egitura elektronikoaren kalkuluek zenbakizko hainbat magnitude ematen dituzte egonkortasunari, erreaktibotasunari eta bibrazio molekularrei lotuta. Gaussian-en irteera-fitxategiak datu hauek mekanika kuantikoaren berezko hitzarmen eta unitate atomikoak erabiliz biltzen ditu. Emaitza hauek behar bezala interpretatzeko, ezinbestekoa da energia osoa, orbital indibidualen energiak eta bibrazio-maiztasunak elkarrengandik bereiztea, eta beharrezko bihurketak egitea elektroi-voltetara edo unitate termodinamikoetara.

## Energia osoa: zer den eta zergatik den negatiboa

Gaussian-ek kalkulatutako energia osoak lau ekarpen fisiko biltzen ditu: elektroien energia zinetikoa, elektroien eta nukleoen arteko erakarpen elektrostatikoa, elektroien arteko aldarapen coulombiarra eta nukleoen arteko aldarapen elektrostatikoa. Sistema atomiko eta molekular egonkorretan, erakarpen-indarrak nagusitzen zaizkie aldarapen-indarrei; horregatik, energia osoa negatiboa da infinituan pausagunean dauden partikula isolatuen egoerarekiko. Balio hori `.log` fitxategiaren `SCF Done` lerroan ageri da (edo dagokion metodo korrelazionatuaren goiburuan), eta beti unitate atomikoetan (hartree-tan) adierazten da.

:::{admonition} Oharra
:class: note
Mekanika kuantiko molekularrean, energiaren zeroa infinituki bananduta eta pausagunean dauden nukleo eta elektroien egoeran kokatzen da ($V = 0$ balioa $r \rightarrow \infty$ denean). Lotura bat edo atomo lotu bat eratzeak energia askatzen du; horrek `SCF Done` lerroko balioa zenbaki negatiboetan kokatzen du. Balio hori zenbat eta negatiboagoa izan, orduan eta handiagoa da sistemaren egonkortasuna bere osagai isolatuekin alderatuta.
:::

## Unitateak: Hartree, eV eta kcal/mol

Gaussian-ek energia elektronikoak hartree (Ha) izeneko unitate atomikoetan adierazten ditu. Balio hauek datu esperimentalekin edo termodinamikoekin erlazionatzeko, bihurketa-faktore estandarrak erabiltzen ditugu: hartree batek 27.21 elektroi-volt, 627.51 kilokaloria moleko edo 2625.5 kilojoule moleko balio du. Kimikan, elektroi-voltak (eV) erabili ohi dira ionizazio-potentzialetarako, afinitate elektronikoetarako eta HOMO–LUMO diferentzietarako. Kilokaloria moleko (kcal/mol) eta kilojoule moleko (kJ/mol) unitateak erreferentziazkoak dira aktibazio-hesietarako, erreakzio-beroetarako eta konformeroen arteko energia-diferentzietarako.

| Hemendik | Hona | Faktorea |
|----------|------|----------|
| Ha       | eV   | × {{ha_to_ev}} |
| Ha       | kcal/mol | × {{ha_to_kcal}} |

:::{admonition} Abisua
:class: warning
Ez alderatu inoiz bi energia unitate desberdinetan daudenean. Bihurtu beti kendu aurretik.
:::

## Energia-diferentziak: benetan axola duena

Hartree-tan neurtutako energia absolutua erreferentzia-hitzarmenaren menpekoa da (infinituan banandutako partikulak) eta ez da zuzenean neurtzen laborategian. Hori dela eta, metodo edo oinarri desberdinekin lortutako energia absolutuak ez dira inoiz alderatu behar. Kimikan fisikoki esanguratsua den magnitudea beti teoria-maila berean kalkulatutako sistema beraren bi egoera edo geometriaren arteko energia-diferentzia erlatiboa da ($\Delta E$). Praktika hauetan, edozein analisi termodinamiko, errotazio-hesi edo potentzial-kurba erreferentziazko egitura batekiko hazkunde erlatibo gisa adierazten dugu.

## Orbital-energiak: ez nahastu energia osoarekin

Fock-en matrizea diagonalizatzean lortutako autobalioak orbital indibidualen energiei dagozkie, eta `.log` fitxategian agertzen dira `Alpha occ. eigenvalues` (orbital okupatuak) eta `Alpha virt. eigenvalues` (orbital birtualak edo hutsak) etiketen azpian. Balio hauek ez dute sistemaren energia osoa adierazten. Orbital okupatu guztien energiak batzeak benetako energiaren gainestimazio fisiko larria ekarriko luke, elektroien arteko aldarapena bi aldiz kontabilizatuko bailitzateke. Hori dela eta, energia osoa adierazpen independente baten bidez kalkulatzen da eta bereizita erakusten da `SCF Done` lerroan.

## Bibrazio-maiztasunak: emaitza desberdin bat

Maiztasunen kalkuluak (`freq`) molekularen bibrazio-modu normalak zehazten ditu zentimetro alderantzizkotan adierazita ($\text{cm}^{-1}$), energia osoaren hartree-ekin alderatuta dimentsio fisiko desberdinak dituen magnitudea izanik. Balio hauek `.log` fitxategian ageri dira `Frequencies --` lerroetan. Maiztasun irudikari bat agertzeak (Gaussian-ek zenbaki negatibo gisa erakusten duena) adierazten du optimizatutako egitura ez dagokiola potentzial-energiaren gainazaleko benetako minimo bati, baizik eta trantsizio-egoera edo zela-puntu bati. Kasu horretan, geometria zuzendu eta berriro optimizatu behar da beste edozein propietate fisikokimiko aztertu aurretik.

:::{admonition} Abisua
:class: warning
Log fitxategian maiztasun negatiboak agertzen badira, geometriari ez dio benetako minimo batera konbergitu. Berriro optimizatu behar da aurrera egin aurretik.
:::

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
