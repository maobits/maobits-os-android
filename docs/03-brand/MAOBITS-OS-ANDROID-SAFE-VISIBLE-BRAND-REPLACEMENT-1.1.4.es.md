# Maobits OS Android — Primer reemplazo seguro de marca visible 1.1.4

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1.4 — Primer reemplazo seguro de marca visible**.

El objetivo es aplicar el primer cambio controlado de identidad visible para Maobits OS Android sin tocar todavía la identidad técnica profunda del proyecto.

Esta fase solo permite modificar:

- `rootProject.name`;
- `app_name`;
- label visible `Share BitChat`;
- evidencia y documentación de la fase.

No se deben modificar todavía `applicationId`, `namespace`, paquetes Kotlin, imports, permisos personalizados, authorities, deep links, clases de aplicación, temas ni lógica de conectividad.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Diagnóstico usado para esta fase

La auditoría limpia confirmó:

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

También confirmó elementos que deben esperar:

```text
com.bitchat.android.permission.FORCE_FINISH
Theme.BitchatAndroid
BitchatApplication
BitchatWatchApplication
bitchat://verify
com.bitchat.*
```

---

## 4. Regla de seguridad

No usar reemplazo masivo.

Prohibido en esta fase:

```bash
sed -i 's/bitchat/maobits/g'
```

Esta fase debe ser quirúrgica, auditable y reversible.

---

## 5. Rama recomendada

Si ya terminaste la rama `brand/1.1-inventory`, primero haz commit de la evidencia. Después crea la rama nueva:

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

Si decides continuar sobre la rama actual, documenta la decisión y no mezcles con otros cambios funcionales.

---

## 6. Copiar esta documentación al proyecto

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/03-brand

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-SAFE-VISIBLE-BRAND-REPLACEMENT-1.1.4.es.md docs/03-brand/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-SAFE-VISIBLE-BRAND-REPLACEMENT-1.1.4.en.md docs/03-brand/
```

---

## 7. Crear evidencia antes del cambio

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

## 8. Aplicar cambios seguros

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

## 9. Confirmar que no se tocaron áreas prohibidas

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

printf '\n=== EXPECTED SAFE CHANGES ===\n'
git diff -- settings.gradle.kts app/src/main/res wear/src/main/res app/src/main/AndroidManifest.xml

printf '\n=== MUST STILL EXIST FOR LATER PHASES ===\n'
git grep -n -I -E "namespace = \"com\.bitchat|applicationId = \"com\.bitchat|Theme\.BitchatAndroid|BitchatApplication|BitchatWatchApplication|com\.bitchat\.android\.permission\.FORCE_FINISH|android:scheme=\"bitchat\"" -- app wear settings.gradle.kts || true
```

---

## 10. Crear evidencia después del cambio

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

## 11. Validar build, tests y lint

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

## 12. Commit recomendado

Solo si todo termina con estado `0`:

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

## 13. Criterios de aceptación

La fase 1.1.4 queda completa cuando:

- `rootProject.name` usa `maobits-os-android`;
- `app_name` usa `Maobits OS`;
- `Share BitChat` cambió a `Share Maobits OS`;
- no se modificó `applicationId`;
- no se modificó `namespace`;
- no se modificaron paquetes Kotlin;
- no se modificaron imports;
- no se modificó conectividad;
- app build termina en `0`;
- wear build termina en `0`;
- tests terminan en `0`;
- lint termina en `0`;
- existe evidencia antes/después.

---

## 14. Próxima fase

```text
Fase 1.1.5 — Auditoría visual de iconos, launcher y recursos gráficos
```

Esa fase revisará iconos, drawables, launcher, adaptive icons, imágenes y recursos gráficos antes de reemplazarlos por identidad visual Maobits OS.

---

## 15. Declaración final

Este primer cambio visible inicia la identidad pública de Maobits OS Android sin comprometer todavía la arquitectura técnica interna.

**Persona → Compromiso → Confirmación**
