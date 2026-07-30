# Maobits OS Android — Corrección de toolchain Java 21 0.9.1

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento registra la corrección necesaria para continuar la **Fase 0.9 — Baseline técnico reproducible**.

Durante la ejecución de Gradle se confirmó que el proyecto puede listar módulos, pero falla al crear tareas de compilación porque el entorno local usa Java 17 y el proyecto requiere una toolchain Java 21.

---

## 2. Diagnóstico

Gradle detectó:

```text
Launcher JVM: 17.0.17
Daemon JVM: /home/maobits/.sdkman/candidates/java/17.0.17-tem
```

El error principal indica:

```text
Cannot find a Java installation on your machine matching: {languageVersion=21}
Toolchain download repositories have not been configured.
```

Esto significa que el repositorio o el plugin Android/Kotlin está configurado para compilar con Java 21, pero el equipo local solo tiene Java 17 activo.

---

## 3. Decisión técnica

La solución correcta en esta fase es instalar Java 21 localmente y usarlo para el baseline.

No se debe modificar todavía el código, Gradle, `applicationId`, `namespace`, paquetes, permisos ni lógica funcional.

---

## 4. Corrección con SDKMAN

El entorno ya muestra uso de SDKMAN, por lo tanto esta es la ruta recomendada.

Ejecutar:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

sdk list java | grep -E "21\..*tem" || true
```

Luego instalar una versión Java 21 Temurin disponible. Ejemplo común:

```bash
sdk install java 21.0.9-tem
```

Si SDKMAN muestra otra versión 21 más reciente, usar exactamente el identificador mostrado por `sdk list java`.

Después activar Java 21 en la terminal actual:

```bash
sdk use java 21.0.9-tem
```

O dejarlo como predeterminado:

```bash
sdk default java 21.0.9-tem
```

Validar:

```bash
java -version
javac -version
```

La salida debe mostrar Java 21.

---

## 5. Alternativa con paquete del sistema

Si se prefiere usar paquetes del sistema y la distribución lo soporta:

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk

sudo update-alternatives --config java
sudo update-alternatives --config javac

java -version
javac -version
```

Si `openjdk-21-jdk` no existe en los repositorios de la distribución, usar SDKMAN.

---

## 6. Repetir baseline después de instalar Java 21

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

{
  echo "=== JAVA AFTER TOOLCHAIN FIX ==="
  java -version 2>&1
  echo
  echo "=== JAVAC AFTER TOOLCHAIN FIX ==="
  javac -version 2>&1
} > "$BASELINE_DIR/BASELINE-JAVA-21-TOOLCHAIN-FIX.txt"

./gradlew tasks --all \
  --no-daemon \
  --stacktrace \
  2>&1 | tee "$BASELINE_DIR/BASELINE-GRADLE-TASKS-AFTER-JAVA21.log"
```

---

## 7. Compilar nuevamente

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BASELINE_DIR="docs/05-audit/evidence/2026-07-29-reproducible-baseline"

set -o pipefail

./gradlew :app:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-APP-ASSEMBLE-DEBUG-AFTER-JAVA21.log"

APP_BUILD_STATUS=${PIPESTATUS[0]}

./gradlew :wear:assembleDebug \
  --no-daemon \
  --stacktrace \
  --warning-mode all \
  2>&1 | tee "$BASELINE_DIR/BASELINE-WEAR-ASSEMBLE-DEBUG-AFTER-JAVA21.log"

WEAR_BUILD_STATUS=${PIPESTATUS[0]}

{
  echo "=== BASELINE BUILD SUMMARY AFTER JAVA 21 ==="
  echo "Generated at: $(date -Iseconds)"
  echo "App build status: $APP_BUILD_STATUS"
  echo "Wear build status: $WEAR_BUILD_STATUS"
} > "$BASELINE_DIR/BASELINE-SUMMARY-AFTER-JAVA21.txt"

cat "$BASELINE_DIR/BASELINE-SUMMARY-AFTER-JAVA21.txt"
```

---

## 8. Criterio de aceptación

La corrección queda aceptada cuando:

- `java -version` muestra Java 21;
- `javac -version` muestra Java 21;
- `./gradlew tasks --all` ya no falla por toolchain Java 21;
- se genera `BASELINE-JAVA-21-TOOLCHAIN-FIX.txt`;
- se genera `BASELINE-SUMMARY-AFTER-JAVA21.txt`;
- el resultado de `app` y `wear` queda documentado;
- no se modificó código funcional.

---

## 9. Commit recomendado

Después de validar y revisar evidencia:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git add docs/05-audit/evidence/2026-07-29-reproducible-baseline \
        docs/05-audit/MAOBITS-OS-ANDROID-JAVA-21-TOOLCHAIN-FIX-0.9.1.es.md \
        docs/05-audit/MAOBITS-OS-ANDROID-JAVA-21-TOOLCHAIN-FIX-0.9.1.en.md

git commit -m "docs(audit): document Java 21 toolchain requirement"
```

---

## 10. Declaración final

Este ajuste no cambia Maobits OS Android. Solo alinea el entorno local con la toolchain requerida para auditar y compilar de forma reproducible.

**Persona → Compromiso → Confirmación**
