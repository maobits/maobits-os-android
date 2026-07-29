# Maobits OS Android — Auditoría inicial del repositorio

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento registra la auditoría inicial del repositorio Android usado como punto de partida para construir **Maobits OS Android**.

El objetivo de esta auditoría es comprender el estado real del código antes de modificarlo, separar marca propia de fuente técnica externa, identificar riesgos, reconocer licencias, mapear módulos críticos y preparar una ruta de personalización profesional desde 0%.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Repositorio de referencia técnica

```text
https://github.com/maobits/bitchat-android
```

Este repositorio se usa como punto de partida técnico y debe conservarse con trazabilidad clara. La marca principal del producto será **Maobits OS Android**.

La fuente técnica externa solo debe mencionarse en créditos, licencias, auditoría de origen, trazabilidad técnica y análisis de arquitectura base.

---

## 4. Comandos de auditoría inicial

Ejecutar desde el espacio de trabajo oficial:

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

## 5. Datos mínimos que deben capturarse

| Área | Información requerida | Estado |
|---|---|---|
| Git | Rama actual, remotos, último commit, estado limpio | Pendiente |
| Gradle | Versión, módulos, plugins, configuración principal | Pendiente |
| Android | namespace, applicationId, minSdk, targetSdk | Pendiente |
| Manifest | permisos, servicios, receivers, activities | Pendiente |
| Código Kotlin/Java | paquetes, servicios, ViewModels, repositorios, transportes | Pendiente |
| Comunicación | BLE, Wi-Fi Aware, Nostr, router, relay, store-and-forward | Pendiente |
| Seguridad | llaves, cifrado, almacenamiento, borrado, permisos sensibles | Pendiente |
| Persistencia | preferencias, archivos, base local, caché, outbox | Pendiente |
| UI | pantallas, navegación, tema, branding, cadenas de texto | Pendiente |
| Legal | licencias, avisos, README, dependencias | Pendiente |
| Riesgos | acoplamiento, marca externa, GPL, privacidad, abuso | Pendiente |

---

## 6. Criterios de aceptación

La auditoría inicial se considera completa cuando:

- el estado de Git fue revisado;
- se identificaron remotos y rama activa;
- se capturó la estructura del proyecto;
- se identificaron archivos Gradle y Manifest;
- se identificaron archivos Kotlin/Java principales;
- se identificaron archivos legales y README;
- se generaron archivos `AUDIT-*`;
- se revisaron permisos Android;
- se mapearon módulos críticos;
- se definió el primer plan de personalización;
- no se modificó código funcional sin entender su impacto.

---

## 7. Riesgos iniciales

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Cambiar marca sin auditoría | Romper recursos, strings, permisos o package references | Inventario previo |
| Cambiar applicationId sin plan | Fallos de build o conflicto de instalación | Fase controlada |
| Tocar conectividad antes de entenderla | Pérdida de funcionalidad base | Pruebas antes/después |
| Ignorar licencias | Riesgo legal y comercial | Auditoría legal explícita |
| Mezclar marca externa con Maobits OS | Riesgo de marca y comunicación | Separación documental |
| Optimizar sin pruebas | Regresiones silenciosas | Baseline técnico y pruebas |

---

## 8. Próxima fase

Después de esta auditoría, la siguiente fase será:

```text
Fase 0.9 — Baseline técnico reproducible
```

Esa fase validará compilación, entorno Android, Gradle, dependencias, pruebas y primer reporte técnico antes de iniciar cambios de personalización.

---

## 9. Declaración final

Esta auditoría protege el proyecto contra modificaciones improvisadas.

Maobits OS Android debe iniciar con claridad, trazabilidad, respeto legal, excelencia técnica y alineación cultural.

**Persona → Compromiso → Confirmación**
