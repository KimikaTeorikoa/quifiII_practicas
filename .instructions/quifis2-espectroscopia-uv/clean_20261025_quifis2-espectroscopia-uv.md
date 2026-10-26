# Clean Document: P2-D — Espectroscopía UV-Vis de Cetonas
# Formalize Phase 0 — Normalized from raw_20261025_quifis2-espectroscopia-uv.md
# Date: 2026-10-25

---

## Scope

Jupyter Book practice scaffold for P2-D of the M_QUIFIS2 computational chemistry lab.
Students calculate UV-Vis spectra of carbonyl-containing compounds using TD-DFT with
implicit solvent (PCM model).

## Important Correction (data wins over content_notes)

The reference log `acetone_acetonitrile.log.txt` contains **formaldehyde (CH₂O)**,
NOT acetone (C₃H₆O). The filename and `content_notes_practices.md` text are misleading.
Stoichiometry confirmed from log: `CH2O`, route: `# opt freq b3lyp/6-311g scrf=(solvent=acetonitrile)`.
The practice targets ketones; the log provides a methodological reference only.

## Confirmed Data (from reference log acetone_acetonitrile.log.txt)

- Method/basis: B3LYP/6-311G (confirmed)
- Solvent model: PCM, solvent = acetonitrile (`scrf=(solvent=acetonitrile)`)
- Job type in log: `opt freq` (no TD-DFT in log — students run TD-DFT themselves)
- HOMO (formaldehyde, optimized geometry, MeCN): **−0.27636 Ha**
- LUMO (formaldehyde, MeCN): **−0.06005 Ha**
- SCF energy (final): −114.501579454 Ha
- Charge: 0, Multiplicity: 1

## Confirmed Data (from content_notes_practices.md)

- TD-DFT keyword: `td` (activates TD-DFT in Gaussian; default: 3 excited states)
- Example Excited State output: `Excited State 1: Singlet-A" 4.2871 eV 289.23 nm f=0.0003`
  (this example is from content_notes, not from a real log)
- Experimental acetona n→π*: 279 nm (cyclohexane), 264 nm (water)
- CO₂ experimental frequencies: referenced in NIST
- 5 ketones × 5 solvents = 25 TD-DFT calculations total

## Systems to Calculate (from content_notes)

**Ketones:** acetona, cloruro de acetilo, acetofenona, ácido acético, metil-etil-cetona
**Solvents:** vacuum (no scrf), cyclohexane, chloroform, ethanol, acetonitrile, water

## Placeholder Gaps

- All calculated UV λ values: empty — students generate during session
- Experimental λ for solvents other than cyclohexane and water: not confirmed in sources
- Gaussian solvent name for water in PCM: `water` (standard keyword, not from log)

## Pedagogical Constraints

- Two-part procedure: (A) HOMO-LUMO gap estimation, (B) TD-DFT.
- Mandatory intuition boxes: chromophores, n→π* vs π→π*, solvatochromism.
- 50 total calculations — explicit file naming convention required.
