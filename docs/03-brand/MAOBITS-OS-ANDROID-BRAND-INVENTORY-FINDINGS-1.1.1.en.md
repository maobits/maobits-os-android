# Maobits OS Android — Brand Inventory Findings 1.1.1

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Evidence time:** 20:37:30-06:00  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document records the first findings from **Phase 1.1 — Brand, Visual Resources, and Visible Text Inventory**.

The evidence confirms that the repository contains a significant amount of inherited references from the technical reference source. This is expected because the project is still in the audit phase and functional customization has not started yet.

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

Observed commit:

```text
c51559a chore(repo): merge audited Maobits OS Android baseline into main
```

---

## 4. Count summary

```text
DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt: 30600
GRADLE-PUBLIC-IDENTITY.txt: 5
MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt: 8
NOTIFICATION-AND-FOREGROUND-UX.txt: 4102
PACKAGE-AND-CODE-REFERENCES.txt: 3539
VISIBLE-TEXT-AND-STRING-MATCHES.txt: 13405
VISUAL-RESOURCES-INVENTORY.txt: 0
```

---

## 5. General interpretation

| File | Count | Interpretation |
|---|---:|---|
| `DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt` | 30600 | Very high. Includes documentation, tooling, previous evidence, and technical references. It must be filtered to separate licenses, credits, own docs, and technical-source references. |
| `VISIBLE-TEXT-AND-STRING-MATCHES.txt` | 13405 | High. May include visible text, technical names, and many generic matches such as `chat`, `mesh`, `peer`, `message`. Requires priority filtering. |
| `NOTIFICATION-AND-FOREGROUND-UX.txt` | 4102 | High. Must be reviewed carefully because it affects visible UX, foreground services, and sensitive permissions. |
| `PACKAGE-AND-CODE-REFERENCES.txt` | 3539 | High but expected. Namespace and packages still use inherited technical identity. Do not change yet. |
| `MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt` | 8 | Low and high priority. Review first because it affects public identity, permissions, providers, and security. |
| `GRADLE-PUBLIC-IDENTITY.txt` | 5 | Low and critical. This is where `applicationId`, `namespace`, and versions are defined. |
| `VISUAL-RESOURCES-INVENTORY.txt` | 0 | No textual brand matches were found, but icons and images still require manual inspection. |

---

## 6. Technical decision

Do not replace everything in bulk.

A high match count does not mean every reference must be changed immediately. Many matches may be:

- legal references that must be preserved;
- historical documentation that must remain;
- technical packages that will be migrated later;
- valid functional terms such as `chat`, `mesh`, `peer`, `message`;
- audit evidence that should not be rewritten;
- protocol references that may remain technically valid.

Customization must be gradual, verifiable, and reversible.

---

## 7. Classification priority

Classification should advance in this order:

1. `GRADLE-PUBLIC-IDENTITY.txt`
2. `MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt`
3. `VISIBLE-TEXT-AND-STRING-MATCHES.txt`
4. `NOTIFICATION-AND-FOREGROUND-UX.txt`
5. `VISUAL-RESOURCES-INVENTORY.txt`
6. `DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt`
7. `PACKAGE-AND-CODE-REFERENCES.txt`

The reason is that public identity and user-visible experience must be understood before touching internal packages.

---

## 8. Immediate actions

The next activity must generate filtered review files:

```text
GRADLE-PUBLIC-IDENTITY-REVIEW.txt
MANIFEST-BRAND-REVIEW.txt
VISIBLE-TEXT-PRIORITY-REVIEW.txt
NOTIFICATION-UX-PRIORITY-REVIEW.txt
PACKAGE-MIGRATION-RISK-REVIEW.txt
BRAND-REPLACEMENT-CANDIDATES.txt
BRAND-PRESERVE-AS-ATTRIBUTION.txt
```

---

## 9. Safety rule

Do not run automatic replacements such as:

```bash
sed -i 's/bitchat/maobits/g'
```

That type of change could break:

- Kotlin packages;
- custom permissions;
- providers;
- imports;
- authorities;
- legal documentation;
- technical-source attribution;
- Gradle build;
- internal compatibility;
- connectivity.

---

## 10. Acceptance criteria for this subphase

Subphase 1.1.1 is complete when:

- inventory counts are recorded;
- reference magnitude is classified;
- review order is defined;
- mass replacement is avoided;
- filtered decision files are prepared;
- no functional code is modified.

---

## 11. Next subphase

```text
Phase 1.1.2 — Filtered classification of public identity and visible brand
```

That subphase will determine which references are replaced, which are preserved as attribution, and which must wait for technical package migration.

---

## 12. Final statement

Maobits OS Android must build its own identity without deleting technical memory or breaking the functional base.

**Person → Commitment → Confirmation**
