# Maobits OS Android — Validación exitosa del reemplazo controlado de launcher icons 1.1.9

**Versión:** 0.1.0  
**Fecha:** 2026-07-30  
**Hora de evidencia:** 17:49:19-05:00  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

## 1. Propósito

Este documento registra la validación exitosa de la **Fase 1.1.9 — Reemplazo controlado de launcher icons**.

La fase aplicó recursos PNG candidatos para `ic_launcher.png` e `ic_launcher_round.png` en `app` y `wear`, y luego ejecutó validación automática de compilación, pruebas y lint.

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

## 3. Resultado de validación automática

La validación reportó:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

Esto confirma que el reemplazo controlado de PNG launcher no rompió la compilación de Android app, la compilación Wear OS, las pruebas unitarias ni el lint configurado del proyecto.

## 4. Observación sobre lint

El proceso de lint terminó con estado `0`, aunque el reporte indicó errores, advertencias e hints administrados por la configuración existente y baseline del proyecto.

Este comportamiento ya se había observado en fases anteriores. No bloquea esta fase porque el resultado final fue exitoso.

## 5. Observación sobre EOG

El mensaje `EOG-WARNING: Thumbnail creation failed` corresponde al visor de imágenes de Ubuntu/GNOME, no al build de Android, no al APK, no al reemplazo de recursos y no al runtime de Maobits OS.

No bloquea la fase.

## 6. Alcance validado

Esta fase permitió reemplazar únicamente recursos PNG launcher:

```text
app/src/main/res/mipmap-*/ic_launcher.png
app/src/main/res/mipmap-*/ic_launcher_round.png
wear/src/main/res/mipmap-*/ic_launcher.png
wear/src/main/res/mipmap-*/ic_launcher_round.png
```

No se deben considerar parte de esta fase los adaptive icons de `mipmap-anydpi-v26`; quedan para 1.1.10.

## 7. Criterios de aceptación cumplidos

| Criterio | Estado |
|---|---|
| App build exitoso | Cumplido |
| Wear build exitoso | Cumplido |
| Tests exitosos | Cumplido |
| Lint exitoso | Cumplido |
| Reemplazo PNG launcher aplicado | Cumplido |
| EOG warning no bloqueante identificado | Cumplido |
| Adaptive icons separados para fase posterior | Cumplido |
| Evidencia automática generada | Cumplido |

## 8. Prueba real recomendada antes del commit final

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

adb devices

./gradlew :app:installDebug --no-daemon --stacktrace --warning-mode all

adb shell am force-stop com.bitchat.droid
adb shell monkey -p com.bitchat.droid -c android.intent.category.LAUNCHER 1
```

Validar manualmente:

```text
[ ] La app abre.
[ ] Sigue apareciendo como Maobits OS.
[ ] No crashea.
[ ] El icono cambia si el launcher usa PNG legacy.
[ ] Si el icono no cambia, continuar con adaptive icons en 1.1.10.
```

## 9. Evidencia recomendada para prueba real

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

## 10. Commit recomendado

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

## 11. Próxima fase

```text
Fase 1.1.10 — Reemplazo controlado de adaptive icons
```

En Android moderno, esta próxima fase puede ser la que actualice realmente el icono visible del launcher.

**Persona → Compromiso → Confirmación**
