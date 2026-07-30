# Maobits OS Android — Auditoría visual de iconos, launcher y recursos gráficos 1.1.5

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1.5 — Auditoría visual de iconos, launcher y recursos gráficos**.

La fase anterior validó el primer reemplazo seguro de marca visible. Esta fase revisa los recursos gráficos antes de reemplazar iconos o identidad visual, para evitar romper compatibilidad con Android, Wear OS, adaptive icons, launcher icons, recursos `mipmap`, recursos `drawable`, previews y tamaños requeridos.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada esperado

Antes de iniciar esta fase, la fase 1.1.4 debe estar validada con:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

---

## 4. Regla principal de esta fase

Esta fase **solo audita e inventaría recursos visuales**.

No reemplazar todavía:

- `ic_launcher`;
- `ic_launcher_round`;
- adaptive icon foreground/background;
- drawables internos;
- imágenes de onboarding;
- recursos de Wear OS;
- colores o tema visual;
- assets de distribución.

---

## 5. Preparar rama

Si la fase 1.1.4 ya fue commiteada, crear rama nueva:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout main
git pull --ff-only origin main

git checkout -b brand/1.1.5-visual-assets-audit
```

Si sigues en `brand/1.1-inventory`, primero confirma el estado:

```bash
git status
git log --oneline --decorate -8
```

---

## 6. Copiar esta documentación al proyecto

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/03-brand

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.es.md docs/03-brand/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.en.md docs/03-brand/
```

---

## 7. Crear carpeta de evidencia

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"
mkdir -p "$VISUAL_AUDIT_DIR"
```

---

## 8. Inventario de recursos visuales versionados

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== TRACKED VISUAL RESOURCES ==="
  git ls-files \
    'app/src/**/res/drawable*/*' \
    'app/src/**/res/mipmap*/*' \
    'app/src/**/res/raw/*' \
    'app/src/**/assets/*' \
    'wear/src/**/res/drawable*/*' \
    'wear/src/**/res/mipmap*/*' \
    'wear/src/**/res/raw/*' \
    'wear/src/**/assets/*' \
    | sort
} > "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"

cat "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
```

---

## 9. Inventario específico de launcher icons

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== LAUNCHER AND ADAPTIVE ICON RESOURCES ==="
  git ls-files \
    'app/src/**/res/mipmap*/ic_launcher*' \
    'app/src/**/res/drawable*/ic_launcher*' \
    'wear/src/**/res/mipmap*/ic_launcher*' \
    'wear/src/**/res/drawable*/ic_launcher*' \
    | sort
  echo
  echo "=== MANIFEST ICON REFERENCES ==="
  git grep -n -I -E "android:icon|android:roundIcon|ic_launcher|ic_launcher_round" \
    -- app/src/main/AndroidManifest.xml wear/src/main/AndroidManifest.xml \
    || true
} > "$VISUAL_AUDIT_DIR/LAUNCHER-ICON-INVENTORY.txt"

cat "$VISUAL_AUDIT_DIR/LAUNCHER-ICON-INVENTORY.txt"
```

---

## 10. Hashes de recursos gráficos

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== VISUAL RESOURCE HASHES ==="
  while IFS= read -r file; do
    if [ -f "$file" ]; then
      sha256sum "$file"
    fi
  done < "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
} > "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-SHA256.txt"

head -120 "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-SHA256.txt"
```

---

## 11. Tipos de archivo y tamaños

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== VISUAL RESOURCE FILE TYPES ==="
  while IFS= read -r file; do
    if [ -f "$file" ]; then
      printf "%s | " "$file"
      file "$file"
    fi
  done < "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
} > "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-FILE-TYPES.txt"

head -160 "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-FILE-TYPES.txt"
```

---

## 12. Dimensiones de imágenes con Python

Este comando usa Python estándar y, si Pillow está disponible, extrae dimensiones. Si Pillow no está instalado, no falla la fase.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

python3 <<'PY' > "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-DIMENSIONS.txt"
from pathlib import Path

inventory = Path("docs/03-brand/evidence/2026-07-29-visual-assets-audit/TRACKED-VISUAL-RESOURCES.txt")
print("=== VISUAL RESOURCE DIMENSIONS ===")

try:
    from PIL import Image
except Exception as exc:
    print(f"Pillow not available: {exc}")
    raise SystemExit(0)

for line in inventory.read_text(encoding="utf-8").splitlines():
    path = Path(line.strip())
    if not path.is_file():
        continue
    if path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
        continue
    try:
        with Image.open(path) as img:
            print(f"{path} | {img.width}x{img.height} | {img.mode}")
    except Exception as exc:
        print(f"{path} | unreadable: {exc}")
PY

cat "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-DIMENSIONS.txt"
```

---

## 13. Colores, temas y referencias visuales XML

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== COLORS, THEMES, STYLES, ICON XML REFERENCES ==="
  git grep -n -I -E "color|Color|theme|Theme|style|Style|ic_launcher|drawable|mipmap|adaptive-icon|foreground|background" \
    -- app/src/main/res wear/src/main/res \
    || true
} > "$VISUAL_AUDIT_DIR/COLORS-THEMES-STYLES-VISUAL-REFERENCES.txt"

head -220 "$VISUAL_AUDIT_DIR/COLORS-THEMES-STYLES-VISUAL-REFERENCES.txt"
```

---

## 14. Resumen automático de auditoría visual

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

VISUAL_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-visual-assets-audit"

{
  echo "=== MAOBITS OS ANDROID - VISUAL ASSETS AUDIT SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== COUNTS ==="
  printf "Tracked visual resources: "
  wc -l < "$VISUAL_AUDIT_DIR/TRACKED-VISUAL-RESOURCES.txt"
  printf "Launcher/adaptive icon references: "
  grep -Eic "ic_launcher|android:icon|android:roundIcon|adaptive-icon" "$VISUAL_AUDIT_DIR/LAUNCHER-ICON-INVENTORY.txt" || true
  printf "Image dimensions lines: "
  grep -Eic "\| [0-9]+x[0-9]+ \|" "$VISUAL_AUDIT_DIR/VISUAL-RESOURCE-DIMENSIONS.txt" || true
  printf "Theme/color reference lines: "
  grep -Eic "color|theme|style|ic_launcher|drawable|mipmap|adaptive-icon" "$VISUAL_AUDIT_DIR/COLORS-THEMES-STYLES-VISUAL-REFERENCES.txt" || true
  echo
  echo "=== EVIDENCE FILES ==="
  find "$VISUAL_AUDIT_DIR" -type f | sort
} > "$VISUAL_AUDIT_DIR/VISUAL-ASSETS-AUDIT-SUMMARY.txt"

cat "$VISUAL_AUDIT_DIR/VISUAL-ASSETS-AUDIT-SUMMARY.txt"
```

---

## 15. Criterios de aceptación

La fase 1.1.5 queda completa cuando:

- existe inventario de recursos visuales versionados;
- existe inventario de launcher/adaptive icons;
- existen hashes SHA256 de recursos visuales;
- existen tipos de archivo;
- existen dimensiones cuando sea posible;
- existen referencias de colores, temas y estilos;
- existe resumen automático;
- no se reemplazaron iconos todavía;
- no se modificó código funcional;
- la documentación bilingüe fue copiada.

---

## 16. Commit recomendado

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-VISUAL-ASSETS-AUDIT-1.1.5.en.md \
        docs/03-brand/evidence/2026-07-29-visual-assets-audit

git commit -m "docs(brand): add visual assets audit"
```

---

## 17. Próxima fase

```text
Fase 1.1.6 — Diseño de iconografía Maobits OS Android
```

Esa fase definirá el reemplazo visual, paleta, launcher icon, adaptive icon, Wear icon y criterios de accesibilidad visual.

---

## 18. Declaración final

La identidad visual debe cambiarse con la misma disciplina que el código: primero inventario, luego diseño, después reemplazo controlado y finalmente validación.

**Persona → Compromiso → Confirmación**
