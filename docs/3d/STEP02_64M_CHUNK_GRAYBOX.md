# Terrain Step 02/10 — 64 × 64 m / 16-chunk Graybox

**Status:** 3D ground geometry, manifest and eight offline tests **verified**; engine/runtime checks **pending**.  
**Date:** 2026-11-04  
**Source:** [Terrain blueprint](01_TERRAIN_BLUEPRINT.md) → Step 02, after [Step 01 calibration](STEP01_SCALE_CALIBRATION.md).  
**Repository:** `jbob-coder/Rpg-game`, `main`.  
**Source-of-truth artifacts:** [generator](../../tools/terrain/build_step02_chunks.py), [tests](../../tests/test_terrain_step02.py), [manifest](../../data/terrain/step02_manifest.json).

## Delivered

- **16 separately exported terrain GLBs** representing a 4 × 4 grid.
- **1 combined preview GLB** containing the same chunks, each transformed once into world coordinates.
- **1 machine-readable manifest** recording IDs, origins, bounds, SHA-256 and file sizes.
- **1 ZIP package** containing all 16 chunk GLBs, manifest and combined GLB.
- **8 executed offline unit tests** validating GLB/manifest consistency, bounds, node transforms, seams and packaging.

### Coordinate and visual contract

| Property | Value |
| --- | --- |
| Coordinate system | 1 unit = 1 meter; +Y up, +X east, -Z north |
| Chunk edge | 16 m |
| Chunk index range | `cx, cz = -2, -1, 0, 1` |
| Chunk origin | `(cx × 16, 0, cz × 16)` |
| Full range | X and Z each from **-32 to +32 m** |
| Ground top elevation | Y=0 for every chunk |
| Graybox ground thickness | 0.20 m below datum |
| Geometry | Flat, colored blocks; four muted alternating shades |
| Chunk ID | `terrain_cx-2_cz+1` style; independent of naming display |
| Navigation / collisions | **Not implemented**; GLB contains visuals only |

### Spatial overview

North is **-Z**. Each square below is 16 × 16 m. The full footprint is 64 × 64 m.

```text
                        NORTH (-Z)
                     X: west → east

Z=-2      [-2,-2] [-1,-2] [ 0,-2] [ 1,-2]
Z=-1      [-2,-1] [-1,-1] [ 0,-1] [ 1,-1]
Z= 0      [-2, 0] [-1, 0] [ 0, 0] [ 1, 0]
Z= 1      [-2, 1] [-1, 1] [ 0, 1] [ 1, 1]

         X=-2     X=-1     X=0      X=1
                        SOUTH (+Z)
```

A standalone chunk's vertices are in **local** bounds `[0,16]` in X and Z, Y `[-0.2,0]`. It must be placed at the origin in its manifest. The combined GLB already has the world transforms; **do not translate it again**. This prevents double-offset errors.

## Reproduce the assets

From repository root with Python and free dependencies:

```sh
python -m pip install -r tools/terrain/requirements.txt
python tools/terrain/build_step02_chunks.py --output-dir build/terrain_step02
python -m unittest discover -s tests -p 'test_terrain_step02.py' -v
```

Generated layout (not every generated binary is committed to GitHub; source and manifest are):

```text
build/terrain_step02/
  terrain_manifest.json
  terrain_step02_full_64m.glb
  terrain_step02_chunks.zip
  chunks/
    terrain_cx-2_cz-2.glb
    ... (all 16 pairs of cx, cz from -2 through +1)
```

The generator uses geometry-library operations, not a particular game engine. It creates a flat **foundation only**, because Step 03 owns paths, Step 04 owns cliffs, and Step 05 owns the river. A flat surface deliberately makes scale and seam errors easier to detect.

## Executed verification

**Test command:** `python -m unittest discover -s ... -p 'test_terrain_step02.py' -v` (run against the generated source snapshot).  
**Observed result:** `Ran 8 tests ... OK`.  
**Environment used:** Python 3.13, numpy 2.3.5, trimesh 4.11.1.

| Check | Result |
| --- | --- |
| Exactly 16 unique IDs covering all 4×4 negative/positive chunk coordinates | PASS |
| Combined GLB AABB equals X/Z -32..32 and Y -0.2..0 | PASS |
| All 16 standalone GLBs re-import in *local* coordinates without duplicated translation | PASS |
| Combined GLB retains node IDs and correct world transforms | PASS |
| All 24 horizontal/vertical neighbor edges have identical boundary coordinates | PASS |
| GLB headers, files, manifest sizes and content hashes match | PASS |
| ZIP has 18 unique entries and passes CRC test | PASS |
| Floor division chooses the correct chunk at negative world positions | PASS |

**Artifact hashes from the tested local run:**

- `terrain_step02_full_64m.glb` — **6,024 bytes**, SHA-256 `8d8f5f4c3f18a6817f2064a85d9189a5a7141863acba3abe191242d970346150`.
- `terrain_step02_chunks.zip` — **13,824 bytes**, SHA-256 `e704c92e2095bb7b2fc11c8698f646a776cef2bbd5e46de8bc4f867b175b764c`.
- `terrain_manifest.json` — **7,716 bytes**, SHA-256 `4edc5eb336a24d1b810929606697ee8a0ca8daa2af89462d4acf998e4d0f229f`.

The generated binaries were attached to the work session for download. Source code, tests and manifest were committed to GitHub so the binaries can be regenerated. **Do not interpret passing geometric tests as proof of physics, streaming, or playable movement.**

## Acceptance and remaining work

- [x] 64 × 64 m blockout constructed from **16 separate identifiable chunks**.
- [x] Stable chunk coordinates and origins including negative indices.
- [x] Ground planes match across seams by numeric world coordinates.
- [x] Individual chunk and assembled preview GLBs can be reloaded offline.
- [x] Automated test suite passes.
- [ ] In-engine visual seam test and physically walk across chunk boundaries.
- [ ] Generate collision shapes and validate a first-person player controller (Step 07).
- [ ] Generate navigation surfaces and verify NPC traversal (Step 08).
- [ ] Chunk streaming/unloading and save/restore implementation (separate future scope).
- [ ] Android frame-time and memory profiling (Step 10).

**Caveat:** Neighboring flat chunks share geometric edge coordinates, but adjacent *closed solid slabs* contain interior coincident side faces. They are hidden from an overhead view; a final production mesh/renderer may need hidden-face removal or merged collision geometry. Tests do not establish the absence of all z-fighting/lighting seams inside a future engine.

## Next: Step 03/10 — Village and castle approach

Lay a continuous **3–4 m clear-width graybox stone path** across the existing chunks, reserve a castle-approach corridor and establish a traversable route graph. The slope/height transitions will follow in Step 04. Do not add decorative characters, final buildings or a full combat UI. Preserve chunk IDs, origins, the grid convention, and the ability to regenerate the flat graybox baseline for regression testing.
