# Hartree-Fock-etik haratago

## Sarrera

Hartree-Fock-en batez besteko eremuaren tratamenduak ez du kontuan hartzen elektroiek elkar aldarazten dutela unean bertan elkarrekintza coulombiarraren ondorioz, korrelazio elektronikoaren energia baztertuz. Muga hori gainditzeko, kimika konputazionalak post-Hartree-Fock metodoetara eta dentsitatearen funtzionalaren teoriara (DFT) jotzen du. Bi ikuspegi hauek energia molekularrak eta propietate kimikoak zehaztasun handiagoz kalkulatzea ahalbidetzen dute: lehenengoek konfigurazio elektroniko anitzak txertatzen dituzte erreferentziako uhin-funtzio batetik abiatuta; DFT-k, berriz, korrelazioa modelatzen du truke- eta korrelazio-funtzionalen bidez, adibidez B3LYP erabiliz.

## Batez besteko eremutik haratago: konfigurazioak gehitzea

Hartree-Fock hurbilketak konfigurazio bakar baten bidez deskribatzen du egoera elektronikoa, hau da, elektroien esleipen finko bat orbital okupatuetara. Konfigurazio-elkarrekintzako metodoek (CI) deskribapen hori hobetzen dute konfigurazioen konbinazio linealak txertatuz, non elektroi bat edo gehiago orbital birtualetara sustatzen diren. Bereziki, CISD metodoak kitzikapen sinple eta bikoitz guztiak barne hartzen ditu erreferentziako determinatzailetik abiatuta. Ikuspegi honek korrelazio elektronikoaren zati handi bat berreskuratzen du, nahiz eta Hartree-Fock-ena baino kalkulu- eta memoria-kostu askoz handiagoa izan.

## DFT: ikuspegi desberdin bat

Dentsitatearen funtzionalaren teoriak (DFT) beste ikuspegi batetik heltzen dio egitura elektronikoaren arazoari: elektroi anitzeko uhin-funtzioaren ordez dentsitate elektroniko espaziala erabiltzen du. Hohenberg eta Kohn-en teoremen arabera, oinarrizko egoeraren energia era zehatzean finkatzen da hiru dimentsioko dentsitate honen bidez. Metodoaren gune nagusia truke- eta korrelazio-funtzionala da, Hartree-Fock-ek alde batera uzten edo era osatugabean hurbiltzen dituen efektu elektronikoak modelatzeaz arduratzen dena. Aukera ugarien artean, B3LYP bezalako funtzional hibridoek Hartree-Fock-en truke zehatzaren zati bat DFT-ren berezko korrelazio-terminoekin konbinatzen dute. Tamaina ertaineko molekula organikoentzat, B3LYP-k % 3tik beherako ohiko errorearekin erreproduzitzen ditu geometriak eta maiztasunak, HF-ren pareko kalkulu-kostuarekin.

:::{admonition} Oharra
:class: note
$N$ elektroiko sistema baten uhin-funtzioa $3N$ koordenatu espazialen menpekoa den bitartean (molekula ertain edo handientzat kalkulu zehatza bideraezina eginez), $\rho(\mathbf{r})$ dentsitate elektronikoa hiru aldagai espazialen $(x, y, z)$ menpeko magnitude behagarria da soilik. Dimentsio-murrizketa nabarmen horri esker, DFT-k korrelazio elektronikoaren efektuak barne har ditzake Hartree-Fock metodoaren pareko kalkulu-kostuarekin.
:::

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
