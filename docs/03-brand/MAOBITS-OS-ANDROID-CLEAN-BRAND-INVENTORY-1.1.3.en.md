# Maobits OS Android — Clean Brand Inventory and Safe Replacement Plan 1.1.3

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.3 — Clean Brand Inventory and Safe Replacement Plan**.

The previous phase generated a broad inventory, but the counts included generated build files, lint reports, documentation evidence, and `build` folders. To make correct decisions, this phase generates a second clean evidence set based on versioned files and real project sources.

The goal is to avoid wrong decisions caused by generated files.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Diagnosis of the previous evidence

The previous output showed files such as:

```text
app/build/intermediates/...
app/build/reports/...
wear/build/intermediates/...
wear/build/reports/...
docs/03-brand/evidence/...
docs/05-audit/evidence/...
```

These files are useful as technical evidence, but they must not directly drive visible-brand replacement decisions.

---

## 4. Methodological decision

From this subphase forward, two evidence types are separated:

| Type | Folder | Use |
|---|---|---|
| Raw evidence | `docs/03-brand/evidence/2026-07-29-brand-inventory` | Keeps everything initially detected |
| Clean evidence | `docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files` | Used to decide real changes |

Clean evidence must be generated with `git grep` and `git ls-files`, because these commands work on versioned files and avoid generated-folder noise.

---

## 5. Safety rule

Do not run mass replacements.

Do not use:

```bash
sed -i 's/bitchat/maobits/g'
```

Do not touch yet:

- `applicationId`;
- `namespace`;
- Kotlin packages;
- `com.bitchat` imports;
- custom permissions;
- authorities;
- services;
- providers;
- receivers;
- connectivity logic;
- encryption;
- store-and-forward.

---

## 6. Create clean evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"
mkdir -p "$CLEAN_BRAND_DIR"

git ls-files > "$CLEAN_BRAND_DIR/TRACKED-FILES.txt"

git ls-files \
  app/src \
  wear/src \
  app/build.gradle.kts \
  wear/build.gradle.kts \
  settings.gradle.kts \
  build.gradle.kts \
  gradle.properties \
  README.md \
  LICENSE.md \
  docs \
  tools \
  > "$CLEAN_BRAND_DIR/TRACKED-REVIEW-SCOPE.txt"
```

---

## 7. Clean Gradle public identity

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== CLEAN GRADLE PUBLIC IDENTITY ==="
  git grep -n -I -E "rootProject.name|namespace|applicationId|versionCode|versionName|archivesName|compileSdk|minSdk|targetSdk" \
    -- settings.gradle.kts build.gradle.kts gradle.properties app/build.gradle.kts wear/build.gradle.kts \
    || true
} > "$CLEAN_BRAND_DIR/CLEAN-GRADLE-PUBLIC-IDENTITY.txt"
```

---

## 8. Clean Manifest review

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== CLEAN MANIFEST BRAND REVIEW ==="
  git grep -n -I -E "android:label|android:icon|android:roundIcon|android:theme|android:authorities|permission|provider|service|activity|receiver|Share BitChat|Bitchat|BitChat|bitchat" \
    -- app/src/main/AndroidManifest.xml app/src/debug/AndroidManifest.xml wear/src/main/AndroidManifest.xml wear/src/debug/AndroidManifest.xml \
    || true
} > "$CLEAN_BRAND_DIR/CLEAN-MANIFEST-BRAND-REVIEW.txt"
```

---

## 9. Clean visible text review

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== CLEAN USER VISIBLE BRAND CANDIDATES ==="
  git grep -n -I -E "app_name|BitChat|Bitchat|bitchat|Share BitChat|about|About|notification|Notification|foreground|Foreground|privacy|Privacy|identity|Identity" \
    -- app/src wear/src \
    || true
} > "$CLEAN_BRAND_DIR/CLEAN-USER-VISIBLE-BRAND-CANDIDATES.txt"
```

---

## 10. Clean notification and foreground service review

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== CLEAN NOTIFICATION UX BRAND CANDIDATES ==="
  git grep -n -I -E "NotificationChannel|setContentTitle|setContentText|notification|Notification|foreground|Foreground|channel|Channel|MeshForegroundService|WearMeshForegroundService|BitChat|Bitchat|bitchat" \
    -- app/src wear/src \
    || true
} > "$CLEAN_BRAND_DIR/CLEAN-NOTIFICATION-UX-BRAND-CANDIDATES.txt"
```

---

## 11. Clean package migration risk

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== CLEAN PACKAGE MIGRATION RISK ==="
  git grep -n -I -E "^package com\.bitchat|^import com\.bitchat|com\.bitchat" \
    -- app/src wear/src app/build.gradle.kts wear/build.gradle.kts settings.gradle.kts \
    || true
} > "$CLEAN_BRAND_DIR/CLEAN-PACKAGE-MIGRATION-RISK.txt"
```

---

## 12. Attribution to preserve

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== CLEAN ATTRIBUTION PRESERVE ==="
  git grep -n -I -E "BitChat|Bitchat|bitchat|permissionlesstech|callebtc|jack|GPL|Unlicense|License|LICENSE|copyright|source|fork|reference" \
    -- README.md LICENSE.md docs tools \
    || true
} > "$CLEAN_BRAND_DIR/CLEAN-ATTRIBUTION-PRESERVE.txt"
```

---

## 13. Clean summary

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

{
  echo "=== MAOBITS OS ANDROID - CLEAN BRAND INVENTORY SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== CLEAN MATCH COUNTS ==="
  for file in "$CLEAN_BRAND_DIR"/CLEAN-*.txt; do
    printf "%s: " "$(basename "$file")"
    grep -Eic "bitchat|BitChat|Bitchat|com\.bitchat|permissionlesstech|callebtc|jack|GPL|Unlicense|License" "$file" || true
  done
} > "$CLEAN_BRAND_DIR/CLEAN-BRAND-INVENTORY-SUMMARY.txt"

cat "$CLEAN_BRAND_DIR/CLEAN-BRAND-INVENTORY-SUMMARY.txt"
```

---

## 14. Minimum manual inspection

After the clean summary, inspect:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

CLEAN_BRAND_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files"

cat "$CLEAN_BRAND_DIR/CLEAN-GRADLE-PUBLIC-IDENTITY.txt"
cat "$CLEAN_BRAND_DIR/CLEAN-MANIFEST-BRAND-REVIEW.txt"

printf '\n=== APP NAME REFERENCES ===\n'
git grep -n -I "app_name" -- app/src wear/src || true

printf '\n=== STRINGS FILES ===\n'
find app/src wear/src -type f -path "*/res/values*/strings.xml" | sort

printf '\n=== MAIN STRINGS SAMPLE ===\n'
sed -n '1,220p' app/src/main/res/values/strings.xml
```

---

## 15. First recommended safe change

The first safe change should be limited to:

```text
rootProject.name
app_name
Share BitChat
strictly confirmed visible text
```

Do not touch:

```text
namespace
applicationId
package com.bitchat.*
import com.bitchat.*
custom permission
providers
authorities
services
receivers
BLE
Wi-Fi Aware
Nostr
encryption
store-and-forward
```

---

## 16. Acceptance criteria

Subphase 1.1.3 is complete when:

- clean evidence is generated;
- raw evidence is separated from evidence useful for changes;
- `app_name` location is confirmed;
- visible labels are confirmed;
- the project documents what can change and what must wait;
- no functional code is modified;
- the project is ready for phase 1.1.4.

---

## 17. Next phase

```text
Phase 1.1.4 — First safe visible-brand replacement
```

That phase will apply controlled changes only to visible name, minimum visible text, and own documentation, followed by build, test, and lint.

---

## 18. Final statement

Maobits OS Android must be customized with surgical precision: visible and safe first, public technical identity second, deep internal identity last.

**Person → Commitment → Confirmation**
