# Maobits OS Android — Clasificación filtrada de marca visible e identidad pública 1.1.2

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Hora de evidencia:** 21:42:39-05:00  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento registra la **Fase 1.1.2 — Clasificación filtrada de identidad pública y marca visible**.

La fase toma la evidencia generada durante el inventario de marca 1.1 y la organiza en grupos de decisión para evitar cambios masivos, preservar atribución legal, mantener conectividad y preparar la primera personalización segura de Maobits OS Android.

---

## 2. Espacio de trabajo oficial

```text
/home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android
```

---

## 3. Rama auditada

```text
brand/1.1-inventory
```

---

## 4. Resumen filtrado recibido

```text
GRADLE-PUBLIC-IDENTITY-REVIEW.txt: 5
MANIFEST-BRAND-REVIEW.txt: 8
VISIBLE-TEXT-PRIORITY-REVIEW.txt: 3992
NOTIFICATION-UX-PRIORITY-REVIEW.txt: 4048
PACKAGE-MIGRATION-RISK-REVIEW.txt: 1973
BRAND-REPLACEMENT-CANDIDATES.txt: 9681
BRAND-PRESERVE-AS-ATTRIBUTION.txt: 81042
```

---

## 5. Interpretación estratégica

Los conteos confirman que el repositorio todavía tiene una identidad heredada profunda, pero no todas las referencias tienen el mismo tipo de riesgo ni el mismo momento de reemplazo.

El proyecto debe separar cuatro grupos:

| Grupo | Descripción | Acción |
|---|---|---|
| Identidad pública Android | `applicationId`, `namespace`, labels, authorities, permisos personalizados | Revisar primero, cambiar en fase controlada |
| Marca visible al usuario | `app_name`, textos UI, notificaciones, onboarding | Primer candidato de personalización segura |
| Identidad técnica interna | paquetes, imports, clases, módulos | No tocar hasta fase de migración técnica |
| Atribución legal y trazabilidad | README, LICENSE, docs, referencias de fuente técnica | Conservar, separar y documentar |

---

## 6. Decisión principal

No se debe reemplazar todo ahora.

La primera personalización segura debe enfocarse en:

1. nombre visible de la aplicación;
2. textos visibles directos;
3. notificaciones visibles;
4. documentación propia de Maobits OS;
5. inventario visual de iconos y recursos.

Deben esperar:

1. `applicationId`;
2. `namespace`;
3. paquetes Kotlin;
4. imports `com.bitchat`;
5. providers y authorities;
6. permiso personalizado `FORCE_FINISH`;
7. cambios de conectividad.

---

## 7. Archivos de mayor prioridad para inspección manual

La siguiente inspección manual debe comenzar con:

```text
GRADLE-PUBLIC-IDENTITY-REVIEW.txt
MANIFEST-BRAND-REVIEW.txt
BRAND-REPLACEMENT-CANDIDATES.txt
```

Luego continuar con:

```text
VISIBLE-TEXT-PRIORITY-REVIEW.txt
NOTIFICATION-UX-PRIORITY-REVIEW.txt
PACKAGE-MIGRATION-RISK-REVIEW.txt
BRAND-PRESERVE-AS-ATTRIBUTION.txt
```

---

## 8. Reglas de preservación

Las referencias legales, créditos, licencias, historial, evidencia de auditoría y menciones de fuente técnica no deben eliminarse.

Deben conservarse cuando aparecen en:

- `LICENSE.md`;
- archivos de licencia;
- créditos;
- documentación de atribución;
- auditorías;
- roadmap;
- documentos donde se explique la fuente técnica;
- trazabilidad del fork;
- notas de cumplimiento.

---

## 9. Reglas de reemplazo futuro

Las referencias pueden reemplazarse cuando aparecen en:

- `app_name`;
- labels visibles;
- textos de pantalla;
- notificaciones visibles;
- onboarding;
- descripción de aplicación;
- textos de permisos para usuario;
- recursos visuales propios;
- documentación institucional propia de Maobits OS.

---

## 10. Reglas de espera técnica

Las referencias deben esperar cuando pertenecen a:

- paquetes Kotlin;
- imports;
- namespace;
- applicationId;
- authorities;
- permisos personalizados;
- servicios foreground;
- receivers;
- providers;
- lógica BLE;
- lógica Wi-Fi Aware;
- lógica Nostr;
- cifrado;
- llaves;
- store-and-forward.

---

## 11. Comandos de inspección recomendados

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

printf '\n=== GRADLE PUBLIC IDENTITY REVIEW ===\n'
cat "$BRAND_AUDIT_DIR/GRADLE-PUBLIC-IDENTITY-REVIEW.txt"

printf '\n=== MANIFEST BRAND REVIEW ===\n'
cat "$BRAND_AUDIT_DIR/MANIFEST-BRAND-REVIEW.txt"

printf '\n=== BRAND REPLACEMENT CANDIDATES SAMPLE ===\n'
head -220 "$BRAND_AUDIT_DIR/BRAND-REPLACEMENT-CANDIDATES.txt"

printf '\n=== VISIBLE TEXT PRIORITY SAMPLE ===\n'
head -220 "$BRAND_AUDIT_DIR/VISIBLE-TEXT-PRIORITY-REVIEW.txt"

printf '\n=== NOTIFICATION UX PRIORITY SAMPLE ===\n'
head -220 "$BRAND_AUDIT_DIR/NOTIFICATION-UX-PRIORITY-REVIEW.txt"
```

---

## 12. Comandos para crear resúmenes por archivo

```bash
cd /home/maobits/Documentos/ingenieria/proyectos/maobits-os/05-maobits-os-source/05.1-maobits-os-source-android

BRAND_AUDIT_DIR="docs/03-brand/evidence/2026-07-29-brand-inventory"

for file in \
  BRAND-REPLACEMENT-CANDIDATES.txt \
  VISIBLE-TEXT-PRIORITY-REVIEW.txt \
  NOTIFICATION-UX-PRIORITY-REVIEW.txt \
  PACKAGE-MIGRATION-RISK-REVIEW.txt \
  BRAND-PRESERVE-AS-ATTRIBUTION.txt
do
  echo "=== $file ==="
  awk -F: '/^[^:]+:[0-9]+:/ {count[$1]++} END {for (path in count) print count[path], path}' "$BRAND_AUDIT_DIR/$file" \
    | sort -nr \
    | head -40
  echo
done > "$BRAND_AUDIT_DIR/FILTERED-CLASSIFICATION-BY-FILE.txt"

cat "$BRAND_AUDIT_DIR/FILTERED-CLASSIFICATION-BY-FILE.txt"
```

---

## 13. Criterios de aceptación de 1.1.2

La subfase 1.1.2 queda completa cuando:

- se generó el resumen filtrado;
- se documentó la magnitud de cada grupo;
- se separaron referencias reemplazables, preservables y pendientes;
- se inspeccionaron Gradle y Manifest;
- se generó resumen por archivo;
- no se modificó código funcional;
- se preparó la fase 1.1.3 de plan de reemplazo seguro.

---

## 14. Próxima fase

```text
Fase 1.1.3 — Plan de reemplazo seguro de marca visible
```

La siguiente fase debe definir el primer paquete de cambios permitido:

- `app_name`;
- textos visibles estrictamente necesarios;
- notificaciones visibles;
- recursos visuales si están claramente identificados;
- sin tocar paquetes, namespace ni applicationId.

---

## 15. Declaración final

Maobits OS Android debe crear identidad propia sin borrar atribución, sin romper conectividad y sin ocultar el origen técnico auditado.

**Persona → Compromiso → Confirmación**
