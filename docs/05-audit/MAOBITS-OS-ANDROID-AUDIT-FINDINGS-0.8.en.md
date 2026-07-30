# Maobits OS Android — Initial Audit Findings 0.8

**Version:** 0.1.0  
**Date:** 2026-07-29  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

---

## 1. Purpose

This document records the first technical findings collected during the initial audit of the Android repository used as the starting point for **Maobits OS Android**.

Its goal is to turn terminal evidence into ordered architectural decisions, without modifying functional code yet.

---

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Observed Git state

The audit was executed on branch:

```text
foundation/00-maobits-os-android-baseline
```

Untracked `AUDIT-*` evidence files were observed before being organized under `docs/05-audit/evidence`.

---

## 4. Detected Android modules

The Gradle structure confirms at least two main modules:

| Module | Gradle file | Initial purpose |
|---|---|---|
| `app` | `./app/build.gradle.kts` | Main Android application |
| `wear` | `./wear/build.gradle.kts` | Wear OS application or component |

Initial architectural decision:

- Maobits OS Android must treat `app` as the main mobile experience.
- The `wear` module must be audited as an independent capability, not removed or renamed yet.
- Any customization must preserve separate build validation for `app` and `wear`.

---

## 5. Detected current Android identity

| Element | Current value | Risk | Future decision |
|---|---|---|---|
| App namespace | `com.bitchat.android` | High due to branding and technical coupling | Migrate in a controlled phase |
| App applicationId | `com.bitchat.droid` | High due to public installation identity | Change only after reproducible baseline |
| App versionCode | `36` | Medium | Define Maobits versioning |
| App versionName | `1.7.5` | Medium | Restart product versioning with traceability |
| Wear namespace | `com.bitchat.watch` | High due to branding | Migrate in a controlled phase |
| Wear applicationId | `com.bitchat.watch` | High due to public identity | Change with Wear OS plan |
| Wear versionCode | `1` | Low | Keep until release strategy is defined |
| Wear versionName | `0.1.0` | Low | Keep until baseline |

---

## 6. Branding decision

Do not immediately change namespace, applicationId, or custom permissions without validating build, tests, and internal references.

The correct path is:

1. audit current references;
2. build baseline without changes;
3. create minimum tests;
4. change visual branding first;
5. change `applicationId`;
6. change `namespace`;
7. migrate Kotlin packages;
8. update custom permissions;
9. validate clean installation;
10. validate upgrade/migration when applicable.

---

## 7. Detected Android permissions

The main app declares permissions for:

- internet and network state;
- network state changes;
- legacy and modern Bluetooth;
- Bluetooth advertise, connect, and scan;
- coarse, fine, and background location;
- notifications;
- Wi-Fi state/change;
- local network;
- wake lock;
- custom forced-finish permission;
- foreground service;
- foreground service connected device;
- foreground service data sync;
- foreground service location;
- boot completed reception;
- microphone;
- camera;
- external storage read;
- image, video, and audio media reads;
- vibration;
- request to ignore battery optimizations.

The Wear module declares permissions related to:

- Bluetooth;
- foreground service;
- connected device;
- notifications;
- microphone;
- vibration.

---

## 8. Sensitive permission risk

| Permission or group | Level | Justification | Maobits OS mitigation |
|---|---|---|---|
| `ACCESS_BACKGROUND_LOCATION` | Critical | Can create privacy concern and strict review | Clear justification, minimal use, educational screen, and opt-out |
| `RECORD_AUDIO` | High | May be perceived as surveillance | Contextual request, visible explanation, never active without clear action |
| `CAMERA` | High | Privacy and trust risk | Use only for QR, evidence, or explicit features |
| `READ_MEDIA_*` | High | Access to personal content | Prefer modern pickers and minimize access |
| `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` | High | May be perceived as invasive | Explain connectivity continuity and allow refusal |
| `BLUETOOTH_SCAN` + location | High | Proximity and metadata exposure | Do not promise absolute anonymity; provide visibility controls |
| `FOREGROUND_SERVICE_LOCATION` | High | Can be associated with tracking | Justify through connectivity/proximity and monitor usage |
| `RECEIVE_BOOT_COMPLETED` | Medium | Automatic startup can be sensitive | Require consent and visible settings |
| Custom permission `com.bitchat.android.permission.FORCE_FINISH` | High | Contains external branding and must be migrated | Change in a controlled phase to a Maobits OS permission |

---

## 9. Detected Android components

Evidence shows:

| Type | App | Wear | Observation |
|---|---:|---:|---|
| Services | 3 | 1 | Exact component names must be identified |
| Activities | 3 | 1 | Navigation and main entry point must be mapped |
| Receivers | 2 main + 1 debug | 1 debug | Boot, debug, and security behavior must be reviewed |
| Providers | 1 | 0 | Exposure, authorities, and file-sharing behavior must be reviewed |

---

## 10. Initial architectural risks

| Risk | Impact | Required action |
|---|---|---|
| Code still uses external technical identity | Branding and distribution risk | Planned migration |
| Highly sensitive permissions exist | Trust, privacy, and store-review risk | Permission governance |
| Foreground services exist | Battery, policy, and UX risk | Behavior baseline |
| Wear OS exists | Increases technical scope | Treat as controlled subproduct |
| Source files list was not received yet | Real Kotlin/Java package map is incomplete | Run deep audit |
| Connectivity is critical | Any change can break core value | Build before modifying |

---

## 11. Mandatory next step

Before modifying code, generate a deeper audit of source files, classes, packages, and real components.

Required evidence:

```text
AUDIT-SOURCE-FILES-DEEP.txt
KOTLIN-PACKAGE-INVENTORY.txt
KOTLIN-CLASS-INVENTORY.txt
COMMUNICATION-SECURITY-INVENTORY.txt
APP-MAIN-MANIFEST-NUMBERED.txt
WEAR-MAIN-MANIFEST-NUMBERED.txt
```

---

## 12. Progress gate

Do not move into visual customization, package rename, applicationId change, or refactor until:

- baseline builds;
- Kotlin/Java structure is mapped;
- services are identified;
- permissions are justified;
- Android license is recorded;
- a branding migration plan exists;
- a documentation audit commit exists.

---

## 13. Final statement

The audit confirms that Maobits OS Android must progress with discipline: understand first, then build, then document, and finally customize.

**Person → Commitment → Confirmation**
