# JIT Guide: GitHub Colaborativo — QUIFIS2

> Cargado cuando la sesión involucra operaciones Git o GitHub (T010, T011, T018).
> Adaptado del protocolo del monorepo PhD para un colaborador sin experiencia en Git.

---

## Contexto del proyecto

Este repositorio es **colaborativo**: Javier contribuye junto a otros autores (David De Sancho et al.).
Reglas no negociables:
- **Nunca** force-push (`git push --force`)
- **Nunca** borrar ramas o commits ajenos
- **Nunca** hacer commits directos a `main`
- Todo cambio → rama feature → Pull Request → revisión → merge

---

## Flujo de trabajo estándar

### Primer uso: clonar el repo

```bash
# Solo la primera vez
git clone <URL_REPO>   # [EXT: pendiente T001]
cd <nombre-repo>
```

**Antes de clonar:** verificar que el directorio destino esté vacío o no exista. Si ya existe contenido, NO sobreescribir — investigar primero.

### Sincronizar con el repositorio remoto (antes de trabajar)

```bash
git fetch origin
git status         # verificar que no hay cambios sin commitear
git pull origin main
```

### Crear rama para trabajar

```bash
git switch -c practice/p2-a-koopmans   # o el nombre de la práctica
```

Convención de nombres: `practice/p2-X-slug` donde X = {a, b, c, d} y slug = nombre de la práctica.

### Hacer commits

```bash
# Revisar qué se va a commitear
git status
git diff

# Añadir archivos específicos (nunca git add -A sin revisar)
git add book/practices/atomos-koopmans.md

# Usar el script del monorepo
bash toolkit/git/phd_commit.sh docs "quifis2 P2-A: scaffold koopmans stub"
```

Tipos de commit (`<type>`): `docs` (contenido), `feat` (nueva funcionalidad), `fix` (corrección), `style` (formato sin cambio de contenido).

### Antes de abrir un PR

Checklist:
- [ ] `git status` limpio — ningún archivo sin commitear
- [ ] `uv run jupyter-book build book/` sin errores
- [ ] Todos los placeholders `[TEXTO HUMANO]` y `[PROPUESTA]` son intencionales (no olvidados)
- [ ] Ningún archivo de datos binarios (`.chk`, `.fchk`, `.log` de Gaussian) en el commit
- [ ] Revisar `git diff main` — solo los cambios esperados

### Abrir el PR

El PR lo abre **Javier manualmente** en la plataforma (GitHub/GitLab).
CC redacta el texto del PR en español cuando se llega a T018.

Formato del título: `[P2-X] Título de la práctica — descripción breve`  
Ejemplo: `[P2-A] Átomos y Teorema de Koopmans — scaffold inicial`

---

## Archivos que NUNCA deben commitearse

```gitignore
# Añadir a .gitignore del repo
*.chk
*.fchk
*.log          # logs de Gaussian (son grandes y binarios-adyacentes)
_build/        # output de jupyter-book
*.gjf          # inputs de Gaussian (solo si son datos, no plantillas)
```

Excepción: los `.gjf` de ejemplo que van en el libro como plantilla educativa sí pueden commitearse.

---

## Si algo sale mal

### Deshacer el último commit (NO publicado aún)
```bash
git reset --soft HEAD~1   # deshace el commit, mantiene los cambios en staging
```

### Descartar cambios no commiteados en un archivo
```bash
git checkout -- book/practices/atomos-koopmans.md
```

### El PR tiene conflictos con main
```bash
git fetch origin
git rebase origin/main    # rebase, NO merge, para historial limpio
# resolver conflictos manualmente, luego:
git rebase --continue
```

---

## Comunicación con colaboradores

- Preguntas sobre el contenido pedagógico → email o reunión
- Conflictos de merge técnicos → resolver localmente antes de abrir el PR
- Dudas sobre el historial → `git log --oneline --graph` para visualizar
