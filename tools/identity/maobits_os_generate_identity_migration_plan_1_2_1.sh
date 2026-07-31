\
#!/usr/bin/env bash
#
# Project: Maobits OS Android
# Module: identity-tools
# File: maobits_os_generate_identity_migration_plan_1_2_1.sh
# Purpose: Generate a technical identity migration decision matrix from the 1.2.0 audit evidence.
#
# Company: Maobits
# Lead developer: Mauricio Chara Hurtado
# Technical contact: os@maobits.com
# Product principle: Person -> Commitment -> Confirmation
#
# Quality standard:
# - Production-grade structure.
# - Clear separation of responsibilities.
# - Auditable behavior and explicit failure paths.
# - Maintainable implementation with meaningful technical comments.
#
# Legal and attribution note:
# - Preserve original third-party license notices when applicable.
# - Do not mix Maobits OS branding with external project branding.

set -Eeuo pipefail

AUDIT_DIR="${1:-docs/04-identity/evidence/2026-07-30-technical-identity-audit}"
PLAN_DIR="${2:-docs/04-identity/evidence/2026-07-30-technical-identity-migration-plan}"
TARGET_MAP="${3:-docs/04-identity/MAOBITS-OS-ANDROID-TECHNICAL-IDENTITY-TARGET-MAP-1.2.1.json}"

mkdir -p "$PLAN_DIR"

if [[ ! -d "$AUDIT_DIR" ]]; then
  echo "ERROR: audit directory not found: $AUDIT_DIR"
  echo "Run phase 1.2.0 first."
  exit 2
fi

if [[ ! -f "$TARGET_MAP" ]]; then
  echo "ERROR: target map not found: $TARGET_MAP"
  echo "Copy the 1.2.1 target map into docs/04-identity first."
  exit 2
fi

write_section() {
  local title="$1"
  printf '\n=== %s ===\n' "$title"
}

count_matches() {
  local pattern="$1"
  local file="$2"
  if [[ -f "$file" ]]; then
    grep -E "$pattern" "$file" | wc -l | tr -d ' '
  else
    echo "0"
  fi
}

GRADLE_COUNT="$(count_matches 'applicationId|namespace|rootProject.name' "$AUDIT_DIR/01-GRADLE-TECHNICAL-IDENTITY.txt")"
MANIFEST_COUNT="$(count_matches 'com\.bitchat|bitchat|permission|authorities|scheme|provider|activity|service|receiver' "$AUDIT_DIR/02-MANIFEST-TECHNICAL-IDENTITY.txt")"
DEEPLINK_COUNT="$(count_matches 'bitchat://|android:scheme|deepLink|ACTION_VIEW|CATEGORY_BROWSABLE' "$AUDIT_DIR/03-DEEP-LINKS-AND-SCHEMES.txt")"
FILEPROVIDER_COUNT="$(count_matches 'FileProvider|fileprovider|authorities|paths.xml' "$AUDIT_DIR/04-FILEPROVIDER-AND-AUTHORITIES.txt")"
PERMISSION_COUNT="$(count_matches 'permission|FORCE_FINISH|com\.bitchat' "$AUDIT_DIR/05-CUSTOM-PERMISSIONS.txt")"
PACKAGE_COUNT="$(count_matches '^.*:package |^.*:import com\.bitchat|^.*:import com\.maobits' "$AUDIT_DIR/06-KOTLIN-JAVA-PACKAGES-AND-IMPORTS.txt")"
CODE_COUNT="$(count_matches 'com\.bitchat|bitchat|BitChat|Bitchat' "$AUDIT_DIR/07-CODE-TECHNICAL-IDENTITY-REFERENCES.txt")"
RESOURCE_COUNT="$(count_matches 'bitchat|BitChat|Bitchat|maobits|Maobits|app_name|provider|scheme' "$AUDIT_DIR/08-RESOURCE-TECHNICAL-IDENTITY-REFERENCES.txt")"
TEST_COUNT="$(count_matches 'com\.bitchat|bitchat|applicationId|namespace|scheme|authority' "$AUDIT_DIR/09-TEST-DEBUG-TECHNICAL-IDENTITY-REFERENCES.txt")"

cat > "$PLAN_DIR/TECHNICAL-IDENTITY-MIGRATION-DECISION-MATRIX.md" <<EOF
# Maobits OS Android — Technical Identity Migration Decision Matrix 1.2.1

Generated at: $(date -Iseconds)

## Source audit

\`\`\`text
$AUDIT_DIR
\`\`\`

## Target map

\`\`\`text
$TARGET_MAP
\`\`\`

## Audit counts

| Area | Count |
|---|---:|
| Gradle identity references | $GRADLE_COUNT |
| Manifest identity references | $MANIFEST_COUNT |
| Deep link / scheme references | $DEEPLINK_COUNT |
| FileProvider / authorities references | $FILEPROVIDER_COUNT |
| Custom permission references | $PERMISSION_COUNT |
| Kotlin/Java package/import references | $PACKAGE_COUNT |
| Code technical identity references | $CODE_COUNT |
| Resource identity references | $RESOURCE_COUNT |
| Test/debug identity references | $TEST_COUNT |

## Recommended migration order

1. Freeze current visual brand state and verify main branch.
2. Decide installation strategy: clean install or migration from old applicationId.
3. Update Gradle \`applicationId\` and \`namespace\` in a dedicated phase.
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
EOF

cat > "$PLAN_DIR/TECHNICAL-IDENTITY-MIGRATION-RISK-REGISTER.md" <<EOF
# Maobits OS Android — Technical Identity Migration Risk Register 1.2.1

Generated at: $(date -Iseconds)

| Risk | Impact | Control |
|---|---|---|
| Changing applicationId creates a different Android app | Existing install/data may not migrate | Decide clean install vs migration before implementation |
| Changing namespace affects generated R/BuildConfig | Compile failures | Apply in a dedicated branch and validate build |
| Changing Kotlin package declarations affects imports | Compile failures and hidden references | Use IDE/refactor or scripted staged migration with tests |
| Changing custom permissions may break receivers/services | Runtime access failure | Update definitions and consumers together |
| Changing FileProvider authority may break shared URIs | Share/open flows fail | Keep \${applicationId}.fileprovider or document explicit authority |
| Changing deep-link scheme may break external links | Legacy links stop working | Support legacy scheme during transition if needed |
| Wear identity mismatch | Mobile/Wear pairing issues | Validate mobile and wear together |
| Attribution removal by mistake | Legal/compliance risk | Preserve original license and attribution sections |
| Mass replacement corrupts unrelated content | Unbounded defects | Prohibit mass replacement |
EOF

{
  write_section "MAOBITS OS ANDROID - TECHNICAL IDENTITY MIGRATION PLAN 1.2.1"
  echo "Generated at: $(date -Iseconds)"
  write_section "CURRENT BRANCH"
  git branch --show-current
  write_section "CURRENT COMMIT"
  git log --oneline --decorate -1
  write_section "AUDIT DIRECTORY"
  echo "$AUDIT_DIR"
  write_section "PLAN DIRECTORY"
  echo "$PLAN_DIR"
  write_section "TARGET MAP"
  cat "$TARGET_MAP"
  write_section "GENERATED PLAN FILES"
  find "$PLAN_DIR" -type f | sort
} > "$PLAN_DIR/TECHNICAL-IDENTITY-MIGRATION-PLAN-SUMMARY.txt"

sha256sum "$PLAN_DIR"/* > "$PLAN_DIR/TECHNICAL-IDENTITY-MIGRATION-PLAN-SHA256.txt" || true

cat "$PLAN_DIR/TECHNICAL-IDENTITY-MIGRATION-PLAN-SUMMARY.txt"
