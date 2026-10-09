#!/usr/bin/env python3
"""Build a manifest from embedded-texture, animated, regular Switch GLBs.

Does not download, modify, or publicly expose any game assets.
"""
from __future__ import annotations
import hashlib
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "switch-manifest.json"
IDLE = re.compile(r"default(?:idle|wait)|battle(?:idle|wait)|fight[_ -]?a|(^|[_-])idle|wait|stand|breath|rest", re.I)
BAD = re.compile(r"attack|damage|faint|death|down|hit|move|run|walk|jump|bind|t[-_ ]?pose", re.I)


def inspect(path: Path) -> dict:
    with path.open("rb") as stream:
        raw = stream.read(20)
        if len(raw) != 20:
            raise ValueError("undersized GLB header")
        magic, version, length, json_size, kind = struct.unpack("<IIIII", raw)
        if magic != 0x46546C67 or version != 2 or kind != 0x4E4F534A:
            raise ValueError("not a GLB 2.0 JSON chunk")
        if length != path.stat().st_size or not 2 <= json_size <= min(length - 20, 24_000_000):
            raise ValueError("invalid GLB length")
        doc = json.loads(stream.read(json_size).rstrip(b" \r\n\t\x00").decode("utf-8"))

    if not doc.get("meshes") or not doc.get("scenes") or not doc.get("materials"):
        raise ValueError("missing meshes/scenes/materials")
    textures = doc.get("textures") or []
    images = doc.get("images") or []
    if not isinstance(textures, list) or not isinstance(images, list):
        raise ValueError("invalid GLB textures or images")
    for material in doc["materials"]:
        slot = (material.get("pbrMetallicRoughness") or {}).get("baseColorTexture")
        if not isinstance(slot, dict):
            raise ValueError("material has no base-color texture")
        index = slot.get("index")
        if not isinstance(index, int) or not 0 <= index < len(textures):
            raise ValueError("invalid base-color texture index")
        image_index = textures[index].get("source")
        if not isinstance(image_index, int) or not 0 <= image_index < len(images):
            raise ValueError("material has no image")
        image = images[image_index]
        if not ("bufferView" in image or str(image.get("uri", "")).startswith("data:")):
            raise ValueError("base-color image is not embedded")

    names = [
        a.get("name") or f"animation_{i}"
        for i, a in enumerate(doc.get("animations") or [])
        if isinstance(a, dict) and a.get("channels") and a.get("samplers")
    ]
    idle = next((name for name in names if IDLE.search(name) and not BAD.search(name)), None)
    if not idle:
        raise ValueError("no verified idle-like animation")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(2 ** 20), b""):
            digest.update(chunk)
    return {
        "dex": int(path.parent.name),
        "form": "regular",
        "path": f"{path.parent.name}/regular.glb",
        "bytes": path.stat().st_size,
        "sha256": digest.hexdigest(),
        "idleAnimation": idle,
        "animations": names,
        "idleBreaks": [],
        "ready": True,
        "valid": True,
    }


def main() -> None:
    entries = []
    errors = {}
    for file in sorted(ROOT.glob("[0-9][0-9][0-9][0-9]/regular.glb")):
        if not 1 <= int(file.parent.name) <= 1025:
            continue
        try:
            entries.append(inspect(file))
        except (OSError, ValueError, TypeError, KeyError, IndexError, json.JSONDecodeError) as exc:
            errors[str(file.relative_to(ROOT))] = str(exc)
    entries.sort(key=lambda entry: entry["dex"])
    result = {
        "format": 1,
        "source": "private-original-switch-glb-catalog",
        "models": len(entries),
        "entries": entries,
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Verified {len(entries)} / {len(entries) + len(errors)} regular GLB(s)")
    if errors:
        print("Skipped invalid or unverified files:")
        for name, error in list(errors.items())[:50]:
            print(f"  {name}: {error}")
    if not entries:
        raise SystemExit("No model passed the strict GLB validation")


if __name__ == "__main__":
    main()
