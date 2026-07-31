# Maobits OS Android — Technical identity audit 1.2.0

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.2.0 — Technical Name, Package, ApplicationId, and Deep-Link Audit**.

This phase is inventory and analysis only. It does not change code, package declarations, `applicationId`, `namespace`, or manifest files.

The goal is to know precisely what still depends on the inherited technical identity before planning a safe migration toward Maobits OS technical identity.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Recommended input state

Before this phase, the first visual block should be closed:

```text
1.1.4 — Maobits OS visible brand.
1.1.7 — Approved visual asset.
1.1.9 — Legacy launcher PNG replaced.
1.1.10 — Adaptive icons replaced.
1.1.11 — Initial visual closure or equivalent evidence.
```

---

## 4. Critical rule

Do not perform mass replacements.

Do not run commands such as:

```bash
sed -i 's/com.bitchat/com.maobits/g'
```

That can break:

```text
installation and updates;
local data;
FileProvider;
deep links;
custom permissions;
services;
receivers;
tests;
Wear module;
backward compatibility.
```

---

## 5. Create branch

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b identity/1.2.0-technical-identity-audit
```

---

## 6. Copy documentation and tool

Download the ZIP into `/home/maobits/Descargas` and run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_IDENTITY_AUDIT_DIR="/tmp/maobits-os-technical-identity-audit-1.2.0"
rm -rf "$TMP_IDENTITY_AUDIT_DIR"
mkdir -p "$TMP_IDENTITY_AUDIT_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-technical-identity-audit-1-2-0.zip -d "$TMP_IDENTITY_AUDIT_DIR"

mkdir -p docs/04-identity
mkdir -p tools/identity

cp "$TMP_IDENTITY_AUDIT_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-AUDIT-1.2.0.es.md" docs/04-identity/
cp "$TMP_IDENTITY_AUDIT_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-AUDIT-1.2.0.en.md" docs/04-identity/

cp "$TMP_IDENTITY_AUDIT_DIR/tools/identity/maobits_os_collect_technical_identity_audit_1_2_0.sh" tools/identity/
chmod +x tools/identity/maobits_os_collect_technical_identity_audit_1_2_0.sh
```

---

## 7. Run audit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

tools/identity/maobits_os_collect_technical_identity_audit_1_2_0.sh \
  docs/04-identity/evidence/2026-07-30-technical-identity-audit
```

---

## 8. Generated evidence files

```text
00-REPOSITORY-STATE.txt
01-GRADLE-TECHNICAL-IDENTITY.txt
02-MANIFEST-TECHNICAL-IDENTITY.txt
03-DEEP-LINKS-AND-SCHEMES.txt
04-FILEPROVIDER-AND-AUTHORITIES.txt
05-CUSTOM-PERMISSIONS.txt
06-KOTLIN-JAVA-PACKAGES-AND-IMPORTS.txt
07-CODE-TECHNICAL-IDENTITY-REFERENCES.txt
08-RESOURCE-TECHNICAL-IDENTITY-REFERENCES.txt
09-TEST-DEBUG-TECHNICAL-IDENTITY-REFERENCES.txt
10-MIGRATION-RISK-SUMMARY.txt
11-AUDIT-FILE-SHA256.txt
```

---

## 9. Validate that no functional changes happened

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git diff --name-only -- app wear settings.gradle.kts build.gradle.kts gradle.properties
```

This must be empty, because this phase only adds documentation, tools, and evidence.

---

## 10. Optional automatic validation

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

IDENTITY_AUDIT_EVIDENCE_DIR="docs/04-identity/evidence/2026-07-30-technical-identity-audit"

set -o pipefail

./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_AUDIT_EVIDENCE_DIR/APP-ASSEMBLE-DEBUG-IDENTITY-AUDIT.log"
APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_AUDIT_EVIDENCE_DIR/WEAR-ASSEMBLE-DEBUG-IDENTITY-AUDIT.log"
WEAR_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_AUDIT_EVIDENCE_DIR/TESTS-IDENTITY-AUDIT.log"
TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug --no-daemon --stacktrace --warning-mode all \
  2>&1 | tee "$IDENTITY_AUDIT_EVIDENCE_DIR/LINT-IDENTITY-AUDIT.log"
LINT_STATUS=${PIPESTATUS[0]}

{
  echo "=== MAOBITS OS ANDROID - TECHNICAL IDENTITY AUDIT VALIDATION SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} > "$IDENTITY_AUDIT_EVIDENCE_DIR/TECHNICAL-IDENTITY-AUDIT-VALIDATION-SUMMARY.txt"

cat "$IDENTITY_AUDIT_EVIDENCE_DIR/TECHNICAL-IDENTITY-AUDIT-VALIDATION-SUMMARY.txt"
```

---

## 11. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-AUDIT-1.2.0.es.md \
        docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-AUDIT-1.2.0.en.md \
        docs/04-identity/evidence/2026-07-30-technical-identity-audit \
        tools/identity/maobits_os_collect_technical_identity_audit_1_2_0.sh

git commit -m "docs(identity): audit technical identity migration scope"

git push -u origin identity/1.2.0-technical-identity-audit
```

---

## 12. Next phase

```text
Phase 1.2.1 — Technical identity migration plan
```

That phase will explicitly decide:

```text
target applicationId;
target namespace;
target Kotlin packages;
target scheme/deep links;
FileProvider authorities;
custom permissions;
update or clean-install strategy;
Wear impact;
rollback.
```

---

## 13. Closure criteria for 1.2.0

The phase is closed when:

```text
audit evidence is generated;
risks are documented;
no functional changes were made;
evidence is versioned;
1.2.1 can be designed without guessing.
```

---

## 14. Final statement

This phase protects the project from a rushed technical migration. First observe everything depending on the inherited identity; then plan the change precisely.

**Person → Commitment → Confirmation**
