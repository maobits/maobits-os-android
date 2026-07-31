# Maobits OS Android — Technical Identity Migration Decision Matrix 1.2.1

Generated at: 2026-07-30T20:25:58-05:00

## Source audit

```text
docs/04-identity/evidence/2026-07-30-technical-identity-audit
```

## Target map

```text
docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-TARGET-MAP-1.2.1.json
```

## Audit counts

| Area | Count |
|---|---:|
| Gradle identity references | 5 |
| Manifest identity references | 81 |
| Deep link / scheme references | 53 |
| FileProvider / authorities references | 151 |
| Custom permission references | 1732 |
| Kotlin/Java package/import references | 1379 |
| Code technical identity references | 197758 |
| Resource identity references | 800 |
| Test/debug identity references | 515 |

## Recommended migration order

1. Freeze current visual brand state and verify main branch.
2. Decide installation strategy: clean install or migration from old applicationId.
3. Update Gradle `applicationId` and `namespace` in a dedicated phase.
4. Update manifest custom permissions and providers in the same controlled phase as applicationId.
5. Update deep-link strategy, preferably supporting legacy scheme during transition.
6. Refactor Kotlin package declarations only after Gradle/Manifest decisions are stable.
7. Update tests/debug references.
8. Run app build, wear build, tests, lint, and real-device install.
9. Document rollback and tag the migration.

## Explicit non-goals

- No mass replacement.
- No blind package refactor.
- No removal of attribution/license materials.
- No deep-link removal without transition decision.
- No migration without rollback instructions.

## Proposed target identity

See the JSON target map in the repository for the authoritative proposal.

## Closure requirement

This plan is accepted only when the target identifiers and migration strategy are explicitly approved.
