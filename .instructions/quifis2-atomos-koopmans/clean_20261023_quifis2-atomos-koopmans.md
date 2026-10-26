# Clean — Scaffold P2-A: Átomos y el Teorema de Koopmans
# Formalize topic: quifis2-atomos-koopmans
# Date: 2026-10-23

## Project Context

**Project:** M_QUIFIS2 — teaching materials for "Química Física II: Prácticas de Ordenador"
(undergraduate course, UPV/EHU). Collaborative Jupyter Book in Spanish.

**Working directory:** `/home/javi/ORGANIZED/PHD/M_QUIFIS2`
**Active branch:** `practice/part2-spectroscopy`

## Inviolable Authoring Rules

1. Final published text is written by a human. Claude compiles, formats, and structures only — never generates final prose. All new text blocks are enclosed in MyST admonitions labeled `[TEXTO HUMANO]`.
2. All student-facing content must be in Spanish (Castilian).
3. New content proposed by Claude is labeled `[PROPUESTA]` and requires explicit human acceptance before inclusion.
4. Pedagogy first: chemistry before computing. GaussView steps are the means, not the end.
5. Students are absolute beginners. GaussView graphical interface exclusively — students do not write input files or use the terminal.

## Task Completed

**Target file:** `content/atomos-koopmans.md`
**Status:** Scaffold written and committed to working tree. ✓

**Goal:** Calculate the ionization energy (IE) of atoms from the 1st and 2nd periods using Koopmans' theorem; compare with experimental values; visualize orbitals in GaussView.

## Scientific Specification

**Central equation:**
$$\text{IE} \approx -\varepsilon_{\text{HOMO}}$$

**Unit conversion:** 1 Ha = 27.2114 eV

**Atom multiplicities (2S+1):**
H=2, He=1, Li=2, Be=1, B=2, C=3, N=4, O=3, F=2, Ne=1

**Reference experimental IEs (eV):**
H=13.60, He=24.59, Li=5.39, Be=9.32, B=8.30, C=11.26, N=14.53, O=13.62, F=17.42, Ne=21.56

## Scaffold Structure (as written in content/atomos-koopmans.md)

### Sections

1. **Introducción** — `[TEXTO HUMANO]` block
2. **Objetivos** — `[TEXTO HUMANO]` block with `[PROPUESTA]` for 4 objectives
3. **Fundamento teórico**
   - Hartree-Fock (campo medio) — `[TEXTO HUMANO]`
   - Koopmans' theorem with LaTeX equation — `[TEXTO HUMANO]` for explanation
   - Unit conversion formula (inline, always visible)
4. **Procedimiento** (5 steps)
   - Step 1: Draw atom in GaussView — `[TEXTO HUMANO]` + `{tip}`
   - Step 2: Configure Gaussian Calculation Setup — table of settings + multiplicity table (always visible)
   - Step 3: Launch and verify — `[TEXTO HUMANO]`
   - Step 4: Read HOMO energy — `{tip}` (GaussView path) + `.log` example fragment (always visible)
   - Step 5: Convert and record — formula (always visible)
5. **Resultados y análisis** — table with experimental IEs pre-loaded, blank columns for student data
6. **Visualización de orbitales** — `{tip}` (GaussView path) + `[TEXTO HUMANO]` + `[PROPUESTA]` for screenshot
7. **Preguntas** — `[TEXTO HUMANO]` + `[PROPUESTA]` for 5 questions

### Content Always Visible (no `[TEXTO HUMANO]` required)

- Koopmans equation and unit conversion
- Multiplicity table (all 10 atoms)
- Gaussian Calculation Setup parameter table
- `.log` fragment example (`Alpha occ. eigenvalues --`)
- Results table with experimental IEs pre-filled

## Open Items Requiring Lab Confirmation

| Item | Status | Risk if wrong |
|------|--------|---------------|
| Gaussian version in lab (09 or 16?) | `[CONFIRMAR]` | Termination line text differs |
| Preferred basis set (STO-3G vs 3-21G) | `[CONFIRMAR]` | Affects accuracy of student results |
| Lab working folder / file naming convention | `[CONFIRMAR]` | Students cannot find their files |
| `Results → Summary` availability in lab GaussView version | `[CONFIRMAR]` | Step 4 alternative path needed |

## Formatting Conventions Used

| Admonition | Purpose |
|------------|---------|
| `{note}` with `[TEXTO HUMANO]` | Human-authored narrative sections |
| `{warning}` | Operational safety warnings |
| `{tip}` | GaussView navigation hints |
| `[PROPUESTA]` inside `{note}` | Claude proposals pending human approval |
