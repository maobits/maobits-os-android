\
#!/usr/bin/env bash
#
# Project: Maobits OS Android
# Module: identity-tools
# File: maobits_os_collect_technical_identity_audit_1_2_0.sh
# Purpose: Collect technical identity audit evidence before package/applicationId/deep-link migration.
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

EVIDENCE_DIR="${1:-docs/04-identity/evidence/2026-07-30-technical-identity-audit}"
mkdir -p "$EVIDENCE_DIR"

write_section() {
  local title="$1"
  printf '\n=== %s ===\n' "$title"
}

{
  write_section "MAOBITS OS ANDROID - TECHNICAL IDENTITY AUDIT 1.2.0"
  echo "Generated at: $(date -Iseconds)"
  write_section "CURRENT BRANCH"
  git branch --show-current
  write_section "CURRENT COMMIT"
  git log --oneline --decorate -1
  write_section "REMOTE CONFIGURATION"
  git remote -v
  write_section "WORKTREE STATUS"
  git status --short
} > "$EVIDENCE_DIR/00-REPOSITORY-STATE.txt"

{
  write_section "GRADLE TECHNICAL IDENTITY"
  grep -RIn --include='*.gradle' --include='*.gradle.kts' --include='settings.gradle.kts' \
    -E 'rootProject.name|namespace\s*=|applicationId\s*=|versionCode|versionName|group\s*=|artifactId' . \
    --exclude-dir=.git --exclude-dir=build --exclude-dir=.gradle || true
} > "$EVIDENCE_DIR/01-GRADLE-TECHNICAL-IDENTITY.txt"

{
  write_section "MANIFEST TECHNICAL IDENTITY"
  grep -RIn --include='AndroidManifest.xml' \
    -E 'package=|android:name=|android:authorities=|android:scheme=|android:host=|android:path|android:permission=|uses-permission|permission android:name|provider|activity|service|receiver|intent-filter|data android:' \
    app/src/main wear/src/main app/src/debug wear/src/debug 2>/dev/null || true
} > "$EVIDENCE_DIR/02-MANIFEST-TECHNICAL-IDENTITY.txt"

{
  write_section "DEEP LINKS AND URL SCHEMES"
  grep -RIn --exclude-dir=build --exclude-dir=.git \
    -E 'android:scheme=|android:host=|android:path|bitchat://|maobits://|IntentFilter|NavDeepLink|deepLink|deeplink|ACTION_VIEW|CATEGORY_BROWSABLE|CATEGORY_DEFAULT' \
    app wear . 2>/dev/null || true
} > "$EVIDENCE_DIR/03-DEEP-LINKS-AND-SCHEMES.txt"

{
  write_section "FILEPROVIDER AND AUTHORITIES"
  grep -RIn --exclude-dir=build --exclude-dir=.git \
    -E 'FileProvider|fileprovider|android:authorities=|provider_paths|paths.xml|external-path|cache-path|files-path|root-path' \
    app wear . 2>/dev/null || true
} > "$EVIDENCE_DIR/04-FILEPROVIDER-AND-AUTHORITIES.txt"

{
  write_section "CUSTOM PERMISSIONS"
  grep -RIn --exclude-dir=build --exclude-dir=.git \
    -E 'permission android:name|uses-permission android:name|FORCE_FINISH|com\.bitchat|com\.maobits' \
    app/src/main wear/src/main app/src/debug wear/src/debug 2>/dev/null || true
} > "$EVIDENCE_DIR/05-CUSTOM-PERMISSIONS.txt"

{
  write_section "KOTLIN JAVA PACKAGE DECLARATIONS"
  find app wear -type f \( -name '*.kt' -o -name '*.java' \) \
    -not -path '*/build/*' -print0 | xargs -0 grep -nH -E '^package |^import com\.bitchat|^import com\.maobits' || true
} > "$EVIDENCE_DIR/06-KOTLIN-JAVA-PACKAGES-AND-IMPORTS.txt"

{
  write_section "CODE REFERENCES TO CURRENT TECHNICAL IDENTITY"
  grep -RIn --exclude-dir=build --exclude-dir=.git \
    -E 'com\.bitchat|com\.maobits|bitchat\.droid|bitchat\.watch|bitchat://|Bitchat|BitChat|bitchat' \
    app wear . 2>/dev/null || true
} > "$EVIDENCE_DIR/07-CODE-TECHNICAL-IDENTITY-REFERENCES.txt"

{
  write_section "RESOURCE REFERENCES TO CURRENT TECHNICAL IDENTITY"
  grep -RIn --exclude-dir=build --exclude-dir=.git \
    -E 'bitchat|Bitchat|BitChat|maobits|Maobits|ic_launcher|app_name|provider|authority|scheme' \
    app/src/main/res wear/src/main/res 2>/dev/null || true
} > "$EVIDENCE_DIR/08-RESOURCE-TECHNICAL-IDENTITY-REFERENCES.txt"

{
  write_section "TEST AND DEBUG REFERENCES"
  grep -RIn --exclude-dir=build --exclude-dir=.git \
    -E 'com\.bitchat|com\.maobits|bitchat|Bitchat|BitChat|applicationId|namespace|scheme|authority' \
    app/src/test app/src/androidTest app/src/debug wear/src/test wear/src/androidTest wear/src/debug 2>/dev/null || true
} > "$EVIDENCE_DIR/09-TEST-DEBUG-TECHNICAL-IDENTITY-REFERENCES.txt"

{
  write_section "MIGRATION RISK SUMMARY"
  echo "This is an inventory phase only. No source file replacement was performed."
  echo
  echo "High-risk areas to plan before migration:"
  echo "- applicationId: affects install/update continuity and app data."
  echo "- namespace: affects generated R/BuildConfig and package references."
  echo "- Kotlin package declarations/imports: affects compilation and refactoring scope."
  echo "- custom permissions: affects receiver/service access and manifest references."
  echo "- FileProvider authorities: affects URI grants and sharing."
  echo "- deep links/schemes: affects external intents and compatibility."
  echo "- debug/test references: may fail after migration if not updated intentionally."
  echo "- Wear module identity: must stay compatible with paired mobile app strategy."
} > "$EVIDENCE_DIR/10-MIGRATION-RISK-SUMMARY.txt"

{
  write_section "AUDIT FILE SHA256"
  find "$EVIDENCE_DIR" -type f | sort | xargs -r sha256sum
} > "$EVIDENCE_DIR/11-AUDIT-FILE-SHA256.txt"

cat "$EVIDENCE_DIR/10-MIGRATION-RISK-SUMMARY.txt"
echo
echo "Evidence written to: $EVIDENCE_DIR"
