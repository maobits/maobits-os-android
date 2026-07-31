# Maobits OS Android — Auditoría de identidad técnica 1.2.0

**Versión:** 0.1.0  
**Fecha:** 2026-07-30  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.2.0 — Auditoría de nombre técnico, package, applicationId y deep links**.

Esta fase es únicamente de inventario y análisis. No cambia código, no reemplaza paquetes, no cambia `applicationId`, no cambia `namespace` y no modifica manifest.

El objetivo es conocer con precisión todo lo que depende todavía de la identidad técnica heredada antes de planificar una migración segura hacia identidad técnica Maobits OS.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada recomendado

Antes de esta fase debe estar cerrado el primer bloque visual:

```text
1.1.4 — Marca visible Maobits OS.
1.1.7 — Asset visual aprobado.
1.1.9 — Launcher PNG legacy reemplazado.
1.1.10 — Adaptive icons reemplazados.
1.1.11 — Cierre visual inicial o evidencia equivalente.
```

---

## 4. Regla crítica

No hacer reemplazos masivos.

No ejecutar comandos como:

```bash
sed -i 's/com.bitchat/com.maobits/g'
```

Eso puede romper:

```text
instalación y actualizaciones;
datos locales;
FileProvider;
deep links;
permisos personalizados;
servicios;
receivers;
tests;
módulo Wear;
compatibilidad con versiones previas.
```

---

## 5. Crear rama

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b identity/1.2.0-technical-identity-audit
```

---

## 6. Copiar documentación y herramienta

Descarga el ZIP en `/home/maobits/Descargas` y ejecuta:

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

## 7. Ejecutar auditoría

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

tools/identity/maobits_os_collect_technical_identity_audit_1_2_0.sh \
  docs/04-identity/evidence/2026-07-30-technical-identity-audit
```

---

## 8. Archivos de evidencia generados

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

## 9. Validación de que no hubo cambios funcionales

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git diff --name-only -- app wear settings.gradle.kts build.gradle.kts gradle.properties
```

Debe salir vacío, porque esta fase solo agrega documentación, herramientas y evidencia.

---

## 10. Validación automática opcional

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

## 11. Commit recomendado

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

## 12. Próxima fase

```text
Fase 1.2.1 — Plan de migración de identidad técnica
```

Esa fase decidirá explícitamente:

```text
applicationId objetivo;
namespace objetivo;
paquetes Kotlin objetivo;
scheme/deep links objetivo;
autoridades FileProvider;
permisos personalizados;
estrategia de actualización o instalación limpia;
impacto en Wear;
rollback.
```

---

## 13. Criterio de cierre de 1.2.0

La fase se considera cerrada cuando:

```text
la auditoría está generada;
los riesgos están documentados;
no hubo cambios funcionales;
la evidencia está versionada;
se puede diseñar 1.2.1 sin adivinar.
```

---

## 14. Declaración final

Esta fase protege el proyecto contra una migración técnica apresurada. Primero se observa todo lo que depende de la identidad heredada; después se planifica el cambio con precisión.

**Persona → Compromiso → Confirmación**
