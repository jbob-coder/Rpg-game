# Rpg-game
Ai solo

## RPG design reference

This repository currently documents the foundations of role-playing games. It is not yet a playable game, and the reference does not prescribe a final engine, ruleset, or balance model.

- [RPG Stats and Core Fundamentals](docs/RPG_STATS_AND_FUNDAMENTALS.md) — primary attributes; health, mana, and stamina; derived combat stats; progression; action resolution; equipment, crafting, NPCs, quests, saving, world simulation, and verification.

## First-person 3D voxel RPG — incremental build

- [Terrain Step 01/10 — Scale calibration (geometry tests passed; runtime pending)](docs/3d/STEP01_SCALE_CALIBRATION.md) — 1 m units, 16 m test pad, 1.8 m player capsule, 3 m/4 m paths and GLB generator/tests.
- [Phase 01 — Terrain blueprint](docs/3d/01_TERRAIN_BLUEPRINT.md) — world scale, modular ground chunks, stone paths, river/waterfall, bridge approaches, elevation, collisions, GLB export contracts, acceptance tests.
- [Saved first-person visual reference (private Google Drive)](https://drive.google.com/file/d/1EGEBCBMkPnbnE63yqvxn3rAMol3w3hPJ/view?usp=drivesdk) — 2D PNG concept art, **not** a 3D GLB mesh.
- **Phase 02 — Character / environment models:** not begun. The character/model specification follows after terrain scale and navigability are verified.
- [RPG systems documentation index](docs/README.md).

## Documentation status

The linked guide distinguishes generally applicable RPG concepts from optional example rules and identifies design decisions that remain open. Mechanics in the guide are **proposals**, not implemented features.
