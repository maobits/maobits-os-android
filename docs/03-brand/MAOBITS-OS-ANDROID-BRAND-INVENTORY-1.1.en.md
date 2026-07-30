# Maobits OS Android — Brand, Visual Resources, and Visible Text Inventory 1.1

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1 — Brand, Visual Resources, and Visible Text Inventory**.

The purpose is to identify every place where the Android repository still contains inherited visual, textual, technical, or public identity from the technical reference source before changing names, logos, icons, packages, `applicationId`, `namespace`, custom permissions, or user-facing text.

Professional customization of Maobits OS Android must preserve traceability, connectivity, licenses, brand separation, and controlled change management.

---

## 2. Expected input state

Before starting this phase, the project must satisfy:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

The official repository should also be configured as:

```text
origin    → https://github.com/maobits/maobits-os-android.git
reference → https://github.com/maobits/bitchat-android.git
```

The official working branch should be:

```text
main
```

---

## 3. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 4. Main rule for this phase

This phase **only inventories and documents**.

Do not modify yet:

- `applicationId`;
- `namespace`;
- nombres de paquetes Kotlin;
- permisos Android;
- servicios, receivers o providers;
- lógica de BLE, Wi-Fi Aware, Nostr, cifrado, outbox, store-and-forward o foreground services;
- licencias;
- dependencias.

---

## 5. Prepare branch and evidence folder

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout main
git pull --ff-only origin main

git checkout -b brand/1.1-inventory

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"
mkdir -p "$BRAND_AUDIT_DIR"
```

---

## 6. Copy this documentation into the project

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/03-brand

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.es.md docs/03-brand/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.en.md docs/03-brand/
```

---

## 7. Visible text inventory

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

## 8. Visual resources inventory

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

## 9. Manifest labels, authorities, and custom permission inventory

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

## 10. Package and technical reference inventory

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

## 11. Gradle public identity inventory

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

## 12. Notification and foreground service inventory

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

## 13. External brand inventory in documentation and tooling

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

## 14. Automatic summary

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

## 15. Classification matrix

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

## 16. Recommended future replacement order

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

## 17. Acceptance criteria

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

## 18. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-BRAND-INVENTORY-1.1.en.md \
        docs/03-brand/evidence/2026-07-29-brand-inventory

git commit -m "docs(brand): add Maobits OS Android brand inventory"
```

---

## 19. Next phase

```text
Phase 1.2 — Legal, license, credits, and attribution matrix
```

Esa fase separará licencias originales, obligaciones por plataforma, créditos técnicos aislados, política de no uso comercial de marca externa, riesgos GPL y estrategia clean-room si aplica.

---

## 20. Final statement

La identidad Maobits OS Android debe construirse con precisión. Antes de reemplazar una marca o un recurso, se debe saber dónde vive, qué impacto tiene, si está protegido por licencia, si afecta al usuario y si puede romper la app.

**Person → Commitment → Confirmation**
