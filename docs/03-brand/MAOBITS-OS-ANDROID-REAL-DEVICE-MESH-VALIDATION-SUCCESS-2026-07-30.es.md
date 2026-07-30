# Maobits OS Android — Validación real exitosa de descubrimiento mesh en dos smartphones

**Versión:** 0.1.0  
**Fecha:** 2026-07-30  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  


## 1. Propósito

Este documento registra una prueba real exitosa de Maobits OS Android instalada en dos smartphones físicos.

La prueba confirma que la aplicación inicia correctamente, entra al canal por defecto y permite descubrimiento/comunicación entre dispositivos cuando las condiciones del dispositivo son adecuadas.

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

## 3. Contexto de la prueba

Durante la primera ejecución, los dos teléfonos entraron al canal por defecto, pero no se reconocieron entre sí.

La causa encontrada fue:

```text
Nivel de batería muy bajo.
```

Después de corregir esa condición, la prueba fue repetida y el usuario confirmó:

```text
Probé y funciona correcto.
```

## 4. Resultado

```text
Estado: Exitoso
Dispositivos: Dos smartphones reales
Aplicación visible: Maobits OS
Paquete interno actual: com.bitchat.droid
Canal: canal por defecto
Descubrimiento entre dispositivos: correcto
Comunicación básica: correcta
Cambio de código requerido: no
```

## 5. Interpretación técnica

La prueba demuestra que el runtime actual de Maobits OS Android puede operar correctamente en dispositivos reales.

El fallo inicial no fue necesariamente un bug del código, sino una condición operativa del sistema Android. En estados de batería muy baja, Android puede restringir escaneo BLE, advertising BLE, servicios en segundo plano, foreground services, Nearby Devices y tareas de conectividad.

## 6. Regla agregada para pruebas reales

Antes de probar conectividad mesh en teléfonos físicos:

```text
Batería mínima recomendada: 30%
Ahorro de batería: desactivado
Bluetooth: activado
Ubicación: activada
Permiso Nearby Devices: permitido
Permiso ubicación: permitido si aplica
Uso de batería de la app: sin restricciones
Pantalla: encendida durante el inicio de la prueba
Distancia entre dispositivos: corta durante descubrimiento inicial
```

## 7. Criterios confirmados manualmente

| Criterio | Estado |
|---|---|
| App instalada en teléfono real | Cumplido |
| App instalada en segundo teléfono real | Cumplido |
| App abre correctamente | Cumplido |
| Ambos teléfonos entran al canal por defecto | Cumplido |
| Descubrimiento funciona al corregir batería | Cumplido |
| Comunicación básica funciona | Cumplido |
| No se requiere cambio de código por este hallazgo | Cumplido |

## 8. Evidencia recomendada en repositorio

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

## 9. Commit recomendado

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

git status

git add docs/03-brand/MAOBITS-OS-ANDROID-REAL-DEVICE-MESH-VALIDATION-SUCCESS-2026-07-30.es.md \
        docs/03-brand/MAOBITS-OS-ANDROID-REAL-DEVICE-MESH-VALIDATION-SUCCESS-2026-07-30.en.md \
        docs/03-brand/evidence/2026-07-30-real-device-mesh-validation-success

git commit -m "test(android): record successful real device mesh validation"
```

## 10. Próxima decisión

Con esta prueba real aprobada, el proyecto puede avanzar con más confianza hacia:

```text
Fase 1.1.7 — Generación controlada de assets visuales Maobits OS
```

La app ya fue verificada en hardware real antes de iniciar cambios visuales más profundos.

## 11. Declaración final

La primera validación funcional en dos smartphones reales fue exitosa. Este resultado confirma que la base actual funciona fuera del entorno de compilación y puede sostener pruebas reales de comunicación.

**Persona → Compromiso → Confirmación**
