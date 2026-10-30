#!/usr/bin/env bash
# ==============================================================================
# run_fabric_review.sh — Auditoría de prosa y estilo con Fabric
#
# Uso:
#   ./scripts/run_fabric_review.sh [archivo_salida.md]
#
# Por defecto genera: sugerencias_fabric.md
# ==============================================================================

set -euo pipefail

# 1. Localizar binario de fabric
FABRIC_BIN="$(command -v fabric 2>/dev/null || true)"
if [[ -z "$FABRIC_BIN" || ! -x "$FABRIC_BIN" ]]; then
    if [[ -x "$HOME/.local/bin/fabric" ]]; then
        FABRIC_BIN="$HOME/.local/bin/fabric"
    elif [[ -x "$HOME/go/bin/fabric" ]]; then
        FABRIC_BIN="$HOME/go/bin/fabric"
    else
        echo "[ERROR] No se encontró el ejecutable 'fabric'." >&2
        echo "Asegúrate de que está en tu PATH o en ~/.local/bin/fabric" >&2
        exit 1
    fi
fi

# 2. Configurar archivo de salida y raíz del repo
OUTPUT_FILE="${1:-sugerencias_fabric.md}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# 3. Lista de archivos objetivo (10 archivos de la Parte 2)
FILES=(
    "content/parte2-gaussian/intros/intro-gaussview.md"
    "content/parte2-gaussian/intros/intro-hartree-fock.md"
    "content/parte2-gaussian/intros/intro-bases.md"
    "content/parte2-gaussian/intros/intro-born-oppenheimer.md"
    "content/parte2-gaussian/intros/intro-mas-alla-hf.md"
    "content/parte2-gaussian/intros/intro-energias.md"
    "content/parte2-gaussian/practicas/atomos-koopmans.md"
    "content/parte2-gaussian/practicas/moleculas-pes.md"
    "content/parte2-gaussian/practicas/modos-normales.md"
    "content/parte2-gaussian/practicas/espectroscopia-uv.md"
)

# 4. Lista de patrones de Fabric a ejecutar (solo los esenciales: diagnostico y propuesta academica)
PATTERNS=(
    "improve_academic_writing"
    "analyze_prose_pinker"
)

# 5. Inicializar encabezado del documento Markdown de salida
cat << 'EOF' > "$OUTPUT_FILE"
# Informe de Sugerencias y Auditoría de Prosa (Fabric)

Documento generado automáticamente con la revisión de estilo y calidad de prosa para los 10 archivos de la Parte 2 (Gaussian & GaussView).

---
EOF

echo "- **Fecha de inicio:** $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT_FILE"
echo "- **Patrones evaluados:** ${PATTERNS[*]}" >> "$OUTPUT_FILE"
echo "- **Archivos analizados:** ${#FILES[@]}" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# 6. Bucle de análisis por archivo
TOTAL_FILES=${#FILES[@]}
CURRENT_FILE_IDX=0

for rel_path in "${FILES[@]}"; do
    CURRENT_FILE_IDX=$((CURRENT_FILE_IDX + 1))
    file_path="$REPO_ROOT/$rel_path"
    file_name="$(basename "$rel_path")"

    if [[ ! -f "$file_path" ]]; then
        echo "[WARN] Archivo no encontrado: $file_path (saltando)" >&2
        continue
    fi

    echo "========================================================================" >&2
    echo "[$CURRENT_FILE_IDX/$TOTAL_FILES] Procesando: $file_name" >&2
    echo "========================================================================" >&2

    # Extraer bloques de prosa narrativa usando Python
    PROSE_BLOCKS="$(python3 - "$file_path" << 'PYEOF'
import sys

filepath = sys.argv[1]
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

sections = []
current_sec = "Introducción General"
current_lines = []
in_comment = False

for line in content.splitlines():
    stripped = line.strip()
    
    # Manejo de comentarios HTML
    if "<!--" in stripped:
        in_comment = True
    if in_comment:
        if "-->" in stripped:
            in_comment = False
        continue

    if stripped.startswith("#"):
        if current_lines:
            text = " ".join(current_lines).strip()
            if len(text) > 40 and not text.startswith("Párrafo"):
                sections.append((current_sec, text))
            current_lines = []
        current_sec = stripped.strip("# ").strip()
    elif (stripped.startswith(":::") or 
          stripped.startswith("::::") or
          stripped.startswith(":") or 
          stripped.startswith("---") or 
          stripped.startswith("|") or 
          stripped.startswith("[") or 
          stripped.startswith("- ") or
          stripped.startswith("$$")):
        continue
    elif stripped:
        current_lines.append(stripped)

if current_lines:
    text = " ".join(current_lines).strip()
    if len(text) > 40 and not text.startswith("Párrafo"):
        sections.append((current_sec, text))

# Filtrar secciones no narrativas
skip_sections = {"Bibliografía", "Objetivos", "Preguntas"}
filtered = [(s, t) for s, t in sections if s not in skip_sections]

for sec, text in filtered:
    print(f"@@@SECTION@@@{sec}")
    print(f"@@@TEXT@@@{text}")
PYEOF
)"

    if [[ -z "$PROSE_BLOCKS" ]]; then
        echo "[INFO] No se extrajo prosa narrativa para $file_name." >&2
        continue
    fi

    echo "## Archivo: \`$rel_path\`" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    SECTION_NAME=""
    while IFS= read -r line; do
        if [[ "$line" =~ ^@@@SECTION@@@(.*) ]]; then
            SECTION_NAME="${BASH_REMATCH[1]}"
        elif [[ "$line" =~ ^@@@TEXT@@@(.*) ]]; then
            PARAGRAPH_TEXT="${BASH_REMATCH[1]}"
            
            echo "  -> Sección: $SECTION_NAME" >&2
            echo "### Sección: $SECTION_NAME" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
            echo "**Texto original:**" >> "$OUTPUT_FILE"
            echo "> $PARAGRAPH_TEXT" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"

            # Ejecutar cada patrón de Fabric
            for pattern in "${PATTERNS[@]}"; do
                echo "     - Evaluando con '$pattern'..." >&2
                echo "#### Patrón: \`$pattern\`" >> "$OUTPUT_FILE"
                echo "" >> "$OUTPUT_FILE"

                # Llamada a Fabric forzando idioma español (-g=es)
                FABRIC_OUT=""
                if ! FABRIC_OUT="$(echo "$PARAGRAPH_TEXT" | "$FABRIC_BIN" --pattern "$pattern" -g=es 2>&1)"; then
                    FABRIC_OUT="[Aviso al ejecutar el patrón $pattern: $FABRIC_OUT]"
                fi

                echo "$FABRIC_OUT" >> "$OUTPUT_FILE"
                echo "" >> "$OUTPUT_FILE"
            done

            echo "---" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
        fi
    done <<< "$PROSE_BLOCKS"

done

echo "" >> "$OUTPUT_FILE"
echo "_Informe completado: $(date '+%Y-%m-%d %H:%M:%S')_" >> "$OUTPUT_FILE"

echo "" >&2
echo "[ÉXITO] Auditoría completada. Informe generado en: $OUTPUT_FILE" >&2
