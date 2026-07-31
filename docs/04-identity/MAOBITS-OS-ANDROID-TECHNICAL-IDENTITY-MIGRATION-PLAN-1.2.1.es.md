# Maobits OS Android — Plan de migración de identidad técnica 1.2.1

**Versión:** 0.1.0  
**Fecha:** 2026-07-30  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.2.1 — Plan de migración de identidad técnica**.

La fase 1.2.0 audita la identidad técnica heredada. La fase 1.2.1 toma esa evidencia y define una estrategia segura antes de tocar `applicationId`, `namespace`, paquetes Kotlin, deep links, permisos personalizados o FileProvider.

Esta fase sigue siendo de planificación. No cambia archivos funcionales de `app` ni `wear`.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada obligatorio

Antes de iniciar:

```text
1.2.0 — Auditoría de identidad técnica generada.
docs/04-identity/evidence/2026-07-30-technical-identity-audit existe.
```

Si no existe la auditoría 1.2.0, detener esta fase.

---

## 4. Regla crítica

No hacer reemplazos masivos.

No ejecutar:

```bash
sed -i 's/com.bitchat/com.maobits/g'
```

El cambio de identidad técnica debe ser por etapas controladas.

---

## 5. Propuesta inicial de identidad objetivo

Esta fase propone, para análisis y aprobación, los siguientes candidatos:

```text
rootProject.name: maobits-os-android

App applicationId candidato:  com.maobits.os.android
Wear applicationId candidato: com.maobits.os.wear

App namespace candidato:  com.maobits.os.android
Wear namespace candidato: com.maobits.os.wear

Package compartido candidato: com.maobits.os
Package app candidato:       com.maobits.os.android
Package wear candidato:      com.maobits.os.wear

Permiso personalizado candidato:
com.maobits.os.android.permission.FORCE_FINISH

FileProvider:
${applicationId}.fileprovider

Deep link principal candidato:
maobitsos://

Deep link heredado transitorio:
bitchat://
```

---

## 6. Decisión importante sobre `applicationId`

Cambiar `applicationId` significa que Android tratará la app como otra aplicación.

Consecuencia:

```text
com.bitchat.droid  → app instalada actual
com.maobits.os.android → app nueva para Android
```

Opciones:

| Opción | Ventaja | Riesgo |
|---|---|---|
| Mantener `com.bitchat.droid` temporalmente | Conserva instalación/datos actuales | Identidad técnica heredada permanece |
| Cambiar a `com.maobits.os.android` antes de producción | Identidad técnica propia | Requiere instalación limpia o migración explícita |
| Usar flavors/transición | Más control | Más complejidad |

Recomendación para esta etapa:

```text
Si la app aún no está publicada oficialmente, cambiar applicationId antes del release público.
Si ya hay usuarios/datos importantes, diseñar migración explícita.
```

---

## 7. Crear rama

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b identity/1.2.1-technical-identity-migration-plan
```

---

## 8. Copiar documentación, target map y herramienta

Descarga el ZIP en `/home/maobits/Descargas` y ejecuta:

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

## 9. Generar matriz de decisión desde la auditoría 1.2.0

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

tools/identity/maobits_os_generate_identity_migration_plan_1_2_1.sh \
  docs/04-identity/evidence/2026-07-30-technical-identity-audit \
  docs/04-identity/evidence/2026-07-30-technical-identity-migration-plan \
  docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-TARGET-MAP-1.2.1.json
```

Archivos generados:

```text
TECHNICAL-IDENTITY-MIGRATION-DECISION-MATRIX.md
TECHNICAL-IDENTITY-MIGRATION-RISK-REGISTER.md
TECHNICAL-IDENTITY-MIGRATION-PLAN-SUMMARY.txt
TECHNICAL-IDENTITY-MIGRATION-PLAN-SHA256.txt
```

---

## 10. Validar que no hubo cambios funcionales

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git diff --name-only -- app wear settings.gradle.kts build.gradle.kts gradle.properties
```

Debe salir vacío.

---

## 11. Validación automática opcional

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

## 12. Criterios de aprobación

Aprobar explícitamente:

```text
[ ] applicationId app objetivo.
[ ] applicationId wear objetivo.
[ ] namespace app objetivo.
[ ] namespace wear objetivo.
[ ] estrategia de instalación limpia o migración.
[ ] deep link principal.
[ ] deep link heredado transitorio sí/no.
[ ] FileProvider authority.
[ ] permiso personalizado.
[ ] orden de migración.
[ ] rollback.
```

---

## 13. Commit recomendado

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

## 14. Próxima fase

```text
Fase 1.2.2 — Dry-run de migración de Gradle identity
```

Esa fase probará primero `applicationId` y `namespace` en una rama aislada, con rollback, sin tocar todavía todos los paquetes Kotlin.

---

## 15. Declaración final

La fase 1.2.1 convierte la auditoría en un plan de migración técnica. El proyecto no debe tocar identidad técnica activa hasta que estas decisiones estén aprobadas.

**Persona → Compromiso → Confirmación**
