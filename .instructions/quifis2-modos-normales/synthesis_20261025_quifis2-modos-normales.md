# Synthesis: quifis2-modos-normales

## 1. Metadata Header

- **Topic:** quifis2-modos-normales
- **Date:** 2026-10-25
- **Version:** 1.0.0
- **Status:** APPROVED
- **Completeness Score:** 88%
- **Rounds Required:** 0 (single pass; CO data fully confirmed from logs)
- **Sources:** raw_20261025_quifis2-modos-normales.md, co_b3lyp_opt.log.txt,
  content_notes_practices.md

---

## 2. Scope and Objectives

**Purpose:** Scaffold for P2-C lab practice — calculation and interpretation of normal
vibrational modes for CO and CO₂ using B3LYP/6-311G.

**Non-Goals:**
- CO₂ reference log does not exist; CO₂ section is student-generated only.
- No scripting or terminal use by students.
- Rovibrational spectrum (optional section) is deferred pending TheoEspRotBib.py
  availability confirmation (Q1_01, optional).

---

## 3. Scientific Invariants and Hard Rules

- **Method:** B3LYP/6-311G (`rob3lyp/6-311g` keyword in Gaussian route)
- **Job type:** `opt freq` combined — optimization MUST precede frequency calculation
- **CO frequency:** 2063.3674 cm⁻¹ (confirmed from log — pre-filled in scaffold)
- **CO R(C–O):** 1.1473 Å (confirmed from log — pre-filled in scaffold)
- **CO₂ experimental:** 1388, 2349, 667 cm⁻¹ (NIST, via content_notes)
- **Normal mode count:** 3N−5 (linear): CO=1, CO₂=4
- **IR selection rule:** mode active if dipole moment changes
- **Unit:** frequencies in cm⁻¹; energies in Ha; distances in Å
- **Data integrity:** log files are read-only; students copy values manually

---

## 4. Technical Specification

**Scaffold file:** `content/modos-normales.md`
**Calculation file expected from students:** `CO_opt_freq_B3LYP_6311G.gjf`
**Save location:** `{{practicas_folder}}ModoNormales/`

**Key GaussView paths:**
- Job type: Calculate → Gaussian Calculation Setup → Job Type → Opt+Freq
- Visualization: Results → Vibrations
- Geometry: Results → Optimization (last frame)

**Log search strings:**
- `R1    R(1,2)` → geometry
- `Frequencies --` → frequencies
- `IR Inten` → IR intensity

---

## 5. Deliverables Inventory

| ID | Artifact | Type | Status |
|----|----------|------|--------|
| D1 | `content/modos-normales.md` | DOC | ✅ Created |
| D2 | This synthesis | DOC | ✅ |
| D3 | CO₂ scaffold sections (Paso 7 + tables) | DOC | ⬜ `[TEXTO HUMANO]` pending |
| D4 | Optional rovibrational section | DOC | ⬜ Pending Q1_01 |

---

## 6. Dependencies and Risks

- **CO data:** fully confirmed ✅
- **CO₂ data:** no reference log — students generate all values; tables intentionally empty
- **TheoEspRotBib.py:** availability in lab unconfirmed (Q1_01 optional) → default: omit script reference

---

## 7. Semantic Revision Changelog

| Version | Date | Tag | Description |
|---------|------|-----|-------------|
| 1.0.0 | 2026-10-25 | Initial | First synthesis from scaffold + confirmed logs |
