# Maobits OS Android — Inventario limpio de marca y plan de reemplazo seguro 1.1.3

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1.3 — Inventario limpio de marca y plan de reemplazo seguro**.

La fase anterior generó un inventario amplio, pero los conteos incluyeron archivos generados por compilación, resultados de lint, evidencia documental y carpetas `build`. Para tomar decisiones correctas, esta fase genera una segunda evidencia limpia basada en archivos versionados y fuentes reales del proyecto.

El objetivo es evitar decisiones equivocadas causadas por archivos generados.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Diagnóstico de la evidencia anterior

La salida anterior mostró archivos como:

```text
app/build/intermediates/...
app/build/reports/...
wear/build/intermediates/...
wear/build/reports/...
docs/03-brand/evidence/...
docs/05-audit/evidence/...
```

Estos archivos sirven como evidencia técnica, pero no deben orientar directamente el reemplazo de marca visible.

---

## 4. Decisión metodológica

Desde esta subfase se separan dos tipos de evidencia:

| Tipo | Carpeta | Uso |
|---|---|---|
| Evidencia bruta | `docs/03-brand/evidence/2026-07-29-brand-inventory` | Conserva todo lo detectado inicialmente |
| Evidencia limpia | `docs/03-brand/evidence/2026-07-29-brand-inventory-clean-tracked-files` | Se usa para decidir cambios reales |

La evidencia limpia debe generarse con `git grep` y `git ls-files`, porque estos comandos trabajan sobre archivos versionados y evitan ruido de carpetas generadas.

---

## 5. Regla de seguridad

No se debe ejecutar ningún reemplazo masivo.

No usar:

```bash
sed -i 's/bitchat/maobits/g'
```

No tocar todavía:

- `applicationId`;
- `namespace`;
- paquetes Kotlin;
- imports `com.bitchat`;
- permisos personalizados;
- authorities;
- services;
- providers;
- receivers;
- lógica de conectividad;
- cifrado;
- store-and-forward.

---

## 6. Crear evidencia limpia

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

## 7. Gradle e identidad pública limpia

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

## 8. Manifest limpio

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

## 9. Textos visibles limpios

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

## 10. Notificaciones y servicios foreground limpios

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

## 11. Riesgo de migración de paquetes limpio

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

## 12. Atribución que debe conservarse

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

## 13. Resumen limpio

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

## 14. Inspección manual mínima

Después del resumen limpio, inspeccionar:

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

## 15. Primer cambio seguro recomendado

El primer cambio seguro debe limitarse a:

```text
rootProject.name
app_name
Share BitChat
textos visibles estrictamente confirmados
```

No debe tocar:

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

## 16. Criterio de aceptación

La subfase 1.1.3 queda completa cuando:

- se genera evidencia limpia;
- se separa evidencia bruta de evidencia útil para cambios;
- se confirma ubicación de `app_name`;
- se confirma ubicación de labels visibles;
- se documenta qué puede cambiar y qué debe esperar;
- no se modifica código funcional;
- el proyecto queda listo para la fase 1.1.4.

---

## 17. Próxima fase

```text
Fase 1.1.4 — Primer reemplazo seguro de marca visible
```

Esa fase aplicará cambios controlados únicamente sobre nombre visible, textos visibles mínimos y documentación propia, con build, test y lint después.

---

## 18. Declaración final

Maobits OS Android debe personalizarse con precisión quirúrgica: primero lo visible y seguro, luego lo público técnico, y por último la identidad interna profunda.

**Persona → Compromiso → Confirmación**
