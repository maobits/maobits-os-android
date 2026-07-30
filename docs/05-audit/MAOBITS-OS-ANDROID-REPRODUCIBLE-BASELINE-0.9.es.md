# Maobits OS Android — Baseline técnico reproducible 0.9

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 0.9 — Baseline técnico reproducible** para Maobits OS Android.

La finalidad es confirmar que el repositorio Android puede compilarse, inspeccionarse y auditarse antes de iniciar cambios de marca, paquetes, `applicationId`, `namespace`, permisos, pantallas o lógica de conectividad.

Esta fase evita modificar código sobre una base desconocida.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado de entrada esperado

Antes de ejecutar esta fase, debe existir un commit documental previo de auditoría inicial.

Commit observado durante la ejecución del proyecto:

```text
4dc40c3 docs(audit): add Android baseline audit evidence
```

La rama esperada es:

```text
foundation/00-maobits-os-android-baseline
```

---

## 4. Regla de seguridad de esta fase

Durante esta fase no se debe:

- cambiar `applicationId`;
- cambiar `namespace`;
- renombrar paquetes Kotlin;
- eliminar permisos;
- eliminar servicios;
- cambiar el nombre comercial en recursos;
- modificar lógica de BLE, Wi-Fi Aware, Nostr, cifrado, store-and-forward o foreground services;
- borrar licencias;
- cambiar archivos originales sin evidencia previa.

El objetivo es **medir y comprobar**, no personalizar.

---

## 5. Evidencia esperada

La evidencia de esta fase debe guardarse en:

```text
docs/05-audit/evidence/2026-07-29-reproducible-baseline
```

Archivos esperados:

```text
BASELINE-GIT-STATE.txt
BASELINE-JAVA-GRADLE.txt
BASELINE-GRADLE-PROJECTS.txt
BASELINE-GRADLE-TASKS.txt
BASELINE-APP-ASSEMBLE-DEBUG.log
BASELINE-WEAR-ASSEMBLE-DEBUG.log
BASELINE-TESTS.log
BASELINE-LINT.log
BASELINE-SUMMARY.txt
```

---

## 6. Comandos de baseline reproducible

Ejecutar desde el repositorio:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"
mkdir -p "$BASELINE_DIR"

{
  echo "=== MAOBITS OS ANDROID - BASELINE GIT STATE ==="
  echo "Generated at: $(date -Iseconds)"
  echo
  echo "=== PWD ==="
  pwd
  echo
  echo "=== CURRENT BRANCH ==="
  git branch --show-current
  echo
  echo "=== GIT STATUS ==="
  git status
  echo
  echo "=== LAST 10 COMMITS ==="
  git log --oneline --decorate -10
  echo
  echo "=== REMOTES ==="
  git remote -v
} > "$BASELINE_DIR/BASELINE-GIT-STATE.txt"

{
  echo "=== JAVA ==="
  java -version 2>&1 || true
  echo
  echo "=== JAVAC ==="
  javac -version 2>&1 || true
  echo
  echo "=== GRADLE WRAPPER FILES ==="
  ls -la gradlew gradle/wrapper 2>&1 || true
} > "$BASELINE_DIR/BASELINE-JAVA-GRADLE.txt"

chmod +x ./gradlew

./gradlew --version \
  --no-daemon \
  2>&1 | tee -a "$BASELINE_DIR/BASELINE-JAVA-GRADLE.txt"

./gradlew projects \
  --no-daemon \
  --stacktrace \
  2>&1 | tee "$BASELINE_DIR/BASELINE-GRADLE-PROJECTS.txt"

./gradlew tasks --all \
  --no-daemon \
  --stacktrace \
  2>&1 | tee "$BASELINE_DIR/BASELINE-GRADLE-TASKS.txt"
```

---

## 7. Compilación controlada

Ejecutar cada compilación por separado para poder aislar errores.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

set -o pipefail

./gradlew :app:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-APP-ASSEMBLE-DEBUG.log"

APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-WEAR-ASSEMBLE-DEBUG.log"

WEAR_BUILD_STATUS=${PIPESTATUS[0]}

{
  echo "=== BASELINE BUILD SUMMARY ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
} > "$BASELINE_DIR/BASELINE-SUMMARY.txt"

cat "$BASELINE_DIR/BASELINE-SUMMARY.txt"
```

---

## 8. Pruebas y lint

Ejecutar solo después de la compilación inicial:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

set -o pipefail

./gradlew testDebugUnitTest \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-TESTS.log"

TEST_STATUS=${PIPESTATUS[0]}

./gradlew lintDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-LINT.log"

LINT_STATUS=${PIPESTATUS[0]}

{
  echo
  echo "=== TEST AND LINT SUMMARY ==="
  echo "Test status: $TEST_STATUS"
  echo "Lint status: $LINT_STATUS"
} >> "$BASELINE_DIR/BASELINE-SUMMARY.txt"

cat "$BASELINE_DIR/BASELINE-SUMMARY.txt"
```

---

## 9. Interpretación de estados

| Código | Significado | Acción |
|---:|---|---|
| `0` | Comando exitoso | Registrar evidencia y continuar |
| Diferente de `0` | Error de compilación, test o lint | No corregir todavía sin analizar log |
| Falta `gradlew` | Repositorio incompleto o estructura no estándar | Revisar archivos base |
| Falla Java/Gradle | Entorno local no compatible | Ajustar entorno antes de tocar código |
| Falla app | Problema en módulo móvil principal | Analizar `BASELINE-APP-ASSEMBLE-DEBUG.log` |
| Falla wear | Problema en Wear OS | Decidir si Wear será mantenido, aplazado o aislado |
| Falla lint | Deuda técnica o reglas estrictas | Documentar antes de corregir |
| Falla test | Pruebas rotas o configuración incompleta | Documentar y corregir en fase separada |

---

## 10. Registro de hallazgos

Después de ejecutar los comandos, registrar:

```text
- Java detectado
- Gradle wrapper detectado
- módulos Gradle detectados
- resultado de app assembleDebug
- resultado de wear assembleDebug
- resultado de testDebugUnitTest
- resultado de lintDebug
- errores principales si existen
- advertencias principales si existen
- decisión de avance
```

---

## 11. Criterios de aceptación

La fase 0.9 se considera terminada cuando:

- la evidencia fue guardada en `docs/05-audit/evidence/2026-07-29-reproducible-baseline`;
- se conoce si `app` compila;
- se conoce si `wear` compila;
- se conoce si existen pruebas unitarias ejecutables;
- se conoce si `lintDebug` pasa o falla;
- se registraron errores sin ocultarlos;
- no se hicieron cambios funcionales improvisados;
- se creó commit documental con evidencia;
- existe decisión formal para pasar a Fase 1.0.

---

## 12. Commit recomendado

Solo después de revisar la evidencia:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/05-audit/evidence/2026-07-29-reproducible-baseline \
        docs/05-audit/MAOBITS-OS-ANDROID-REPRODUCIBLE-BASELINE-0.9.es.md \
        docs/05-audit/MAOBITS-OS-ANDROID-REPRODUCIBLE-BASELINE-0.9.en.md

git commit -m "docs(audit): add reproducible Android baseline evidence"
```

---

## 13. Próxima fase

Si el baseline es exitoso o si los errores quedan claramente documentados, el siguiente paso será:

```text
Fase 1.0 — Plan de repositorio oficial maobits-os-android
```

Esa fase definirá:

- creación o conexión del repositorio oficial;
- `origin` para Maobits OS Android;
- remoto separado para fuente técnica de referencia;
- ramas protegidas;
- tags iniciales;
- política de commits;
- política de cambios por Pull Request;
- separación de marca y licencias.

---

## 14. Declaración final

El baseline técnico reproducible es el punto donde Maobits OS Android deja de ser una intención y empieza a convertirse en un proyecto controlado.

**Persona → Compromiso → Confirmación**
