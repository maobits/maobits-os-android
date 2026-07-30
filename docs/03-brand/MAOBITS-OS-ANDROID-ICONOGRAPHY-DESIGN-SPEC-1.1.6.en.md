# Maobits OS Android — Iconography Design Specification 1.1.6

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.1.6 — Maobits OS Android Iconography Design**.

The previous phase audited the project's visual resources. This phase does not replace files yet; it defines the visual identity that will later be implemented in launcher icons, adaptive icons, round icons, Wear OS resources, base colors, and visual documentation.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Expected input state

Before starting this phase, evidence must exist for:

```text
Phase 1.1.4 — First safe visible-brand replacement validated
Phase 1.1.5 — Visual audit of icons and graphic resources generated
```

The visual audit reported:

```text
Tracked visual resources: 83
Launcher/adaptive icon references: 29
Image dimensions lines: 15
Theme/color reference lines: 113
```

---

## 4. Main rule for this phase

This phase **designs and specifies**.

Do not replace yet:

- `ic_launcher`;
- `ic_launcher_round`;
- adaptive icon foreground/background;
- images;
- drawables;
- themes;
- global colors;
- Wear OS resources.

---

## 5. Base visual concept

Maobits OS Android must communicate:

```text
person
trust
private communication
resilient connectivity
verifiable commitment
confirmation
living network
ethical security
institutional clarity
```

The visual symbol should avoid looking like a generic chat app. It should suggest a trusted human network, not just messages.

---

## 6. Recommended visual direction

### 6.1 Main symbol

Concept proposal:

```text
A central human or identity node connected to three external nodes representing:
1. Person
2. Commitment
3. Confirmation
```

It can also be represented as:

```text
M + node network
M + subtle shield
M + distributed signal
M + circular confirmation
```

### 6.2 Avoid

Do not use:

- a traditional chat bubble as the only symbol;
- an aggressive lock as the main symbol;
- military iconography;
- hacker aesthetics;
- alert colors as the main identity;
- elements that imitate external brands;
- copied inherited icons.

---

## 7. Proposed visual palette

Initial institutional palette:

| Role | Suggested color | Use |
|---|---|---|
| Primary deep | `#1F2F2F` | Background, serious identity, dark mode |
| Trust green | `#2E7D6F` | Primary action, connection, security |
| Technology mint | `#62C6A7` | Active states, accents, living signal |
| Warm white | `#F7F7F2` | Contrast, light backgrounds |
| Technical gray | `#AEB7B3` | Secondary text, borders |
| Confirmation amber | `#F2B84B` | Confirmation, verified state, moderate attention |

This palette must later be validated for contrast and visual accessibility.

---

## 8. Visual typography

No custom font is defined yet.

The first stage should use Android system typography for:

- stability;
- performance;
- compatibility;
- smaller APK size;
- lower legal risk;
- native integration.

---

## 9. Launcher icon requirements

Iconography must be prepared in layers:

```text
adaptive icon background
adaptive icon foreground
launcher icon legacy
round icon
monochrome icon if required later
Wear OS icon
```

Files must not be replaced until all required formats are ready.

---

## 10. Adaptive icon design criteria

The design must satisfy:

- centered symbol;
- enough visual margin;
- readability at small sizes;
- clear shape when clipped by system masks;
- good contrast in light and dark mode;
- no small text inside the icon;
- no excessive detail;
- no dependency on complex gradients;
- Android and Wear OS compatibility.

---

## 11. Proposed resource names for future implementation

The implementation phase may use these names:

```text
app/src/main/res/drawable/ic_maobits_os_foreground.xml
app/src/main/res/drawable/ic_maobits_os_background.xml
app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml
app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml
wear/src/main/res/drawable/ic_maobits_os_wear_foreground.xml
wear/src/main/res/drawable/ic_maobits_os_wear_background.xml
```

If `ic_launcher` names already exist, they may remain as Android entry points while internally referencing Maobits OS resources.

---

## 12. Design evidence

Create folder:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

ICON_DESIGN_DIR="docs/03-brand/evidence/2026-07-29-iconography-design"
mkdir -p "$ICON_DESIGN_DIR"
```

Create decision document:

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

## 13. Create target resource manifest

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

## 14. Create palette specification

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

## 15. Automatic summary

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

## 16. Acceptance criteria

Phase 1.1.6 is complete when:

- a visual decision exists;
- a target resource manifest exists;
- an initial palette exists;
- an automatic summary exists;
- Android resources were not replaced;
- themes were not modified;
- code colors were not modified;
- functionality was not modified;
- bilingual documentation was copied;
- the next phase can generate visual assets.

---

## 17. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-ICONOGRAPHY-DESIGN-SPEC-1.1.6.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-ICONOGRAPHY-DESIGN-SPEC-1.1.6.en.md \
        docs/03-brand/evidence/2026-07-29-iconography-design

git commit -m "docs(brand): define Maobits OS iconography design"
```

---

## 18. Next phase

```text
Phase 1.1.7 — Controlled generation of Maobits OS visual assets
```

That phase may generate or import proprietary visual resources and prepare technical replacement with validation.

---

## 19. Final statement

Maobits OS Android visual identity must be proprietary, sober, technical, and human. The icon must represent a trusted network, verifiable commitment, and private communication without depending on external brands.

**Person → Commitment → Confirmation**
