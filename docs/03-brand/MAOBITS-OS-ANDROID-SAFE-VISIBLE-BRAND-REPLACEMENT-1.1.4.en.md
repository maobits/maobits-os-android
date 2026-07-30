# Maobits OS Android — First Safe Visible-Brand Replacement 1.1.4

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.4 — First Safe Visible-Brand Replacement**.

The goal is to apply the first controlled visible-identity change for Maobits OS Android without touching the deep technical identity of the project yet.

This phase only allows changing:

- `rootProject.name`;
- `app_name`;
- visible label `Share BitChat`;
- phase evidence and documentation.

Do not modify `applicationId`, `namespace`, Kotlin packages, imports, custom permissions, authorities, deep links, application classes, themes, or connectivity logic yet.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Diagnosis used for this phase

The clean audit confirmed:

```text
settings.gradle.kts: rootProject.name = "bitchat-android"
app/build.gradle.kts: namespace = "com.bitchat.android"
app/build.gradle.kts: applicationId = "com.bitchat.droid"
wear/build.gradle.kts: namespace = "com.bitchat.watch"
wear/build.gradle.kts: applicationId = "com.bitchat.watch"
app/src/main/AndroidManifest.xml: android:label="@string/app_name"
app/src/main/AndroidManifest.xml: android:label="Share BitChat"
wear/src/main/AndroidManifest.xml: android:label="@string/app_name"
```

It also confirmed elements that must wait:

```text
com.bitchat.android.permission.FORCE_FINISH
Theme.BitchatAndroid
BitchatApplication
BitchatWatchApplication
bitchat://verify
com.bitchat.*
```

---

## 4. Safety rule

Do not use mass replacement.

Forbidden in this phase:

```bash
sed -i 's/bitchat/maobits/g'
```

This phase must be surgical, auditable, and reversible.

---

## 5. Recommended branch

If the `brand/1.1-inventory` branch is complete, commit the evidence first. Then create the new branch:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout brand/1.1-inventory
git status

git add docs/03-brand
git commit -m "docs(brand): add clean brand inventory and classification evidence" || true

git checkout main
git pull --ff-only origin main

git checkout -b brand/1.1.4-visible-brand
```

If you decide to continue on the current branch, document the decision and do not mix unrelated functional changes.

---

## 6. Copy this documentation into the project

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/03-brand

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-SAFE-VISIBLE-BRAND-REPLACEMENT-1.1.4.es.md docs/03-brand/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-SAFE-VISIBLE-BRAND-REPLACEMENT-1.1.4.en.md docs/03-brand/
```

---

## 7. Create before-change evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISIBLE_BRAND_DIR="docs/03-brand/evidence/2026-07-29-safe-visible-brand-replacement"
mkdir -p "$VISIBLE_BRAND_DIR"

{
  echo "=== BEFORE SAFE VISIBLE BRAND REPLACEMENT ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== GIT ==="
  git branch --show-current
  git log --oneline --decorate -1
  git status --short
  echo
  echo "=== ROOT PROJECT NAME ==="
  grep -n "rootProject.name" settings.gradle.kts || true
  echo
  echo "=== APP NAME STRINGS ==="
  git grep -n -I '<string name="app_name"' -- app/src wear/src || true
  echo
  echo "=== SHARE LABEL ==="
  grep -n 'Share BitChat\|Share Maobits OS' app/src/main/AndroidManifest.xml || true
} > "$VISIBLE_BRAND_DIR/BEFORE-SAFE-VISIBLE-BRAND-REPLACEMENT.txt"
```

---

## 8. Apply safe changes

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 <<'PY'
from pathlib import Path
import re

changes = []

def update_file(path: str, replacements):
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    original = text

    for old, new in replacements:
        text = text.replace(old, new)

    if text != original:
        file_path.write_text(text, encoding="utf-8")
        changes.append(path)

update_file(
    "settings.gradle.kts",
    [
        ('rootProject.name = "bitchat-android"', 'rootProject.name = "maobits-os-android"'),
    ],
)

for root in [Path("app/src/main/res"), Path("wear/src/main/res")]:
    for strings_file in sorted(root.glob("values*/strings.xml")):
        text = strings_file.read_text(encoding="utf-8")
        original = text

        text = re.sub(
            r'(<string\s+name="app_name"[^>]*>)(.*?)(</string>)',
            r'\1Maobits OS\3',
            text,
            flags=re.DOTALL,
        )

        if text != original:
            strings_file.write_text(text, encoding="utf-8")
            changes.append(str(strings_file))

update_file(
    "app/src/main/AndroidManifest.xml",
    [
        ('android:label="Share BitChat"', 'android:label="Share Maobits OS"'),
    ],
)

print("Updated files:")
for item in changes:
    print(f"- {item}")
PY
```

---

## 9. Confirm forbidden areas were not changed

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

printf '\n=== EXPECTED SAFE CHANGES ===\n'
git diff -- settings.gradle.kts app/src/main/res wear/src/main/res app/src/main/AndroidManifest.xml

printf '\n=== MUST STILL EXIST FOR LATER PHASES ===\n'
git grep -n -I -E "namespace = \"com\.bitchat|applicationId = \"com\.bitchat|Theme\.BitchatAndroid|BitchatApplication|BitchatWatchApplication|com\.bitchat\.android\.permission\.FORCE_FINISH|android:scheme=\"bitchat\"" -- app wear settings.gradle.kts || true
```

---

## 10. Create after-change evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISIBLE_BRAND_DIR="docs/03-brand/evidence/2026-07-29-safe-visible-brand-replacement"

{
  echo "=== AFTER SAFE VISIBLE BRAND REPLACEMENT ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== GIT STATUS ==="
  git status --short
  echo
  echo "=== ROOT PROJECT NAME ==="
  grep -n "rootProject.name" settings.gradle.kts || true
  echo
  echo "=== APP NAME STRINGS ==="
  git grep -n -I '<string name="app_name"' -- app/src wear/src || true
  echo
  echo "=== SHARE LABEL ==="
  grep -n 'Share BitChat\|Share Maobits OS' app/src/main/AndroidManifest.xml || true
} > "$VISIBLE_BRAND_DIR/AFTER-SAFE-VISIBLE-BRAND-REPLACEMENT.txt"

cat "$VISIBLE_BRAND_DIR/AFTER-SAFE-VISIBLE-BRAND-REPLACEMENT.txt"
```

---

## 11. Validate build, tests, and lint

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISIBLE_BRAND_DIR="docs/03-brand/evidence/2026-07-29-safe-visible-brand-replacement"

set -o pipefail

./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$VISIBLE_BRAND_DIR/APP-ASSEMBLE-DEBUG-AFTER-VISIBLE-BRAND.log"
APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$VISIBLE_BRAND_DIR/WEAR-ASSEMBLE-DEBUG-AFTER-VISIBLE-BRAND.log"
WEAR_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$VISIBLE_BRAND_DIR/TESTS-AFTER-VISIBLE-BRAND.log"
TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$VISIBLE_BRAND_DIR/LINT-AFTER-VISIBLE-BRAND.log"
LINT_STATUS=${PIPESTATUS[0]}

{
  echo "=== SAFE VISIBLE BRAND VALIDATION SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} > "$VISIBLE_BRAND_DIR/SAFE-VISIBLE-BRAND-VALIDATION-SUMMARY.txt"

cat "$VISIBLE_BRAND_DIR/SAFE-VISIBLE-BRAND-VALIDATION-SUMMARY.txt"
```

---

## 12. Recommended commit

Only if all validations return status `0`:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add settings.gradle.kts \
        app/src/main/res \
        wear/src/main/res \
        app/src/main/AndroidManifest.xml \
        docs/03-brand/MAOBITS-OS-ANDROID-SAFE-VISIBLE-BRAND-REPLACEMENT-1.1.4.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-SAFE-VISIBLE-BRAND-REPLACEMENT-1.1.4.en.md \
        docs/03-brand/evidence/2026-07-29-safe-visible-brand-replacement

git commit -m "brand(app): apply safe visible Maobits OS naming"
```

---

## 13. Acceptance criteria

Phase 1.1.4 is complete when:

- `rootProject.name` uses `maobits-os-android`;
- `app_name` uses `Maobits OS`;
- `Share BitChat` changed to `Share Maobits OS`;
- `applicationId` was not changed;
- `namespace` was not changed;
- Kotlin packages were not changed;
- imports were not changed;
- connectivity was not changed;
- app build returns `0`;
- wear build returns `0`;
- tests return `0`;
- lint returns `0`;
- before/after evidence exists.

---

## 14. Next phase

```text
Phase 1.1.5 — Visual audit of icons, launcher, and graphic resources
```

That phase will review icons, drawables, launcher, adaptive icons, images, and graphic resources before replacing them with Maobits OS visual identity.

---

## 15. Final statement

This first visible change starts the public identity of Maobits OS Android without compromising the internal technical architecture yet.

**Person → Commitment → Confirmation**
