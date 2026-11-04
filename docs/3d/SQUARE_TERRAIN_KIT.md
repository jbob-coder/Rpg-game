# Square terrain GLB kit — First-person RPG

## Deliverables

- `assets/tiles/`: **9 separate** modular 3D GLB pieces at 1 × 1 m (the water tile is a flat water surface).
- `assets/chunks/`: **16 independent GLB terrain chunks**, 16 × 16 m each.
- `assets/world_64m_terrain_preview.glb`: **one assembled 64 × 64 m world GLB**, with stepped grassy hills, dirt/stone cliffs, snow peaks, winding river and an approximate waterfall.
- `assets/terrain_pixel_atlas.png`: low-resolution 64 × 64 atlas, also **embedded in the GLBs**.
- `manifest.json`: dimensions, stable IDs, world transform and checksums.
- `source/generate_square_terrain.py`: deterministic generator (no Blender required).
- `source/test_square_terrain.py`: self-contained validation tests, including chunk seam checks.

This is an **original 3D interpretation** of the user-supplied concept image, **not** a pixel-perfect or geometry-exact reconstruction from a single image.

## Piece names

| GLB filename | Purpose |
| --- | --- |
| `grass_1m.glb` | Grass top with dirt/cliff side |
| `dirt_1m.glb` | Brown soil / earth block |
| `stone_1m.glb` | Stone / cliff block |
| `bedrock_1m.glb` | Dark rock / lower layers |
| `snow_1m.glb` | White mountain snow |
| `sand_1m.glb` | Light sandy shore |
| `gravel_1m.glb` | Riverbed pebble ground |
| `mossy_stone_1m.glb` | Stone with moss-covered top |
| `water_surface_1m.glb` | Thin, textured 1 × 1 m water surface |

## Geometry conventions

- 1 glTF unit = 1 meter, **+Y up**, +X east, -Z north.
- Each solid tile is **1 m × 1 m × 1 m**, from local corner (0, 0, 0) to (1, 1, 1). Place at integer world positions for shared edges.
- Water surface tile is **1 m × 1 m** with surface at local Y=0.10; it is **not a water volume**.
- Each standalone chunk uses **local** X and Z in `[0,16]` and should be placed at `(cx*16, 0, cz*16)` using `coord` from the manifest, *exactly once*. For example: `terrain_cx-2_cz1.glb` goes at `(-32, 0, 16)`.
- The **combined world GLB is already world-positioned** from -32 to +32 on X/Z. Do not reapply chunk offsets to this preview.
- Texture atlas cells are 16 × 16 pixel art. Filtering may need **nearest-neighbor** in the target engine to retain crisp pixels.
- The river upstream is rendered at Y=2.55, lower channel at Y=0.55, with a vertical water curtain near Z=0. Water is *visual geometry only*.

## Blender inspection

In Blender: **File → Import → glTF 2.0 (.glb/.gltf)**. Import the full preview or any individual prefab. Use Material Preview to display the embedded texture. For best pixel look, turn texture interpolation to *Closest* where desired. Do not interpret the separated blocks as collision shapes.

## Game integration notes

- GLB stores renderable **mesh geometry + materials + texture**. No `CollisionShape3D`, rigid bodies, navmesh, water buoyancy, controller, game camera or streaming code is included.
- Import/export interpretation, material transparency and triangle winding should be checked in the engine actually chosen for the game.
- For a mobile game, consider greedy-meshing, hidden-face removal, LOD, instanced details and collision simplification. This generator removes internal terrain wall faces based on global neighboring heights but deliberately retains 1 m top quads for tile appearance.
- The 64 m example is a visual **blockout**. It is not a complete open world, no player-tested routes and no buildings or characters.
- Mesh blocks are voxel-style because the supplied reference depicts stepped square blocks. They can be replaced by smoother terrain later without changing the 16 m chunk coordinate scheme.

## Regeneration

Requires Python 3.10+ and these free Python libraries: `numpy`, `Pillow`, `trimesh`.

```bash
python -m pip install numpy Pillow trimesh
python source/generate_square_terrain.py --out .
python source/test_square_terrain.py
```

The generator writes the atlas, 25 GLB files, manifest and ZIP. It packages only the explicitly declared assets and source files; caches and unrelated local files are excluded. The test script regenerates assets in a clean temporary directory and verifies GLB 2.0 headers, embedded PNG textures, dimensions, 16 unique chunk IDs, world bounds, all 24 internal chunk seams, water/terrain variety and ZIP allowlist/integrity. The ZIP only includes files present at the moment of packaging; regenerate after changing source/docs.

## Evidence — 2026-11-04

**9 / 9 automated tests passed** after regenerating assets in an isolated temporary directory on 2026-11-04. This is offline mesh/asset verification, not a Blender, Godot or Android runtime test. No claim of actual first-person navigation, physics or gameplay.

## Version 2 changes

- Fixed packaging to exclude Python cache files and unrelated outputs.
- Tests rebuild the kit from tracked source; they do not trust previously generated assets.
- Verified all 24 internal chunk boundaries include the required cliff-wall faces when neighboring heights differ.
- Scene appearance and procedural terrain parameters were intentionally kept unchanged.
