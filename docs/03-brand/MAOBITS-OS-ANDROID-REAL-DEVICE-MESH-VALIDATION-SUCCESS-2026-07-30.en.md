# Maobits OS Android — Successful Real-Device Mesh Validation on Two Smartphones

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

## 1. Purpose

This document records a successful real-device test of Maobits OS Android installed on two physical smartphones.

The test confirms that the application starts correctly, enters the default channel, and allows device discovery/communication when device conditions are appropriate.

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

## 3. Test context

During the first run, both phones entered the default channel but did not discover each other.

The root cause found was:

```text
Very low battery level.
```

After correcting that condition, the test was repeated and the user confirmed that it worked correctly.

## 4. Result

```text
Status: Successful
Devices: Two real smartphones
Visible application: Maobits OS
Current internal package: com.bitchat.droid
Channel: default channel
Device discovery: correct
Basic communication: correct
Required code change: no
```

## 5. Technical interpretation

The test demonstrates that the current Maobits OS Android runtime can operate correctly on real devices.

The initial failure was not necessarily a code bug, but an Android operational condition. In very low battery states, Android may restrict BLE scanning, BLE advertising, background services, foreground services, Nearby Devices, and connectivity-related tasks.

## 6. Rule added for real-device tests

Before testing mesh connectivity on physical phones:

```text
Recommended minimum battery: 30%
Battery saver: disabled
Bluetooth: enabled
Location: enabled
Nearby Devices permission: allowed
Location permission: allowed if applicable
App battery usage: unrestricted
Screen: on during initial discovery
Device distance: short during initial discovery
```

## 7. Manually confirmed criteria

| Criterion | Status |
|---|---|
| App installed on real phone | Met |
| App installed on second real phone | Met |
| App opens correctly | Met |
| Both phones enter the default channel | Met |
| Discovery works after battery condition is resolved | Met |
| Basic communication works | Met |
| No code change is required for this finding | Met |

## 8. Recommended repository evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

REAL_MESH_TEST_DIR="docs/03-brand/evidence/2026-07-30-real-device-mesh-validation-success"
mkdir -p "$REAL_MESH_TEST_DIR"

cat > "$REAL_MESH_TEST_DIR/REAL-DEVICE-MESH-VALIDATION-SUCCESS.txt" <<'EOF'
=== MAOBITS OS ANDROID - REAL DEVICE MESH VALIDATION SUCCESS ===

Date:
2026-07-30

Tester:
Mauricio Chara Hurtado

Scenario:
Maobits OS Android installed on two real smartphones.

Initial condition:
Both devices opened the app and entered the default channel, but did not discover each other.

Root cause found:
Very low battery level.

Resolution:
After resolving the low battery condition, both smartphones discovered each other and communication worked correctly.

Result:
Successful real-device mesh smoke test.

Current visible app name:
Maobits OS

Current internal package:
com.bitchat.droid

Code change required:
No.

Operational rule:
Future real-device mesh tests must use devices with battery level above 30%, battery saver disabled, Bluetooth enabled, location enabled, Nearby Devices allowed, and unrestricted app battery usage.

Status:
Approved.
EOF

cat "$REAL_MESH_TEST_DIR/REAL-DEVICE-MESH-VALIDATION-SUCCESS.txt"
```

## 9. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-REAL-DEVICE-MESH-VALIDATION-SUCCESS-2026-07-30.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-REAL-DEVICE-MESH-VALIDATION-SUCCESS-2026-07-30.en.md \
        docs/03-brand/evidence/2026-07-30-real-device-mesh-validation-success

git commit -m "test(android): record successful real device mesh validation"
```

## 10. Next decision

With this real-device test approved, the project can move forward with more confidence toward:

```text
Phase 1.1.7 — Controlled generation of Maobits OS visual assets
```

The app has now been verified on real hardware before deeper visual changes are introduced.

## 11. Final statement

The first functional validation on two real smartphones was successful. This result confirms that the current base works beyond the build environment and can support real communication tests.

**Person → Commitment → Confirmation**
