# Maobits OS Android — Technical conversion of assets into Android resources 1.1.8

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.8 — Technical Conversion of Assets into Android/Wear Resources**.

The phase takes the approved 1.1.7 icon and converts it into candidate resources for Android and Wear OS, but it still **does not directly replace** active project resources.

The intention is to avoid blind changes:

```text
approved design → candidate technical conversion → review → controlled replacement → build/lint/test → real-device test
```

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Required input state

Before starting:

```text
1.1.4 — Maobits OS visible branding validated.
1.1.5 — Visual audit generated.
1.1.6 — Iconography design documented.
1.1.7 — Approved icon packaged as a controlled asset.
Real-device test on two physical smartphones approved.
```

---

## 4. Strict phase rule

This phase generates candidate resources in:

```text
docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/
```

It does not modify yet:

```text
app/src/main/res/
wear/src/main/res/
AndroidManifest.xml
active ic_launcher
active ic_launcher_round
active adaptive icon
```

---

## 5. Included candidate resources

The package generates:

```text
app/src/main/res/mipmap-mdpi/ic_launcher.png          48x48
app/src/main/res/mipmap-hdpi/ic_launcher.png          72x72
app/src/main/res/mipmap-xhdpi/ic_launcher.png         96x96
app/src/main/res/mipmap-xxhdpi/ic_launcher.png        144x144
app/src/main/res/mipmap-xxxhdpi/ic_launcher.png       192x192

app/src/main/res/mipmap-mdpi/ic_launcher_round.png    48x48
app/src/main/res/mipmap-hdpi/ic_launcher_round.png    72x72
app/src/main/res/mipmap-xhdpi/ic_launcher_round.png   96x96
app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png  144x144
app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png 192x192

equivalent wear/src/main/res/mipmap-* files
preview/maobits-os-icon-preview-*.png
SHA256SUMS.txt
```

---

## 6. Copy documentation, tool, and candidate resources

Download the ZIP into `/home/maobits/Descargas` and run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_ICON_CONVERSION_DIR="/tmp/maobits-os-icon-conversion-1.1.8"
rm -rf "$TMP_ICON_CONVERSION_DIR"
mkdir -p "$TMP_ICON_CONVERSION_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-technical-icon-conversion-1-1-8.zip -d "$TMP_ICON_CONVERSION_DIR"

mkdir -p docs/03-brand
mkdir -p docs/03-brand/generated
mkdir -p tools/brand

cp "$TMP_ICON_CONVERSION_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.es.md" docs/03-brand/
cp "$TMP_ICON_CONVERSION_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.en.md" docs/03-brand/

cp "$TMP_ICON_CONVERSION_DIR/tools/brand/maobits_os_generate_icon_resources_1_1_8.py" tools/brand/

cp -a "$TMP_ICON_CONVERSION_DIR/generated/2026-07-30-maobits-os-icon-android-candidate" \
  docs/03-brand/generated/
```

---

## 7. Reproduce candidate generation

If you want to regenerate from the approved asset already in the repository:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_generate_icon_resources_1_1_8.py \
  --source docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png \
  --output docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate
```

---

## 8. Create conversion evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_CONVERSION_DIR="docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate"
ICON_CONVERSION_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-technical-icon-conversion"
mkdir -p "$ICON_CONVERSION_EVIDENCE_DIR"

{
  echo "=== MAOBITS OS ANDROID - TECHNICAL ICON CONVERSION 1.1.8 ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== GENERATED CANDIDATE FILES ==="
  find "$ICON_CONVERSION_DIR" -type f | sort
  echo
  echo "=== STATUS ==="
  echo "Candidate Android/Wear resources generated under docs only."
  echo "Active Android resources were not replaced in this phase."
} > "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-SUMMARY.txt"

sha256sum $(find "$ICON_CONVERSION_DIR" -type f | sort) \
  > "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-SHA256.txt" || true

file $(find "$ICON_CONVERSION_DIR" -type f | sort) \
  > "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-FILE-TYPES.txt" || true

cat "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-SUMMARY.txt"
```

---

## 9. Visual review of generated sizes

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

xdg-open docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/preview/maobits-os-icon-preview-1024.png
xdg-open docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/preview/maobits-os-icon-preview-128.png
xdg-open docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/preview/maobits-os-icon-preview-48.png
```

Checklist:

```text
[ ] 1024px looks correct.
[ ] 128px remains readable.
[ ] 48px still identifies the M and central hub.
[ ] It does not look superposed.
[ ] Nodes do not disappear at small size.
[ ] Dark background works.
[ ] Approved for controlled replacement in phase 1.1.9.
```

---

## 10. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.en.md \
        docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate \
        docs/03-brand/evidence/2026-07-30-technical-icon-conversion \
        tools/brand/maobits_os_generate_icon_resources_1_1_8.py

git commit -m "brand(icons): generate Maobits OS Android icon candidates"
```

---

## 11. Next phase

```text
Phase 1.1.9 — Controlled launcher icon replacement
```

That phase will apply candidates to `app/src/main/res` and `wear/src/main/res` with backup, build, lint, real-device test, and rollback.

---

## 12. Final statement

Phase 1.1.8 converts the approved design into candidate technical resources without touching active resources yet. This preserves traceability and avoids blind visual changes.

**Person → Commitment → Confirmation**
