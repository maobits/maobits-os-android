# Maobits OS Android — Technical Identity Migration Risk Register 1.2.1

Generated at: 2026-07-30T20:25:58-05:00

| Risk | Impact | Control |
|---|---|---|
| Changing applicationId creates a different Android app | Existing install/data may not migrate | Decide clean install vs migration before implementation |
| Changing namespace affects generated R/BuildConfig | Compile failures | Apply in a dedicated branch and validate build |
| Changing Kotlin package declarations affects imports | Compile failures and hidden references | Use IDE/refactor or scripted staged migration with tests |
| Changing custom permissions may break receivers/services | Runtime access failure | Update definitions and consumers together |
| Changing FileProvider authority may break shared URIs | Share/open flows fail | Keep ${applicationId}.fileprovider or document explicit authority |
| Changing deep-link scheme may break external links | Legacy links stop working | Support legacy scheme during transition if needed |
| Wear identity mismatch | Mobile/Wear pairing issues | Validate mobile and wear together |
| Attribution removal by mistake | Legal/compliance risk | Preserve original license and attribution sections |
| Mass replacement corrupts unrelated content | Unbounded defects | Prohibit mass replacement |
