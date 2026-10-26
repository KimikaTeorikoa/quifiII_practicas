# M_QUIFIS2 — Instrucciones locales

## Contexto
Jupyter Book de prácticas de química computacional para alumnos novatos (sin terminal, sin scripting).
Forma parte del monorepo PhD. Las invariantes globales de `/CLAUDE.md` se aplican aquí también.

## Reglas de escritura — carga siempre
Al iniciar cualquier chat de scaffold o redacción de contenido, cargar:
- `.instructions/quifis2-materials/jit_quifis2_style.md` — normas estructurales + reglas anti-LLM-ese (§10)
- `.instructions/quifis2-materials/jit_quifis2_gaussian.md` — convenciones de Gaussian 16 y GaussView

**Las reglas anti-LLM-ese (§10 del JIT de estilo) se aplican a TODO texto generado,
incluyendo placeholders, descripciones de tablas y comentarios de estructura.**

## Suspensión de la norma "sin prosa LLM"
La norma general del monorepo que prohíbe generar prosa con LLM queda suspendida en
este subproyecto bajo la condición de aplicar íntegramente las reglas del §10 del JIT
de estilo. Si esas reglas no se cargan, la norma general vuelve a estar en vigor.

## Build
```bash
uv run jupyter-book build .
```
Los archivos compilados van a `_build/` (gitignoreado excepto el commit de referencia).
