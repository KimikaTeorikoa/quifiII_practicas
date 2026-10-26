---
topic: quifis2-atomos-koopmans
date: 2026-10-23
author: Javier (human brief) / Formalize pipeline (structure)
version: 1.0.0
status: APPROVED
completeness_score: 87%
rounds_required: 0
sources:
  - raw_20261023_quifis2-atomos-koopmans.md
  - content_briefs.md (Chat 3)
  - content/atomos-koopmans.md (scaffold output)
---

# Synthesis: quifis2-atomos-koopmans

## 1. Metadata Header

- **Topic:** quifis2-atomos-koopmans
- **Date:** 2026-10-23
- **Version:** 1.0.0
- **Status:** APPROVED
- **Completeness Score:** 87%
- **Rounds Required:** 0 (score ≥ 85%, all gaps optional)
- **Project:** M_QUIFIS2 — Química Física II: Prácticas de Ordenador (UPV/EHU)

---

## 2. Scope and Objectives

### Scope

Page `content/atomos-koopmans.md` (Practice P2-A) in the M_QUIFIS2 Jupyter Book.

**Purpose:** Teach undergraduate students to calculate atomic ionization energies via
Koopmans' theorem using HF/STO-3G in GaussView, compare with experiment, and visualize
orbitals.

**Target atoms:** H, He, Li, Be, B, C, N, O, F, Ne (1st and 2nd periods).

**Student profile:** Absolute beginners. No terminal access. GaussView GUI exclusively.

### Non-Goals

- This page does NOT cover DFT, post-HF correlation methods, or basis set convergence tests.
- This page does NOT teach how to install Gaussian or GaussView (covered in `gaussview-intro.md`).
- Students do NOT write `.gjf` input files manually.
- Claude does NOT author final prose — all narrative text is `[TEXTO HUMANO]`.

---

## 3. Scientific Invariants and Hard Rules

### Authoring invariants

1. All new narrative text → `:::{note} [TEXTO HUMANO] :::` admonition.
2. Claude proposals → `[PROPUESTA]` inside `{note}`, require explicit human acceptance.
3. All student-facing text in Spanish (Castilian).
4. GaussView steps as the means, chemistry as the end.

### Physics constants and units

| Constant/conversion | Value |
|--------------------|-------|
| Hartree → eV conversion | 1 Ha = 27.2114 eV |
| Koopmans relation | IE ≈ −ε_HOMO |

### Multiplicities (2S+1)

| H | He | Li | Be | B | C | N | O | F | Ne |
|---|----|----|----|----|---|---|---|---|-----|
| 2 | 1  | 2  | 1  | 2  | 3 | 4 | 3 | 2 | 1  |

### Reference experimental IEs (eV)

| H | He | Li | Be | B | C | N | O | F | Ne |
|---|----|----|----|----|---|---|---|---|-----|
| 13.60 | 24.59 | 5.39 | 9.32 | 8.30 | 11.26 | 14.53 | 13.62 | 17.42 | 21.56 |

### Data integrity

Rule 4.2: No raw scientific data or student results are modified by this scaffold.
The IE experimental values in the table are read-only reference data.

---

## 4. Technical Specification

### Output artifact

`content/atomos-koopmans.md` — MyST Markdown, buildable with `jupyter-book build .`

### Gaussian Calculation Setup parameters

| Tab | Field | Value |
|-----|-------|-------|
| Job Type | Job Type | Energy |
| Method | Method | HF |
| Method | Basis Set | STO-3G (default) |
| Method | Charge | 0 |
| Method | Spin | per multiplicity table |
| Additional Keywords | — | `pop=full` |

### GaussView output reading paths

**Option A (GUI):** Results → Summary → HOMO energy (Ha)

**Option B (.log file):** Search for `Alpha occ. eigenvalues --`; last value = ε_HOMO

### MyST admonition conventions

| Admonition | Role |
|------------|------|
| `{note}` + `[TEXTO HUMANO]` | Human narrative sections |
| `{warning}` | Operational safety (e.g., termination check, wrong multiplicity) |
| `{tip}` | GaussView navigation shortcuts |
| `[PROPUESTA]` inside `{note}` | Claude suggestions pending human approval |

---

## 5. Deliverables Inventory

| # | Artifact | Type | Status |
|---|---------|------|--------|
| D1 | `content/atomos-koopmans.md` (scaffold) | DOC | ✓ DONE |
| D2 | Multiplicity table (10 atoms) | DOC | ✓ in D1 |
| D3 | Results table with experimental IEs pre-loaded | DOC | ✓ in D1 |
| D4 | Koopmans equation + unit conversion (LaTeX) | DOC | ✓ in D1 |
| D5 | `.log` fragment example for ε_HOMO reading | DOC | ✓ in D1 |
| D6 | Human narrative text (all `[TEXTO HUMANO]` blocks) | DOC | ⏳ PENDING (human author) |
| D7 | Lab-specific procedure details | DOC | ⏳ PENDING (after lab confirmation) |

---

## 6. Dependencies and Risks

### Prerequisites

- `gaussview-intro.md` must precede this page in the book (students must know how to use GaussView)
- Gaussian 16 (or 09) installed in lab computers

### Open Items (optional — scaffold works without resolution)

| ID | Item | Default in scaffold | Risk if not confirmed |
|----|------|--------------------|-----------------------|
| C1 | Gaussian version (09 vs 16) | "Gaussian 16" | Different termination line text |
| C2 | Preferred basis set | STO-3G | Students may get poor agreement |
| C3 | Lab working folder / file naming | `[TEXTO HUMANO]` placeholder | Students lose their files |
| C4 | `Results → Summary` availability | Fallback to `.log` provided | None (fallback already in scaffold) |

---

## 7. Semantic Revision Changelog

| Version | Date | Tag | Change |
|---------|------|-----|--------|
| 1.0.0 | 2026-10-23 | INITIAL | Scaffold written; synthesis created. |
