---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Python programaziorako sarrera
Praktika hauen lehen zatian [Python](https://www.python.org/) programazio-lengoaia
erabiliko dugu. Horretarako, ingurune oso erraz bat baliatuko dugu: *Python
Notebook-ak*, zeinek [Google Colab](https://colab.research.google.com/) bezalako
lankidetza-inguruneetan linean programatzea ahalbidetzen baitute. Baina horietan
sakondu aurretik, laburki bada ere Linux sistema eragilearen lan-ingurunea aipatu
behar dugu, bertan erraztasunez moldatzeko gai izan behar baitugu.

## Linux sistema eragilearekin lan egiten
```{image} https://upload.wikimedia.org/wikipedia/commons/6/69/Linus_Torvalds.jpeg
:alt: linus
:class: bg-primary mb-1
:width: 220px
:align: left
```

```{image} https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg
:alt: tux
:width: 220px
:align: right
```
Linux munduko superordenagailuen % 94k, interneteko zerbitzari gehienek,
finantza-merkataritza gehienak eta Android erabiltzen duten mila milioi
gailuk erabiltzen duten sistema eragilea da.
Sistema eragile hau [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)-ek
sortu zuen, Helsinkiko ikasle batek.
1991n, Torvalds-ek sistema eragile baten nukleoa (*kernel*) idazteko proiektu
bat abiarazi zuen. Produktuari [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel) deitu zion.
1992an, [GNU](https://en.wikipedia.org/wiki/GNU_Project) proiektuak (Software Librearen
Aldeko Fundazioak) Linux lizentziatu zuen lizentzia publiko orokorra (GPL)
erabiliz; horrek mundu osoan garatzaileen komunitate bat sortzea erraztu zuen.
90eko hamarkadaren erdialdean garatzaile ezberdinek Linux-en "banaketak" sortu zituzten.
Linux-ek asko hartu zuen Unix sistema eragiletik, baina kode irekiko eta doako
sistema eragile gisa sortu zen.

## Terminala
Python programazio-lengoaia erabiltzeko hainbat aukera ditugu.
Horietako bat **Linux**eko **terminal** batean **komando-lerroa** erabiltzea da.
Terminala gure ordenagailuarekin elkareragiteko aukera ematen digun programa bat da,
eta beheko irudiaren antzeko itxura du.

![terminal](https://upload.wikimedia.org/wikipedia/commons/2/29/Linux_command-line._Bash._GNOME_Terminal._screenshot.png)

Hainbat "shell" mota daude, baina gu ohikoenean zentratuko gara: Bash edo
[Bourne Again Shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell)).
Garrantzitsua da komando batzuk ezagutzea gure sistema eragilean nabigatzeko,
direktorio baten edukia zerrendatzeko edo fitxategiak kopiatu zein ezabatzeko.
Jarraian horietako batzuk erakusten ditugu:
* Nabigazio- eta Esplorazio-komandoak:
    - `pwd`: Uneko direktorioa erakusten du (Print Working Directory).
    - `ls`: Uneko direktorioko fitxategiak eta direktorioak zerrendatzen ditu.
    - `ls -l`: Xehetasun osagarriekin zerrendatzen du (baimenak, jabea, tamaina, etab.).
    - `cd [direktorioa]`: Zehaztutako direktoriora aldatzen da.
    - `cd ..`: Maila bat igotzen da direktorio-zuhaitzean.
* Fitxategi eta Direktorioen Kudeaketa:
	- `touch [fitxategia]`: Fitxategi huts bat sortzen du.
	- `mkdir [direktorioa]`: Direktorio berri bat sortzen du.
	- `cp [iturburua] [helmuga]`: Fitxategiak edo direktorioak kopiatzen ditu.
	- `mv [iturburua] [helmuga]`: Fitxategiak edo direktorioak mugitzen edo berrizendatzen ditu.
	- `rm [fitxategia]`: Fitxategi bat ezabatzen du.
	- `rm -r [direktorioa]`: Direktorio bat ezabatzen du modu errekurtsiboan.
	- `locate [fitxategia]`: Fitxategi bat bilatzen du sisteman.
* Fitxategiak Ikusi eta Editatu:
	- `cat [fitxategia]`: Fitxategi baten edukia erakusten du.
	- `more [fitxategia]`: Fitxategi bat orrialdeka ikusteko aukera ematen du.
	- `head -n [zenbakia] [fitxategia]`: Lehenengo n lerroak erakusten ditu.
	- `tail [fitxategia]`: Fitxategi baten azken lerroak erakusten ditu.
	- `nano [fitxategia]`: Testu-editore sinple bat irekitzen du.
	- `vim [fitxategia]`: Testu-editore aurreratu bat irekitzen du.

Komando hauek guztiak oso baliagarriak dira gure **fitxategi-sisteman** (*filesystem*)
mugitu ahal izateko, direktorio eta fitxategien zuhaitz bat dena, ondorengo diagraman
erakusten den bezalakoa:

```{image} https://raw.githubusercontent.com/swcarpentry/shell-novice/refs/heads/main/episodes/fig/filesystem.svg
:alt: filesystem 
:width: 400px
:align: center 
```

## Python kalkulagailu gisa
[Python](https://www.python.org/) programazio-lengoaia zein *scripting*-lengoaia bat da.
Beste programazio-lengoaia askotan ez bezala, agindu batzuk exekutatzeko nahikoa da
Python-en interprete batean idaztea. Adibidez, Python erabil dezakegu gure
kalkulagailua ordezkatzeko:

```{code-cell} python
3 + 5 * 4
```

## Python programak exekutatzen
Python kodea exekutatzeko, aukera ugari ditugu. Lehenik eta behin, programa bat
idatz dezakegu testu-editore batean eta terminaletik exekutatu.
Programa hau (`kaixo_mundua.py` izenekoa) honelako sinplea izan liteke:
```python
#!/usr/bin/env python
# Gure lehenengo Python programa
print ("Kaixo mundua!")
```
Gure terminalean, ondoren honako hau idatzi beharko genuke:
```bash
foo@bar:~$ python kaixo_mundua.py
```
Programa Python terminal batean ere exekuta dezakegu, `python` edo `ipython`
tekleatuz gure terminalean.
```shell
foo@bar:~$ python
Python 3.9.16 | packaged by conda-forge | (main, Feb  1 2023, 21:42:20)
[Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Azkenik, praktika hauetan egingo dugun moduan, *Jupyter Notebook* bat erabil genezake.
Notebook-ak IPython-erako interfaze grafikoak dira, kode- eta testu-gelaxkak
konbinatzea ahalbidetzen dutenak.

![jupyter](https://jupyter-notebook.readthedocs.io/en/latest/_images/notebook-running-code.png)

Python oso programazio-lengoaia boteretsua da: ordenagailu-programak idatzi,
datuen analisi interaktiboa egin, web-orriak eraiki edo gure sistema eragilea
kontrola dezakegu berarekin.
Bere potentzial handia eta kodea ulergarria izateari ematen dion garrantzia
kontuan hartuta, Python aproposa da programazioaren munduan hasteko.

![python-flying](https://imgs.xkcd.com/comics/python.png)
