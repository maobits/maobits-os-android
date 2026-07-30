# Maobits OS Android — Filtered Visible Brand and Public Identity Classification 1.1.2

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Evidence time:** 21:42:39-05:00  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document records **Phase 1.1.2 — Filtered Public Identity and Visible Brand Classification**.

This phase takes the evidence generated during brand inventory 1.1 and organizes it into decision groups to avoid mass changes, preserve legal attribution, keep connectivity stable, and prepare the first safe customization of Maobits OS Android.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Audited branch

```text
brand/1.1-inventory
```

---

## 4. Received filtered summary

```text
GRADLE-PUBLIC-IDENTITY-REVIEW.txt: 5
MANIFEST-BRAND-REVIEW.txt: 8
VISIBLE-TEXT-PRIORITY-REVIEW.txt: 3992
NOTIFICATION-UX-PRIORITY-REVIEW.txt: 4048
PACKAGE-MIGRATION-RISK-REVIEW.txt: 1973
BRAND-REPLACEMENT-CANDIDATES.txt: 9681
BRAND-PRESERVE-AS-ATTRIBUTION.txt: 81042
```

---

## 5. Strategic interpretation

The counts confirm that the repository still has a deep inherited identity, but not every reference has the same risk type or replacement timing.

The project must separate four groups:

| Group | Description | Action |
|---|---|---|
| Android public identity | `applicationId`, `namespace`, labels, authorities, custom permissions | Review first, change in a controlled phase |
| User-visible brand | `app_name`, UI text, notifications, onboarding | First candidate for safe customization |
| Internal technical identity | packages, imports, classes, modules | Do not touch until technical migration phase |
| Legal attribution and traceability | README, LICENSE, docs, technical-source references | Preserve, separate, and document |

---

## 6. Main decision

Do not replace everything now.

The first safe customization should focus on:

1. visible application name;
2. direct visible text;
3. visible notifications;
4. Maobits OS own documentation;
5. visual icon and resource inventory.

The following must wait:

1. `applicationId`;
2. `namespace`;
3. Kotlin packages;
4. `com.bitchat` imports;
5. providers and authorities;
6. custom `FORCE_FINISH` permission;
7. connectivity changes.

---

## 7. Highest-priority files for manual inspection

Manual inspection must begin with:

```text
GRADLE-PUBLIC-IDENTITY-REVIEW.txt
MANIFEST-BRAND-REVIEW.txt
BRAND-REPLACEMENT-CANDIDATES.txt
```

Then continue with:

```text
VISIBLE-TEXT-PRIORITY-REVIEW.txt
NOTIFICATION-UX-PRIORITY-REVIEW.txt
PACKAGE-MIGRATION-RISK-REVIEW.txt
BRAND-PRESERVE-AS-ATTRIBUTION.txt
```

---

## 8. Preservation rules

Legal references, credits, licenses, history, audit evidence, and technical-source mentions must not be removed.

They must be preserved when they appear in:

- `LICENSE.md`;
- license files;
- credits;
- attribution documentation;
- audits;
- roadmap;
- documents that explain the technical source;
- fork traceability;
- compliance notes.

---

## 9. Future replacement rules

References may be replaced when they appear in:

- `app_name`;
- visible labels;
- screen text;
- visible notifications;
- onboarding;
- app description;
- user-facing permission text;
- own visual resources;
- Maobits OS institutional documentation.

---

## 10. Technical wait rules

References must wait when they belong to:

- Kotlin packages;
- imports;
- namespace;
- applicationId;
- authorities;
- custom permissions;
- foreground services;
- receivers;
- providers;
- BLE logic;
- Wi-Fi Aware logic;
- Nostr logic;
- encryption;
- keys;
- store-and-forward.

---

## 11. Recommended inspection commands

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

printf '\n=== GRADLE PUBLIC IDENTITY REVIEW ===\n'
cat "$BRAND_AUDIT_DIR/GRADLE-PUBLIC-IDENTITY-REVIEW.txt"

printf '\n=== MANIFEST BRAND REVIEW ===\n'
cat "$BRAND_AUDIT_DIR/MANIFEST-BRAND-REVIEW.txt"

printf '\n=== BRAND REPLACEMENT CANDIDATES SAMPLE ===\n'
head -220 "$BRAND_AUDIT_DIR/BRAND-REPLACEMENT-CANDIDATES.txt"

printf '\n=== VISIBLE TEXT PRIORITY SAMPLE ===\n'
head -220 "$BRAND_AUDIT_DIR/VISIBLE-TEXT-PRIORITY-REVIEW.txt"

printf '\n=== NOTIFICATION UX PRIORITY SAMPLE ===\n'
head -220 "$BRAND_AUDIT_DIR/NOTIFICATION-UX-PRIORITY-REVIEW.txt"
```

---

## 12. Commands to create file-level summaries

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

for file in \
  BRAND-REPLACEMENT-CANDIDATES.txt \
  VISIBLE-TEXT-PRIORITY-REVIEW.txt \
  NOTIFICATION-UX-PRIORITY-REVIEW.txt \
  PACKAGE-MIGRATION-RISK-REVIEW.txt \
  BRAND-PRESERVE-AS-ATTRIBUTION.txt
do
  echo "=== $file ==="
  awk -F: '/^[^:]+:[0-9]+:/ {count[$1]++} END {for (path in count) print count[path], path}' "$BRAND_AUDIT_DIR/$file" \
    | sort -nr \
    | head -40
  echo
done > "$BRAND_AUDIT_DIR/FILTERED-CLASSIFICATION-BY-FILE.txt"

cat "$BRAND_AUDIT_DIR/FILTERED-CLASSIFICATION-BY-FILE.txt"
```

---

## 13. Acceptance criteria for 1.1.2

Subphase 1.1.2 is complete when:

- the filtered summary has been generated;
- the magnitude of each group has been documented;
- replaceable, preservable, and pending references have been separated;
- Gradle and Manifest have been inspected;
- file-level summary has been generated;
- no functional code was modified;
- phase 1.1.3 safe visible-brand replacement plan is prepared.

---

## 14. Next phase

```text
Phase 1.1.3 — Safe visible-brand replacement plan
```

The next phase must define the first permitted change package:

- `app_name`;
- strictly necessary visible text;
- visible notifications;
- visual resources if clearly identified;
- no package, namespace, or applicationId changes.

---

## 15. Final statement

Maobits OS Android must create its own identity without deleting attribution, breaking connectivity, or hiding the audited technical origin.

**Person → Commitment → Confirmation**
