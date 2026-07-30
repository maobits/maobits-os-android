\
#!/usr/bin/env python3
"""
Project: Maobits OS Android
Module: brand-tools
File: maobits_os_generate_icon_resources_1_1_8.py
Purpose: Generate candidate launcher icon PNG resources from an approved Maobits OS icon image.

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
from pathlib import Path
from typing import Dict

try:
    from PIL import Image
except Exception as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "Pillow is required for icon generation. Install it with: python3 -m pip install --user pillow"
    ) from exc


DENSITY_SIZES: Dict[str, int] = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_launcher_resources(image: Image.Image, output_root: Path, module: str) -> None:
    for density, size in DENSITY_SIZES.items():
        density_dir = output_root / module / "src" / "main" / "res" / density
        density_dir.mkdir(parents=True, exist_ok=True)

        resized = image.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(density_dir / "ic_launcher.png")
        resized.save(density_dir / "ic_launcher_round.png")


def save_previews(image: Image.Image, output_root: Path) -> None:
    preview_dir = output_root / "preview"
    preview_dir.mkdir(parents=True, exist_ok=True)

    for size in [1024, 512, 256, 128, 96, 72, 48]:
        image.resize((size, size), Image.Resampling.LANCZOS).save(
            preview_dir / f"maobits-os-icon-preview-{size}.png"
        )


def write_hash_manifest(output_root: Path) -> None:
    lines = []
    for path in sorted(output_root.rglob("*")):
        if path.is_file() and path.name != "SHA256SUMS.txt":
            lines.append(f"{sha256_file(path)}  {path.relative_to(output_root)}")
    (output_root / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate candidate Maobits OS Android launcher icon resources."
    )
    parser.add_argument("--source", required=True, help="Approved source PNG image path.")
    parser.add_argument("--output", required=True, help="Output candidate resource folder.")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)

    if not source.is_file():
        raise SystemExit(f"Source image not found: {source}")

    output.mkdir(parents=True, exist_ok=True)

    image = Image.open(source).convert("RGBA").resize((1024, 1024), Image.Resampling.LANCZOS)

    save_launcher_resources(image, output, "app")
    save_launcher_resources(image, output, "wear")
    save_previews(image, output)

    (output / "README.md").write_text(
        "Generated Maobits OS Android candidate icon resources. "
        "Do not apply blindly to active Android resources.\n",
        encoding="utf-8",
    )

    write_hash_manifest(output)

    print("Generated candidate icon resources:")
    print(output)
    for path in sorted(output.rglob("*")):
        if path.is_file():
            print(path.relative_to(output))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
