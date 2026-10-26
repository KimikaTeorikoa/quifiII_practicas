# Diff — raw → clean
# topic: quifis2-atomos-koopmans
# date: 2026-10-23

## Structural Changes

| # | Type | Raw text | Clean text | Reason |
|---|------|----------|------------|--------|
| 1 | Formatting | Unicode box-drawing characters (━━━) for section headers | Markdown `##` headers | MyST compatibility |
| 2 | Restructuring | Inline rules list mixed with task description | Separated into distinct sections | Clarity and auditability |
| 3 | Addition | "Resultado" listed tasks only | Added "Content Always Visible" subsection to distinguish scaffold invariants | Completeness scoring requires it |
| 4 | Addition | Open items scattered in raw | Consolidated into `[CONFIRMAR]` table with risk column | Dispatch needs explicit blockers |

## Bracket Resolutions

| Bracket | Category | Resolution |
|---------|----------|------------|
| `[CONFIRMAR con laboratorio]: versión de Gaussian` | Question-Guidance | → `questions.yaml Q1_01` |
| `[CONFIRMAR]: disponibilidad de Results → Summary` | Question-Guidance | → `questions.yaml Q1_02` |
| `[CONFIRMAR]: base STO-3G vs 3-21G preferida` | Question-Guidance | → `questions.yaml Q1_03` |
| `[CONFIRMAR]: carpeta de trabajo, nombres de archivo` | Question-Guidance | → `questions.yaml Q1_04` |

## No scientific content altered

All multiplicities, experimental IE values, unit conversion factor, and equation form
are preserved verbatim from raw.
