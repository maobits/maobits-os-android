\
#!/usr/bin/env python3
"""
Project: Maobits OS Android
Module: brand-tools
File: maobits_os_apply_adaptive_icons_1_1_10.py
Purpose: Apply or rollback Maobits OS adaptive icon resources with auditable backups.

Company: Maobits
Lead developer: Mauricio Chara Hurtado
Technical contact: os@maobits.com
Product principle: Person -> Commitment -> Confirmation

Quality standard:
- Production-grade structure.
- Clear separation of responsibilities.
- Auditable behavior and explicit failure paths.
- Maintainable implementation with meaningful technical comments.

Legal and attribution note:
- Preserve original third-party license notices when applicable.
- Do not mix Maobits OS branding with external project branding.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

try:
    from PIL import Image
except Exception as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "Pillow is required for adaptive icon generation. Install it with: python3 -m pip install --user pillow"
    ) from exc


ADAPTIVE_FOREGROUND_SIZES = {
    "mipmap-mdpi": 108,
    "mipmap-hdpi": 162,
    "mipmap-xhdpi": 216,
    "mipmap-xxhdpi": 324,
    "mipmap-xxxhdpi": 432,
}

MODULES = ["app", "wear"]

ADAPTIVE_ICON_XML = """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/maobits_os_icon_background" />
    <foreground android:drawable="@mipmap/ic_launcher_foreground" />
</adaptive-icon>
"""

COLORS_XML = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="maobits_os_icon_background">#061F23</color>
</resources>
"""


@dataclass
class AdaptiveIconOperation:
    mode: str
    relative_path: str
    target_path: str
    backup_path: Optional[str]
    before_sha256: Optional[str]
    after_sha256: Optional[str]
    status: str


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def sha256_file(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def target_paths(repo_root: Path) -> List[Path]:
    paths: List[Path] = []
    for module in MODULES:
        paths.extend([
            repo_root / module / "src" / "main" / "res" / "mipmap-anydpi-v26" / "ic_launcher.xml",
            repo_root / module / "src" / "main" / "res" / "mipmap-anydpi-v26" / "ic_launcher_round.xml",
            repo_root / module / "src" / "main" / "res" / "values" / "maobits_os_icon_colors.xml",
        ])
        for density in ADAPTIVE_FOREGROUND_SIZES:
            paths.append(
                repo_root / module / "src" / "main" / "res" / density / "ic_launcher_foreground.png"
            )
    return paths


def backup_target(repo_root: Path, evidence_dir: Path, target: Path) -> Optional[Path]:
    if not target.exists():
        return None
    backup_root = evidence_dir / "backup-before-adaptive-icon-replacement"
    relative = target.relative_to(repo_root)
    backup = backup_root / relative
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target, backup)
    return backup


def write_manifest(evidence_dir: Path, operations: List[AdaptiveIconOperation]) -> None:
    evidence_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_at": now_iso(),
        "phase": "1.1.10",
        "purpose": "Controlled Maobits OS adaptive icon replacement.",
        "operations": [asdict(item) for item in operations],
    }
    (evidence_dir / "ADAPTIVE-ICON-REPLACEMENT-MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lines = [
        "=== MAOBITS OS ANDROID - ADAPTIVE ICON REPLACEMENT SUMMARY ===",
        f"Generated at: {manifest['generated_at']}",
        "",
        "=== OPERATIONS ===",
    ]
    for item in operations:
        lines.append(f"{item.status}: {item.relative_path}")

    (evidence_dir / "ADAPTIVE-ICON-REPLACEMENT-SUMMARY.txt").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def dry_run(repo_root: Path, source: Path, evidence_dir: Path) -> int:
    operations: List[AdaptiveIconOperation] = []

    source_status = "source-ready" if source.is_file() else "missing-source"
    operations.append(
        AdaptiveIconOperation(
            mode="dry-run",
            relative_path=str(source),
            target_path=str(source),
            backup_path=None,
            before_sha256=None,
            after_sha256=sha256_file(source),
            status=source_status,
        )
    )

    for target in target_paths(repo_root):
        operations.append(
            AdaptiveIconOperation(
                mode="dry-run",
                relative_path=str(target.relative_to(repo_root)),
                target_path=str(target),
                backup_path=None,
                before_sha256=sha256_file(target),
                after_sha256=None,
                status="will-create-or-replace",
            )
        )

    write_manifest(evidence_dir, operations)

    if not source.is_file():
        print(f"Approved source icon not found: {source}")
        return 2

    print("Dry-run completed. Adaptive icon replacement is ready.")
    print(evidence_dir / "ADAPTIVE-ICON-REPLACEMENT-SUMMARY.txt")
    return 0


def write_text_target(repo_root: Path, evidence_dir: Path, target: Path, content: str) -> AdaptiveIconOperation:
    before_sha = sha256_file(target)
    backup = backup_target(repo_root, evidence_dir, target)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

    return AdaptiveIconOperation(
        mode="apply",
        relative_path=str(target.relative_to(repo_root)),
        target_path=str(target),
        backup_path=str(backup) if backup else None,
        before_sha256=before_sha,
        after_sha256=sha256_file(target),
        status="applied",
    )


def write_image_target(repo_root: Path, evidence_dir: Path, target: Path, image: Image.Image, size: int) -> AdaptiveIconOperation:
    before_sha = sha256_file(target)
    backup = backup_target(repo_root, evidence_dir, target)

    target.parent.mkdir(parents=True, exist_ok=True)
    resized = image.resize((size, size), Image.Resampling.LANCZOS)
    resized.save(target)

    return AdaptiveIconOperation(
        mode="apply",
        relative_path=str(target.relative_to(repo_root)),
        target_path=str(target),
        backup_path=str(backup) if backup else None,
        before_sha256=before_sha,
        after_sha256=sha256_file(target),
        status="applied",
    )


def apply_icons(repo_root: Path, source: Path, evidence_dir: Path) -> int:
    if not source.is_file():
        print(f"Approved source icon not found: {source}")
        return 2

    image = Image.open(source).convert("RGBA")
    operations: List[AdaptiveIconOperation] = []

    for module in MODULES:
        res_root = repo_root / module / "src" / "main" / "res"

        operations.append(write_text_target(
            repo_root,
            evidence_dir,
            res_root / "mipmap-anydpi-v26" / "ic_launcher.xml",
            ADAPTIVE_ICON_XML,
        ))
        operations.append(write_text_target(
            repo_root,
            evidence_dir,
            res_root / "mipmap-anydpi-v26" / "ic_launcher_round.xml",
            ADAPTIVE_ICON_XML,
        ))
        operations.append(write_text_target(
            repo_root,
            evidence_dir,
            res_root / "values" / "maobits_os_icon_colors.xml",
            COLORS_XML,
        ))

        for density, size in ADAPTIVE_FOREGROUND_SIZES.items():
            operations.append(write_image_target(
                repo_root,
                evidence_dir,
                res_root / density / "ic_launcher_foreground.png",
                image,
                size,
            ))

    write_manifest(evidence_dir, operations)

    print("Adaptive icon replacement applied.")
    print(evidence_dir / "ADAPTIVE-ICON-REPLACEMENT-SUMMARY.txt")
    return 0


def rollback(repo_root: Path, evidence_dir: Path) -> int:
    backup_root = evidence_dir / "backup-before-adaptive-icon-replacement"
    manifest_path = evidence_dir / "ADAPTIVE-ICON-REPLACEMENT-MANIFEST.json"

    if not manifest_path.is_file():
        print(f"Replacement manifest not found: {manifest_path}")
        return 2

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    operations: List[AdaptiveIconOperation] = []

    for item in manifest.get("operations", []):
        if item.get("mode") != "apply":
            continue

        relative = Path(item["relative_path"])
        target = repo_root / relative
        backup_path = item.get("backup_path")
        backup = Path(backup_path) if backup_path else None

        before_sha = sha256_file(target)

        if backup and backup.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(backup, target)
            status = "restored"
        else:
            if target.exists():
                target.unlink()
            status = "removed-created-file"

        operations.append(
            AdaptiveIconOperation(
                mode="rollback",
                relative_path=str(relative),
                target_path=str(target),
                backup_path=str(backup) if backup else None,
                before_sha256=before_sha,
                after_sha256=sha256_file(target),
                status=status,
            )
        )

    write_manifest(evidence_dir, operations)
    print("Adaptive icon rollback completed.")
    print(evidence_dir / "ADAPTIVE-ICON-REPLACEMENT-SUMMARY.txt")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply or rollback Maobits OS adaptive launcher icons."
    )
    parser.add_argument("--mode", required=True, choices=["dry-run", "apply", "rollback"])
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--source",
        default="docs/03-brand/assets/2026-07-30-maobits-os-icon-proposal-approved/maobits-os-icon-proposal-approved-1024.png",
        help="Approved source PNG icon.",
    )
    parser.add_argument(
        "--evidence-dir",
        default="docs/03-brand/evidence/2026-07-30-controlled-adaptive-icon-replacement",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    source = (repo_root / args.source).resolve()
    evidence_dir = (repo_root / args.evidence_dir).resolve()

    if args.mode == "dry-run":
        return dry_run(repo_root, source, evidence_dir)
    if args.mode == "apply":
        return apply_icons(repo_root, source, evidence_dir)
    if args.mode == "rollback":
        return rollback(repo_root, evidence_dir)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
