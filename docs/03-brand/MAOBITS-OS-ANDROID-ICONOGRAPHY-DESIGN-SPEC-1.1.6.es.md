# Maobits OS Android — Especificación de diseño de iconografía 1.1.6

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.1.6 — Diseño de iconografía Maobits OS Android**.

La fase anterior auditó los recursos visuales del proyecto. Esta fase no reemplaza todavía archivos; define la identidad visual que será implementada después en launcher icons, adaptive icons, round icons, recursos Wear OS, colores base y documentación visual.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada esperado

Antes de iniciar esta fase debe existir evidencia de:

```text
Fase 1.1.4 — Primer reemplazo seguro de marca visible validado
Fase 1.1.5 — Auditoría visual de iconos y recursos gráficos generada
```

La auditoría visual reportó:

```text
Tracked visual resources: 83
Launcher/adaptive icon references: 29
Image dimensions lines: 15
Theme/color reference lines: 113
```

---

## 4. Regla principal de esta fase

Esta fase **diseña y especifica**.

No reemplazar todavía:

- `ic_launcher`;
- `ic_launcher_round`;
- adaptive icon foreground/background;
- imágenes;
- drawables;
- temas;
- colores globales;
- recursos Wear OS.

---

## 5. Concepto visual base

Maobits OS Android debe transmitir:

```text
persona
confianza
comunicación privada
conectividad resiliente
compromiso verificable
confirmación
red viva
seguridad ética
claridad institucional
```

El símbolo visual debe evitar parecer una app de chat genérica. Debe sugerir una red humana confiable, no solo mensajes.

---

## 6. Dirección visual recomendada

### 6.1 Símbolo principal

Propuesta conceptual:

```text
Un nodo central humano o punto de identidad, conectado a tres nodos externos que representan:
1. Persona
2. Compromiso
3. Confirmación
```

También puede representarse como:

```text
M + red de nodos
M + escudo sutil
M + señal distribuida
M + confirmación circular
```

### 6.2 Evitar

No usar:

- burbuja de chat tradicional como único símbolo;
- candado agresivo como símbolo principal;
- iconografía militar;
- estética hacker;
- colores de alerta como identidad principal;
- elementos que imiten marcas externas;
- copia de iconos heredados.

---

## 7. Paleta visual propuesta

Paleta institucional inicial:

| Rol | Color sugerido | Uso |
|---|---|---|
| Primario profundo | `#1F2F2F` | Fondo, identidad seria, modo oscuro |
| Verde confianza | `#2E7D6F` | Acción principal, conexión, seguridad |
| Verde claro tecnológico | `#62C6A7` | Estados activos, acentos, señal viva |
| Blanco cálido | `#F7F7F2` | Contraste, fondos claros |
| Gris técnico | `#AEB7B3` | Texto secundario, bordes |
| Ámbar confirmación | `#F2B84B` | Confirmación, estado verificado, atención moderada |

Esta paleta debe validarse posteriormente con contraste y accesibilidad visual.

---

## 8. Tipografía visual

No se define una fuente personalizada todavía.

La primera etapa debe usar tipografía del sistema Android para:

- estabilidad;
- rendimiento;
- compatibilidad;
- menor tamaño de APK;
- menor riesgo legal;
- integración nativa.

---

## 9. Requisitos para launcher icon

La iconografía debe prepararse en capas:

```text
adaptive icon background
adaptive icon foreground
launcher icon legacy
round icon
monochrome icon si el proyecto lo requiere después
Wear OS icon
```

No se deben reemplazar archivos hasta que estén listos todos los formatos requeridos.

---

## 10. Criterios de diseño para adaptive icon

El diseño debe cumplir:

- símbolo centrado;
- margen visual suficiente;
- legibilidad en tamaños pequeños;
- forma clara al recortarse por máscaras del sistema;
- buen contraste en modo claro y oscuro;
- sin texto pequeño dentro del icono;
- sin detalles excesivos;
- sin dependencia de gradientes complejos;
- compatible con Android y Wear OS.

---

## 11. Nombres de recursos propuestos para futura implementación

La fase de implementación puede usar estos nombres:

```text
app/src/main/res/drawable/ic_maobits_os_foreground.xml
app/src/main/res/drawable/ic_maobits_os_background.xml
app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml
app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml
wear/src/main/res/drawable/ic_maobits_os_wear_foreground.xml
wear/src/main/res/drawable/ic_maobits_os_wear_background.xml
```

Si ya existen nombres `ic_launcher`, se pueden mantener como punto de entrada Android, pero cambiando internamente sus referencias a recursos Maobits OS.

---

## 12. Evidencia de diseño

Crear carpeta:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_DESIGN_DIR="docs/03-brand/evidence/2026-07-29-iconography-design"
mkdir -p "$ICON_DESIGN_DIR"
```

Crear documento de decisión:

```bash
cat > "$ICON_DESIGN_DIR/ICONOGRAPHY-DESIGN-DECISION.txt" <<'EOF'
=== MAOBITS OS ANDROID - ICONOGRAPHY DESIGN DECISION ===

Decision:
Design a proprietary Maobits OS iconography system before replacing Android resources.

Core concept:
Person → Commitment → Confirmation represented as a trusted human-centered network.

Visual direction:
- central identity node
- three connected commitment/confirmation nodes
- institutional technology aesthetic
- ethical privacy
- resilient connectivity

Do not use:
- external project logos
- inherited icons without review
- generic chat bubble as the only symbol
- aggressive lock/hacker/military aesthetics

Implementation status:
Design only. No icon files replaced in this phase.
EOF
```

---

## 13. Crear manifiesto de recursos objetivo

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_DESIGN_DIR="docs/03-brand/evidence/2026-07-29-iconography-design"

cat > "$ICON_DESIGN_DIR/TARGET-VISUAL-RESOURCE-MANIFEST.txt" <<'EOF'
=== TARGET VISUAL RESOURCE MANIFEST ===

Android app:
- adaptive icon background
- adaptive icon foreground
- launcher icon
- round launcher icon
- optional monochrome icon
- preview/splash resources if applicable

Wear OS:
- wearable launcher icon
- wearable round icon
- small notification-safe icon if required

Design validation:
- light background
- dark background
- circular mask
- rounded-square mask
- small size visibility
- notification visibility
- accessibility contrast review
EOF
```

---

## 14. Crear especificación de paleta

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_DESIGN_DIR="docs/03-brand/evidence/2026-07-29-iconography-design"

cat > "$ICON_DESIGN_DIR/MAOBITS-OS-COLOR-PALETTE.txt" <<'EOF'
=== MAOBITS OS ANDROID - INITIAL COLOR PALETTE ===

Primary deep:
#1F2F2F

Trust green:
#2E7D6F

Technology mint:
#62C6A7

Warm white:
#F7F7F2

Technical gray:
#AEB7B3

Confirmation amber:
#F2B84B

Status:
Design proposal only. Not applied to Android resources yet.
EOF
```

---

## 15. Resumen automático

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_DESIGN_DIR="docs/03-brand/evidence/2026-07-29-iconography-design"

{
  echo "=== MAOBITS OS ANDROID - ICONOGRAPHY DESIGN SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== CURRENT COMMIT ==="
  git log --oneline --decorate -1
  echo
  echo "=== DESIGN FILES ==="
  find "$ICON_DESIGN_DIR" -type f | sort
  echo
  echo "=== DESIGN STATUS ==="
  echo "No Android resource files were replaced in this phase."
  echo "Next phase will generate or import icon assets after approval."
} > "$ICON_DESIGN_DIR/ICONOGRAPHY-DESIGN-SUMMARY.txt"

cat "$ICON_DESIGN_DIR/ICONOGRAPHY-DESIGN-SUMMARY.txt"
```

---

## 16. Criterios de aceptación

La fase 1.1.6 queda completa cuando:

- existe una decisión visual documentada;
- existe manifiesto de recursos objetivo;
- existe paleta inicial;
- existe resumen automático;
- no se reemplazaron recursos Android;
- no se modificaron temas;
- no se modificaron colores del código;
- no se modificó funcionalidad;
- la documentación bilingüe fue copiada;
- la siguiente fase puede generar assets visuales.

---

## 17. Commit recomendado

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-ICONOGRAPHY-DESIGN-SPEC-1.1.6.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-ICONOGRAPHY-DESIGN-SPEC-1.1.6.en.md \
        docs/03-brand/evidence/2026-07-29-iconography-design

git commit -m "docs(brand): define Maobits OS iconography design"
```

---

## 18. Próxima fase

```text
Fase 1.1.7 — Generación controlada de assets visuales Maobits OS
```

Esa fase puede generar o importar recursos visuales propios y preparar reemplazo técnico con validación.

---

## 19. Declaración final

La identidad visual de Maobits OS Android debe ser propia, sobria, técnica y humana. El icono debe representar red confiable, compromiso verificable y comunicación privada sin depender de marcas externas.

**Persona → Compromiso → Confirmación**
