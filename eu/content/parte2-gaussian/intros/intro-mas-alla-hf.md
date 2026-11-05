# Hartree-Focketik haratago

## Sarrera

Hartree-Focken batez besteko eremuaren tratamenduak ez du kontuan hartzen elektroiek berehalako aldaratze-indarra dutela elkarren artean, elkarreragin coulombiarraren ondorioz, eta horrek elektroi-korrelazioaren energia alde batera uzten du. Muga hori gainditzeko, kimika konputazionalak Hartree-Focken ondorengo metodoak eta dentsitatearen funtzionalaren teoria (DFT) erabiltzen ditu. Bi ikuspegi horiek molekula-energiak eta propietate kimikoak zehaztasun handiagoz kalkulatzeko aukera ematen dute: lehenengoek konfigurazio elektroniko anitz gehitzen dituzte erreferentziazko uhin-funtzio batetik abiatuta, eta DFTk, berriz, truke- eta korrelazio-funtzionalen bidez modelatzen du korrelazioa, hala nola B3LYP.

## Batez besteko eremutik haratago: konfigurazioak gehitzea

Hartree-Focken hurbilketak egoera elektronikoa konfigurazio bakar baten bidez deskribatzen du, hau da, elektroiak orbital okupatuetara esleitzea. Konfigurazioen arteko elkarreraginaren metodoek deskribapen hori hobetzen dute, konfigurazioen konbinazio linealak gehituz, non elektroi bat edo gehiago orbital birtualetara igotzen diren. Zehazki, CISD metodoak erreferentziazko determinatzailetik abiatuta kitzikapen sinple eta bikoitz guztiak barne hartzen ditu. Ikuspegi honek elektroi-korrelazioaren zati handi bat berreskuratzen du, baina Hartree-Focken kostu konputazional eta memoria-kostu askoz handiagoarekin.

## DFT: beste ikuspegi bat

Dentsitatearen funtzionalaren teoriak (DFT) egitura elektronikoaren arazoa beste ikuspegi batetik jorratzen du: uhin-funtzio elektroi anitzekoa espazio-dentsitate elektronikoarekin ordezkatzen du. Hohenberg eta Kohnen teoremen arabera, oinarrizko egoeraren energia zehaztasunez zehazten da hiru dimentsioko dentsitate horren bidez. Metodoaren funtsezko pieza truke- eta korrelazio-funtzionala da, Hartree-Fockek alde batera uzten edo modu osatugabean hurbiltzen dituen efektu elektronikoak modelatzeko ardura duena. Eskuragarri dauden aukeren artean, B3LYP bezalako funtzional hibridoek Hartree-Focken truke zehatzaren zati bat konbinatzen dute DFTren korrelazio-termino propioekin. Tamaina ertaineko molekula organikoentzat, B3LYPk geometriak eta maiztasunak erreproduzitzen ditu, % 3tik beherako errore tipikoekin, HFren antzeko kostu konputazionalarekin.

:::{admonition} Oharra
:class: note

$N$ elektroiko sistema baten uhin-funtzioak $3N$ koordenatu espazialen araberakoa da (horrek ezinezko egiten du kalkulu zehatza molekula ertain edo handientzat), baina dentsitate elektronikoa $\rho(\mathbf{r})$ magnitude behagarria da, hiru aldagai espazialen araberakoa soilik $(x, y, z)$. Murrizketa dimentsional zorrotz horri esker, DFTk elektroi-korrelazioaren efektuak barne har ditzake, Hartree-Fock metodoaren antzeko kostu konputazionalarekin.

:::

---

## Bibliografia

- {{gaussian_cite}}
- Szabo, A.; Ostlund, N. S. *Modern Quantum Chemistry*. Dover, 1996.
