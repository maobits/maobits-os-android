\
#!/usr/bin/env python3
"""
Project: Maobits OS Android
Module: brand-tools
File: maobits_os_apply_launcher_icons_1_1_9.py
Purpose: Apply or rollback Maobits OS launcher icon PNG candidates with auditable backups.

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
from typing import Iterable, List, Optional


@dataclass
class IconOperation:
    mode: str
    relative_path: str
    source_path: Optional[str]
    target_path: str
    backup_path: Optional[str]
    before_sha256: Optional[str]
    after_sha256: Optional[str]
    status: str


DENSITY_DIRS = [
    "mipmap-mdpi",
    "mipmap-hdpi",
    "mipmap-xhdpi",
    "mipmap-xxhdpi",
    "mipmap-xxxhdpi",
]

ICON_NAMES = [
    "ic_launcher.png",
    "ic_launcher_round.png",
]


def sha256_file(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def iter_candidate_mappings(repo_root: Path, candidate_root: Path) -> Iterable[tuple[Path, Path, str]]:
    for module in ["app", "wear"]:
        for density in DENSITY_DIRS:
            for icon_name in ICON_NAMES:
                relative_path = Path(module) / "src" / "main" / "res" / density / icon_name
                source = candidate_root / relative_path
                target = repo_root / relative_path
                yield source, target, str(relative_path)


def write_manifest(evidence_dir: Path, operations: List[IconOperation]) -> None:
    evidence_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "generated_at": now_iso(),
        "phase": "1.1.9",
        "purpose": "Controlled Maobits OS launcher icon PNG replacement.",
        "operations": [asdict(item) for item in operations],
    }

    (evidence_dir / "LAUNCHER-ICON-REPLACEMENT-MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lines = [
        "=== MAOBITS OS ANDROID - LAUNCHER ICON REPLACEMENT SUMMARY ===",
        f"Generated at: {manifest['generated_at']}",
        "",
        "=== OPERATIONS ===",
    ]
    for item in operations:
        lines.append(f"{item.status}: {item.relative_path}")

    (evidence_dir / "LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def dry_run(repo_root: Path, candidate_root: Path, evidence_dir: Path) -> int:
    operations: List[IconOperation] = []

    for source, target, relative_path in iter_candidate_mappings(repo_root, candidate_root):
        status = "ready" if source.is_file() else "missing-candidate"
        operations.append(
            IconOperation(
                mode="dry-run",
                relative_path=relative_path,
                source_path=str(source),
                target_path=str(target),
                backup_path=None,
                before_sha256=sha256_file(target),
                after_sha256=sha256_file(source),
                status=status,
            )
        )

    write_manifest(evidence_dir, operations)

    missing = [item for item in operations if item.status == "missing-candidate"]
    if missing:
        print("Missing candidate files:")
        for item in missing:
            print(f"- {item.relative_path}")
        return 2

    print("Dry-run completed. Candidate files are ready.")
    print(evidence_dir / "LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt")
    return 0


def apply_icons(repo_root: Path, candidate_root: Path, evidence_dir: Path) -> int:
    backup_root = evidence_dir / "backup-before-active-launcher-icon-replacement"
    operations: List[IconOperation] = []

    for source, target, relative_path in iter_candidate_mappings(repo_root, candidate_root):
        if not source.is_file():
            operations.append(
                IconOperation(
                    mode="apply",
                    relative_path=relative_path,
                    source_path=str(source),
                    target_path=str(target),
                    backup_path=None,
                    before_sha256=sha256_file(target),
                    after_sha256=None,
                    status="missing-candidate",
                )
            )
            continue

        backup = backup_root / relative_path
        backup.parent.mkdir(parents=True, exist_ok=True)

        before_sha = sha256_file(target)
        if target.is_file():
            shutil.copy2(target, backup)

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        after_sha = sha256_file(target)

        operations.append(
            IconOperation(
                mode="apply",
                relative_path=relative_path,
                source_path=str(source),
                target_path=str(target),
                backup_path=str(backup) if backup.exists() else None,
                before_sha256=before_sha,
                after_sha256=after_sha,
                status="applied",
            )
        )

    write_manifest(evidence_dir, operations)

    failures = [item for item in operations if item.status != "applied"]
    if failures:
        print("Some launcher icon files were not applied:")
        for item in failures:
            print(f"- {item.status}: {item.relative_path}")
        return 2

    print("Launcher icon PNG replacement applied.")
    print(evidence_dir / "LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt")
    return 0


def rollback(repo_root: Path, evidence_dir: Path) -> int:
    backup_root = evidence_dir / "backup-before-active-launcher-icon-replacement"
    operations: List[IconOperation] = []

    if not backup_root.is_dir():
        print(f"Backup directory not found: {backup_root}")
        return 2

    for backup in sorted(backup_root.rglob("*")):
        if not backup.is_file():
            continue

        relative_path = backup.relative_to(backup_root)
        target = repo_root / relative_path
        before_sha = sha256_file(target)

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(backup, target)

        operations.append(
            IconOperation(
                mode="rollback",
                relative_path=str(relative_path),
                source_path=str(backup),
                target_path=str(target),
                backup_path=str(backup),
                before_sha256=before_sha,
                after_sha256=sha256_file(target),
                status="restored",
            )
        )

    write_manifest(evidence_dir, operations)

    print("Rollback completed from launcher icon backup.")
    print(evidence_dir / "LAUNCHER-ICON-REPLACEMENT-SUMMARY.txt")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply or rollback Maobits OS launcher icon PNG candidates."
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=["dry-run", "apply", "rollback"],
        help="Execution mode.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root. Default: current directory.",
    )
    parser.add_argument(
        "--candidate-root",
        default="docs/03-brand/generated/2026-07-30-maobits-os-icon-android-candidate",
        help="Candidate icon resource root.",
    )
    parser.add_argument(
        "--evidence-dir",
        default="docs/03-brand/evidence/2026-07-30-controlled-launcher-icon-replacement",
        help="Evidence and backup directory.",
    )

    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    candidate_root = (repo_root / args.candidate_root).resolve()
    evidence_dir = (repo_root / args.evidence_dir).resolve()

    if args.mode in {"dry-run", "apply"} and not candidate_root.is_dir():
        print(f"Candidate root not found: {candidate_root}")
        return 2

    if args.mode == "dry-run":
        return dry_run(repo_root, candidate_root, evidence_dir)
    if args.mode == "apply":
        return apply_icons(repo_root, candidate_root, evidence_dir)
    if args.mode == "rollback":
        return rollback(repo_root, evidence_dir)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
