# Maobits OS Android — Controlled visual asset generation 1.1.7

**Version:** 0.2.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document regenerates **Phase 1.1.7 — Controlled Generation of Maobits OS Visual Assets**, using the manually approved visual version.

The phase preserves the approved visual proposal in the repository, generates review sizes, and creates evidence, but **does not replace active Android resources yet**.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Input state

Before this phase, the following already exist:

```text
1.1.4 — Maobits OS visible branding validated.
1.1.5 — Visual resource audit generated.
1.1.6 — Iconography specification documented.
Real-device test on two physical smartphones approved.
```

---

## 4. Visual decision

The approved icon version preserves:

```text
- corporate dark background;
- clear M monogram;
- central hub;
- three network nodes;
- clean connectors;
- subtle network ring;
- enough visual separation;
- readable app-icon size.
```

---

## 5. Strict phase rule

Assets are stored only as a proposal in:

```text
docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/
```

Do not modify yet:

```text
app/src/main/res/mipmap*
app/src/main/res/drawable*
wear/src/main/res/mipmap*
wear/src/main/res/drawable*
AndroidManifest.xml
ic_launcher
ic_launcher_round
adaptive icon foreground/background
```

---

## 6. Included assets

```text
maobits-os-icon-proposal-approved-original.png
maobits-os-icon-proposal-approved-1024.png
maobits-os-icon-proposal-approved-512.png
maobits-os-icon-proposal-approved-256.png
maobits-os-icon-proposal-approved-128.png
maobits-os-icon-approved-colors.json
SHA256SUMS.txt
README.md
```

---

## 7. Copy documentation and assets into the project

Download the ZIP into `/home/maobits/Descargas` and run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_ASSET_DIR="/tmp/maobits-os-visual-assets-1.1.7-approved"
rm -rf "$TMP_ASSET_DIR"
mkdir -p "$TMP_ASSET_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-visual-asset-generation-1-1-7-final-approved.zip -d "$TMP_ASSET_DIR"

mkdir -p docs/03-brand
mkdir -p docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved

cp "$TMP_ASSET_DIR/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.es.md" docs/03-brand/
cp "$TMP_ASSET_DIR/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.en.md" docs/03-brand/

cp -a "$TMP_ASSET_DIR/assets/2026-07-30-maobits-os-icon-proposal-approved/." \
  docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/
```

---

## 8. Create evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_ASSET_DIR="docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved"
VISUAL_ASSET_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-visual-asset-generation-approved"
mkdir -p "$VISUAL_ASSET_EVIDENCE_DIR"

{
  echo "=== MAOBITS OS ANDROID - CONTROLLED VISUAL ASSET GENERATION APPROVED ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== APPROVED PROPOSAL FILES ==="
  find "$VISUAL_ASSET_DIR" -type f | sort
  echo
  echo "=== STATUS ==="
  echo "Approved proposal assets only. Android active resources were not replaced."
} > "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-GENERATION-APPROVED-SUMMARY.txt"

sha256sum "$VISUAL_ASSET_DIR"/* > "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-APPROVED-SHA256.txt" || true
file "$VISUAL_ASSET_DIR"/* > "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-APPROVED-FILE-TYPES.txt" || true

cat "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-GENERATION-APPROVED-SUMMARY.txt"
```

---

## 9. Manual review

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

xdg-open docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png
```

Checklist:

```text
[ ] Clear Maobits OS identity.
[ ] Does not look like an external-brand copy.
[ ] Does not use small text.
[ ] Remains readable at small size.
[ ] M monogram does not feel superposed.
[ ] Person → Commitment → Confirmation network is understandable.
[ ] Approved for Android technical conversion.
```

---

## 10. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.en.md \
        docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved \
        docs/03-brand/evidence/2026-07-30-visual-asset-generation-approved

git commit -m "brand(assets): add approved Maobits OS icon proposal"
```

---

## 11. Next phase

```text
Phase 1.1.8 — Technical conversion of assets into Android resources
```

That phase will convert the approved asset into Android/Wear resources with validation, avoiding blind changes.

---

## 12. Final statement

The approved visual version is preserved as a controlled proposal asset. Technical implementation into `ic_launcher`, adaptive icons, and Wear resources must only happen in the next phase.

**Person → Commitment → Confirmation**
