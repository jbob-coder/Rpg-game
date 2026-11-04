# Rpg-game
Ai solo

## RPG design reference

This repository currently documents the foundations of role-playing games. It is not yet a playable game, and the reference does not prescribe a final engine, ruleset, or balance model.

- [RPG Stats and Core Fundamentals](docs/RPG_STATS_AND_FUNDAMENTALS.md) — primary attributes; health, mana, and stamina; derived combat stats; progression; action resolution; equipment, crafting, NPCs, quests, saving, world simulation, and verification.

## First-person 3D voxel RPG — incremental build

- **Terrain coordinates and GLB joins (2026-11-04):** [coordinate contract](docs/3d/TERRAIN_COORDINATE_CONTRACT.md), [world/chunk helper](tools/terrain/coordinates.py), and [5 GLB coordinate tests](tests/test_terrain_coordinates.py). Five independent local tests passed; original 64 m generator and engine integration have not been rerun.
- **Latest terrain asset:** [Square terrain GLB kit specifications](docs/3d/SQUARE_TERRAIN_KIT.md), [generator](tools/terrain/generate_square_terrain.py), [9 geometry/packaging tests](tests/test_square_terrain.py) and [64 m world manifest](data/terrain/square_terrain_manifest.json). Nine offline checks passed, including all 24 internal section seams. Assets are saved in ChatGPT Library at `Rpg-game/SquareTerrainGLB/V2`.
- [Terrain Step 02/10 — 64 × 64 m / 16-chunk graybox (8 geometry tests passed)](docs/3d/STEP02_64M_CHUNK_GRAYBOX.md) — generator, 16 GLB chunks, preview, manifest and ZIP; engine integration pending.
- [Terrain Step 01/10 — Scale calibration (geometry tests passed; runtime pending)](docs/3d/STEP01_SCALE_CALIBRATION.md) — 1 m units, 16 m test pad, 1.8 m player capsule, 3 m/4 m paths and GLB generator/tests.
- [Download Step 01 calibration GLB (private Google Drive)](https://drive.google.com/file/d/1veJXJbCspj71pPDcyO--O3XobUKv4aic/view?usp=drivesdk).
- [Phase 01 — Terrain blueprint](docs/3d/01_TERRAIN_BLUEPRINT.md) — world scale, modular ground chunks, stone paths, river/waterfall, bridge approaches, elevation, collisions, GLB export contracts, acceptance tests.
- [Saved first-person visual reference (private Google Drive)](https://drive.google.com/file/d/1EGEBCBMkPnbnE63yqvxn3rAMol3w3hPJ/view?usp=drivesdk) — 2D PNG concept art, **not** a 3D GLB mesh.
- **Second workstream — 3D character model:** not begun. Only natural terrain meshes and the character model are in scope; no buildings, NPC systems or gameplay features.
- [RPG systems documentation index](docs/README.md).

## Documentation status

The linked guide distinguishes generally applicable RPG concepts from optional example rules and identifies design decisions that remain open. Mechanics in the guide are **proposals**, not implemented features.
