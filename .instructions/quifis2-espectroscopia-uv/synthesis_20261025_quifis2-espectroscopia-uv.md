# Synthesis: quifis2-espectroscopia-uv

## 1. Metadata Header

- **Topic:** quifis2-espectroscopia-uv
- **Date:** 2026-10-25
- **Version:** 1.0.0
- **Status:** APPROVED (with open optional questions Q1_01–Q1_03)
- **Completeness Score:** 82%
- **Rounds Required:** 0 (one open optional question; scaffold structurally complete)
- **Sources:** raw_20261025_quifis2-espectroscopia-uv.md,
  acetone_acetonitrile.log.txt, content_notes_practices.md

---

## 2. Scope and Objectives

**Purpose:** Scaffold for P2-D lab practice — TD-DFT calculation of UV-Vis spectra
of carbonyl compounds, effect of substituent and solvent on n→π* absorption.

**Non-Goals:**
- No ab initio excited-state theory derivations.
- No scripting; all data extracted manually from GaussView or .log files.
- Calculated UV values are entirely student-generated; scaffold tables are empty.

---

## 3. Scientific Invariants and Hard Rules

- **Method:** B3LYP/6-311G for geometry optimization
- **TD-DFT keyword:** `td` (activates time-dependent DFT in Gaussian)
- **Solvent model:** PCM via `scrf=(solvent=X)`
- **Reference molecule correction:** `acetone_acetonitrile.log` = formaldehyde (CH₂O),
  NOT acetone — confirmed by stoichiometry. HOMO/LUMO values in scaffold example
  belong to formaldehyde, labeled correctly.
- **HOMO (formaldehyde, MeCN):** −0.27636 Ha (confirmed)
- **LUMO (formaldehyde, MeCN):** −0.06005 Ha (confirmed)
- **Gap → λ formula:** λ (nm) = 1239.8 / (ΔE_gap × 27.2114)
- **Experimental acetone n→π*:** 279 nm (cyclohexane), 264 nm (water) — confirmed
- **TD-DFT example output** (from content_notes): 289.23 nm, f=0.0003, Singlet-A"
  → used as pedagogical example only, not as student result
- **Unit:** λ in nm; energy in eV and Ha; f dimensionless

---

## 4. Technical Specification

**Scaffold file:** `content/espectroscopia-uv.md`
**Calculation files (student-generated):** `cetona_disolvente_opt.gjf`, `cetona_disolvente_td.gjf`
**Save location:** `{{practicas_folder}}EspectroscopiaUV/`

**Key GaussView paths:**
- Job type: Calculate → Gaussian Calculation Setup → Job Type → Energy (for TD-DFT single point)
- Additional keywords field: `td scrf=(solvent=X) geom=connectivity`
- Spectrum visualization: Results → UV-Vis

**Log search strings:**
- `Alpha  occ. eigenvalues` → last value = HOMO
- `Alpha virt. eigenvalues` → first value = LUMO
- `Excited State` → λ and f values

---

## 5. Deliverables Inventory

| ID | Artifact | Type | Status |
|----|----------|------|--------|
| D1 | `content/espectroscopia-uv.md` | DOC | ✅ Created |
| D2 | This synthesis | DOC | ✅ |
| D3 | Experimental λ table (solvents beyond cyclohexane/water) | DOC | ⬜ Q1_01 open |
| D4 | Optional convolved spectrum section | DOC | ⬜ `[TEXTO HUMANO]` |

---

## 6. Dependencies and Risks

- **Formaldehyde log:** methodological reference only — HOMO/LUMO example values confirmed ✅
- **TD-DFT example values:** from content_notes, not a real log — used as pedagogical
  illustration, students generate their own ✅
- **Experimental data gap:** Q1_01 open — solvents beyond cyclohexane/water unconfirmed.
  Default: leave experimental column empty in Table B until professor provides values.
- **50 calculations:** workload is high — Q1_02 asks if scope should be reduced.
  Default: keep full matrix; if time is limited, professor can advise at lab session.

---

## 7. Semantic Revision Changelog

| Version | Date | Tag | Description |
|---------|------|-----|-------------|
| 1.0.0 | 2026-10-25 | Initial | First synthesis; formaldehyde correction applied |
