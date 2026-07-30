# Maobits OS Android — Reemplazo controlado de launcher icons 1.1.9

**Versión:** 0.1.0  
**Fecha:** 2026-07-30  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1.9 — Reemplazo controlado de launcher icons**.

Esta fase aplica los recursos candidatos generados en 1.1.8 sobre los PNG activos `ic_launcher.png` e `ic_launcher_round.png` de `app` y `wear`, con respaldo previo, evidencia, validación de build/lint/test y prueba real.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada obligatorio

Antes de iniciar deben existir:

```text
1.1.7 — Asset visual aprobado.
1.1.8 — Recursos candidatos generados bajo docs/03-brand/generated/.
```

También debe existir la prueba real exitosa en dos smartphones antes de modificar recursos visuales activos.

---

## 4. Alcance exacto

Esta fase puede reemplazar únicamente:

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

wear/src/main/res/mipmap-* equivalentes
```

No modifica todavía:

```text
mipmap-anydpi-v26/ic_launcher.xml
mipmap-anydpi-v26/ic_launcher_round.xml
adaptive icon foreground/background XML
AndroidManifest.xml
applicationId
namespace
paquetes Kotlin
tema visual
colores globales
```

> Nota: en Android moderno puede existir adaptive icon en `mipmap-anydpi-v26`. Si el launcher todavía muestra el ícono anterior después de esta fase, no es falla; significa que la fase siguiente debe reemplazar las capas adaptive icon.

---

## 5. Crear rama

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git checkout -b brand/1.1.9-controlled-launcher-icons
```

---

## 6. Copiar documentación y herramienta

Descarga el ZIP en `/home/maobits/Descargas` y ejecuta:

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

## 7. Auditoría previa del estado activo

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

## 8. Dry-run obligatorio

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_launcher_icons_1_1_9.py \
  --mode dry-run \
  --repo-root . \
  --candidate-root docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement

cat docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement/LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt
```

Si aparecen candidatos faltantes, detener la fase.

---

## 9. Aplicar reemplazo controlado

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

## 10. Revisar diff

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

## 11. Validación automática

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

## 12. Prueba real en teléfono

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

adb devices

./gradlew :app:installDebug --no-daemon --stacktrace --warning-mode all

adb shell am force-stop com.bitchat.droid
adb shell monkey -p com.bitchat.droid -c android.intent.category.LAUNCHER 1
```

Revisar manualmente:

```text
[ ] La app abre.
[ ] Sigue apareciendo como Maobits OS.
[ ] No crashea.
[ ] El ícono se actualiza si el launcher usa PNG legacy.
[ ] Si el ícono no se actualiza, revisar adaptive icon en 1.1.10.
```

---

## 13. Rollback si algo falla

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_apply_launcher_icons_1_1_9.py \
  --mode rollback \
  --repo-root . \
  --evidence-dir docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement
```

Luego repetir build/test/lint.

---

## 14. Commit recomendado

Solo si todo valida:

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

## 15. Próxima fase

```text
Fase 1.1.10 — Reemplazo controlado de adaptive icons
```

Esa fase revisará y reemplazará `mipmap-anydpi-v26`, foreground/background y recursos adaptativos si el dispositivo moderno todavía muestra el icono anterior.

---

## 16. Declaración final

Esta fase reemplaza solo los PNG launcher legacy con respaldo, evidencia y validación. Los adaptive icons quedan separados para evitar romper Android moderno por cambios visuales no auditados.

**Persona → Compromiso → Confirmación**
