# Maobits OS Android — Hallazgos del inventario de marca 1.1.1

**Versión:** 0.1.0  
**Fecha:** 2026-07-29  
**Hora de evidencia:** 20:37:30-06:00  
**Proyecto:** Maobits OS Android  
**Empresa:** Maobits  
**Dirección conceptual y desarrollador principal:** Mauricio Chara Hurtado  
**Email técnico:** os@maobits.com  
**Principio de producto:** Persona → Compromiso → Confirmación  

---

## 1. Propósito

Este documento registra los primeros hallazgos de la **Fase 1.1 — Inventario de marca, recursos visuales y textos visibles**.

La evidencia confirma que el repositorio contiene una cantidad significativa de referencias heredadas de la fuente técnica de referencia. Esto es esperado porque el proyecto todavía se encuentra en fase de auditoría y no se ha iniciado la personalización funcional.

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

Commit observado:

```text
c51559a chore(repo): merge audited Maobits OS Android baseline into main
```

---

## 4. Resumen de conteos

```text
DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt: 30600
GRADLE-PUBLIC-IDENTITY.txt: 5
MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt: 8
NOTIFICATION-AND-FOREGROUND-UX.txt: 4102
PACKAGE-AND-CODE-REFERENCES.txt: 3539
VISIBLE-TEXT-AND-STRING-MATCHES.txt: 13405
VISUAL-RESOURCES-INVENTORY.txt: 0
```

---

## 5. Interpretación general

| Archivo | Conteo | Interpretación |
|---|---:|---|
| `DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt` | 30600 | Muy alto. Incluye documentación, herramientas, evidencia previa y referencias técnicas. Requiere filtrado para separar licencias, créditos, docs propios y fuente técnica. |
| `VISIBLE-TEXT-AND-STRING-MATCHES.txt` | 13405 | Alto. Puede incluir textos visibles, nombres técnicos y muchas coincidencias genéricas como `chat`, `mesh`, `peer`, `message`. Requiere depuración por prioridad. |
| `NOTIFICATION-AND-FOREGROUND-UX.txt` | 4102 | Alto. Debe revisarse con cuidado porque afecta experiencia visible, servicios foreground y permisos sensibles. |
| `PACKAGE-AND-CODE-REFERENCES.txt` | 3539 | Alto, pero esperado. El namespace y paquetes todavía usan identidad técnica heredada. No cambiar todavía. |
| `MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt` | 8 | Bajo y prioritario. Debe revisarse primero porque afecta identidad pública, permisos, providers y seguridad. |
| `GRADLE-PUBLIC-IDENTITY.txt` | 5 | Bajo y crítico. Aquí viven `applicationId`, `namespace` y versiones. |
| `VISUAL-RESOURCES-INVENTORY.txt` | 0 | El conteo de marca no encontró coincidencias textuales, pero aún deben revisarse iconos e imágenes manualmente. |

---

## 6. Decisión técnica

No se debe reemplazar todo de forma masiva.

El conteo alto no significa que todo deba cambiarse inmediatamente. Muchas coincidencias pueden ser:

- referencias legales que deben conservarse;
- documentación histórica que debe mantenerse;
- paquetes técnicos que se migrarán en fase posterior;
- términos funcionales válidos como `chat`, `mesh`, `peer`, `message`;
- evidencia de auditoría que no debe reescribirse;
- referencias a protocolos que pueden conservarse técnicamente.

La personalización debe ser gradual, verificable y reversible.

---

## 7. Prioridad de clasificación

La clasificación debe avanzar en este orden:

1. `GRADLE-PUBLIC-IDENTITY.txt`
2. `MANIFEST-LABELS-AUTHORITIES-PERMISSIONS.txt`
3. `VISIBLE-TEXT-AND-STRING-MATCHES.txt`
4. `NOTIFICATION-AND-FOREGROUND-UX.txt`
5. `VISUAL-RESOURCES-INVENTORY.txt`
6. `DOCUMENTATION-AND-TOOLING-BRAND-REFERENCES.txt`
7. `PACKAGE-AND-CODE-REFERENCES.txt`

La razón es que primero se deben entender los puntos de identidad pública y experiencia visible antes de tocar paquetes internos.

---

## 8. Acciones inmediatas

La siguiente actividad debe generar archivos filtrados de revisión:

```text
GRADLE-PUBLIC-IDENTITY-REVIEW.txt
MANIFEST-BRAND-REVIEW.txt
VISIBLE-TEXT-PRIORITY-REVIEW.txt
NOTIFICATION-UX-PRIORITY-REVIEW.txt
PACKAGE-MIGRATION-RISK-REVIEW.txt
BRAND-REPLACEMENT-CANDIDATES.txt
BRAND-PRESERVE-AS-ATTRIBUTION.txt
```

---

## 9. Regla de seguridad

No ejecutar todavía reemplazos automáticos como:

```bash
sed -i 's/bitchat/maobits/g'
```

Ese tipo de cambio podría romper:

- paquetes Kotlin;
- permisos personalizados;
- providers;
- imports;
- authorities;
- documentación legal;
- atribución de fuente;
- build Gradle;
- compatibilidad interna;
- conectividad.

---

## 10. Criterios de aceptación de esta subfase

La subfase 1.1.1 queda completa cuando:

- se registran los conteos del inventario;
- se clasifica la magnitud de referencias;
- se define el orden de revisión;
- se evita reemplazo masivo;
- se preparan archivos filtrados para decisión;
- no se modifica código funcional.

---

## 11. Próxima subfase

```text
Fase 1.1.2 — Clasificación filtrada de identidad pública y marca visible
```

Esa subfase determinará qué referencias se reemplazan, cuáles se conservan como atribución y cuáles deben esperar a la migración técnica de paquetes.

---

## 12. Declaración final

Maobits OS Android debe construir su identidad propia sin borrar la memoria técnica ni romper la base funcional.

**Persona → Compromiso → Confirmación**
