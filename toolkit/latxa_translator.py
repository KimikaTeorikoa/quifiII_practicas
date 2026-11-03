#!/usr/bin/env python3
"""Latxa Translation Tooling for M_QUIFIS2 (UPV/EHU Kimika Fisikoa II).

Translates Markdown files and Jupyter Notebooks from Spanish to Basque
using HiTZ's Latxa open model on Hugging Face (or dry-run / local review mode).

Enforces UPV/EHU physical chemistry terminology and lab invariants:
- GaussView menu paths preserved in English bold (**Calculate → Gaussian Calculation Setup**).
- MyST directives (:::, ::::{dropdown}) and LaTeX math ($$, ```{math}) protected.
- Jupyter Notebook code cells untouched (only markdown cells translated).
- Produces clean translation or bilingual side-by-side review sheets for human validation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Tuple

DEFAULT_MODEL = "HiTZ/Latxa-Llama-3.1-8B-Instruct"
HF_API_URL = "https://router.huggingface.co/hf-inference/models/{model}/v1/chat/completions"

SYSTEM_PROMPT = """You are a bilingual professor and scientific translator specializing in Physical Chemistry at the University of the Basque Country (UPV/EHU).
Your task is to translate university lab course materials from Spanish to academic Basque (Euskara batua).

CRITICAL CONSTRAINTS:
1. Chemistry Terminology:
   - "ecuación de Schrödinger" -> "Schrödinger-en ekuazioa"
   - "función de onda" -> "uhin-funtzioa"
   - "partícula en una caja" -> "partikula kaxa batean" (or "kutxa batean")
   - "pozo de potencial" -> "potentzial-putzua"
   - "pozo finito" -> "putzu finitua"
   - "oscilador armónico" -> "osziladore harmonikoa"
   - "diferencias finitas" -> "diferentzia finituak"
   - "superficie de energía potencial" -> "potentzial-energiaren gainazala (PEG)"
   - "modos normales de vibración" -> "bibrazio-modu normalak"
   - "frecuencia armónica" -> "maiztasun harmonikoa"
   - "optimización de geometría" -> "geometria-optimizazioa"
   - "base de funciones / conjunto de bases" -> "oinarri-multzoa"
   - "base de valencia dividida" -> "balentzia zatituko oinarria"
   - "funciones de polarización" -> "polarizazio-funtzioak"
   - "funciones difusas" -> "funtzio difusoak"
   - "teorema de Koopmans" -> "Koopmans-en teorema"
   - "energía de ionización" -> "ionizazio-energia"
   - "espectroscopía infrarroja" -> "infragorri-espektroskopia (IR)"
   - "espectroscopía UV-Vis" -> "UV-Vis espektroskopia"

2. Lab & Software Invariants:
   - GaussView menu paths MUST remain strictly in English bold: e.g. **Calculate → Gaussian Calculation Setup**, **Results → MOs**, **Results → Vibrations**.
   - Filenames and extensions (.gjf, .log, .chk) must remain unchanged.
   - LaTeX formulas ($...$, $$...$$, ```{math}...```) and MyST directives (:::, ::::{...}) must remain untouched.
   - Do NOT use em-dashes (—). Use commas, periods, or parentheses.
   - Deliver clear, direct academic Basque. Output ONLY the translated text, without conversational chatter or preambles.
"""


def extract_protected_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    """Extract code blocks, math blocks, and directives to protect them from alteration."""
    placeholders: Dict[str, str] = {}
    counter = 0

    def replace_block(match: re.Match[str]) -> str:
        nonlocal counter
        key = f"__PROTECTED_BLOCK_{counter}__"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    # Protect code fences (```...```) and colon fences (:::...:::)
    pattern_fence = re.compile(r"(```[\s\S]*?```|:::{1,4}[\s\S]*?:::{1,4})", re.MULTILINE)
    text = pattern_fence.sub(replace_block, text)

    # Protect display math ($$...$$)
    pattern_math = re.compile(r"(\$\$[\s\S]*?\$\$)", re.MULTILINE)
    text = pattern_math.sub(replace_block, text)

    # Protect inline math ($...$)
    pattern_inline_math = re.compile(r"(\$[^\$\n]+?\$)")
    text = pattern_inline_math.sub(replace_block, text)

    return text, placeholders


def restore_protected_blocks(text: str, placeholders: Dict[str, str]) -> str:
    """Restore previously extracted protected blocks."""
    for key, val in placeholders.items():
        text = text.replace(key, val)
    return text


def query_latxa(
    text: str,
    hf_token: str,
    model: str = DEFAULT_MODEL,
    retries: int = 3,
    wait_sec: int = 5,
) -> str:
    """Query Latxa via Hugging Face Inference API."""
    url = HF_API_URL.format(model=model)
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Itzuli testu hau euskarara UPV/EHUko estilo akademikoan:\n\n{text}",
            },
        ],
        "max_tokens": 2048,
        "temperature": 0.1,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {hf_token}",
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]["content"]
                return choice.strip()
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            print(f"[Warning] HTTP {e.code} on attempt {attempt}: {err_body}", file=sys.stderr)
            if e.code == 503:  # Model is loading
                time.sleep(wait_sec * attempt)
            else:
                raise
        except Exception as e:
            print(f"[Warning] Error on attempt {attempt}: {e}", file=sys.stderr)
            time.sleep(wait_sec)

    raise RuntimeError("Failed to query Latxa after retries.")


def translate_text(
    text: str,
    hf_token: str | None,
    model: str,
    dry_run: bool = False,
) -> str:
    """Safely translate a text segment, respecting protected blocks."""
    if not text.strip():
        return text

    masked, placeholders = extract_protected_blocks(text)

    if dry_run or not hf_token:
        # In dry run, return masked indicator for inspection
        translated_masked = f"[LATXA-DRAFT-EU]\n{masked}"
    else:
        translated_masked = query_latxa(masked, hf_token=hf_token, model=model)

    return restore_protected_blocks(translated_masked, placeholders)


def translate_markdown(
    src_path: Path,
    dest_path: Path,
    hf_token: str | None,
    model: str,
    dry_run: bool = False,
) -> None:
    """Translate a Markdown file."""
    content = src_path.read_text(encoding="utf-8")

    # Handle YAML frontmatter
    frontmatter = ""
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = f"---{parts[1]}---\n"
            body = parts[2]

    # Split body into major sections / paragraphs to keep prompt size optimal
    paragraphs = re.split(r"(\n\n+)", body)
    translated_paras: List[str] = []

    for item in paragraphs:
        if item.strip():
            translated = translate_text(item, hf_token=hf_token, model=model, dry_run=dry_run)
            translated_paras.append(translated)
        else:
            translated_paras.append(item)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(frontmatter + "".join(translated_paras), encoding="utf-8")
    print(f"Processed: {src_path} -> {dest_path}")


def translate_notebook(
    src_path: Path,
    dest_path: Path,
    hf_token: str | None,
    model: str,
    dry_run: bool = False,
) -> None:
    """Translate a Jupyter Notebook (only markdown cells)."""
    with open(src_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    for idx, cell in enumerate(cells):
        if cell.get("cell_type") == "markdown":
            source_text = "".join(cell.get("source", []))
            if source_text.strip():
                print(f"  Translating cell {idx} ({len(source_text)} chars)...")
                translated = translate_text(
                    source_text,
                    hf_token=hf_token,
                    model=model,
                    dry_run=dry_run,
                )
                cell["source"] = [line + "\n" for line in translated.split("\n")]
                # Strip extra trailing newline from last element
                if cell["source"] and cell["source"][-1].endswith("\n"):
                    cell["source"][-1] = cell["source"][-1][:-1]

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"Processed Notebook: {src_path} -> {dest_path}")


def generate_bilingual_review(
    src_md: Path,
    trans_md: Path,
    out_review_md: Path,
) -> None:
    """Generate a clean side-by-side or block-by-block comparison for human review."""
    src_text = src_md.read_text(encoding="utf-8")
    trans_text = trans_md.read_text(encoding="utf-8")

    src_paras = [p.strip() for p in re.split(r"\n\n+", src_text) if p.strip()]
    trans_paras = [p.strip() for p in re.split(r"\n\n+", trans_text) if p.strip()]

    lines = [
        f"# Berrikuspen fitxa bilingüea: {src_md.name}",
        "> **Norentzat**: Xabi / Irakasle arduraduna",
        "> **Argibidea**: Egiaztatu termino zientifikoak eta esaldien naturaltasuna.",
        "",
        "| Jatorrizkoa (Gaztelaniaz) | Proposamena (Euskaraz) | Oharrak / Zuzenketak |",
        "|---|---|---|",
    ]

    max_len = max(len(src_paras), len(trans_paras))
    for i in range(max_len):
        sp = src_paras[i].replace("\n", " ") if i < len(src_paras) else ""
        tp = trans_paras[i].replace("\n", " ") if i < len(trans_paras) else ""
        # Escape pipes
        sp = sp.replace("|", "\\|")
        tp = tp.replace("|", "\\|")
        lines.append(f"| {sp} | {tp} | |")

    out_review_md.parent.mkdir(parents=True, exist_ok=True)
    out_review_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated bilingual review sheet: {out_review_md}")


def export_prompts(src_path: Path, prompt_out: Path) -> None:
    """Export text blocks from a markdown file or notebook into a single file ready for Latxa web."""
    meta_path = prompt_out.with_suffix(".json")
    blocks: Dict[int, Dict[str, Any]] = {}

    header = (
        "# ================================================================\n"
        "# UPV/EHU Kimika Fisikoa II — Latxa Itzulpen Prompta\n"
        "# Argibidea: Kopiatu beheko testua eta itsatsi https://latxa.hitz.eus/ edo https://www.apps.euskadi.eus/latxa/\n"
        "# GARRANTZITSUA: Mantendu \"=== BLOKEA X ===\" eta \"__PROTECTED_BLOCK_X__\" etiketak bere horretan.\n"
        "# ================================================================\n\n"
        "Itzuli ondorengo testu zientifikoak euskarara estilo akademikoan (UPV/EHUko Kimika Fisikoa II mailan).\n"
        "Mesedez, mantendu \"=== BLOKEA X ===\" banatzaileak eta formulen etiketak aldatu gabe:\n\n"
    )

    body_chunks: List[str] = []

    if src_path.suffix == ".ipynb":
        with open(src_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
        for idx, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") == "markdown":
                text = "".join(cell.get("source", []))
                if text.strip():
                    masked, placeholders = extract_protected_blocks(text)
                    blocks[idx] = {
                        "type": "cell",
                        "raw": text,
                        "masked": masked,
                        "placeholders": placeholders,
                    }
                    body_chunks.append(f"=== BLOKEA {idx} ===\n{masked.strip()}\n")
    else:
        content = src_path.read_text(encoding="utf-8")
        frontmatter = ""
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = f"---{parts[1]}---\n"
                body = parts[2]

        paras = [p.strip() for p in re.split(r"\n\n+", body) if p.strip()]
        for idx, para in enumerate(paras):
            masked, placeholders = extract_protected_blocks(para)
            blocks[idx] = {
                "type": "para",
                "raw": para,
                "masked": masked,
                "placeholders": placeholders,
                "frontmatter": frontmatter if idx == 0 else "",
            }
            body_chunks.append(f"=== BLOKEA {idx} ===\n{masked.strip()}\n")

    prompt_out.parent.mkdir(parents=True, exist_ok=True)
    prompt_out.write_text(header + "\n".join(body_chunks), encoding="utf-8")

    meta_data = {
        "source": str(src_path),
        "suffix": src_path.suffix,
        "blocks": {str(k): v for k, v in blocks.items()},
    }
    meta_path.write_text(json.dumps(meta_data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Exported {len(blocks)} blocks to: {prompt_out}")
    print(f"Metadata sidecar saved to: {meta_path}")


def import_responses(
    src_path: Path,
    response_in: Path,
    dest_path: Path,
    review_sheet: Path | None = None,
) -> None:
    """Import Latxa web responses, restore protected blocks, and write translated file."""
    meta_path = response_in.with_suffix(".json")
    if not meta_path.exists():
        # Fallback to search in prompt_in location if user named response differently
        possible_meta = list(response_in.parent.glob("*.json"))
        if possible_meta:
            meta_path = possible_meta[0]

    if not meta_path.exists():
        raise FileNotFoundError(
            f"Metadata file '{meta_path}' not found. Make sure the .json generated during --export is present."
        )

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    blocks_meta = meta["blocks"]

    raw_response = response_in.read_text(encoding="utf-8")
    # Split by === BLOKEA (\d+) ===
    pattern = re.compile(r"=== BLOKEA\s+(\d+)\s*===", re.IGNORECASE)
    splits = pattern.split(raw_response)

    translated_blocks: Dict[str, str] = {}
    # splits[0] is preamble before first block
    for i in range(1, len(splits), 2):
        block_id = splits[i].strip()
        block_content = splits[i + 1].strip()
        translated_blocks[block_id] = block_content

    print(f"Found {len(translated_blocks)} translated blocks in response file.")

    review_rows: List[Tuple[str, str]] = []

    if src_path.suffix == ".ipynb":
        with open(src_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        for str_idx, bmeta in blocks_meta.items():
            idx = int(str_idx)
            raw_es = bmeta["raw"]
            placeholders = bmeta["placeholders"]

            if str_idx in translated_blocks:
                trans_masked = translated_blocks[str_idx]
                trans_restored = restore_protected_blocks(trans_masked, placeholders)
            else:
                print(f"[Warning] Block {str_idx} not found in responses. Keeping original.")
                trans_restored = raw_es

            nb["cells"][idx]["source"] = [line + "\n" for line in trans_restored.split("\n")]
            if nb["cells"][idx]["source"] and nb["cells"][idx]["source"][-1].endswith("\n"):
                nb["cells"][idx]["source"][-1] = nb["cells"][idx]["source"][-1][:-1]

            review_rows.append((raw_es, trans_restored))

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"Successfully generated notebook: {dest_path}")

    else:
        # Markdown file
        restored_paras: List[str] = []
        frontmatter = ""

        for str_idx, bmeta in blocks_meta.items():
            raw_es = bmeta["raw"]
            placeholders = bmeta["placeholders"]
            if bmeta.get("frontmatter"):
                frontmatter = bmeta["frontmatter"]

            if str_idx in translated_blocks:
                trans_masked = translated_blocks[str_idx]
                trans_restored = restore_protected_blocks(trans_masked, placeholders)
            else:
                print(f"[Warning] Block {str_idx} not found in responses. Keeping original.")
                trans_restored = raw_es

            restored_paras.append(trans_restored)
            review_rows.append((raw_es, trans_restored))

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(frontmatter + "\n\n".join(restored_paras) + "\n", encoding="utf-8")
        print(f"Successfully generated markdown: {dest_path}")

    if review_sheet:
        review_lines = [
            f"# Berrikuspen Fitxa Bilingüea: {src_path.name}",
            "> **Norentzat**: Xabi / Irakasle arduraduna",
            "> **Argibidea**: Egiaztatu termino zientifikoak eta esaldien naturaltasuna.",
            "",
            "| Jatorrizkoa (Gaztelaniaz) | Proposamena (Euskaraz - Latxa) | Oharrak / Zuzenketak |",
            "|---|---|---|",
        ]
        for es, eu in review_rows:
            es_clean = es.replace("\n", " ").replace("|", "\\|")
            eu_clean = eu.replace("\n", " ").replace("|", "\\|")
            review_lines.append(f"| {es_clean} | {eu_clean} | |")

        review_sheet.parent.mkdir(parents=True, exist_ok=True)
        review_sheet.write_text("\n".join(review_lines), encoding="utf-8")
        print(f"Generated bilingual review sheet: {review_sheet}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate M_QUIFIS2 course materials into Basque using Latxa."
    )
    parser.add_argument("source", type=Path, help="Input Markdown file or directory.")
    parser.add_argument("-o", "--output", type=Path, help="Output file or directory.")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Latxa model id on Hugging Face (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("HF_TOKEN"),
        help="Hugging Face API token (or set via HF_TOKEN env var).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate translation and show prompt structures without calling API.",
    )
    parser.add_argument(
        "--export-prompts",
        type=Path,
        help="Export blocks into a single TXT file ready to copy-paste into Latxa web.",
    )
    parser.add_argument(
        "--import-responses",
        type=Path,
        help="Import Latxa web responses from TXT file and build target notebook/markdown.",
    )
    parser.add_argument(
        "--review-sheet",
        type=Path,
        help="Generate a bilingual comparison Markdown review sheet for Xabi.",
    )

    args = parser.parse_args()

    if not args.source.exists():
        print(f"Error: Source path '{args.source}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Workflow 1: Export prompts for web Latxa
    if args.export_prompts:
        export_prompts(args.source, args.export_prompts)
        return

    # Workflow 2: Import responses from web Latxa
    if args.import_responses:
        if not args.output:
            print("Error: Specify -o / --output when importing responses.", file=sys.stderr)
            sys.exit(1)
        import_responses(args.source, args.import_responses, args.output, args.review_sheet)
        return

    # Workflow 3: Live HF API (or dry-run)
    if not args.token and not args.dry_run:
        print(
            "Notice: No HF_TOKEN provided. Running in --dry-run mode.\n"
            "To call the live Latxa API, provide --token or export HF_TOKEN='...'",
            file=sys.stderr,
        )
        args.dry_run = True

    if args.source.is_file():
        output = args.output or args.source.with_name(f"{args.source.stem}_eu{args.source.suffix}")
        if args.source.suffix == ".ipynb":
            translate_notebook(args.source, output, args.token, args.model, args.dry_run)
        else:
            translate_markdown(args.source, output, args.token, args.model, args.dry_run)

        if args.review_sheet:
            generate_bilingual_review(args.source, output, args.review_sheet)
    else:
        if not args.output:
            print("Error: For directory translation, specify -o / --output.", file=sys.stderr)
            sys.exit(1)
        for path in args.source.rglob("*"):
            if path.suffix in [".md", ".ipynb"]:
                rel = path.relative_to(args.source)
                dest = args.output / rel
                if path.suffix == ".ipynb":
                    translate_notebook(path, dest, args.token, args.model, args.dry_run)
                else:
                    translate_markdown(path, dest, args.token, args.model, args.dry_run)


if __name__ == "__main__":
    main()
