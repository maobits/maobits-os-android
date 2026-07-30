# Maobits OS Android — Visual Audit of Icons, Launcher, and Graphic Resources 1.1.5

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.5 — Visual Audit of Icons, Launcher, and Graphic Resources**.

The previous phase validated the first safe visible-brand replacement. This phase reviews graphic resources before replacing icons or visual identity, preventing compatibility issues with Android, Wear OS, adaptive icons, launcher icons, `mipmap` resources, `drawable` resources, previews, and required sizes.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Expected input state

Before starting this phase, phase 1.1.4 must be validated with:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

---

## 4. Main rule for this phase

This phase **only audits and inventories visual resources**.

Do not replace yet:

- `ic_launcher`;
- `ic_launcher_round`;
- adaptive icon foreground/background;
- internal drawables;
- onboarding images;
- Wear OS resources;
- colors or visual theme;
- distribution assets.

---

## 5. Prepare branch

If phase 1.1.4 has already been committed, create a new branch:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout main
git pull --ff-only origin main

git checkout -b brand/1.1.5-visual-assets-audit
```

If you are still on `brand/1.1-inventory`, first confirm the state:

```bash
git status
git log --oneline --decorate -8
```

---

## 6. Copy this documentation into the project

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/03-brand

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.es.md docs/03-brand/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.en.md docs/03-brand/
```

---

## 7. Create evidence folder

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"
mkdir -p "$VISUAL_AUDIT_DIR"
```

---

## 8. Versioned visual resources inventory

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== TRACKED VISUAL RESOURCES ==="
  git ls-files \
    'app/src/**/res/drawable*/*' \
    'app/src/**/res/mipmap*/*' \
    'app/src/**/res/raw/*' \
    'app/src/**/assets/*' \
    'wear/src/**/res/drawable*/*' \
    'wear/src/**/res/mipmap*/*' \
    'wear/src/**/res/raw/*' \
    'wear/src/**/assets/*' \
    | sort
} > "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"

cat "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
```

---

## 9. Launcher icon inventory

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== LAUNCHER AND ADAPTIVE ICON RESOURCES ==="
  git ls-files \
    'app/src/**/res/mipmap*/ic_launcher*' \
    'app/src/**/res/drawable*/ic_launcher*' \
    'wear/src/**/res/mipmap*/ic_launcher*' \
    'wear/src/**/res/drawable*/ic_launcher*' \
    | sort
  echo
  echo "=== MANIFEST ICON REFERENCES ==="
  git grep -n -I -E "android:icon|android:roundIcon|ic_launcher|ic_launcher_round" \
    -- app/src/main/AndroidManifest.xml wear/src/main/AndroidManifest.xml \
    || true
} > "$VISUAL_AUDIT_DIR/LAUNCHER-ICON-INVENTORY.txt"

cat "$VISUAL_AUDIT_DIR/LAUNCHER-ICON-INVENTORY.txt"
```

---

## 10. Graphic resource hashes

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== VISUAL RESOURCE HASHES ==="
  while IFS= read -r file; do
    if [ -f "$file" ]; then
      sha256sum "$file"
    fi
  done < "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
} > "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-SHA256.txt"

head -120 "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-SHA256.txt"
```

---

## 11. File types and sizes

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== VISUAL RESOURCE FILE TYPES ==="
  while IFS= read -r file; do
    if [ -f "$file" ]; then
      printf "%s | " "$file"
      file "$file"
    fi
  done < "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
} > "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-FILE-TYPES.txt"

head -160 "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-FILE-TYPES.txt"
```

---

## 12. Image dimensions with Python

This command uses standard Python and, if Pillow is available, extracts dimensions. If Pillow is not installed, the phase does not fail.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

python3 <<'PY' > "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-DIMENSIONS.txt"
from pathlib import Path

inventory = Path("docs/03-brand/evidence/2026-07-29-visual-assets-audit/TRACKED-VISUAL-RESOURCES.txt")
print("=== VISUAL RESOURCE DIMENSIONS ===")

try:
    from PIL import Image
except Exception as exc:
    print(f"Pillow not available: {exc}")
    raise SystemExit(0)

for line in inventory.read_text(encoding="utf-8").splitlines():
    path = Path(line.strip())
    if not path.is_file():
        continue
    if path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
        continue
    try:
        with Image.open(path) as img:
            print(f"{path} | {img.width}x{img.height} | {img.mode}")
    except Exception as exc:
        print(f"{path} | unreadable: {exc}")
PY

cat "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-DIMENSIONS.txt"
```

---

## 13. Colors, themes, and XML visual references

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== COLORS, THEMES, STYLES, ICON XML REFERENCES ==="
  git grep -n -I -E "color|Color|theme|Theme|style|Style|ic_launcher|drawable|mipmap|adaptive-icon|foreground|background" \
    -- app/src/main/res wear/src/main/res \
    || true
} > "$VISUAL_AUDIT_DIR/COLORS-THEMES-STYLES-VISUAL-REFERENCES.txt"

head -220 "$VISUAL_AUDIT_DIR/COLORS-THEMES-STYLES-VISUAL-REFERENCES.txt"
```

---

## 14. Automatic visual audit summary

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== MAOBITS OS ANDROID - VISUAL ASSETS AUDIT SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== COUNTS ==="
  printf "Tracked visual resources: "
  wc -l < "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
  printf "Launcher/adaptive icon references: "
  grep -Eic "ic_launcher|android:icon|android:roundIcon|adaptive-icon" "$VISUAL_AUDIT_DIR/LAUNCHER-ICON-INVENTORY.txt" || true
  printf "Image dimensions lines: "
  grep -Eic "\| [0-9]+x[0-9]+ \|" "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-DIMENSIONS.txt" || true
  printf "Theme/color reference lines: "
  grep -Eic "color|theme|style|ic_launcher|drawable|mipmap|adaptive-icon" "$VISUAL_AUDIT_DIR/COLORS-THEMES-STYLES-VISUAL-REFERENCES.txt" || true
  echo
  echo "=== EVIDENCE FILES ==="
  find "$VISUAL_AUDIT_DIR" -type f | sort
} > "$VISUAL_AUDIT_DIR/VISUAL-ASSETS-AUDIT-SUMMARY.txt"

cat "$VISUAL_AUDIT_DIR/VISUAL-ASSETS-AUDIT-SUMMARY.txt"
```

---

## 15. Acceptance criteria

Phase 1.1.5 is complete when:

- a versioned visual resource inventory exists;
- launcher/adaptive icons are inventoried;
- visual resource SHA256 hashes exist;
- file types exist;
- dimensions exist when possible;
- color, theme, and style references exist;
- an automatic summary exists;
- icons have not been replaced yet;
- functional code was not modified;
- bilingual documentation was copied.

---

## 16. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.en.md \
        docs/03-brand/evidence/2026-07-29-visual-assets-audit

git commit -m "docs(brand): add visual assets audit"
```

---

## 17. Next phase

```text
Phase 1.1.6 — Maobits OS Android iconography design
```

That phase will define the visual replacement, palette, launcher icon, adaptive icon, Wear icon, and visual accessibility criteria.

---

## 18. Final statement

Visual identity must be changed with the same discipline as code: inventory first, design second, controlled replacement third, and validation last.

**Person → Commitment → Confirmation**
