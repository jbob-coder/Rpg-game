# Terrain Step 01/10 — Coordinate Scale and Player Calibration

**Status:** Geometry generated and tested; **engine/runtime validation pending**.  
**Date:** 2026-11-04  
**Parent plan:** [Terrain Blueprint](01_TERRAIN_BLUEPRINT.md), task 01.  
**Scope:** Only world-unit scale and first-person traversal clearances. **No** 64 m map, terrain streaming, water, vegetation, architecture or character rig is implemented yet.

## Selected reversible scale baseline

| Concept | Step 01 baseline | Constraint |
| --- | --- | --- |
| World unit | 1 unit = 1 meter | All scene meshes authored/exported at scale 1 |
| Coordinate system | Right-handed, +Y up, +X east, -Z north/forward | Camera should look toward -Z when facing north |
| Ground datum | Ground top at Y=0 | Mesh may extend below Y=0 |
| Primary ground tile | 1 × 1 m | Decorative blocks may be 0.25 m later |
| Chunk size | 16 × 16 m | Will be exercised in Step 02, not here |
| Proposed initial world | 4 × 4 chunks = 64 × 64 m | Future Step 02 scope, not built |
| Character proxy height | 1.80 m | Temporary, not character art |
| Character proxy radius | 0.35 m | Body diameter about 0.70 m |
| First-person eye height | 1.65 m above ground | Marker only; no camera scripted yet |
| Main walkway clearance | 3–4 m | Samples of both widths generated |
| Provisional regular step rise | 0.25–0.35 m | Depends on runtime movement controller; not tested |

**Policy:** These are controlled **provisional design defaults**, not final values approved for all games. Change them in source, update this document, rebuild and retest before adding dependent assets.

## Saved GLB calibration asset

- [Rpg-game_step01_scale_calibration.glb — Google Drive, private](https://drive.google.com/file/d/1veJXJbCspj71pPDcyO--O3XobUKv4aic/view?usp=drivesdk)
- File size: **14,520 bytes**, verified against Drive metadata.
- Local build SHA-256: `b3f67bc9263a8fb385a543b9c21fb0782ff10f6846f99f7301f7d267af84aa28`.
- The asset is derived from the tracked source generator. It is a visual scale calibration mesh, **not** an engine project or complete game.

## GLB scale-test scene

`tools/terrain/build_scale_calibration.py` generates one binary glTF 2.0 (`.glb`) with the following purely visual geometry:

| Mesh name | Meaning | Dimensions / coordinates |
| --- | --- | --- |
| `Ground_16m_x_16m_TopY0` | Single test pad (not 16 streamed tiles) | 16 × 0.2 × 16 m, top Y=0 |
| `Path_ClearWidth_3m` | Stone-path size reference | 3 m wide, 14 m long, X-center=-4 |
| `Path_ClearWidth_4m` | Alternative path size reference | 4 m wide, 14 m long, X-center=+3.5 |
| `PlayerProxy_Capsule_1p8m` | Capsule for clearance and height comparison | 1.80 m tall, radius 0.35 m, X=-4, Z=+4 |
| `EyeMarker_Y1p65m_FacingNorth` | Camera-eye alignment reference | center Y=1.65 m; on forward/-Z face |
| `UnitCube_1m` | Reference cube | 1 × 1 × 1 m, foot Y=0 |
| `AxisPositiveX_East` | East direction marker | Red bar near east border |
| `AxisNegativeZ_North` | North direction marker | Blue bar near north border |

**Usable width check (geometry only):** Player diameter 0.70 m leaves **2.30 m** spare width on a 3.00 m path, or **3.30 m** on a 4.00 m path. These are cross-sectional calculations, not verified collision/passing tests. The 1.80 m proxy is 60% of a 3 m path width; the camera marker is 1.65 m off the world datum.

**Important:** A glTF mesh's node names do not create a player controller, collision body, walkable navmesh, camera or physics. The scene is a **scale diagnostic**, not a playable game or finished voxel art.

## Rebuild instructions

Install dependencies in an isolated Python environment (Python 3.10+ recommended):

```sh
python -m pip install -r tools/terrain/requirements.txt
python tools/terrain/build_scale_calibration.py --output build/step01_scale_calibration.glb
python -m unittest discover -s tests -p 'test_terrain_scale.py' -v
```

The generator is deterministic in geometry, but byte-for-byte GLB output may change with library versions or exporter ordering. Check node names, meter dimensions and test results instead of assuming identical binary hashes across all environments.

## Tests and observed evidence

Executed locally on 2026-11-04 using Python, numpy 2.3.5 and trimesh 4.11.1:

1. Binary GLB header/version/length and successful re-import with trimesh — **PASS**.
2. 16 × 16 m ground bounding box and Y=0 top — **PASS**.
3. 3 m and 4 m lane widths and clearance arithmetic — **PASS**.
4. 1.80 m character proxy height, foot at ground level, and placement inside the 3 m lane — **PASS**.
5. Eye marker at Y=1.65 m and located forward in -Z — **PASS**.
6. 1 m cube dimensions and bottom at ground level — **PASS**.

The initial local run found a character-capsule translation error (bottom Y=-0.55 m); it was corrected by centering the capsule at `PLAYER_HEIGHT_M / 2`. A fresh run reported **6 tests OK**. These checks validate geometric data only; they do **not** prove first-person ergonomics in an actual engine.

## Acceptance status / remaining block

- [x] Explicit world units, orientation, provisional reference dimensions defined.
- [x] Reproducible GLB generator source created.
- [x] A GLB calibration asset generated locally and re-imported successfully.
- [x] Player scale and path-width geometric clearance checked by automated tests.
- [ ] Confirm actual engine and version; import the GLB into a runtime scene.
- [ ] Position an actual player controller and camera at the marker and walk both route samples.
- [ ] Check step handling, collisions, slopes, touch/gamepad input and perceived width on target hardware.

**Step 01 state:** **Geometry milestone passed; engine integration sign-off not yet possible.** Do not claim an engine test passed until one has run.

## Step 02 follow-up

[Step 02 graybox](STEP02_64M_CHUNK_GRAYBOX.md) generated a 64 × 64 m area from 16 distinct 16 × 16 m chunks. Offline geometric checks passed; collision and movement remain unverified in an actual engine. Do not build character or environmental models until terrain scale and spatial conventions are verified in the selected runtime.
