"""Build a 4x4, 64-meter terrain graybox from sixteen 16-meter GLB chunks.

Each standalone GLB is authored in local coordinates [0, 16] on X and Z,
with its ground top at Y=0. Place it once at (cx*16, 0, cz*16).
This is render geometry only: no engine collision, navigation, streaming or paths.

Install: python -m pip install -r tools/terrain/requirements.txt
Run:     python tools/terrain/build_step02_chunks.py --output-dir build/terrain_step02
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

import numpy as np
import trimesh

# Matches the documented Step 01 calibration baseline (meters, Y-up).
CHUNK_SIZE_M = 16
WORLD_CHUNKS_PER_AXIS = 4
CHUNK_COORDINATES = range(-2, 2)  # [-2, -1, 0, 1] on both axes.
WORLD_MIN_M = -32
WORLD_MAX_M = 32
GROUND_THICKNESS_M = 0.2
SCHEMA_VERSION = 1
# Muted alternating shades help recognize the 16 chunks without adding props.
COLORS = (
    (99, 166, 95, 255),
    (111, 174, 102, 255),
    (91, 157, 91, 255),
    (108, 163, 94, 255),
)


def chunk_id(cx: int, cz: int) -> str:
    """Stable readable IDs, including negative grid coordinates."""
    return f"terrain_cx{cx:+d}_cz{cz:+d}"


def chunk_mesh(cx: int, cz: int) -> trimesh.Trimesh:
    """One local-space 16 x 16 x 0.2 m closed block, top at Y=0."""
    mesh = trimesh.creation.box(extents=(CHUNK_SIZE_M, GROUND_THICKNESS_M, CHUNK_SIZE_M))
    mesh.apply_translation((CHUNK_SIZE_M / 2, -GROUND_THICKNESS_M / 2, CHUNK_SIZE_M / 2))
    mesh.visual.vertex_colors = np.array(COLORS[(cx - cz) % len(COLORS)], dtype=np.uint8)
    return mesh


def chunk_records() -> list[dict]:
    records: list[dict] = []
    # Z major order starts at northern (-Z) boundary and proceeds toward south.
    for cz in CHUNK_COORDINATES:
        for cx in CHUNK_COORDINATES:
            x0, z0 = cx * CHUNK_SIZE_M, cz * CHUNK_SIZE_M
            records.append({
                "id": chunk_id(cx, cz),
                "cx": cx, "cz": cz,
                "filename": f"{chunk_id(cx, cz)}.glb",
                "origin_m": [x0, 0, z0],
                "world_bounds_xz_m": [[x0, z0], [x0 + CHUNK_SIZE_M, z0 + CHUNK_SIZE_M]],
                "top_y_m": 0.0,
            })
    return records


def _assert_glb(data: bytes) -> None:
    if data[:4] != b"glTF" or int.from_bytes(data[4:8], "little") != 2:
        raise ValueError("Invalid glTF 2.0 binary header")
    if int.from_bytes(data[8:12], "little") != len(data):
        raise ValueError("GLB header length does not match file length")


def build(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    chunk_dir = output_dir / "chunks"
    chunk_dir.mkdir(parents=True, exist_ok=True)
    records = chunk_records()
    combined = trimesh.Scene()

    for record in records:
        cx, cz = record["cx"], record["cz"]
        name = record["id"]
        mesh = chunk_mesh(cx, cz)

        # Standalone: coordinates local to chunk origin. No world offset baked in.
        standalone = trimesh.Scene()
        standalone.add_geometry(mesh, node_name=name, geom_name=name)
        encoded = standalone.export(file_type="glb")
        _assert_glb(encoded)
        destination = chunk_dir / record["filename"]
        destination.write_bytes(encoded)
        record["sha256"] = hashlib.sha256(encoded).hexdigest()
        record["bytes"] = len(encoded)

        # Preview: same local mesh plus ONE translation to its world origin.
        world_transform = trimesh.transformations.translation_matrix(record["origin_m"])
        combined.add_geometry(mesh.copy(), node_name=name, geom_name=name, transform=world_transform)

    full_glb = combined.export(file_type="glb")
    _assert_glb(full_glb)
    preview_name = "terrain_step02_full_64m.glb"
    (output_dir / preview_name).write_bytes(full_glb)

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "purpose": "Step 02/10 terrain graybox; no engine physics or streaming",
        "units": "meters",
        "axes": {"east": "+X", "up": "+Y", "north": "-Z"},
        "coordinate_rule": "chunk_origin = (cx * 16, 0, cz * 16)",
        "chunk_size_m": CHUNK_SIZE_M,
        "ground_thickness_m": GROUND_THICKNESS_M,
        "world_bounds_xz_m": [[WORLD_MIN_M, WORLD_MIN_M], [WORLD_MAX_M, WORLD_MAX_M]],
        "world_dimensions_xz_m": [WORLD_CHUNKS_PER_AXIS * CHUNK_SIZE_M] * 2,
        "preview": {"file": preview_name, "sha256": hashlib.sha256(full_glb).hexdigest(), "bytes": len(full_glb)},
        "chunks": records,
    }
    (output_dir / "terrain_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # ZIP contents have deterministic names and metadata. Files are still verified by SHA-256.
    zip_path = output_dir / "terrain_step02_chunks.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted([output_dir / "terrain_manifest.json", output_dir / preview_name, *chunk_dir.glob("*.glb")]):
            arcname = path.relative_to(output_dir).as_posix()
            meta = zipfile.ZipInfo(arcname, date_time=(2026, 1, 1, 0, 0, 0))
            meta.compress_type = zipfile.ZIP_DEFLATED
            meta.external_attr = 0o644 << 16
            zf.writestr(meta, path.read_bytes())

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("build/terrain_step02"))
    args = parser.parse_args()
    manifest = build(args.output_dir)
    print(f"Generated {len(manifest['chunks'])} standalone terrain GLBs")
    print(f"World: {manifest['world_dimensions_xz_m']} m; boundaries: {manifest['world_bounds_xz_m']}")
    print(f"Preview: {args.output_dir / manifest['preview']['file']}")
    print(f"ZIP: {args.output_dir / 'terrain_step02_chunks.zip'}")
    print("Visual-only blockout; no paths, cliffs, river, collision or navigation")


if __name__ == "__main__":
    main()
