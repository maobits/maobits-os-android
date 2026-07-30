# Maobits OS Android — Inventario de marca, recursos visuales y textos visibles 1.1

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1 — Inventario de marca, recursos visuales y textos visibles**.

La finalidad es identificar todos los puntos donde el repositorio Android todavía contiene identidad visual, textual, técnica o pública heredada de la fuente técnica de referencia, antes de cambiar nombres, logos, iconos, paquetes, `applicationId`, `namespace`, permisos personalizados o textos de interfaz.

La personalización profesional de Maobits OS Android debe hacerse con trazabilidad, sin romper conectividad, sin ocultar licencias, sin mezclar marcas y sin improvisar cambios masivos.

---

## 2. Estado de entrada esperado

Antes de iniciar esta fase, el proyecto debe cumplir:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

Además, el repositorio oficial debe estar configurado así:

```text
origin    → https://github.com/maobits/maobits-os-android.git
reference → https://github.com/maobits/bitchat-android.git
```

La rama oficial de trabajo debe ser:

```text
main
```

---

## 3. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 4. Regla principal de esta fase

Esta fase **solo inventaría y documenta**.

No debe modificar todavía:

- `applicationId`;
- `namespace`;
- nombres de paquetes Kotlin;
- permisos Android;
- servicios, receivers o providers;
- lógica de BLE, Wi-Fi Aware, Nostr, cifrado, outbox, store-and-forward o foreground services;
- licencias;
- dependencias.

---

## 5. Preparar rama y carpeta de evidencia

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout main
git pull --ff-only origin main

git checkout -b brand/1.1-inventory

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"
mkdir -p "$BRAND_AUDIT_DIR"
```

---

## 6. Copiar esta documentación al proyecto

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/03-brand

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.es.md docs/03-brand/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.en.md docs/03-brand/
```

---

## 7. Inventario de textos visibles

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== STRING RESOURCES ==="
  find app wear -type f \
    \( -path "*/res/values/*.xml" -o -path "*/res/values-*/*.xml" \) \
    | sort
  echo
  echo "=== STRING CONTENT MATCHES ==="
  grep -RInE "bitchat|BitChat|Bitchat|chat|mesh|panic|noise|nostr|bluetooth|peer|channel|favorite|geohash|privacy|identity|message|notification" \
    app/src wear/src \
    --include="*.xml" \
    --include="*.kt" \
    --include="*.java" \
    --include="*.properties" \
    2>/dev/null || true
} > "$BRAND_AUDIT_DIR/VISIBLE-TEXT-AND-STRING-MATCHES.txt"
```

---

## 8. Inventario de recursos visuales

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== DRAWABLE RESOURCES ==="
  find app wear -type f -path "*/res/drawable*" | sort
  echo
  echo "=== MIPMAP RESOURCES ==="
  find app wear -type f -path "*/res/mipmap*" | sort
  echo
  echo "=== RAW RESOURCES ==="
  find app wear -type f -path "*/res/raw*" | sort
  echo
  echo "=== ASSETS ==="
  find app wear -type f -path "*/assets/*" | sort
} > "$BRAND_AUDIT_DIR/VISUAL-RESOURCES-INVENTORY.txt"
```

---

## 9. Inventario de Manifest, labels, authorities y permisos personalizados

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== MANIFEST LABELS AND COMPONENTS ==="
  grep -RInE "android:label|android:icon|android:roundIcon|android:theme|android:authorities|permission|provider|service|activity|receiver" \
    app/src/main/AndroidManifest.xml \
    app/src/debug/AndroidManifest.xml \
    wear/src/main/AndroidManifest.xml \
    wear/src/debug/AndroidManifest.xml \
    2>/dev/null || true
  echo
  echo "=== CUSTOM PERMISSION REFERENCES ==="
  grep -RInE "com\.bitchat|permission\.FORCE_FINISH|authorities|FileProvider" \
    app/src wear/src \
    --include="*.xml" \
    --include="*.kt" \
    --include="*.java" \
    2>/dev/null || true
} > "$BRAND_AUDIT_DIR/MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt"
```

---

## 10. Inventario de paquetes y referencias técnicas

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== PACKAGE DECLARATIONS ==="
  grep -RIn "^package " app/src wear/src \
    --include="*.kt" \
    --include="*.java" \
    2>/dev/null || true
  echo
  echo "=== IMPORT REFERENCES ==="
  grep -RIn "^import com\.bitchat" app/src wear/src \
    --include="*.kt" \
    --include="*.java" \
    2>/dev/null || true
  echo
  echo "=== FULL com.bitchat REFERENCES ==="
  grep -RIn "com\.bitchat" app wear \
    --include="*.kt" \
    --include="*.java" \
    --include="*.xml" \
    --include="*.kts" \
    --include="*.properties" \
    2>/dev/null || true
} > "$BRAND_AUDIT_DIR/PACKAGE-AND-CODE-REFERENCES.txt"
```

---

## 11. Inventario Gradle de identidad pública

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== GRADLE IDENTITY ==="
  grep -RInE "namespace|applicationId|versionCode|versionName|archivesName|rootProject.name|compileSdk|minSdk|targetSdk" \
    settings.gradle.kts \
    build.gradle.kts \
    gradle.properties \
    app/build.gradle.kts \
    wear/build.gradle.kts \
    2>/dev/null || true
  echo
  echo "=== PLUGINS ==="
  grep -RInE "plugins|id\(|alias\(" \
    settings.gradle.kts \
    build.gradle.kts \
    app/build.gradle.kts \
    wear/build.gradle.kts \
    2>/dev/null || true
} > "$BRAND_AUDIT_DIR/GRADLE-PUBLIC-IDENTITY.txt"
```

---

## 12. Inventario de notificaciones y foreground services

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== NOTIFICATION AND FOREGROUND SERVICE REFERENCES ==="
  grep -RInE "Notification|notification|Foreground|foreground|channel|Channel|service|Service|title|contentText|setContentTitle|setContentText" \
    app/src wear/src \
    --include="*.kt" \
    --include="*.java" \
    --include="*.xml" \
    2>/dev/null || true
} > "$BRAND_AUDIT_DIR/NOTIFICATION-AND-FOREGROUND-UX.txt"
```

---

## 13. Inventario de marca externa en documentación y tooling

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== DOCUMENTATION AND TOOLING BRAND REFERENCES ==="
  grep -RInE "bitchat|BitChat|Bitchat|permissionlesstech|callebtc|jack|Nostr|Noise|BLE|mesh" \
    README.md LICENSE.md tools docs gradle.properties settings.gradle.kts build.gradle.kts app/build.gradle.kts wear/build.gradle.kts \
    --include="*.md" \
    --include="*.txt" \
    --include="*.kts" \
    --include="*.properties" \
    2>/dev/null || true
} > "$BRAND_AUDIT_DIR/DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt"
```

---

## 14. Resumen automático

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

{
  echo "=== MAOBITS OS ANDROID - BRAND INVENTORY SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== REMOTES ==="
  git remote -v
  echo
  echo "=== EVIDENCE FILES ==="
  find "$BRAND_AUDIT_DIR" -type f | sort
  echo
  echo "=== MATCH COUNTS ==="
  for file in "$BRAND_AUDIT_DIR"/*.txt; do
    printf "%s: " "$(basename "$file")"
    grep -Eic "bitchat|BitChat|Bitchat|com\.bitchat|permissionlesstech|callebtc|jack" "$file" || true
  done
} > "$BRAND_AUDIT_DIR/BRAND-INVENTORY-SUMMARY.txt"

cat "$BRAND_AUDIT_DIR/BRAND-INVENTORY-SUMMARY.txt"
```

---

## 15. Matriz de clasificación

| Categoría | Descripción | Acción futura |
|---|---|---|
| Marca visible | Lo ve el usuario en pantalla | Reemplazar por Maobits OS |
| Identidad Android pública | `applicationId`, labels, icons, authorities | Migrar con pruebas |
| Identidad técnica interna | namespace, paquetes, imports | Migrar en fase controlada |
| Referencia legal | licencia, créditos, atribución | Conservar y separar |
| Referencia técnica | documentación de arquitectura base | Conservar como fuente técnica |
| Recurso visual externo | logos, iconos o imágenes heredadas | Reemplazar o validar licencia |
| Texto de sistema | notificaciones, permisos, foreground | Redactar con enfoque ético |
| Riesgo de privacidad | ubicación, audio, cámara, media | Requiere justificación y UX transparente |

---

## 16. Orden recomendado de reemplazo futuro

1. textos visibles;
2. recursos visuales;
3. nombre visible de aplicación;
4. descripción del repositorio;
5. documentación propia;
6. notificaciones;
7. permisos personalizados;
8. `applicationId`;
9. `namespace`;
10. paquetes Kotlin;
11. referencias internas profundas;
12. release signing;
13. distribución.

---

## 17. Criterios de aceptación

La fase 1.1 queda completa cuando:

- existe rama `brand/1.1-inventory`;
- se generó evidencia en `docs/03-brand/evidence/2026-07-29-brand-inventory`;
- se identificaron textos visibles;
- se identificaron recursos visuales;
- se identificaron labels del Manifest;
- se identificaron authorities y providers;
- se identificaron permisos personalizados con marca externa;
- se identificaron referencias Gradle de identidad pública;
- se identificaron referencias de paquetes;
- se identificaron referencias en documentación y tooling;
- se generó resumen automático;
- la documentación bilingüe fue copiada;
- no se modificó código funcional.

---

## 18. Commit recomendado

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.en.md \
        docs/03-brand/evidence/2026-07-29-brand-inventory

git commit -m "docs(brand): add Maobits OS Android brand inventory"
```

---

## 19. Próxima fase

```text
Fase 1.2 — Matriz legal, licencias, créditos y atribución
```

Esa fase separará licencias originales, obligaciones por plataforma, créditos técnicos aislados, política de no uso comercial de marca externa, riesgos GPL y estrategia clean-room si aplica.

---

## 20. Declaración final

La identidad Maobits OS Android debe construirse con precisión. Antes de reemplazar una marca o un recurso, se debe saber dónde vive, qué impacto tiene, si está protegido por licencia, si afecta al usuario y si puede romper la app.

**Persona → Compromiso → Confirmación**
