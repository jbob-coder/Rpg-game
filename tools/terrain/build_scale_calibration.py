"""Build a metric scale calibration GLB for the first-person voxel RPG.

Design-only scene: no collision bodies, character rig, game engine or actual terrain.
Run: python tools/terrain/build_scale_calibration.py --output /path/to/scale_calibration.glb
Dependencies: trimesh and numpy (both free/open-source).
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import trimesh

# Authoritative *provisional* dimensions for terrain Step 01 (world units = meters).
GROUND_SIZE_M = 16.0
GROUND_THICKNESS_M = 0.2
TILE_SIZE_M = 1.0
CHUNK_SIZE_M = 16.0
TEST_WORLD_SIZE_M = 64.0  # A future Step 02 target; NOT constructed here.
PLAYER_HEIGHT_M = 1.8
PLAYER_RADIUS_M = 0.35
EYE_HEIGHT_M = 1.65
PATH_WIDTHS_M = (3.0, 4.0)
PATH_LENGTH_M = 14.0
PATH_THICKNESS_M = 0.01
PLAYER_SPAWN_XZ_M = (-4.0, 4.0)

# Coordinate convention: +Y up, +X east, -Z north / player forward.
# Ground top surface is Y=0; all marker heights above this datum.
COLORS = {
    "grass": [91, 155, 80, 255],
    "path3": [162, 166, 176, 255],
    "path4": [189, 185, 175, 255],
    "cube": [249, 155, 51, 255],
    "player": [55, 91, 170, 255],
    "eye": [251, 219, 47, 255],
    "east": [239, 65, 65, 255],
    "north": [49, 119, 243, 255],
}


def _box(extents: tuple[float, float, float], center: tuple[float, float, float], color: str) -> trimesh.Trimesh:
    mesh = trimesh.creation.box(extents=extents)
    mesh.apply_translation(center)
    mesh.visual.vertex_colors = np.asarray(COLORS[color], dtype=np.uint8)
    return mesh


def _player_capsule() -> trimesh.Trimesh:
    cylinder_height = PLAYER_HEIGHT_M - 2 * PLAYER_RADIUS_M
    if cylinder_height <= 0:
        raise ValueError("Player height must be greater than twice radius")
    # trimesh centers the full capsule at origin and aligns its long axis to Z.
    mesh = trimesh.creation.capsule(height=cylinder_height, radius=PLAYER_RADIUS_M, count=[12, 16])
    mesh.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]))
    mesh.apply_translation([PLAYER_SPAWN_XZ_M[0], PLAYER_HEIGHT_M / 2, PLAYER_SPAWN_XZ_M[1]])
    mesh.visual.vertex_colors = np.asarray(COLORS["player"], dtype=np.uint8)
    return mesh


def build_scene() -> trimesh.Scene:
    scene = trimesh.Scene()

    def add(name: str, mesh: trimesh.Trimesh) -> None:
        scene.add_geometry(mesh, node_name=name, geom_name=name)

    # Unit-size blockout floor, deliberately smaller than future 64 m test world.
    add("Ground_16m_x_16m_TopY0", _box((GROUND_SIZE_M, GROUND_THICKNESS_M, GROUND_SIZE_M), (0, -GROUND_THICKNESS_M / 2, 0), "grass"))
    # Two separated, straight width calibration lanes. No collision implied.
    add("Path_ClearWidth_3m", _box((PATH_WIDTHS_M[0], PATH_THICKNESS_M, PATH_LENGTH_M), (-4.0, PATH_THICKNESS_M / 2, 0), "path3"))
    add("Path_ClearWidth_4m", _box((PATH_WIDTHS_M[1], PATH_THICKNESS_M, PATH_LENGTH_M), (3.5, PATH_THICKNESS_M / 2, 0), "path4"))

    add("PlayerProxy_Capsule_1p8m", _player_capsule())
    # Eye marker is centered on the forward (-Z) side of the proxy; marker itself is not a camera.
    eye = trimesh.creation.icosphere(subdivisions=1, radius=0.06)
    eye.apply_translation([PLAYER_SPAWN_XZ_M[0], EYE_HEIGHT_M, PLAYER_SPAWN_XZ_M[1] - PLAYER_RADIUS_M - 0.04])
    eye.visual.vertex_colors = np.asarray(COLORS["eye"], dtype=np.uint8)
    add("EyeMarker_Y1p65m_FacingNorth", eye)

    # 1 m calibration block; bottom exactly at Y=0.
    add("UnitCube_1m", _box((1.0, 1.0, 1.0), (-6.75, 0.5, -5.75), "cube"))
    # Axis markers near boundary; colored but not part of walkable route.
    add("AxisPositiveX_East", _box((0.8, 0.15, 0.15), (7.0, 0.08, 0), "east"))
    add("AxisNegativeZ_North", _box((0.15, 0.15, 0.8), (0, 0.08, -7.0), "north"))
    return scene


def write_glb(output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = build_scene().export(file_type="glb")
    if not isinstance(payload, bytes) or payload[:4] != b"glTF":
        raise RuntimeError("Exporter did not produce a valid GLB header")
    output_path.write_bytes(payload)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("build/step01_scale_calibration.glb"))
    args = parser.parse_args()
    path = write_glb(args.output)
    print(f"Wrote {path} ({path.stat().st_size:,} bytes)")
    print("Scale: 1 unit = 1 m; +Y up; +X east; -Z north")
    print("Proxy: 1.8 m tall, 0.35 m radius; eye Y=1.65 m; path samples 3 m and 4 m")
    print("This GLB contains visual meshes only, no physics, camera, or navmesh.")


if __name__ == "__main__":
    main()
