# Maobits OS Android — Conversión técnica de assets a recursos Android 1.1.8

**Versión:** 0.1.0  
**Fecha:** 2026-07-30  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1.8 — Conversión técnica de assets a recursos Android/Wear**.

La fase toma el ícono aprobado en 1.1.7 y lo convierte en recursos candidatos para Android y Wear OS, pero todavía **no reemplaza directamente** los recursos activos del proyecto.

La intención es evitar cambios a ciegas:

```text
diseño aprobado → conversión técnica candidata → revisión → reemplazo controlado → build/lint/test → prueba real
```

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada obligatorio

Antes de iniciar:

```text
1.1.4 — Marca visible Maobits OS validada.
1.1.5 — Auditoría visual generada.
1.1.6 — Diseño de iconografía documentado.
1.1.7 — Ícono aprobado empaquetado como asset controlado.
Prueba real en dos smartphones físicos aprobada.
```

---

## 4. Regla estricta de esta fase

Esta fase genera recursos candidatos en:

```text
docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/
```

No modifica todavía:

```text
app/src/main/res/
wear/src/main/res/
AndroidManifest.xml
ic_launcher activo
ic_launcher_round activo
adaptive icon activo
```

---

## 5. Recursos candidatos incluidos

El paquete genera:

```text
app/src/main/res/mipmap-mdpi/ic_launcher.png          48x48
app/src/main/res/mipmap-hdpi/ic_launcher.png          72x72
app/src/main/res/mipmap-xhdpi/ic_launcher.png         96x96
app/src/main/res/mipmap-xxhdpi/ic_launcher.png        144x144
app/src/main/res/mipmap-xxxhdpi/ic_launcher.png       192x192

app/src/main/res/mipmap-mdpi/ic_launcher_round.png    48x48
app/src/main/res/mipmap-hdpi/ic_launcher_round.png    72x72
app/src/main/res/mipmap-xhdpi/ic_launcher_round.png   96x96
app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png  144x144
app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png 192x192

wear/src/main/res/mipmap-* equivalentes
preview/maobits-os-icon-preview-*.png
SHA256SUMS.txt
```

---

## 6. Copiar documentación, herramienta y recursos candidatos

Descarga el ZIP en `/home/maobits/Descargas` y ejecuta:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_ICON_CONVERSION_DIR="/tmp/maobits-os-icon-conversion-1.1.8"
rm -rf "$TMP_ICON_CONVERSION_DIR"
mkdir -p "$TMP_ICON_CONVERSION_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-technical-icon-conversion-1-1-8.zip -d "$TMP_ICON_CONVERSION_DIR"

mkdir -p docs/03-brand
mkdir -p docs/03-brand/generated
mkdir -p tools/brand

cp "$TMP_ICON_CONVERSION_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.es.md" docs/03-brand/
cp "$TMP_ICON_CONVERSION_DIR/docs/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.en.md" docs/03-brand/

cp "$TMP_ICON_CONVERSION_DIR/tools/brand/maobits_os_generate_icon_resources_1_1_8.py" tools/brand/

cp -a "$TMP_ICON_CONVERSION_DIR/generated/2026-07-30-maobits-os-icon-android-candidate" \
  docs/03-brand/generated/
```

---

## 7. Regenerar recursos candidatos de forma reproducible

Si quieres regenerar desde el asset aprobado que ya está en el repo:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

python3 tools/brand/maobits_os_generate_icon_resources_1_1_8.py \
  --source docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png \
  --output docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate
```

---

## 8. Crear evidencia de conversión

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_CONVERSION_DIR="docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate"
ICON_CONVERSION_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-technical-icon-conversion"
mkdir -p "$ICON_CONVERSION_EVIDENCE_DIR"

{
  echo "=== MAOBITS OS ANDROID - TECHNICAL ICON CONVERSION 1.1.8 ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== GENERATED CANDIDATE FILES ==="
  find "$ICON_CONVERSION_DIR" -type f | sort
  echo
  echo "=== STATUS ==="
  echo "Candidate Android/Wear resources generated under docs only."
  echo "Active Android resources were not replaced in this phase."
} > "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-SUMMARY.txt"

sha256sum $(find "$ICON_CONVERSION_DIR" -type f | sort) \
  > "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-SHA256.txt" || true

file $(find "$ICON_CONVERSION_DIR" -type f | sort) \
  > "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-FILE-TYPES.txt" || true

cat "$ICON_CONVERSION_EVIDENCE_DIR/TECHNICAL-ICON-CONVERSION-SUMMARY.txt"
```

---

## 9. Revisión visual de tamaños

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

xdg-open docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/preview/maobits-os-icon-preview-1024.png
xdg-open docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/preview/maobits-os-icon-preview-128.png
xdg-open docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate/preview/maobits-os-icon-preview-48.png
```

Checklist:

```text
[ ] 1024px se ve correcto.
[ ] 128px mantiene lectura clara.
[ ] 48px todavía permite identificar la M y el nodo central.
[ ] No se ve superpuesto.
[ ] Los nodos no se pierden por tamaño.
[ ] Fondo oscuro funciona.
[ ] Aprobado para reemplazo controlado en la fase 1.1.9.
```

---

## 10. Commit recomendado

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-TECHNICAL-ICON-CONVERSION-1.1.8.en.md \
        docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate \
        docs/03-brand/evidence/2026-07-30-technical-icon-conversion \
        tools/brand/maobits_os_generate_icon_resources_1_1_8.py

git commit -m "brand(icons): generate Maobits OS Android icon candidates"
```

---

## 11. Próxima fase

```text
Fase 1.1.9 — Reemplazo controlado de launcher icons
```

Esa fase aplicará los candidatos a `app/src/main/res` y `wear/src/main/res` con respaldo previo, build, lint, prueba en dispositivo real y rollback.

---

## 12. Declaración final

La fase 1.1.8 convierte el diseño aprobado en recursos técnicos candidatos sin tocar aún los recursos activos. Esto conserva la trazabilidad y evita cambios visuales a ciegas.

**Persona → Compromiso → Confirmación**
