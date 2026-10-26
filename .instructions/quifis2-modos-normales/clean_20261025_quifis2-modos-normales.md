# Clean Document: P2-C — Modos Normales de Vibración
# Formalize Phase 0 — Normalized from raw_20261025_quifis2-modos-normales.md
# Date: 2026-10-25

---

## Scope

Jupyter Book practice scaffold for P2-C of the M_QUIFIS2 computational chemistry lab.
Covers calculation and interpretation of normal vibrational modes for:
1. **CO (carbon monoxide):** Confirmed reference log `co_b3lyp_opt.log.txt` exists.
2. **CO₂ (carbon dioxide):** No reference log; students generate all data.

## Confirmed Data (from reference log co_b3lyp_opt.log.txt)

- Method/basis: B3LYP/6-311G (keyword `rob3lyp/6-311g`)
- Job type: `opt freq` combined calculation
- CO charge: 0, multiplicity: 1
- R(C–O) optimized: **1.1473 Å**
- SCF energy: −113.296812140 Ha
- Frequency CO: **2063.3674 cm⁻¹** (1 mode, IR active, Inten=70.16)
- Reduced mass: 13.4388 uma; force constant: 33.7103 mdyne/Å
- HOMO: −0.38412 Ha; LUMO: −0.04879 Ha
- GaussView path for visualization: Results → Vibrations

## Confirmed Data (external, from content_notes_practices.md)

- CO experimental frequency: ~2143 cm⁻¹ (source: content_notes)
- CO₂ experimental frequencies: 1388, 2349, 667 cm⁻¹ (source: NIST, cited in content_notes)

## Normal Mode Count (derived, no log needed)

- CO (N=2, linear): 3N−5 = **1 mode**
- CO₂ (N=3, linear): 3N−5 = **4 modes**

## Placeholder Gaps

- CO₂ calculated frequencies: empty — students generate during session
- CO₂ geometry: no reference log → procedure text is `[TEXTO HUMANO]`
- Optional: rovibrational spectrum — references TheoEspRotBib.py script (unconfirmed
  availability in lab); section marked `[TEXTO HUMANO]`

## Pedagogical Constraints

- Same as all P2 practices (beginners, GaussView only, no scripting).
- Mandatory: intuition boxes for "modes normaux" concept and IR selection rules.
- Warning: always optimize geometry before calculating frequencies.
