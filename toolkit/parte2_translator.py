#!/usr/bin/env python3
"""Parte 2 (Gaussian) Latxa Extraction, Chunking (max 2 chunks) and Reassembly Engine.

- Extracts pure text, protecting LaTeX math, figures (swapping to Basque SVGs),
  code fences, inline code, GaussView menu paths, and MyST directives.
- Chunks into AT MOST 1 or 2 parts per chapter.
- Stores all prompt files flat in toolkit/prompts/parte2/ with clean prefixes.
- Overwrite workflow: user replaces Spanish in .txt with Basque translation.
- `python3 toolkit/parte2_translator.py sync` updates the book in eu/ and verifies build.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

SYSTEM_INSTRUCTION = """# ================================================================
# UPV/EHU Kimika Fisikoa II — Latxa Itzulpen Prompta
# Fitxategia: {filename} (Zatia {part_idx}/{total_parts})
# ================================================================

Itzuli ondorengo testu zientifikoak euskarara estilo akademikoan (UPV/EHUko Kimika Fisikoa II mailan).
Mesedez, mantendu "=== BLOKEA X ===" banatzaileak eta "__PROTECTED_BLOCK_X__" formulen etiketak aldatu gabe:
"""

GAUSSVIEW_UI_KEYWORDS = [
    "Method", "Job Type", "Title", "Link 0", "General", "Guess", "PBC",
    "Solvation", "Preview", "Calculate", "Results", "Builder palette",
    "Inquire", "Modify Bond", "Add Hydrogens", "Undo", "Select All",
    "New", "Open", "Save", "Quick Launch"
]

CHAPTERS: List[Dict[str, str]] = [
    {"prefix": "00_index", "src": "es/content/parte2-gaussian/index.md", "dest": "eu/content/parte2-gaussian/index.md", "slug": "index"},
    {"prefix": "01_intro-gaussview", "src": "es/content/parte2-gaussian/intros/intro-gaussview.md", "dest": "eu/content/parte2-gaussian/intros/intro-gaussview.md", "slug": "intro-gaussview"},
    {"prefix": "02_intro-hartree-fock", "src": "es/content/parte2-gaussian/intros/intro-hartree-fock.md", "dest": "eu/content/parte2-gaussian/intros/intro-hartree-fock.md", "slug": "intro-hartree-fock"},
    {"prefix": "03_intro-bases", "src": "es/content/parte2-gaussian/intros/intro-bases.md", "dest": "eu/content/parte2-gaussian/intros/intro-bases.md", "slug": "intro-bases"},
    {"prefix": "04_intro-energias", "src": "es/content/parte2-gaussian/intros/intro-energias.md", "dest": "eu/content/parte2-gaussian/intros/intro-energias.md", "slug": "intro-energias"},
    {"prefix": "05_atomos-koopmans", "src": "es/content/parte2-gaussian/practicas/atomos-koopmans.md", "dest": "eu/content/parte2-gaussian/practicas/atomos-koopmans.md", "slug": "atomos-koopmans"},
    {"prefix": "06_intro-born-oppenheimer", "src": "es/content/parte2-gaussian/intros/intro-born-oppenheimer.md", "dest": "eu/content/parte2-gaussian/intros/intro-born-oppenheimer.md", "slug": "intro-born-oppenheimer"},
    {"prefix": "07_intro-mas-alla-hf", "src": "es/content/parte2-gaussian/intros/intro-mas-alla-hf.md", "dest": "eu/content/parte2-gaussian/intros/intro-mas-alla-hf.md", "slug": "intro-mas-alla-hf"},
    {"prefix": "08_moleculas-pes", "src": "es/content/parte2-gaussian/practicas/moleculas-pes.md", "dest": "eu/content/parte2-gaussian/practicas/moleculas-pes.md", "slug": "moleculas-pes"},
    {"prefix": "09_modos-normales", "src": "es/content/parte2-gaussian/practicas/modos-normales.md", "dest": "eu/content/parte2-gaussian/practicas/modos-normales.md", "slug": "modos-normales"},
    {"prefix": "10_espectroscopia-uv", "src": "es/content/parte2-gaussian/practicas/espectroscopia-uv.md", "dest": "eu/content/parte2-gaussian/practicas/espectroscopia-uv.md", "slug": "espectroscopia-uv"},
]

def parse_responses_text(text: str) -> Dict[int, str]:
    """Parse a text string containing === BLOKEA X === blocks into a dict."""
    pattern = re.compile(r"=== BLOKEA\s+(\d+)\s*===", re.IGNORECASE)
    splits = pattern.split(text)
    res: Dict[int, str] = {}
    for i in range(1, len(splits), 2):
        bid = int(splits[i].strip())
        bcontent = splits[i + 1].strip()
        res[bid] = bcontent
    return res


def reassemble_file(meta_data: Dict[str, Any], responses: Dict[int, str]) -> str:
    """Reassemble Markdown file from meta structure and translated blocks."""
    template = meta_data["template"]
    placeholders = meta_data["placeholders"]
    frontmatter = meta_data.get("frontmatter", "")

    restored_items: List[str] = []

    for item in template:
        if item["type"] == "placeholder":
            pid = item["pid"]
            restored_items.append(placeholders[pid])
        elif item["type"] == "block":
            bid = item["bid"]
            raw_orig = item["text"]
            trans_text = responses.get(bid, raw_orig)

            # Special handling for dropdown titles
            if "[DROPDOWN_TITLE]" in trans_text or "[DROPDOWN_TITLE]" in raw_orig:
                m_title = re.search(r"###\s*\[DROPDOWN_TITLE\]\s*([^\n]+)", trans_text)
                title_val = m_title.group(1).strip() if m_title else trans_text.replace("###", "").strip()
                for j in range(len(restored_items) - 1, -1, -1):
                    if "__DROPDOWN_TITLE_PLACEHOLDER__" in restored_items[j]:
                        restored_items[j] = restored_items[j].replace("__DROPDOWN_TITLE_PLACEHOLDER__", title_val)
                        break
                continue

            # Special handling for note titles
            if "[NOTE_TITLE]" in trans_text or "[NOTE_TITLE]" in raw_orig:
                m_title = re.search(r"###\s*\[NOTE_TITLE\]\s*([^\n]+)", trans_text)
                title_val = m_title.group(1).strip() if m_title else trans_text.replace("###", "").strip()
                for j in range(len(restored_items) - 1, -1, -1):
                    if "__NOTE_TITLE_PLACEHOLDER__" in restored_items[j]:
                        restored_items[j] = restored_items[j].replace("__NOTE_TITLE_PLACEHOLDER__", title_val)
                        break
                continue

            # Restore placeholders inside text block
            for pid in sorted(placeholders.keys(), key=len, reverse=True):
                trans_text = trans_text.replace(pid, placeholders[pid])

            restored_items.append(trans_text)

    doc_text = "\n\n".join(restored_items).strip() + "\n"
    return frontmatter + doc_text


def is_file_translated_to_euskera(txt: str) -> bool:
    """Heuristic: verify if text contains Basque keywords rather than Spanish."""
    body = txt.lower()
    eu_count = len(re.findall(r"\b(dira|eta|da|bere|dute|bidez|kalkulua|lortzeko|balio|funtzio|uhin|aztertzen)\b", body))
    es_count = len(re.findall(r"\b(para|como|este|estos|entre|mediante|cuando|donde|todos|cada|esta|las|los|debe)\b", body))
    return eu_count > es_count


def sync_book(prompts_dir: Path = Path("toolkit/prompts/parte2"), build: bool = True) -> None:
    """Scan all prompt files, reassemble any translated chapters into eu/, and run build."""
    meta_dir = prompts_dir / ".meta"
    if not meta_dir.exists():
        print("Error: .meta directory not found.", file=sys.stderr)
        return

    print("=" * 78)
    print("SYNC: Scanning prompt files for translations...")
    print("=" * 78)

    updated_count = 0

    for ch in CHAPTERS:
        prefix = ch["prefix"]
        meta_file = meta_dir / f"{prefix}.meta.json"
        if not meta_file.exists():
            continue

        meta_data = json.loads(meta_file.read_text(encoding="utf-8"))
        total_b = meta_data["total_blocks"]

        matching_files = sorted(prompts_dir.glob(f"{prefix}*.txt"))
        responses: Dict[int, str] = {}
        has_euskera = False

        for f in matching_files:
            txt = f.read_text(encoding="utf-8")
            # Verify file actually belongs to this chapter
            m_head = re.search(r"Fitxategia:\s*([^\n]+)", txt)
            if m_head and meta_data["filename"] not in m_head.group(1):
                continue

            if is_file_translated_to_euskera(txt):
                has_euskera = True
                parsed = parse_responses_text(txt)
                responses.update(parsed)

        if has_euskera:
            dest_path = Path(ch["dest"])
            res_md = reassemble_file(meta_data, responses)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_text(res_md, encoding="utf-8")
            status_tag = f"✅ {len(responses)}/{total_b} bloke itzulita" if len(responses) == total_b else f"⏳ {len(responses)}/{total_b} bloke"
            print(f"{prefix:28s} -> {dest_path} [{status_tag}]")
            updated_count += 1
        else:
            print(f"{prefix:28s} -> (gaztelaniaz oraindik, 0/{total_b})")

    print("-" * 78)
    if build and updated_count > 0:
        print("Building Jupyter Book (eu)...")
        res = subprocess.run(["jupyter-book", "build", "eu"], capture_output=True, text=True)
        if res.returncode == 0:
            print("✅ Build 'eu' succeeded with 0 errors!")
        else:
            print(f"❌ Build failed:\n{res.stderr}\n{res.stdout}")
    print("=" * 78)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parte 2 Latxa Extraction and Reassembly Tool.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sync
    p_sync = subparsers.add_parser("sync", help="Scan prompt files, reassemble translated chapters into eu/, and build.")
    p_sync.add_argument("--no-build", action="store_true", help="Skip jupyter-book build.")
    p_sync.add_argument("--prompts-dir", type=Path, default=Path("toolkit/prompts/parte2"), help="Prompts root dir.")

    # Status
    p_stat = subparsers.add_parser("status", help="Show translation status.")
    p_stat.add_argument("--prompts-dir", type=Path, default=Path("toolkit/prompts/parte2"), help="Prompts root dir.")

    args = parser.parse_args()

    if args.command == "sync":
        sync_book(args.prompts_dir, build=(not args.no_build))

    elif args.command == "status":
        sync_book(args.prompts_dir, build=False)


if __name__ == "__main__":
    main()
