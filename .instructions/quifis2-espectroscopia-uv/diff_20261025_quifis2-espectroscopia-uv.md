# Diff Report: P2-D — Espectroscopía UV-Vis de Cetonas
# Formalize Phase 0 — Bracket and normalization audit
# Date: 2026-10-25

---

## Bracket Inventory

| # | Original bracket text | Category | Resolution |
|---|----------------------|----------|------------|
| 1 | `[TEXTO HUMANO]` (×6 sections) | Editorial placeholder | Left in scaffold |
| 2 | `[CAPTURA: ...]` (×4) | Editorial placeholder | Left in scaffold |

## Data Corrections (data wins over content_notes)

| Issue | Original claim | Correction | Source |
|-------|---------------|------------|--------|
| Molecule identity | `acetone_acetonitrile.log` described as acetona in content_notes | **Formaldehyde (CH₂O)** | Stoichiometry line in log: `CH2O`; C3H6O never appears |
| HOMO/LUMO attribution | Values attributed to "acetona en MeCN" in content_notes | Belong to **formaldehyde in MeCN** | Log lines 919–921 confirmed |
| TD-DFT example output | `Excited State 1: ... 289.23 nm` shown as from log | Source is **content_notes only**; no TD-DFT job in log | Log route: `opt freq`, no `td` keyword |

## Structural Changes (raw → clean)

- Added explicit correction note for formaldehyde vs. acetone discrepancy.
- Scaffold already marks all calculated values as empty (students generate).
- No invented data introduced.
