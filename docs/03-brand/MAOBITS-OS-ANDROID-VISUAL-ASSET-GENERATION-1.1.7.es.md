# Maobits OS Android — Generación controlada de assets visuales 1.1.7

**Versión:** 0.2.0  
**Fecha:** 2026-07-30  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define nuevamente la **Fase 1.1.7 — Generación controlada de assets visuales Maobits OS**, usando la versión visual aprobada por revisión manual.

La fase conserva la propuesta visual aprobada en el repositorio, genera tamaños de revisión y crea evidencia, pero **todavía no reemplaza los recursos Android activos**.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada

Antes de esta fase ya existen:

```text
1.1.4 — Marca visible Maobits OS validada.
1.1.5 — Auditoría visual de recursos generada.
1.1.6 — Especificación de iconografía documentada.
Prueba real en dos smartphones físicos aprobada.
```

---

## 4. Decisión visual

La versión aprobada del ícono mantiene:

```text
- fondo oscuro corporativo;
- monograma M claro;
- nodo central;
- tres nodos de red;
- conectores limpios;
- anillo de red sutil;
- separación visual suficiente;
- lectura clara en tamaño de app icon.
```

---

## 5. Regla estricta de esta fase

Los assets se guardan únicamente como propuesta en:

```text
docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/
```

No modificar todavía:

```text
app/src/main/res/mipmap*
app/src/main/res/drawable*
wear/src/main/res/mipmap*
wear/src/main/res/drawable*
AndroidManifest.xml
ic_launcher
ic_launcher_round
adaptive icon foreground/background
```

---

## 6. Assets incluidos

```text
maobits-os-icon-proposal-approved-original.png
maobits-os-icon-proposal-approved-1024.png
maobits-os-icon-proposal-approved-512.png
maobits-os-icon-proposal-approved-256.png
maobits-os-icon-proposal-approved-128.png
maobits-os-icon-approved-colors.json
SHA256SUMS.txt
README.md
```

---

## 7. Copiar documentación y assets al proyecto

Descarga el ZIP en `/home/maobits/Descargas` y ejecuta:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

TMP_ASSET_DIR="/tmp/maobits-os-visual-assets-1.1.7-approved"
rm -rf "$TMP_ASSET_DIR"
mkdir -p "$TMP_ASSET_DIR"

unzip -o /home/maobits/Descargas/maobits-os-android-visual-asset-generation-1-1-7-final-approved.zip -d "$TMP_ASSET_DIR"

mkdir -p docs/03-brand
mkdir -p docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved

cp "$TMP_ASSET_DIR/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.es.md" docs/03-brand/
cp "$TMP_ASSET_DIR/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.en.md" docs/03-brand/

cp -a "$TMP_ASSET_DIR/assets/2026-07-30-maobits-os-icon-proposal-approved/." \
  docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/
```

---

## 8. Crear evidencia

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_ASSET_DIR="docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved"
VISUAL_ASSET_EVIDENCE_DIR="docs/03-brand/evidence/2026-07-30-visual-asset-generation-approved"
mkdir -p "$VISUAL_ASSET_EVIDENCE_DIR"

{
  echo "=== MAOBITS OS ANDROID - CONTROLLED VISUAL ASSET GENERATION APPROVED ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== APPROVED PROPOSAL FILES ==="
  find "$VISUAL_ASSET_DIR" -type f | sort
  echo
  echo "=== STATUS ==="
  echo "Approved proposal assets only. Android active resources were not replaced."
} > "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-GENERATION-APPROVED-SUMMARY.txt"

sha256sum "$VISUAL_ASSET_DIR"/* > "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-APPROVED-SHA256.txt" || true
file "$VISUAL_ASSET_DIR"/* > "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-APPROVED-FILE-TYPES.txt" || true

cat "$VISUAL_ASSET_EVIDENCE_DIR/VISUAL-ASSET-GENERATION-APPROVED-SUMMARY.txt"
```

---

## 9. Revisión manual

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

xdg-open docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png
```

Checklist:

```text
[ ] Identidad Maobits OS clara.
[ ] No parece copia de marca externa.
[ ] No usa texto pequeño.
[ ] Se entiende en tamaño pequeño.
[ ] El monograma M no se ve superpuesto.
[ ] La red Persona → Compromiso → Confirmación se entiende.
[ ] Aprobado para conversión técnica Android.
```

---

## 10. Commit recomendado

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSET-GENERATION-1.1.7.en.md \
        docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved \
        docs/03-brand/evidence/2026-07-30-visual-asset-generation-approved

git commit -m "brand(assets): add approved Maobits OS icon proposal"
```

---

## 11. Próxima fase

```text
Fase 1.1.8 — Conversión técnica de assets a recursos Android
```

Esa fase convertirá el asset aprobado a recursos Android/Wear con validación, sin cambios a ciegas.

---

## 12. Declaración final

La versión visual aprobada queda conservada como asset de propuesta controlado. La implementación técnica en `ic_launcher`, adaptive icons y recursos Wear debe hacerse únicamente en la siguiente fase.

**Persona → Compromiso → Confirmación**
