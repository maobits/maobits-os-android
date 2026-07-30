# Maobits OS Android — Reproducible Technical Baseline 0.9

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 0.9 — Reproducible Technical Baseline** for Maobits OS Android.

The purpose is to confirm that the Android repository can be built, inspected, and audited before changing branding, packages, `applicationId`, `namespace`, permissions, screens, or connectivity logic.

This phase prevents code changes on an unknown base.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Expected input state

Before running this phase, a previous documentation commit for the initial audit should exist.

Observed project commit:

```text
4dc40c3 docs(audit): add Android baseline audit evidence
```

Expected branch:

```text
foundation/00-maobits-os-android-baseline
```

---

## 4. Safety rule for this phase

During this phase do not:

- change `applicationId`;
- change `namespace`;
- rename Kotlin packages;
- remove permissions;
- remove services;
- change commercial naming in resources;
- modify BLE, Wi-Fi Aware, Nostr, encryption, store-and-forward, or foreground service logic;
- delete licenses;
- change original files without prior evidence.

The goal is to **measure and verify**, not customize.

---

## 5. Expected evidence

Evidence for this phase must be stored in:

```text
docs/05-audit/evidence/2026-07-29-reproducible-baseline
```

Expected files:

```text
BASELINE-GIT-STATE.txt
BASELINE-JAVA-GRADLE.txt
BASELINE-GRADLE-PROJECTS.txt
BASELINE-GRADLE-TASKS.txt
BASELINE-APP-ASSEMBLE-DEBUG.log
BASELINE-WEAR-ASSEMBLE-DEBUG.log
BASELINE-TESTS.log
BASELINE-LINT.log
BASELINE-SUMMARY.txt
```

---

## 6. Reproducible baseline commands

Run from the repository:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"
mkdir -p "$BASELINE_DIR"

{
  echo "=== MAOBITS OS ANDROID - BASELINE GIT STATE ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== PWD ==="
  pwd
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== GIT STATUS ==="
  git status
  echo
  echo "=== LAST 10 COMMITS ==="
  git log --oneline --decorate -10
  echo
  echo "=== REMOTES ==="
  git remote -v
} > "$BASELINE_DIR/BASELINE-GIT-STATE.txt"

{
  echo "=== JAVA ==="
  java -version 2>&1 || true
  echo
  echo "=== JAVAC ==="
  javac -version 2>&1 || true
  echo
  echo "=== GRADLE WRAPPER FILES ==="
  ls -la gradlew gradle/wrapper 2>&1 || true
} > "$BASELINE_DIR/BASELINE-JAVA-GRADLE.txt"

chmod +x ./gradlew

./gradlew --version \
  --no-daemon \
  2>&1 | tee -a "$BASELINE_DIR/BASELINE-JAVA-GRADLE.txt"

./gradlew projects \
  --no-daemon \
  --stacktrace \
  2>&1 | tee "$BASELINE_DIR/BASELINE-GRADLE-PROJECTS.txt"

./gradlew tasks --all \
  --no-daemon \
  --stacktrace \
  2>&1 | tee "$BASELINE_DIR/BASELINE-GRADLE-TASKS.txt"
```

---

## 7. Controlled build

Run each build separately to isolate errors.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

set -o pipefail

./gradlew :app:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-APP-ASSEMBLE-DEBUG.log"

APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-WEAR-ASSEMBLE-DEBUG.log"

WEAR_BUILD_STATUS=${PIPESTATUS[0]}

{
  echo "=== BASELINE BUILD SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
} > "$BASELINE_DIR/BASELINE-SUMMARY.txt"

cat "$BASELINE_DIR/BASELINE-SUMMARY.txt"
```

---

## 8. Tests and lint

Run only after the initial build:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

set -o pipefail

./gradlew testDebugUnitTest \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-TESTS.log"

TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-LINT.log"

LINT_STATUS=${PIPESTATUS[0]}

{
  echo
  echo "=== TEST AND LINT SUMMARY ==="
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} >> "$BASELINE_DIR/BASELINE-SUMMARY.txt"

cat "$BASELINE_DIR/BASELINE-SUMMARY.txt"
```

---

## 9. Status interpretation

| Code | Meaning | Action |
|---:|---|---|
| `0` | Command succeeded | Record evidence and continue |
| Non-zero | Build, test, or lint error | Do not fix yet without analyzing the log |
| Missing `gradlew` | Incomplete repository or non-standard structure | Review base files |
| Java/Gradle failure | Local environment not compatible | Adjust environment before touching code |
| App failure | Main mobile module problem | Analyze `BASELINE-APP-ASSEMBLE-DEBUG.log` |
| Wear failure | Wear OS problem | Decide whether Wear is maintained, postponed, or isolated |
| Lint failure | Technical debt or strict rules | Document before correcting |
| Test failure | Broken tests or incomplete setup | Document and fix in a separate phase |

---

## 10. Findings register

After running the commands, record:

```text
- detected Java
- detected Gradle wrapper
- detected Gradle modules
- app assembleDebug result
- wear assembleDebug result
- testDebugUnitTest result
- lintDebug result
- main errors if any
- main warnings if any
- progress decision
```

---

## 11. Acceptance criteria

Phase 0.9 is complete when:

- evidence is stored under `docs/05-audit/evidence/2026-07-29-reproducible-baseline`;
- it is known whether `app` builds;
- it is known whether `wear` builds;
- executable unit tests are known;
- `lintDebug` result is known;
- errors are recorded honestly;
- no improvised functional code changes were made;
- a documentation commit with evidence exists;
- a formal decision exists to enter Phase 1.0.

---

## 12. Recommended commit

Only after reviewing the evidence:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/05-audit/evidence/2026-07-29-reproducible-baseline \
        docs/05-audit/MAOBITS-OS-ANDROID-REPRODUCIBLE-BASELINE-0.9.es.md \
        docs/05-audit/MAOBITS-OS-ANDROID-REPRODUCIBLE-BASELINE-0.9.en.md

git commit -m "docs(audit): add reproducible Android baseline evidence"
```

---

## 13. Next phase

If the baseline succeeds or errors are clearly documented, the next step will be:

```text
Phase 1.0 — Official maobits-os-android repository plan
```

That phase will define:

- official repository creation or connection;
- `origin` for Maobits OS Android;
- separate remote for the technical reference source;
- protected branches;
- initial tags;
- commit policy;
- Pull Request change policy;
- brand and license separation.

---

## 14. Final statement

The reproducible technical baseline is the point where Maobits OS Android stops being an intention and starts becoming a controlled project.

**Person → Commitment → Confirmation**
