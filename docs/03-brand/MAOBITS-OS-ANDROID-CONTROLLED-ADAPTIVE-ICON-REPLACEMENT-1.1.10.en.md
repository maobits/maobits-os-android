# Maobits OS Android — Controlled adaptive icon replacement 1.1.10

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.10 — Controlled Adaptive Icon Replacement**.

Phase 1.1.9 replaced legacy launcher PNGs. On modern Android, launchers commonly use adaptive resources under `mipmap-anydpi-v26`. This phase therefore replaces, in a controlled way:

```text
mipmap-anydpi-v26/ic_launcher.xml
mipmap-anydpi-v26/ic_launcher_round.xml
density-specific ic_launcher_foreground.png
adaptive icon background color
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
1.1.7 — Approved icon.
1.1.8 — Technical conversion generated.
1.1.9 — Legacy launcher PNGs replaced and validated.
```

---

## 4. Allowed scope

This phase may modify:

```text
app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml
app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml
app/src/main/res/mipmap-*/ic_launcher_foreground.png
app/src/main/res/values/maobits_os_icon_colors.xml

wear/src/main/res/mipmap-anydpi-v26/ic_launcher.xml
wear/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml
wear/src/main/res/mipmap-*/ic_launcher_foreground.png
wear/src/main/res/values/maobits_os_icon_colors.xml
```

It does not modify:

```text
applicationId
namespace
Kotlin packages
AndroidManifest.xml
permissions
BLE/Wi-Fi/Nostr
visible text
general app theme
```

---

## 5. Create branch

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b brand/1.1.10-controlled-adaptive-icons
```

---

## 6. Copy documentation and tool

Download the ZIP into `/home/maobits/Descargas` and run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_ADAPTIVE_ICON_DIR="/tmp/maobits-os-adaptive-icon-replacement-1.1.10"
rm -rf "$TMP_ADAPTIVE_ICON_DIR"
mkdir -p "$TMP_ADAPTIVE_ICON_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-controlled-adaptive-icon-replacement-1-1-10.zip -d "$TMP_ADAPTIVE_ICON_DIR"

mkdir -p docs/03-brand
mkdir -p tools/brand

cp "$TMP_ADAPTIVE_ICON_DIR/docs/MAOBITS-OS-ANDROID-CONTROLLED-ADAPTIVE-ICON-REPLACEMENT-1.1.10.es.md" docs/03-brand/
cp "$TMP_ADAPTIVE_ICON_DIR/docs/MAOBITS-OS-ANDROID-CONTROLLED-ADAPTIVE-ICON-REPLACEMENT-1.1.10.en.md" docs/03-brand/

cp "$TMP_ADAPTIVE_ICON_DIR/tools/brand/maobits_os_apply_adaptive_icons_1_1_10.py" tools/brand/
chmod +x tools/brand/maobits_os_apply_adaptive_icons_1_1_10.py
```

---

## 7. Pre-change audit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ADAPTIVE_ICON_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement"
mkdir -p "$ADAPTIVE_ICON_EVIDENCE_DIR"

{
  echo "=== BEFORE CONTROLLED ADAPTIVE ICON REPLACEMENT ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== ADAPTIVE ICON FILES ==="
  find app/src/main/res wear/src/main/res -type f \( \
    -path '*mipmap-anydpi-v26*' -o \
    -name 'ic_launcher_foreground.png' -o \
    -name 'maobits_os_icon_colors.xml' \
  \) | sort
} > "$ADAPTIVE_ICON_EVIDENCE_DIR/BEFORE-ADAPTIVE-ICON-STATE.txt"

cat "$ADAPTIVE_ICON_EVIDENCE_DIR/BEFORE-ADAPTIVE-ICON-STATE.txt"
```

---

## 8. Mandatory dry-run

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_adaptive_icons_1_1_10.py \
  --mode dry-run \
  --repo-root . \
  --source docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement

cat docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement/ADAPTIVE-ICON-REPLACEMENT-SUMMARY.txt
```

If the approved source asset is missing, stop.

---

## 9. Apply controlled replacement

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_adaptive_icons_1_1_10.py \
  --mode apply \
  --repo-root . \
  --source docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement

cat docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement/ADAPTIVE-ICON-REPLACEMENT-SUMMARY.txt
```

---

## 10. Review diff

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status --short

git diff --name-only -- \
  app/src/main/res \
  wear/src/main/res \
  docs/03-brand \
  tools/brand
```

---

## 11. Automatic validation

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ADAPTIVE_ICON_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement"

set -o pipefail

./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ADAPTIVE_ICON_EVIDENCE_DIR/APP-ASSEMBLE-DEBUG-AFTER-ADAPTIVE-ICON.log"
APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ADAPTIVE_ICON_EVIDENCE_DIR/WEAR-ASSEMBLE-DEBUG-AFTER-ADAPTIVE-ICON.log"
WEAR_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ADAPTIVE_ICON_EVIDENCE_DIR/TESTS-AFTER-ADAPTIVE-ICON.log"
TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ADAPTIVE_ICON_EVIDENCE_DIR/LINT-AFTER-ADAPTIVE-ICON.log"
LINT_STATUS=${PIPESTATUS[0]}

{
  echo "=== CONTROLLED ADAPTIVE ICON REPLACEMENT VALIDATION SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} > "$ADAPTIVE_ICON_EVIDENCE_DIR/CONTROLLED-ADAPTIVE-ICON-VALIDATION-SUMMARY.txt"

cat "$ADAPTIVE_ICON_EVIDENCE_DIR/CONTROLLED-ADAPTIVE-ICON-VALIDATION-SUMMARY.txt"
```

---

## 12. Real-device test

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

adb devices

./gradlew :app:installDebug --no-daemon --stacktrace --warning-mode all

adb shell am force-stop com.bitchat.droid
adb shell monkey -p com.bitchat.droid -c android.intent.category.LAUNCHER 1
```

If the launcher keeps its old icon cache, use controlled uninstall only if app data can be lost:

```bash
adb uninstall com.bitchat.droid || true
./gradlew :app:installDebug --no-daemon --stacktrace --warning-mode all
adb shell monkey -p com.bitchat.droid -c android.intent.category.LAUNCHER 1
```

Validate:

```text
[ ] App opens.
[ ] App still appears as Maobits OS.
[ ] No crash.
[ ] Modern icon updates.
[ ] Icon is not severely cropped.
[ ] Approved visual identity is recognizable.
```

---

## 13. Rollback if anything fails

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_adaptive_icons_1_1_10.py \
  --mode rollback \
  --repo-root . \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement
```

Then repeat build/test/lint.

---

## 14. Recommended commit

Only if everything validates:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add app/src/main/res \
        wear/src/main/res \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-ADAPTIVE-ICON-REPLACEMENT-1.1.10.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-ADAPTIVE-ICON-REPLACEMENT-1.1.10.en.md \
        docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement \
        tools/brand/maobits_os_apply_adaptive_icons_1_1_10.py

git commit -m "brand(icons): replace adaptive launcher icon resources"
```

---

## 15. Next phase

```text
Phase 1.1.11 — Real visual validation of icons and initial brand closure
```

That phase will document real screenshots, final icon state, build/lint/test status, and formal closure of the first visual identity block.

---

## 16. Final statement

This phase updates adaptive icons in an auditable way, with backup and rollback. It is the phase most likely to make modern Android show the new icon in the real launcher.

**Person → Commitment → Confirmation**
