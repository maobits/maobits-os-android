# Maobits OS Android — Hallazgos de auditoría inicial 0.8

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento registra los primeros hallazgos técnicos obtenidos durante la auditoría inicial del repositorio Android usado como punto de partida para **Maobits OS Android**.

Su objetivo es convertir la evidencia de terminal en decisiones arquitectónicas ordenadas, sin modificar aún código funcional.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Estado Git observado

La auditoría fue ejecutada sobre la rama:

```text
foundation/00-maobits-os-android-baseline
```

Se observaron archivos de evidencia `AUDIT-*` pendientes de seguimiento antes de ser organizados dentro de `docs/05-audit/evidence`.

---

## 4. Módulos Android detectados

La estructura Gradle confirma al menos dos módulos principales:

| Módulo | Archivo Gradle | Propósito inicial |
|---|---|---|
| `app` | `./app/build.gradle.kts` | Aplicación Android principal |
| `wear` | `./wear/build.gradle.kts` | Aplicación o componente Wear OS |

Decisión arquitectónica inicial:

- Maobits OS Android debe tratar el módulo `app` como experiencia móvil principal.
- El módulo `wear` debe auditarse como capacidad independiente, no eliminarse ni renombrarse todavía.
- Cualquier personalización debe conservar compilación separada para `app` y `wear`.

---

## 5. Identidad Android actual detectada

| Elemento | Valor actual | Riesgo | Decisión futura |
|---|---|---|---|
| App namespace | `com.bitchat.android` | Alto por marca y acoplamiento técnico | Migrar en fase controlada |
| App applicationId | `com.bitchat.droid` | Alto por identidad pública de instalación | Cambiar solo después de baseline reproducible |
| App versionCode | `36` | Medio | Definir versionado propio Maobits |
| App versionName | `1.7.5` | Medio | Reiniciar versión propia con trazabilidad |
| Wear namespace | `com.bitchat.watch` | Alto por marca | Migrar en fase controlada |
| Wear applicationId | `com.bitchat.watch` | Alto por identidad pública | Cambiar con plan de Wear OS |
| Wear versionCode | `1` | Bajo | Mantener hasta definir release propio |
| Wear versionName | `0.1.0` | Bajo | Mantener hasta baseline |

---

## 6. Decisión de marca

No se debe cambiar de inmediato el namespace, applicationId ni permisos personalizados sin validar compilación, pruebas y referencias internas.

La ruta correcta será:

1. auditar referencias actuales;
2. compilar baseline sin cambios;
3. crear pruebas mínimas;
4. cambiar branding visual primero;
5. cambiar `applicationId`;
6. cambiar `namespace`;
7. migrar paquetes Kotlin;
8. actualizar permisos personalizados;
9. validar instalación limpia;
10. validar upgrade/migración si aplica.

---

## 7. Permisos Android detectados

La app principal declara permisos de:

- internet y estado de red;
- cambio de estado de red;
- Bluetooth clásico y Bluetooth moderno;
- Bluetooth advertise, connect y scan;
- ubicación aproximada, precisa y en segundo plano;
- notificaciones;
- Wi-Fi state/change;
- red local;
- wake lock;
- permiso personalizado de finalización forzada;
- foreground service;
- foreground service connected device;
- foreground service data sync;
- foreground service location;
- recepción de boot completed;
- micrófono;
- cámara;
- lectura de almacenamiento externo;
- lectura de imágenes, video y audio;
- vibración;
- solicitud para ignorar optimizaciones de batería.

El módulo Wear declara permisos relacionados con:

- Bluetooth;
- foreground service;
- connected device;
- notificaciones;
- micrófono;
- vibración.

---

## 8. Riesgo de permisos sensibles

| Permiso o grupo | Nivel | Justificación | Mitigación Maobits OS |
|---|---|---|---|
| `ACCESS_BACKGROUND_LOCATION` | Crítico | Puede generar preocupación de privacidad y revisión estricta | Justificación clara, uso mínimo, pantalla educativa y opción de desactivar |
| `RECORD_AUDIO` | Alto | Riesgo de percepción de vigilancia | Solicitud contextual, explicación visible, no activar sin acción clara |
| `CAMERA` | Alto | Riesgo de privacidad y confianza | Uso solo para QR, evidencia o funciones explícitas |
| `READ_MEDIA_*` | Alto | Acceso a contenido personal | Usar selectores modernos y limitar acceso cuando sea posible |
| `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` | Alto | Puede ser visto como invasivo | Explicar continuidad de conectividad y permitir no aceptar |
| `BLUETOOTH_SCAN` + ubicación | Alto | Exposición de proximidad y metadatos | No prometer anonimato absoluto; controles de visibilidad |
| `FOREGROUND_SERVICE_LOCATION` | Alto | Asociación con rastreo | Justificar por conectividad y proximidad; monitorear uso |
| `RECEIVE_BOOT_COMPLETED` | Medio | Inicio automático puede ser sensible | Consentimiento y configuración visible |
| Permiso personalizado `com.bitchat.android.permission.FORCE_FINISH` | Alto | Contiene marca externa y debe migrarse | Cambiar en fase controlada a permiso Maobits OS |

---

## 9. Componentes Android detectados

La evidencia muestra:

| Tipo | App | Wear | Observación |
|---|---:|---:|---|
| Services | 3 | 1 | Requieren identificación exacta por nombre |
| Activities | 3 | 1 | Requieren mapeo de navegación y entrada principal |
| Receivers | 2 main + 1 debug | 1 debug | Requieren revisión de arranque, debug y seguridad |
| Providers | 1 | 0 | Requiere revisión de exposición, autoridades y archivos compartidos |

---

## 10. Riesgos arquitectónicos iniciales

| Riesgo | Impacto | Acción requerida |
|---|---|---|
| El código aún usa identidad técnica externa | Riesgo de marca y distribución | Migración planificada |
| Hay permisos altamente sensibles | Riesgo de confianza, privacidad y revisión de tienda | Gobernanza de permisos |
| Hay servicios foreground | Riesgo de consumo, política y experiencia | Baseline de comportamiento |
| Hay Wear OS | Incrementa alcance técnico | Tratar como subproducto controlado |
| No se recibieron aún archivos fuente listados | Falta mapa real de paquetes Kotlin/Java | Ejecutar auditoría profunda |
| La conectividad es crítica | Cualquier cambio puede romper el valor base | Compilar antes de modificar |

---

## 11. Próximo paso obligatorio

Antes de modificar código, se debe generar una auditoría profunda de archivos fuente, clases, paquetes y componentes reales.

Evidencia requerida:

```text
AUDIT-SOURCE-FILES-DEEP.txt
KOTLIN-PACKAGE-INVENTORY.txt
KOTLIN-CLASS-INVENTORY.txt
COMMUNICATION-SECURITY-INVENTORY.txt
APP-MAIN-MANIFEST-NUMBERED.txt
WEAR-MAIN-MANIFEST-NUMBERED.txt
```

---

## 12. Criterio de avance

No se debe pasar a personalización visual, cambio de paquete, cambio de applicationId o refactor hasta que:

- el baseline compile;
- la estructura Kotlin/Java esté mapeada;
- los servicios estén identificados;
- los permisos estén justificados;
- la licencia Android esté registrada;
- exista plan de migración de marca;
- exista commit documental de auditoría.

---

## 13. Declaración final

La auditoría confirma que Maobits OS Android debe avanzar con disciplina: primero entender, luego compilar, después documentar, y finalmente personalizar.

**Persona → Compromiso → Confirmación**
