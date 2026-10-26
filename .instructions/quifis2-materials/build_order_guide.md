---
name: quifis2-build-order-guide
description: "Orden de construcción de materiales M_QUIFIS2 — pasadas horizontales por tipo de contenido para evitar deriva de voz"
metadata:
  type: project
---

# Guía de construcción de materiales M_QUIFIS2

**Principio rector:** pasadas horizontales (mismo tipo de contenido en todas las prácticas) antes de pasar al siguiente tipo. Nunca pasadas verticales (práctica A completa antes de empezar B).

## Orden de pasadas

| # | Tipo | Estado | Archivo/Destino |
|---|------|--------|-----------------|
| 1 | Esqueleto global — secciones, objetivos en 2 frases, placeholders | ✅ Completo | `content/*.md` |
| 2 | Ecuaciones y constantes — LaTeX verificado, todas las prácticas | ✅ Completo | `content/equations-reference.md` |
| 3 | Tablas de resultados | ✅ Completo — P2-A sin tabla (Excel colaborativo); P2-B PES es gráfico; P2-C tablas ya en esqueleto; P2-D HOMO/LUMO ya integrados | dentro de cada práctica |
| 4 | Procedimientos GaussView — pasos numerados con rutas de menú | ⬜ Pendiente | dentro de cada práctica |
| 5 | Placeholders de capturas — derivados de los procedimientos | ⬜ Pendiente | dentro de cada práctica |
| 6 | Preguntas — todas las prácticas juntas para consistencia de dificultad | ⬜ Pendiente | dentro de cada práctica |
| 7 | Bloques de intuición física — admonitions, voz analógica, 3-4 frases | ⬜ Pendiente | dentro de cada práctica |
| 8 | Introducción y objetivos — última pasada narrativa | ⬜ Pendiente | dentro de cada práctica |
| 9 | Bibliografía — mecánica, última | ⬜ Pendiente | dentro de cada práctica |

## Postproceso de prosa (pasos 7 y 8)

Tras generar cada bloque de prosa, pasar por fabric antes de insertarlo como `[TEXTO HUMANO]`:

```bash
echo "texto generado" | fabric -p humanize
# o
echo "texto generado" | fabric -p improve_writing
```

## Notas de arquitectura

- Las ecuaciones viven en `content/equations-reference.md` como fuente de verdad; las prácticas las referencian o las copian con el número de versión.
- Las substituciones MyST (`{{ha_to_ev}}`, `{{gaussian_version}}`, etc.) están en `_config.yml` — nunca hardcodear valores numéricos en el texto.
- P2-B (`moleculas-pes.md`) está bloqueada hasta que el profesor confirme el método/base para dihaloetanos.

**Why:** La deriva de voz ocurre cuando las últimas secciones escritas tienen diferente profundidad y estilo que las primeras. Las pasadas horizontales rompen esa dependencia temporal.

**How to apply:** Al iniciar cualquier sesión de redacción, consultar esta tabla, identificar la pasada activa, y trabajar esa pasada en todas las prácticas antes de avanzar al siguiente número.
