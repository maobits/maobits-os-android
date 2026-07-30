# Maobits OS Android — Controlled launcher icon replacement 1.1.9

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.9 — Controlled Launcher Icon Replacement**.

This phase applies the candidate resources generated in 1.1.8 to the active `ic_launcher.png` and `ic_launcher_round.png` files for `app` and `wear`, with backup, evidence, build/lint/test validation, and real-device testing.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Required input state

Before starting, the following must exist:

```text
1.1.7 — Approved visual asset.
1.1.8 — Candidate resources generated under docs/03-brand/generated/.
```

A successful real-device test on two smartphones must also exist before active visual resources are changed.

---

## 4. Exact scope

This phase may replace only:

```text
app/src/main/res/mipmap-mdpi/ic_launcher.png
app/src/main/res/mipmap-hdpi/ic_launcher.png
app/src/main/res/mipmap-xhdpi/ic_launcher.png
app/src/main/res/mipmap-xxhdpi/ic_launcher.png
app/src/main/res/mipmap-xxxhdpi/ic_launcher.png

app/src/main/res/mipmap-mdpi/ic_launcher_round.png
app/src/main/res/mipmap-hdpi/ic_launcher_round.png
app/src/main/res/mipmap-xhdpi/ic_launcher_round.png
app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png
app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png

equivalent wear/src/main/res/mipmap-* files
```

It does not modify yet:

```text
mipmap-anydpi-v26/ic_launcher.xml
mipmap-anydpi-v26/ic_launcher_round.xml
adaptive icon foreground/background XML
AndroidManifest.xml
applicationId
namespace
Kotlin packages
visual theme
global colors
```

> Note: on modern Android, an adaptive icon may exist under `mipmap-anydpi-v26`. If the launcher still shows the previous icon after this phase, that is not a failure; it means the next phase must replace the adaptive icon layers.

---

## 5. Create branch

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b brand/1.1.9-controlled-launcher-icons
```

---

## 6. Copy documentation and tool

Download the ZIP into `/home/maobits/Descargas` and run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_ICON_REPLACEMENT_DIR="/tmp/maobits-os-launcher-icon-replacement-1.1.9"
rm -rf "$TMP_ICON_REPLACEMENT_DIR"
mkdir -p "$TMP_ICON_REPLACEMENT_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-controlled-launcher-icon-replacement-1-1-9.zip -d "$TMP_ICON_REPLACEMENT_DIR"

mkdir -p docs/03-brand
mkdir -p tools/brand

cp "$TMP_ICON_REPLACEMENT_DIR/docs/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-REPLACEMENT-1.1.9.es.md" docs/03-brand/
cp "$TMP_ICON_REPLACEMENT_DIR/docs/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-REPLACEMENT-1.1.9.en.md" docs/03-brand/

cp "$TMP_ICON_REPLACEMENT_DIR/tools/brand/maobits_os_apply_launcher_icons_1_1_9.py" tools/brand/
chmod +x tools/brand/maobits_os_apply_launcher_icons_1_1_9.py
```

---

## 7. Pre-change active-state audit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_REPLACEMENT_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement"
mkdir -p "$ICON_REPLACEMENT_EVIDENCE_DIR"

{
  echo "=== BEFORE CONTROLLED LAUNCHER ICON REPLACEMENT ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== ACTIVE ICON FILES ==="
  find app/src/main/res wear/src/main/res -type f \( -name 'ic_launcher*' -o -name '*launcher*' \) | sort
  echo
  echo "=== ADAPTIVE ICON XML FILES ==="
  find app/src/main/res wear/src/main/res -path '*mipmap-anydpi-v26*' -type f | sort
} > "$ICON_REPLACEMENT_EVIDENCE_DIR/BEFORE-ACTIVE-LAUNCHER-ICON-STATE.txt"

cat "$ICON_REPLACEMENT_EVIDENCE_DIR/BEFORE-ACTIVE-LAUNCHER-ICON-STATE.txt"
```

---

## 8. Mandatory dry-run

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_launcher_icons_1_1_9.py \
  --mode dry-run \
  --repo-root . \
  --candidate-root docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement

cat docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement/LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt
```

If any candidate file is missing, stop the phase.

---

## 9. Apply controlled replacement

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_launcher_icons_1_1_9.py \
  --mode apply \
  --repo-root . \
  --candidate-root docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement

cat docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement/LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt
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

ICON_REPLACEMENT_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement"

set -o pipefail

./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ICON_REPLACEMENT_EVIDENCE_DIR/APP-ASSEMBLE-DEBUG-AFTER-ICON-REPLACEMENT.log"
APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ICON_REPLACEMENT_EVIDENCE_DIR/WEAR-ASSEMBLE-DEBUG-AFTER-ICON-REPLACEMENT.log"
WEAR_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ICON_REPLACEMENT_EVIDENCE_DIR/TESTS-AFTER-ICON-REPLACEMENT.log"
TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$ICON_REPLACEMENT_EVIDENCE_DIR/LINT-AFTER-ICON-REPLACEMENT.log"
LINT_STATUS=${PIPESTATUS[0]}

{
  echo "=== CONTROLLED LAUNCHER ICON REPLACEMENT VALIDATION SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} > "$ICON_REPLACEMENT_EVIDENCE_DIR/CONTROLLED-LAUNCHER-ICON-REPLACEMENT-VALIDATION-SUMMARY.txt"

cat "$ICON_REPLACEMENT_EVIDENCE_DIR/CONTROLLED-LAUNCHER-ICON-REPLACEMENT-VALIDATION-SUMMARY.txt"
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

Manual review:

```text
[ ] App opens.
[ ] App still shows as Maobits OS.
[ ] No crash.
[ ] Icon updates if the launcher uses legacy PNG resources.
[ ] If icon does not update, review adaptive icons in 1.1.10.
```

---

## 13. Rollback if anything fails

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_launcher_icons_1_1_9.py \
  --mode rollback \
  --repo-root . \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement
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
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-REPLACEMENT-1.1.9.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-REPLACEMENT-1.1.9.en.md \
        docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement \
        tools/brand/maobits_os_apply_launcher_icons_1_1_9.py

git commit -m "brand(icons): replace launcher icon PNG resources"
```

---

## 15. Next phase

```text
Phase 1.1.10 — Controlled adaptive icon replacement
```

That phase will review and replace `mipmap-anydpi-v26`, foreground/background, and adaptive resources if modern devices still show the previous icon.

---

## 16. Final statement

This phase replaces only legacy launcher PNG files with backup, evidence, and validation. Adaptive icons remain separated to avoid breaking modern Android through unaudited visual changes.

**Person → Commitment → Confirmation**
