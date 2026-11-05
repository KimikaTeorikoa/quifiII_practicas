# Energia eta unitateak Gaussianen

## Sarrera

Egitura elektronikoaren kalkuluek hainbat magnitude numeriko ematen dituzte, molekulen egonkortasunari, erreaktibotasunari eta bibrazioei buruzkoak. Gaussianen irteera-fitxategiak datu horiek biltzen ditu mekanika kuantikoaren berezko hitzarmen eta unitate atomikoak erabiliz. Emaitza horiek behar bezala interpretatzeko, beharrezkoa da energia totala, orbital indibidualen energiak eta bibrazio-maiztasunak bereiztea, eta beharrezko bihurketak aplikatzea elektroi-voltera edo unitate termodinamikoetara.

## Energia totala: zer den eta zergatik den negatiboa

Gaussianek kalkulatutako energia totalak lau ekarpen fisiko hartzen ditu barne: elektroien energia zinetikoa, elektroi eta nukleoen arteko erakarpen elektrostatikoa, elektroien arteko aldarapen coulombiarra eta nukleoen arteko aldarapen elektrostatikoa. Sistema atomiko eta molekular egonkorretan, indar erakargarriak nagusitzen dira aldarapenen gainetik; beraz, energia totala negatiboa da partikula isolatu eta geldikorren egoerarekiko. Balio hori `SCF Done` lerroan agertzen da `.log` fitxategian (edo metodo korrelazionatuaren goiburuan), eta beti unitate atomikoetan (hartree) adierazten da.

:::{admonition} Oharra
:class: note

Mekanika kuantiko molekularrean, energiaren zeroa nukleo eta elektroi infinituki banandu eta geldikorren egoeran kokatzen da ($V = 0$ denean $r \rightarrow \infty$). Lotura edo atomo lotu bat eratzean, energia askatzen da, eta horrek `SCF Done` balioa zenbaki negatiboetan kokatzen du. Zenbat eta negatiboagoa izan balio hori, orduan eta egonkorragoa da sistema osagai isolatuekiko.

:::

## Unitateak: Hartree, eV eta kcal/mol

Gaussianek energia elektronikoak unitate atomikoetan adierazten ditu, hartree (Ha) izenekoetan. Balio horiek datu esperimental edo termodinamikoekin erlazionatzeko, bihurketa-faktore estandarrak erabiltzen ditugu: hartree bat 27,21 elektroi-volt, 627,51 kilokaloria mol-ko edo 2625,5 kilojulio mol-ko da. Kimikan, elektroi-voltak (eV) erabili ohi dira ionizazio-potentzialak, elektroi-afinitateak eta HOMO-LUMO desberdintasunak adierazteko. Kilokaloriak mol-ko (kcal/mol) eta kilojulioak mol-ko (kJ/mol) erreferentziazko unitateak dira aktibazio-oztopoak, erreakzio-beroak eta konformeroen arteko energia-desberdintasunak adierazteko.

| De | A | Faktorea |
|----|---|----------|
| Ha | eV | × {{ha_to_ev}} |
| Ha | kcal/mol | × {{ha_to_kcal}} |

:::{admonition} Abisua
:class: warning

Inoiz ez alderatu bi energia unitate desberdinetan. Bihurtu beti kendu aurretik.

:::

## Energia-desberdintasunak: benetan axola duena

Hartree-tan adierazitako energia absolutua erreferentzia-hitzarmenaren araberakoa da (partikula bereiziak infinituan) eta ez da zuzenean neurtzen laborategian. Horregatik, inoiz ez dira alderatu behar metodo edo oinarri desberdinekin lortutako energia absolutuak. Kimikan garrantzia duen magnitude fisikoa beti da bi egoera edo geometriaren arteko energia erlatiboaren desberdintasuna ($\Delta E$), teoria-maila berean kalkulatuta. Praktika hauetan, edozein analisi termodinamiko, errotazio-hesia edo potentzial-kurba erreferentziazko egitura batekiko igoera erlatibo gisa adierazten dugu.

## Orbitalen energiak: ez nahastu energia totalarekin

Fock matrizea diagonalizatzean lortutako autobalioak orbital indibidualen energiei dagozkie, `.log` fitxategian zerrendatuta `Alpha occ. eigenvalues` (orbital okupatuak) eta `Alpha virt. eigenvalues` (orbital birtualak edo desokupatuak) etiketekin. Balio horiek ez dute sistemaren energia totala adierazten. Orbital okupatu guztien energiak batuz gero, energia errealaren gainestimazio fisiko larria sortuko litzateke, elektroien arteko aldarapena bi aldiz kontabilizatuko bailitzateke. Hori dela eta, energia totala adierazpen independente baten bidez kalkulatzen da eta bereizita erakusten da `SCF Done` lerroan.

## Bibrazio-maiztasunak: emaitza desberdina

Maiztasunen kalkuluak (`freq`) bibrazio-modu normal molekularrak zehazten ditu, alderantzizko zentimetroetan adierazita ($\text{cm}^{-1}$), dimentsio desberdinak dituen magnitude fisikoa, energia totalaren hartree-ekin alderatuta. Balio horiek `.log` fitxategian agertzen dira `Frequencies --` lerroetan. Maiztasun irudikari bat agertzeak (Gaussianek zenbaki negatibo gisa erakusten duena) adierazten du optimizatutako egitura ez dagokiola energia potentzialaren gainazaleko minimo erreal bati, baizik eta trantsizio-egoera edo zela-puntu bati. Kasu horretan, geometria zuzendu eta berriz optimizatu behar da beste edozein propietate fisiko-kimiko aztertu aurretik.

:::{admonition} Abisua
:class: warning

Log-ean maiztasun negatiboak agertzen badira, geometria ez da minimo erreal batera konbergitu. Berriz optimizatu behar da jarraitu aurretik.

:::

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
