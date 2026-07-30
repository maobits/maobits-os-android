# Maobits OS Android — Java 21 Toolchain Fix 0.9.1

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document records the required fix to continue **Phase 0.9 — Reproducible Technical Baseline**.

During Gradle execution, the project successfully listed modules, but failed while creating compilation tasks because the local environment uses Java 17 and the project requires a Java 21 toolchain.

---

## 2. Diagnosis

Gradle detected:

```text
Launcher JVM: 17.0.17
Daemon JVM: /home/maobits/.sdkman/candidates/java/17.0.17-tem
```

The main error says:

```text
Cannot find a Java installation on your machine matching: {languageVersion=21}
Toolchain download repositories have not been configured.
```

This means the repository or Android/Kotlin plugin is configured to compile with Java 21, but the local machine only has Java 17 active.

---

## 3. Technical decision

The correct solution in this phase is to install Java 21 locally and use it for the baseline.

Do not change code, Gradle, `applicationId`, `namespace`, packages, permissions, or functional logic yet.

---

## 4. Fix with SDKMAN

The environment already shows SDKMAN usage, so this is the recommended path.

Run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

sdk list java | grep -E "21\..*tem" || true
```

Then install an available Java 21 Temurin version. Common example:

```bash
sdk install java 21.0.9-tem
```

If SDKMAN shows a newer Java 21 version, use exactly the identifier shown by `sdk list java`.

Then activate Java 21 in the current terminal:

```bash
sdk use java 21.0.9-tem
```

Or set it as default:

```bash
sdk default java 21.0.9-tem
```

Validate:

```bash
java -version
javac -version
```

The output must show Java 21.

---

## 5. Alternative with system package

If you prefer system packages and your distribution supports it:

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk

sudo update-alternatives --config java
sudo update-alternatives --config javac

java -version
javac -version
```

If `openjdk-21-jdk` is not available in your distribution repositories, use SDKMAN.

---

## 6. Repeat baseline after installing Java 21

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

{
  echo "=== JAVA AFTER TOOLCHAIN FIX ==="
  java -version 2>&1
  echo
  echo "=== JAVAC AFTER TOOLCHAIN FIX ==="
  javac -version 2>&1
} > "$BASELINE_DIR/BASELINE-JAVA-21-TOOLCHAIN-FIX.txt"

./gradlew tasks --all \
  --no-daemon \
  --stacktrace \
  2>&1 | tee "$BASELINE_DIR/BASELINE-GRADLE-TASKS-AFTER-JAVA21.log"
```

---

## 7. Build again

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

set -o pipefail

./gradlew :app:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-APP-ASSEMBLE-DEBUG-AFTER-JAVA21.log"

APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-WEAR-ASSEMBLE-DEBUG-AFTER-JAVA21.log"

WEAR_BUILD_STATUS=${PIPESTATUS[0]}

{
  echo "=== BASELINE BUILD SUMMARY AFTER JAVA 21 ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
} > "$BASELINE_DIR/BASELINE-SUMMARY-AFTER-JAVA21.txt"

cat "$BASELINE_DIR/BASELINE-SUMMARY-AFTER-JAVA21.txt"
```

---

## 8. Acceptance criteria

The fix is accepted when:

- `java -version` shows Java 21;
- `javac -version` shows Java 21;
- `./gradlew tasks --all` no longer fails due to Java 21 toolchain;
- `BASELINE-JAVA-21-TOOLCHAIN-FIX.txt` is generated;
- `BASELINE-SUMMARY-AFTER-JAVA21.txt` is generated;
- `app` and `wear` results are documented;
- no functional code was modified.

---

## 9. Recommended commit

After validating and reviewing evidence:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git add docs/05-audit/evidence/2026-07-29-reproducible-baseline \
        docs/05-audit/MAOBITS-OS-ANDROID-JAVA-21-TOOLCHAIN-FIX-0.9.1.es.md \
        docs/05-audit/MAOBITS-OS-ANDROID-JAVA-21-TOOLCHAIN-FIX-0.9.1.en.md

git commit -m "docs(audit): document Java 21 toolchain requirement"
```

---

## 10. Final statement

This adjustment does not change Maobits OS Android. It only aligns the local environment with the required toolchain for reproducible auditing and builds.

**Person → Commitment → Confirmation**
