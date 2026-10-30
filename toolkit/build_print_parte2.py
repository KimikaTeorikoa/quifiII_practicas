"""Genera un único HTML imprimible con toda la Parte 2, en orden de TOC."""

from pathlib import Path
from bs4 import BeautifulSoup

BUILD = Path(__file__).parent.parent / "es/_build/html"
OUT   = Path(__file__).parent.parent / "es/_build/parte2_print.html"

PAGES = [
    BUILD / "content/parte2-gaussian/intros/intro-gaussview.html",
    BUILD / "content/parte2-gaussian/intros/intro-hartree-fock.html",
    BUILD / "content/parte2-gaussian/intros/intro-bases.html",
    BUILD / "content/parte2-gaussian/intros/intro-energias.html",
    BUILD / "content/parte2-gaussian/practicas/atomos-koopmans.html",
    BUILD / "content/parte2-gaussian/intros/intro-born-oppenheimer.html",
    BUILD / "content/parte2-gaussian/intros/intro-mas-alla-hf.html",
    BUILD / "content/parte2-gaussian/practicas/moleculas-pes.html",
    BUILD / "content/parte2-gaussian/practicas/modos-normales.html",
    BUILD / "content/parte2-gaussian/practicas/espectroscopia-uv.html",
]

# Toma CSS del primer archivo
first = BeautifulSoup(PAGES[0].read_text(), "html.parser")
head_links = "\n".join(str(t) for t in first.find_all("link", rel="stylesheet"))
base_url = BUILD.as_uri()

chapters = []
for page in PAGES:
    soup = BeautifulSoup(page.read_text(), "html.parser")
    main = soup.find("div", {"role": "main"}) or soup.find("article") or soup.find("main")
    if main:
        # Convierte rutas relativas de imágenes a absolutas
        for tag in main.find_all(True, src=True):
            src = tag["src"]
            if not src.startswith(("http", "data:", "/")):
                tag["src"] = (page.parent / src).resolve().as_uri()
        chapters.append(str(main))

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Parte 2 — Introducción a la Química Computacional con Gaussian</title>
{head_links}
<base href="{base_url}/">
<style>
  body {{ max-width: 900px; margin: 0 auto; padding: 2rem; font-family: serif; }}
  .chapter-break {{ page-break-before: always; border-top: 2px solid #ccc; margin-top: 3rem; padding-top: 2rem; }}
  @media print {{
    .chapter-break {{ page-break-before: always; }}
    nav, .sidebar, .header-article, .prev-next-area {{ display: none !important; }}
  }}
</style>
</head>
<body>
{"".join(f'<div class="chapter-break">{ch}</div>' for ch in chapters)}
</body>
</html>"""

OUT.write_text(html)
print(f"Escrito: {OUT}")
