# Maobits OS Android — Technical identity migration plan 1.2.1

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.2.1 — Technical Identity Migration Plan**.

Phase 1.2.0 audits the inherited technical identity. Phase 1.2.1 takes that evidence and defines a safe strategy before touching `applicationId`, `namespace`, Kotlin packages, deep links, custom permissions, or FileProvider.

This is still a planning phase. It does not change functional `app` or `wear` files.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Required input state

Before starting:

```text
1.2.0 — Technical identity audit generated.
docs/04-identity/evidence/2026-07-30-technical-identity-audit exists.
```

If the 1.2.0 audit does not exist, stop this phase.

---

## 4. Critical rule

Do not perform mass replacements.

Do not run:

```bash
sed -i 's/com.bitchat/com.maobits/g'
```

Technical identity must change through controlled stages.

---

## 5. Initial target identity proposal

This phase proposes the following candidates for analysis and approval:

```text
rootProject.name: maobits-os-android

App applicationId candidate:  com.maobits.os.android
Wear applicationId candidate: com.maobits.os.wear

App namespace candidate:  com.maobits.os.android
Wear namespace candidate: com.maobits.os.wear

Shared package candidate: com.maobits.os
App package candidate:    com.maobits.os.android
Wear package candidate:   com.maobits.os.wear

Custom permission candidate:
com.maobits.os.android.permission.FORCE_FINISH

FileProvider:
${applicationId}.fileprovider

Primary deep-link candidate:
maobitsos://

Transitional legacy deep-link:
bitchat://
```

---

## 6. Important applicationId decision

Changing `applicationId` means Android treats the app as a different application.

Consequence:

```text
com.bitchat.droid  → current installed app
com.maobits.os.android → new app for Android
```

Options:

| Option | Advantage | Risk |
|---|---|---|
| Keep `com.bitchat.droid` temporarily | Preserves current install/data | Inherited technical identity remains |
| Change to `com.maobits.os.android` before production | Own technical identity | Requires clean install or explicit migration |
| Use flavors/transition | More control | More complexity |

Recommendation for this stage:

```text
If the app is not officially published yet, change applicationId before public release.
If there are important users/data, design explicit migration.
```

---

## 7. Create branch

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b identity/1.2.1-technical-identity-migration-plan
```

---

## 8. Copy documentation, target map, and tool

Download the ZIP into `/home/maobits/Descargas` and run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_IDENTITY_PLAN_DIR="/tmp/maobits-os-technical-identity-plan-1.2.1"
rm -rf "$TMP_IDENTITY_PLAN_DIR"
mkdir -p "$TMP_IDENTITY_PLAN_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-technical-identity-migration-plan-1-2-1.zip -d "$TMP_IDENTITY_PLAN_DIR"

mkdir -p docs/04-identity
mkdir -p tools/identity

cp "$TMP_IDENTITY_PLAN_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-MIGRATION-PLAN-1.2.1.es.md" docs/04-identity/
cp "$TMP_IDENTITY_PLAN_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-MIGRATION-PLAN-1.2.1.en.md" docs/04-identity/

cp "$TMP_IDENTITY_PLAN_DIR/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-TARGET-MAP-1.2.1.json" docs/04-identity/

cp "$TMP_IDENTITY_PLAN_DIR/tools/identity/maobits_os_generate_identity_migration_plan_1_2_1.sh" tools/identity/
chmod +x tools/identity/maobits_os_generate_identity_migration_plan_1_2_1.sh
```

---

## 9. Generate decision matrix from the 1.2.0 audit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

tools/identity/maobits_os_generate_identity_migration_plan_1_2_1.sh \
  docs/04-identity/evidence/2026-07-30-technical-identity-audit \
  docs/04-identity/evidence/2026-07-30-technical-identity-migration-plan \
  docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-TARGET-MAP-1.2.1.json
```

Generated files:

```text
TECHNICAL-IDENTITY-MIGRATION-DECISION-MATRIX.md
TECHNICAL-IDENTITY-MIGRATION-RISK-REGISTER.md
TECHNICAL-IDENTITY-MIGRATION-PLAN-SUMMARY.txt
TECHNICAL-IDENTITY-MIGRATION-PLAN-SHA256.txt
```

---

## 10. Validate that no functional changes occurred

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git diff --name-only -- app wear settings.gradle.kts build.gradle.kts gradle.properties
```

This must be empty.

---

## 11. Optional automatic validation

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

IDENTITY_PLAN_EVIDENCE_DIR="docs/04-identity/evidence/2026-07-30-technical-identity-migration-plan"

set -o pipefail

./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_PLAN_EVIDENCE_DIR/APP-ASSEMBLE-DEBUG-IDENTITY-PLAN.log"
APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_PLAN_EVIDENCE_DIR/WEAR-ASSEMBLE-DEBUG-IDENTITY-PLAN.log"
WEAR_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_PLAN_EVIDENCE_DIR/TESTS-IDENTITY-PLAN.log"
TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_PLAN_EVIDENCE_DIR/LINT-IDENTITY-PLAN.log"
LINT_STATUS=${PIPESTATUS[0]}

{
  echo "=== MAOBITS OS ANDROID - TECHNICAL IDENTITY MIGRATION PLAN VALIDATION SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} > "$IDENTITY_PLAN_EVIDENCE_DIR/TECHNICAL-IDENTITY-MIGRATION-PLAN-VALIDATION-SUMMARY.txt"

cat "$IDENTITY_PLAN_EVIDENCE_DIR/TECHNICAL-IDENTITY-MIGRATION-PLAN-VALIDATION-SUMMARY.txt"
```

---

## 12. Approval criteria

Explicitly approve:

```text
[ ] target app applicationId.
[ ] target wear applicationId.
[ ] target app namespace.
[ ] target wear namespace.
[ ] clean install or migration strategy.
[ ] primary deep link.
[ ] transitional legacy deep link yes/no.
[ ] FileProvider authority.
[ ] custom permission.
[ ] migration order.
[ ] rollback.
```

---

## 13. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-MIGRATION-PLAN-1.2.1.es.md \
        docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-MIGRATION-PLAN-1.2.1.en.md \
        docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-TARGET-MAP-1.2.1.json \
        docs/04-identity/evidence/2026-07-30-technical-identity-migration-plan \
        tools/identity/maobits_os_generate_identity_migration_plan_1_2_1.sh

git commit -m "docs(identity): plan technical identity migration"

git push -u origin identity/1.2.1-technical-identity-migration-plan
```

---

## 14. Next phase

```text
Phase 1.2.2 — Gradle identity migration dry-run
```

That phase will test `applicationId` and `namespace` first in an isolated branch, with rollback, without changing all Kotlin packages yet.

---

## 15. Final statement

Phase 1.2.1 converts the audit into a technical migration plan. The project must not touch active technical identity until these decisions are approved.

**Person → Commitment → Confirmation**
