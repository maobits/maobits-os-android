# Maobits OS Android — Initial Repository Audit

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document records the initial audit of the Android repository used as the starting point for building **Maobits OS Android**.

The goal of this audit is to understand the real codebase before modifying it, separate the Maobits OS brand from the external technical source, identify risks, recognize licenses, map critical modules, and prepare a professional customization path from 0%.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Technical reference repository

```text
https://github.com/maobits/bitchat-android
```

This repository is used as the technical starting point and must keep clear traceability. The main product brand will be **Maobits OS Android**.

The external technical source must only be mentioned in credits, licenses, origin audit, technical traceability, and base architecture analysis.

---

## 4. Initial audit commands

Run from the official workspace:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

pwd
git status
git remote -v
git branch --show-current
git log --oneline --decorate -10

find . -maxdepth 3 -type f | sort | sed 's#^./##' > AUDIT-FILES-MAXDEPTH-3.txt

find . -maxdepth 3 -type d | sort | sed 's#^./##' > AUDIT-DIRECTORIES-MAXDEPTH-3.txt

find . -maxdepth 4 \
  -type f \
  \( -name "*.gradle" -o -name "*.gradle.kts" -o -name "settings.gradle" -o -name "settings.gradle.kts" -o -name "gradle.properties" -o -name "AndroidManifest.xml" \) \
  | sort > AUDIT-ANDROID-STRUCTURE.txt

find . -maxdepth 5 \
  -type f \
  \( -name "*.kt" -o -name "*.java" \) \
  | sort > AUDIT-SOURCE-FILES.txt

find . -maxdepth 5 \
  -type f \
  \( -iname "*license*" -o -iname "*copying*" -o -iname "*notice*" -o -iname "README*" \) \
  | sort > AUDIT-LEGAL-README-FILES.txt
```

---

## 5. Minimum information to capture

| Area | Required information | Status |
|---|---|---|
| Git | Current branch, remotes, latest commit, clean status | Pending |
| Gradle | Version, modules, plugins, main configuration | Pending |
| Android | namespace, applicationId, minSdk, targetSdk | Pending |
| Manifest | permissions, services, receivers, activities | Pending |
| Kotlin/Java code | packages, services, ViewModels, repositories, transports | Pending |
| Communication | BLE, Wi-Fi Aware, Nostr, router, relay, store-and-forward | Pending |
| Security | keys, encryption, storage, wipe, sensitive permissions | Pending |
| Persistence | preferences, files, local database, cache, outbox | Pending |
| UI | screens, navigation, theme, branding, string resources | Pending |
| Legal | licenses, notices, README, dependencies | Pending |
| Risks | coupling, external branding, GPL, privacy, abuse | Pending |

---

## 6. Acceptance criteria

The initial audit is complete when:

- Git status has been reviewed;
- remotes and active branch have been identified;
- the project structure has been captured;
- Gradle and Manifest files have been identified;
- main Kotlin/Java files have been identified;
- legal and README files have been identified;
- `AUDIT-*` files have been generated;
- Android permissions have been reviewed;
- critical modules have been mapped;
- the first customization plan has been defined;
- no functional code has been modified without understanding its impact.

---

## 7. Initial risks

| Risk | Impact | Mitigation |
|---|---|---|
| Rebranding without audit | May break resources, strings, permissions, or package references | Prior inventory |
| Changing applicationId without a plan | Build failures or installation conflicts | Controlled phase |
| Touching connectivity before understanding it | Loss of baseline functionality | Before/after tests |
| Ignoring licenses | Legal and commercial risk | Explicit legal audit |
| Mixing external branding with Maobits OS | Brand and communication risk | Documentation separation |
| Optimizing without tests | Silent regressions | Technical baseline and tests |

---

## 8. Next phase

After this audit, the next phase will be:

```text
Phase 0.9 — Reproducible Technical Baseline
```

That phase will validate build, Android environment, Gradle, dependencies, tests, and the first technical report before customization changes begin.

---

## 9. Final statement

This audit protects the project from improvised modifications.

Maobits OS Android must start with clarity, traceability, legal respect, technical excellence, and cultural alignment.

**Person → Commitment → Confirmation**
