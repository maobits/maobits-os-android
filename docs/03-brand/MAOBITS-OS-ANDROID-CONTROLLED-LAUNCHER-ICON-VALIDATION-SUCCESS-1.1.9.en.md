# Maobits OS Android — Successful validation of controlled launcher icon replacement 1.1.9

**Version:** 0.1.0  
**Date:** 2026-07-30  
**Evidence time:** 17:49:19-05:00  
**Project:** Maobits OS Android  
**Company:** Maobits  
**Conceptual direction and lead developer:** Mauricio Chara Hurtado  
**Technical email:** os@maobits.com  
**Product principle:** Person → Commitment → Confirmation  

## 1. Purpose

This document records the successful validation of **Phase 1.1.9 — Controlled Launcher Icon Replacement**.

The phase applied candidate PNG resources for `ic_launcher.png` and `ic_launcher_round.png` in `app` and `wear`, then ran automatic build, test, and lint validation.

## 2. Official workspace

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

## 3. Automatic validation result

The validation reported:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

This confirms that the controlled PNG launcher replacement did not break Android app build, Wear OS build, unit tests, or configured project lint.

## 4. Lint observation

The lint process ended with status `0`, although the report indicated errors, warnings, and hints managed by the existing project configuration and baseline.

This behavior had already been observed in previous phases. It does not block this phase because the final result was successful.

## 5. EOG observation

The message `EOG-WARNING: Thumbnail creation failed` belongs to the Ubuntu/GNOME image viewer, not to the Android build, APK, resource replacement, or Maobits OS runtime.

It does not block the phase.

## 6. Validated scope

This phase allowed replacing only launcher PNG resources:

```text
app/src/main/res/mipmap-*/ic_launcher.png
app/src/main/res/mipmap-*/ic_launcher_round.png
wear/src/main/res/mipmap-*/ic_launcher.png
wear/src/main/res/mipmap-*/ic_launcher_round.png
```

Adaptive icons under `mipmap-anydpi-v26` are not part of this phase and remain for 1.1.10.

## 7. Acceptance criteria met

| Criterion | Status |
|---|---|
| App build successful | Met |
| Wear build successful | Met |
| Tests successful | Met |
| Lint successful | Met |
| Launcher PNG replacement applied | Met |
| Non-blocking EOG warning identified | Met |
| Adaptive icons separated for later phase | Met |
| Automatic evidence generated | Met |

## 8. Recommended real-device test before final commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

adb devices

./gradlew :app:installDebug --no-daemon --stacktrace --warning-mode all

adb shell am force-stop com.bitchat.droid
adb shell monkey -p com.bitchat.droid -c android.intent.category.LAUNCHER 1
```

Manual validation:

```text
[ ] App opens.
[ ] App still appears as Maobits OS.
[ ] No crash.
[ ] Icon changes if launcher uses legacy PNG resources.
[ ] If icon does not change, continue with adaptive icons in 1.1.10.
```

## 9. Recommended real-device evidence

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

REAL_ICON_TEST_DIR="docs/03-brand/evidence/2026-07-30-real-device-launcher-icon-test"
mkdir -p "$REAL_ICON_TEST_DIR"

cat > "$REAL_ICON_TEST_DIR/REAL-DEVICE-LAUNCHER-ICON-TEST.txt" <<'EOF'
=== MAOBITS OS ANDROID - REAL DEVICE LAUNCHER ICON TEST ===

Date:
2026-07-30

Scenario:
Maobits OS Android installed after controlled launcher PNG replacement.

Expected:
App opens successfully.
Visible app name remains Maobits OS.
Launcher icon may update if launcher uses PNG legacy resources.
If launcher still shows the old icon, adaptive icon replacement is required in phase 1.1.10.

Result:
Pending manual confirmation.

Notes:
Pending manual entry.
EOF

cat "$REAL_ICON_TEST_DIR/REAL-DEVICE-LAUNCHER-ICON-TEST.txt"
```

## 10. Recommended commit

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add app/src/main/res \
        wear/src/main/res \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-REPLACEMENT-1.1.9.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-REPLACEMENT-1.1.9.en.md \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-VALIDATION-SUCCESS-1.1.9.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-CONTROLLED-LAUNCHER-ICON-VALIDATION-SUCCESS-1.1.9.en.md \
        docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement \
        tools/brand/maobits_os_apply_launcher_icons_1_1_9.py

git commit -m "brand(icons): replace launcher icon PNG resources"
```

## 11. Next phase

```text
Phase 1.1.10 — Controlled adaptive icon replacement
```

On modern Android, this next phase may be the one that actually updates the visible launcher icon.

**Person → Commitment → Confirmation**
