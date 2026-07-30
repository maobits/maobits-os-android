# Maobits OS Android — Official Repository Plan 1.0

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document defines **Phase 1.0 — Official `maobits-os-android` Repository Plan**.

Phase 0.9 confirmed that the Android project has a reproducible technical baseline:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

Phase 1.0 turns that baseline into a formal Git strategy to separate:

- the official **Maobits OS Android** product;
- the technical reference fork;
- foundation branches;
- license traceability;
- future customization phases;
- the quality flow through Pull Requests.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Official repository name

The official product repository must be named:

```text
maobits-os-android
```

This will be the main repository for the Maobits OS Android product.

The previous technical source remains a technical reference, not the commercial identity of the product.

---

## 4. Brand policy inside Git

| Element | Decision |
|---|---|
| Product name | Maobits OS Android |
| Official repository | `maobits-os-android` |
| Brand visible in own documentation | Maobits OS |
| External brand | Only credits, licenses, audit, and traceability |
| Main branch | `main` |
| Current foundation branch | `foundation/00-maobits-os-android-baseline` |
| Previous technical base | Separate remote, for example `reference` or `upstream-reference` |

---

## 5. Expected state before starting

Before running this phase, validate:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git log --oneline --decorate -8
git remote -v
git branch --show-current
```

Expected state:

```text
Branch: foundation/00-maobits-os-android-baseline
Working tree: clean
Documentation commits for audit and baseline are present
```

If pending files exist, do not continue until they are reviewed and confirmed.

---

## 6. Remote strategy

The recommended strategy is to separate the official remote from the reference remote.

```text
origin             → official Maobits OS Android repository
reference          → fork or technical reference source
```

If the current `origin` points to the previous fork, rename it to keep it as a reference.

---

## 7. Audit remotes before changing

Run:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git remote -v
```

If you see something similar to:

```text
origin  https://github.com/maobits/bitchat-android.git (fetch)
origin  https://github.com/maobits/bitchat-android.git (push)
```

then `origin` still represents the technical reference fork and must be renamed.

---

## 8. Rename current remote as reference

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git remote rename origin reference

git remote -v
```

Expected result:

```text
reference  https://github.com/maobits/bitchat-android.git (fetch)
reference  https://github.com/maobits/bitchat-android.git (push)
```

---

## 9. Create or connect the official remote

After creating the empty `maobits-os-android` repository in the corresponding account or organization, add it as `origin`.

HTTPS example:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git remote add origin https://github.com/maobits/maobits-os-android.git

git remote -v
```

Expected result:

```text
origin     https://github.com/maobits/maobits-os-android.git (fetch)
origin     https://github.com/maobits/maobits-os-android.git (push)
reference  https://github.com/maobits/bitchat-android.git (fetch)
reference  https://github.com/maobits/bitchat-android.git (push)
```

---

## 10. Prepare the official main branch

Do not lose the foundation branch. The recommendation is to create `main` from the audited baseline.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout foundation/00-maobits-os-android-baseline

git status

git checkout -b main
```

If `main` already exists locally, use:

```bash
git checkout main
git merge --no-ff foundation/00-maobits-os-android-baseline
```

---

## 11. First push to the official repository

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git push -u origin main

git push origin foundation/00-maobits-os-android-baseline
```

---

## 12. Recommended tags

Create tags to preserve control points.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git tag -a maobits-os-android-baseline-0.9.3 \
  -m "Maobits OS Android reproducible baseline: build, test and lint successful"

git push origin maobits-os-android-baseline-0.9.3
```

---

## 13. Branch policy

| Branch | Purpose | Recommended protection |
|---|---|---|
| `main` | Stable product line | Yes |
| `foundation/*` | Foundation and audit phases | Medium |
| `docs/*` | Documentation, roadmap, and evidence | Low/medium |
| `audit/*` | Technical and legal audits | Medium |
| `brand/*` | Visual and brand customization | Medium |
| `legal/*` | Licenses, credits, notices, and compliance | High |
| `architecture/*` | Modularization and architecture | High |
| `feature/*` | New features | Medium |
| `fix/*` | Small fixes | Medium |
| `release/*` | Release preparation | High |

---

## 14. Commit convention

Use clear and atomic commits:

```text
docs(scope): message
audit(scope): message
build(scope): message
chore(scope): message
refactor(scope): message
feat(scope): message
fix(scope): message
test(scope): message
legal(scope): message
brand(scope): message
```

Examples:

```bash
git commit -m "docs(repo): add official repository plan"
git commit -m "legal(licenses): preserve technical source attribution"
git commit -m "brand(app): add Maobits OS visual resource inventory"
git commit -m "build(android): configure Maobits OS application id"
```

---

## 15. Pull Request policy

Each Pull Request must include:

- change objective;
- roadmap phase;
- modified files;
- expected impact;
- build evidence;
- test evidence;
- lint evidence;
- license review when applicable;
- Android permission review when applicable;
- screenshots when UI changes;
- privacy note when identity, messages, location, camera, microphone, or storage are affected.

---

## 16. Minimum merge gate

Before merging to `main`, run:

```bash
./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all
./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all
./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all
./gradlew lintDebug --no-daemon --stacktrace --warning-mode all
```

All commands must exit with status `0`.

---

## 17. Bilingual documentation policy

Every new Markdown document must exist in two versions:

```text
*.es.md
*.en.md
```

Each delivery must be downloadable and include a copy command from:

```text
/home/maobits/Descargas
```

to the corresponding project folder.

---

## 18. Code comments and headers policy

All new code must use technical English comments and an institutional header when applicable.

Base Kotlin template:

```kotlin
/*
 * Project: Maobits OS Android
 * Module: <module-name>
 * File: <file-name>
 * Purpose: <clear technical purpose of this file>
 *
 * Company: Maobits
 * Lead developer: Mauricio Chara Hurtado
 * Technical contact: os@maobits.com
 * Product principle: Person → Commitment → Confirmation
 *
 * Quality standard:
 * - Production-grade structure.
 * - Clear separation of responsibilities.
 * - Auditable behavior and explicit failure paths.
 * - Maintainable implementation with meaningful technical comments.
 *
 * Legal and attribution note:
 * - Preserve original third-party license notices when applicable.
 * - Do not mix Maobits OS branding with external project branding.
 */
```

---

## 19. Rules to avoid breaking connectivity

Before touching communication, preserve evidence for:

- BLE;
- Bluetooth permissions;
- Wi-Fi Aware;
- Nostr;
- MessageRouter;
- foreground services;
- store-and-forward;
- encryption;
- keys;
- outbox;
- notifications;
- sensitive permissions.

Any change in those areas must have its own branch, tests, and clear rollback path.

---

## 20. Technical-source decision matrix

| Situation | Recommended decision |
|---|---|
| Architecture documentation only | Keep technical reference in credits |
| Direct Android code reuse | Review GPL v3 and obligations |
| Closed commercial product | Avoid GPL contamination through clean-room or legal review |
| GPL-compatible open product | Preserve license and corresponding source |
| Visual branding change | Allowed if licenses and authorship are not hidden |
| External brand use in marketing | Not allowed as Maobits OS identity |

---

## 21. Commit command for this phase

After copying this documentation:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

mkdir -p docs/01-repository

cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-OFFICIAL-REPOSITORY-PLAN-1.0.es.md docs/01-repository/
cp /home/maobits/Descargas/MAOBITS-OS-ANDROID-OFFICIAL-REPOSITORY-PLAN-1.0.en.md docs/01-repository/

git add docs/01-repository/MAOBITS-OS-ANDROID-OFFICIAL-REPOSITORY-PLAN-1.0.es.md \
        docs/01-repository/MAOBITS-OS-ANDROID-OFFICIAL-REPOSITORY-PLAN-1.0.en.md

git commit -m "docs(repo): add official Maobits OS Android repository plan"
```

---

## 22. Acceptance criteria for phase 1.0

Phase 1.0 is complete when:

- official `maobits-os-android` repository exists;
- `origin` points to the official repository;
- `reference` preserves the previous technical source;
- `main` exists and contains the validated baseline;
- the foundation branch has been pushed;
- baseline 0.9.3 tag exists;
- bilingual documentation has been copied;
- documentation has been versioned;
- no functional code was changed;
- the project is ready for Phase 1.1.

---

## 23. Next phase

```text
Phase 1.1 — Brand, visual resources, and visible text inventory
```

This phase will identify:

- current visible app name;
- strings;
- logos;
- icons;
- colors;
- themes;
- custom permissions with external branding;
- Manifest labels;
- FileProvider authorities;
- notifications;
- onboarding text;
- reusable or replaceable assets.

---

## 24. Final statement

Phase 1.0 separates the Maobits OS Android project from its technical reference source without removing traceability or licenses.

From this point forward, the official repository must protect Maobits OS identity, technical quality, evidence, ethics, digital citizenship, and the principle:

**Person → Commitment → Confirmation**
