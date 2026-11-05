# Continuous terrain direction — non-Minecraft prototype v1

**Date:** 2026-11-05  
**Repo:** jbob-coder/Rpg-game  
**Branch:** work/nonvoxel-terrain-prototype-20261105  
**Scope:** Terrain GLB geometry only. Character model is the separate second task. No buildings, NPCs, settlement logic, or gameplay.

## Owner direction
Remove the Minecraft-like visual treatment from the RPG world. The 2026-11-04 `generate_square_terrain.py` creates solid 1-meter cubic prefabs and a stepped column-height world. It is a **legacy prototype**, not the target look. Do not perpetuate visible stacked cubes, horizontal layer steps, or exposed block faces in the active terrain design.

**Preserve coordinate semantics, not cubic meshes:** 1 unit = 1 meter, X east, Y up, -Z north; stable 16 x 16 m chunks, 64 x 64 m initial world, chunk IDs and negative integer coordinates. A terrain grid square is a 1 x 1 m **sampling cell**. Its surface vertices can vary continuously in Y; it is not necessarily a 1 x 1 x 1 meter solid cube.

## Geometry prototype produced in this session
An independent, reversible local generator built:
- 16 terrain chunk GLBs, each in local [0,16] x [0,16] XZ coordinates.
- 1 combined world-space GLB, 64 x 64 meters.
- A manifest with coordinates, per-file SHA-256 and origin transforms.
- Continuous hills, valleys, mountain peaks, grass/rock/snow vertex colors.
- No cubic block walls, voxel layers or Minecraft material textures.

The generator, test script, all GLB assets and manifest were packaged into one downloadable ZIP in this conversation. **The GLB binaries and source are not committed by this documentation-only change**; download the archive from the conversation to preserve them externally.

## Verified locally
On 2026-11-05, five independent Python unittest checks passed:
1. Non-flat finite terrain heights.
2. All 24 internal chunk seams match for vertex height and vertex color on **reimported standalone GLBs**.
3. Standalone GLBs have local XZ bounds of 0..16, exactly 512 top-facing triangles and 289 vertices; no cube/cliff wall triangles.
4. Combined GLB reimports at world bounds of -32..32 on X/Z with 16 named section geometries.
5. Manifest, offsets, declared hashes, and glTF GLB signatures are consistent.

These are **geometry tests**, not visual/runtime approval. Engine import, collision, character movement, Android performance and final art materials remain unverified.

## Migration procedure
1. Visually inspect the continuous-terrain GLB and check that the new low-poly silhouette is appropriate.
2. Import a chunk and the world preview in the selected engine; confirm transforms/collision before making the new generator authoritative.
3. On acceptance, mark `generate_square_terrain.py`, its cubic prefab manifest and legacy-specific tests/docs as superseded, remove their links from the active README, and keep their history in Git.
4. Do not delete old files or rewrite historical test evidence on `main` during exploratory work.

**Recommendation:** Preserve the coordinate contract in `docs/3d/TERRAIN_COORDINATE_CONTRACT.md` and replace the stepped-column mesh strategy with globally sampled continuous heightfield triangles.