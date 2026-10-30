# Química Física II: Prácticas de Ordenador

[![Licencia: CC BY 4.0](https://img.shields.io/badge/Licencia-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/deed.es)
[![Código: MIT](https://img.shields.io/badge/C%C3%B3digo-MIT-yellow.svg)](LICENSE-CODE)

Libro de prácticas de ordenador de la asignatura **Química Física II**
(Grado en Química, UPV/EHU), escrito con
[Jupyter Book](https://jupyterbook.org).

Versión en línea: <https://kimikateorikoa.github.io/quifiII_practicas/>

## Contenido

1. **Modelos sencillos con Python.** Introducción a Python y resolución
   numérica de la ecuación de Schrödinger por diferencias finitas:
   partícula en una caja, pozo de potencial, oscilador armónico y un
   modelo simplificado del enlace químico.
2. **Introducción a la Química Computacional con Gaussian.** Cálculos
   Hartree-Fock y más allá con Gaussian 16 y GaussView: energías de
   ionización y teorema de Koopmans, superficies de energía potencial,
   modos normales y espectroscopía UV-visible.

## Compilar el libro

```bash
pip install -r requirements.txt
jupyter-book build .
```

El HTML queda en `_build/html/`. Cada envío a `master` compila el libro y
lo publica en GitHub Pages (`.github/workflows/deploy.yml`).

## Autores

- [David De Sancho](https://github.com/daviddesancho) (UPV/EHU)
- Xabier López (UPV/EHU), ORCID [0000-0002-2711-3588](https://orcid.org/0000-0002-2711-3588)
- Jose M. Mercero (UPV/EHU), ORCID [0000-0003-4857-6685](https://orcid.org/0000-0003-4857-6685)
- Ion Mitxelena (UPV/EHU), ORCID [0000-0003-1064-5139](https://orcid.org/0000-0003-1064-5139)
- Irene Casademont Reig (DIPC), ORCID [0000-0002-0842-1040](https://orcid.org/0000-0002-0842-1040)
- [Javier Domínguez Calvo](https://github.com/javierdomcal) (DIPC)

## Licencia

El material docente (texto, figuras e imágenes) se distribuye bajo la
licencia
[Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es):
puedes copiarlo, adaptarlo y redistribuirlo citando a sus autores.
Texto legal en [`LICENSE`](LICENSE).

El código (scripts de Python y celdas de código de los notebooks) se
distribuye bajo la licencia [MIT](LICENSE-CODE).
