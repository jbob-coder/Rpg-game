# Terrain coordinate contract — square GLB kit

**Project:** jbob-coder/Rpg-game. **Scope:** 3D terrain only; character GLB remains a separate phase.  
**Status:** coordinate helpers and five independent GLB export/reimport tests executed locally on 2026-11-04. Tests **do not** prove engine collisions or revalidate the existing 64 m generator.

## 1. Fixed conventions

- **1 glTF unit = 1 meter.** +X is east, +Y is up and -Z is north. +Z points south.
- One square terrain cell occupies **1 × 1 meter** horizontally, on the half-open interval [x, x+1) × [z, z+1).
- The corner with minimum X and minimum Z is **northwest**, not southwest. The old V2 manifest's tile-origin wording says southwest but conflicts with its own -Z=north definition. This document explicitly clarifies the orientation; the original binary assets are not changed.
- The reusable solid tile GLBs occupy local [0,1] on all three axes; their top is at local Y=1. The reusable 1 × 1 m water GLB has a visual face at local Y=0.10 and is not a water volume.
- The current assembled procedural terrain uses integer height h(x,z), with the **top of each column** at Y=h. A tile's base translation and a column's surface elevation are not interchangeable.
- The final visual style can use continuous heightfield surfaces with pixel-art textures, without changing the coordinate rules. The existing geometry is stepped, not smooth.

## 2. Cells, chunks and world positions

The current test world consists of 16 chunks on a 4 × 4 grid. Each chunk contains **16 × 16 cells**: total extent 64 × 64 m, X and Z from -32 to +32 m.

| Operation | Rule | Example |
| --- | --- | --- |
| World integer cell to chunk | cx = x // 16; cz = z // 16 | cell (-1,0) => chunk (-1,0) |
| Cell to local coordinates | lx = x - 16*cx; lz = z - 16*cz | cell (-1,0) => local (15,0) |
| Chunk origin | (16*cx, 0, 16*cz) | chunk (-2,1) => (-32,0,16) |
| Local cell to world | (16*cx+lx, 16*cz+lz) | chunk (0,0), local (3,4) => (3,4) |
| Continuous world to cell | (floor(X), floor(Z)) | (-0.01,3.9) => (-1,3) |
| Exact boundary | positive-side cell owns exact boundary | X=16 => chunk 1, local 0 |

**Use floor division, not truncation toward zero**, including for negative world coordinates. Chunk-local coordinates must stay in [0,15] per axis.

Each **standalone chunk GLB has local X/Z vertices in [0,16]**. When placed into the scene, apply its manifest origin **once**. The **combined preview GLB is already positioned in world coordinates**: never apply individual offsets again.

Implementation: [coordinates.py](../../tools/terrain/coordinates.py). The names of GLB files are identifiers, not coordinate authority; the manifest and world-to-chunk formulas are authoritative.

## 3. The three required join cases

**A — Same height:** cell A at (0,0), top Y=3; cell B at (1,0), top Y=3. Both share the edge endpoints (1,3,0) and (1,3,1). The joined terrain mesh must omit unnecessary interior walls. Individual closed cubic prefabs may have overlapping interior faces; do not render those for a large assembled terrain.

**B — Different heights:** cell A at (0,0), top Y=4; cell B at (1,0), top Y=2. Their boundary is the vertical plane X=1; the exposed cliff wall must span Y=2..4, with outward-oriented normals and no interior duplicate walls.

**C — Across chunks:** local cell (15,0) in chunk (-1,0) occupies world X [-1,0). Local cell (0,0) in chunk (0,0) occupies world X [0,1). Their shared edge is X=0. Their GLBs must have node translations (-16,0,0) and (0,0,0) respectively, applied exactly once. Compute edge heights using **global neighboring cells**, not only cells within the same chunk.

For future smooth terrain, heights must be identical at every shared **corner vertex** on neighboring cells and chunks. Shared center-column values alone do not ensure watertight sloped surfaces.

## 4. Real GLB tests

Run from the repository root after installing the existing free dependencies (numpy, trimesh):

    python -m pip install -r tools/terrain/requirements.txt
    python -m unittest discover -s tests -p 'test_terrain_coordinates.py' -v

The new [test_terrain_coordinates.py](../../tests/test_terrain_coordinates.py) includes five tests:

1. World/cell/chunk conversion, negative X/Z, exact borders and round-trip mapping.
2. Validation of nonfinite, fractional or out-of-range grid coordinates.
3. Same-height adjacent surface meshes, exported and reimported as actual GLB with equal shared-edge vertices.
4. Different-height adjacent surface meshes, with reimported exposed wall covering exactly the elevation difference.
5. Two individually localized chunk surfaces, exported and reimported as GLB, showing correct **single** world transform at a chunk boundary.

**Local evidence, 2026-11-04:** Ran 5 tests; all 5 **OK**, using trimesh 4.11.1 and numpy 2.3.5. These are independent GLB **fixtures**, not integration tests against every mesh emitted by the current generator. Earlier tests for the world kit reported nine passes; they were **not rerun here**. The generator's complete 24-seam validation must still be rerun before changing its meshes.

## 5. Integration acceptance criteria and pending work

- Maintain 1 m cells, 16 m chunks, stable identifiers and negative coordinate behavior.
- Keep standalone GLB geometry local and record the single world-space translation separately.
- Compare both sides of **all 24 internal chunk seams**, including elevation changes and correct cliff wall faces.
- For smooth terrain, share boundary vertex samples to eliminate cracks. Eliminate duplicate hidden faces and check material/UV continuity.
- Re-export and reimport GLBs, and independently verify geometry, normals, transforms, boundaries and scale.
- Engine import, visual seams, collision, movement, water physics and Android performance are **not verified**.
- No buildings, NPCs, settlements or gameplay systems are included.

**Next small task:** integrate the helper functions and boundary tests with the existing full terrain generator, regenerate the kit and rerun the full test suite before further terrain mesh/material changes. The character model remains a separate later phase.
