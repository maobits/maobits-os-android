# Maobits OS Android — Plan de repositorio oficial 1.0

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento define la **Fase 1.0 — Plan de repositorio oficial `maobits-os-android`**.

La fase 0.9 confirmó que el proyecto Android tiene baseline técnico reproducible:

```text
App build status: 0
Wear build status: 0
Test status: 0
Lint status: 0
```

La fase 1.0 convierte ese baseline en una estrategia Git formal para separar:

- el producto oficial **Maobits OS Android**;
- el fork de referencia técnica;
- las ramas de fundación;
- la trazabilidad de licencias;
- las futuras fases de personalización;
- el flujo de calidad por Pull Request.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Nombre oficial del repositorio

El repositorio oficial del producto debe llamarse:

```text
maobits-os-android
```

Este será el repositorio principal del producto Maobits OS Android.

La fuente técnica anterior queda como referencia técnica, no como identidad comercial del producto.

---

## 4. Política de marca dentro de Git

| Elemento | Decisión |
|---|---|
| Nombre del producto | Maobits OS Android |
| Repositorio oficial | `maobits-os-android` |
| Marca visible en documentación propia | Maobits OS |
| Marca externa | Solo créditos, licencias, auditoría y trazabilidad |
| Rama principal | `main` |
| Rama actual de fundación | `foundation/00-maobits-os-android-baseline` |
| Base técnica previa | remoto separado, por ejemplo `reference` o `upstream-reference` |

---

## 5. Estado esperado antes de iniciar

Antes de ejecutar esta fase, validar:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status
git log --oneline --decorate -8
git remote -v
git branch --show-current
```

Estado esperado:

```text
Rama: foundation/00-maobits-os-android-baseline
Working tree: clean
Commits documentales de auditoría y baseline presentes
```

Si hay archivos pendientes, no continuar hasta revisar y confirmar.

---

## 6. Estrategia de remotos

La estrategia recomendada es separar el remoto oficial del remoto de referencia.

```text
origin             → repositorio oficial Maobits OS Android
reference          → fork o fuente técnica de referencia
```

Si el remoto actual `origin` apunta al fork anterior, se debe renombrar para conservarlo como referencia.

---

## 7. Auditoría de remotos antes de cambiar

Ejecutar:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git remote -v
```

Si aparece algo similar a:

```text
origin  https://github.com/maobits/bitchat-android.git (fetch)
origin  https://github.com/maobits/bitchat-android.git (push)
```

entonces `origin` todavía representa el fork de referencia técnica y debe renombrarse.

---

## 8. Renombrar remoto actual como referencia

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git remote rename origin reference

git remote -v
```

Resultado esperado:

```text
reference  https://github.com/maobits/bitchat-android.git (fetch)
reference  https://github.com/maobits/bitchat-android.git (push)
```

---

## 9. Crear o conectar remoto oficial

Después de crear el repositorio vacío `maobits-os-android` en la cuenta u organización correspondiente, agregarlo como `origin`.

Ejemplo con HTTPS:

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git remote add origin https://github.com/maobits/maobits-os-android.git

git remote -v
```

Resultado esperado:

```text
origin     https://github.com/maobits/maobits-os-android.git (fetch)
origin     https://github.com/maobits/maobits-os-android.git (push)
reference  https://github.com/maobits/bitchat-android.git (fetch)
reference  https://github.com/maobits/bitchat-android.git (push)
```

---

## 10. Preparar rama principal oficial

No se debe perder la rama de fundación. La recomendación es crear `main` desde el baseline ya auditado.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git checkout foundation/00-maobits-os-android-baseline

git status

git checkout -b main
```

Si `main` ya existe localmente, usar:

```bash
git checkout main
git merge --no-ff foundation/00-maobits-os-android-baseline
```

---

## 11. Primer push al repositorio oficial

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git push -u origin main

git push origin foundation/00-maobits-os-android-baseline
```

---

## 12. Tags recomendados

Crear tags para conservar puntos de control.

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git tag -a maobits-os-android-baseline-0.9.3 \
  -m "Maobits OS Android reproducible baseline: build, test and lint successful"

git push origin maobits-os-android-baseline-0.9.3
```

---

## 13. Política de ramas

| Rama | Propósito | Protección recomendada |
|---|---|---|
| `main` | Línea estable del producto | Sí |
| `foundation/*` | Fases de fundación y auditoría | Media |
| `docs/*` | Documentación, roadmap y evidencia | Baja/media |
| `audit/*` | Auditorías técnicas y legales | Media |
| `brand/*` | Personalización visual y marca | Media |
| `legal/*` | Licencias, créditos, avisos y cumplimiento | Alta |
| `architecture/*` | Modularización y arquitectura | Alta |
| `feature/*` | Funcionalidades nuevas | Media |
| `fix/*` | Correcciones pequeñas | Media |
| `release/*` | Preparación de versiones | Alta |

---

## 14. Convención de commits

Usar commits claros y atómicos:

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

Ejemplos:

```bash
git commit -m "docs(repo): add official repository plan"
git commit -m "legal(licenses): preserve technical source attribution"
git commit -m "brand(app): add Maobits OS visual resource inventory"
git commit -m "build(android): configure Maobits OS application id"
```

---

## 15. Política de Pull Request

Cada Pull Request debe incluir:

- objetivo del cambio;
- fase del roadmap;
- archivos modificados;
- impacto esperado;
- evidencia de build;
- evidencia de tests;
- evidencia de lint;
- revisión de licencias si aplica;
- revisión de permisos Android si aplica;
- capturas si cambia UI;
- nota de privacidad si toca identidad, mensajes, ubicación, cámara, micrófono o almacenamiento.

---

## 16. Gate mínimo antes de merge

Antes de fusionar a `main`, ejecutar:

```bash
./gradlew :app:assembleDebug --no-daemon --stacktrace --warning-mode all
./gradlew :wear:assembleDebug --no-daemon --stacktrace --warning-mode all
./gradlew testDebugUnitTest --no-daemon --stacktrace --warning-mode all
./gradlew lintDebug --no-daemon --stacktrace --warning-mode all
```

Todos deben terminar con estado `0`.

---

## 17. Política de documentación bilingüe

Todo Markdown nuevo debe existir en dos versiones:

```text
*.es.md
*.en.md
```

Cada entrega debe ser descargable y debe incluir comando de copia desde:

```text
/home/maobits/Descargas
```

hacia la carpeta correspondiente del proyecto.

---

## 18. Política de comentarios y encabezados de código

Todo código nuevo debe tener comentarios técnicos en inglés y encabezado institucional cuando aplique.

Plantilla base para Kotlin:

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

## 19. Reglas para no romper conectividad

Antes de tocar comunicación, se debe conservar evidencia de:

- BLE;
- Bluetooth permissions;
- Wi-Fi Aware;
- Nostr;
- MessageRouter;
- foreground services;
- store-and-forward;
- cifrado;
- llaves;
- outbox;
- notificaciones;
- permisos sensibles.

Cualquier cambio en esas áreas debe tener rama propia, pruebas y rollback claro.

---

## 20. Matriz de decisión para fuente técnica

| Situación | Decisión recomendada |
|---|---|
| Solo documentación de arquitectura | Mantener referencia técnica en créditos |
| Reutilización directa de código Android | Revisar GPL v3 y obligaciones |
| Producto cerrado comercial | Evitar contaminación GPL mediante clean-room o revisión legal |
| Producto abierto compatible GPL | Conservar licencia y fuente correspondiente |
| Cambio de marca visual | Permitido si no oculta licencias ni autoría |
| Uso de marca externa en marketing | No permitido como identidad de Maobits OS |

---

## 21. Comando de commit de esta fase

Después de copiar esta documentación:

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

## 22. Criterios de aceptación de fase 1.0

La fase 1.0 queda completa cuando:

- existe repositorio oficial `maobits-os-android`;
- `origin` apunta al repositorio oficial;
- `reference` conserva la fuente técnica anterior;
- `main` existe y contiene el baseline validado;
- la rama de fundación fue subida;
- existe tag del baseline 0.9.3;
- la documentación bilingüe fue copiada;
- la documentación fue versionada;
- no se modificó código funcional;
- el proyecto queda listo para Fase 1.1.

---

## 23. Próxima fase

```text
Fase 1.1 — Inventario de marca, recursos visuales y textos visibles
```

Esa fase identificará:

- nombre visible actual de la app;
- strings;
- logos;
- iconos;
- colores;
- themes;
- permisos personalizados con marca externa;
- labels del Manifest;
- FileProvider authorities;
- notificaciones;
- textos de onboarding;
- assets reutilizables o reemplazables.

---

## 24. Declaración final

La fase 1.0 separa el proyecto Maobits OS Android de su fuente técnica de referencia sin borrar trazabilidad ni licencias.

Desde este punto, el repositorio oficial debe proteger la identidad Maobits OS, la calidad técnica, la evidencia, la ética, la ciudadanía digital y el principio:

**Persona → Compromiso → Confirmación**
