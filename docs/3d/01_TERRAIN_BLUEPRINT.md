# First-Person Voxel RPG — Phase 01: Terrain Blueprint

**Status:** DESIGN / NOT IMPLEMENTED  
**Phase:** 01 — Terrain only. Phase 02 will cover reusable 3D models, after terrain acceptance.  
**Repository:** `jbob-coder/Rpg-game`, branch `main`  
**Reference date:** 2026-11-04  
**Implementation platform:** Unknown; do **not** assume a Godot, Unity, Unreal or custom engine version.

## 0. Saved visual reference and what it is

**Image:** [first_person_voxel_rpg_reference.png (Google Drive, private)](https://drive.google.com/file/d/1EGEBCBMkPnbnE63yqvxn3rAMol3w3hPJ/view?usp=drivesdk)

- Source: image generated in this project's conversation; saved unchanged to Drive.
- Format: PNG, 1254 × 1254 pixels, 2,155,535 bytes.
- SHA-256 of the verified local source: `92413ab4461b8c0a3134a45b8d21fc2f29a154336e1cd8f3baded9bd4b4ab525`.
- Drive visibility at verification: private, not shared publicly. A repository reader may lack permission to view the image.
- **The image is a 2D concept illustration, not a `.glb` file, playable scene, editable mesh, UV atlas, or proven game screenshot.** It cannot establish exact real-world dimensions or hidden geometry.
- Desired look: **first-person 3D environment** with square/blocky/voxel-inspired terrain, geometric silhouettes, bright colors and pixel-like textures, not a flat 2D tile map.

### Observed elements relevant to terrain

Visible in the reference: a broad stone-paved route, grassy stepped embankments, raised castle terrain, river and waterfall, stone bridge crossing, distant mountainous skyline, vegetation clusters and a village-level valley. The player views the route and elevated castle from street height, with the river primarily to the right.

Visible but **outside this terrain phase:** buildings, characters, trees as individually authored mesh assets, sword, shield, chests, lanterns, signs, quest markers, minimap, inventory bar, clouds, and castle architecture. Use temporary placeholders if required to assess spatial composition.

## 1. Objective and completion definition

Build or specify a **traversable modular ground environment** matching the composition of the reference, without requiring polished character or building meshes. Its minimum navigable loop is:

**village spawn → walkable stone path → raised approach/stairs → bridge crossing and river viewpoint → accessible castle plateau → return to spawn**.

This is a proposed route, not a claim that the image already contains a continuous physical path. The reference is stylized, and the implementation must fill visibility and geometry gaps logically.

Terrain is complete **only when** scale, elevation, walkability, collision, water boundaries, section seams, asset hierarchy, and first-person readability are checked in an actual engine. At present, all are **unverified**.

## 2. Coordinate convention and provisional measurements

Everything below is a **reversible engineering proposal**, not a measurement taken from the image.

| Parameter | Proposed value | Rationale / dependency |
| --- | --- | --- |
| World units | meters | Engine-neutral metric-scale interchange |
| Axes | X = east, Y = up, -Z = north | Align castle direction with forward first-person traversal |
| Ground grid | 1 × 1 m major tiles | Predictable placement, navigation and modular GLB |
| Optional decorative detail | 0.25 m block accents | Preserve chunky geometry without excessive mesh complexity |
| Chunk footprint | 16 × 16 major tiles (16 × 16 m) | Streaming and bounds test unit |
| Initial test world | 4 × 4 chunks = 64 × 64 m | First playable terrain blockout, not final map size |
| Player eye height | about 1.65 m | Reference scale for first-person readability |
| Player collider radius | about 0.30–0.35 m | Collision clearance for paths and doors |
| Ordinary step threshold | about 0.25–0.35 m | Higher terraces require stairs or ramps |
| Main route clear width | 3–4 m target | Navigation, NPC passing and camera comfort |
| Waterbed and bridge level | set after blockout | Do not hard-code the same height across all crossings |
| Target platform | unknown; optimize provisionally for Android | Must verify project engine, hardware and frame time |

Use one coordinate system consistently; placement, physics and mesh transforms must agree. Negative world coordinates must be supported for chunks. One image pixel does not equal one in-game meter.

## 3. Terrain composition and topological layout

Top-down orientation: **north = -Z**. This sketch describes connectivity, not a screenshot-accurate metric reconstruction.

```text
                           NORTH (-Z)
               [distant mountain silhouette]
             [castle plateau / destination]
              [switchback or stair ascent]
    [west terrace] [upper path] [waterfall source]
        [village]      |        [river gorge]
        [market] -- [bridge] -- [east bank path]
        [homes ]      |        [river channel]
             [spawn and starting stone path]
                           SOUTH (+Z)
```

The bridge is an **elevation-aware crossing**: water passes beneath it, and the deck must connect both banks with no impossible jump. The castle plateau must be reachable via valid walking geometry rather than by a hidden teleport.

### Terrain zones (all may use proxy materials)

| Zone | Terrain work | Terrain acceptance |
| --- | --- | --- |
| **T01 — Village floor** | Relatively level grass/soil base; building footprints represented by pads only | Player can walk from spawn to route without snagging |
| **T02 — Stone path** | Modular paved ground strips, curves/turns, edge transitions | Continuous connected route; no floating tiles |
| **T03 — Terraces / slopes** | Chunky, stepped grassy hills and exposed stone faces | Every traversable terrace has a reachable path |
| **T04 — River course** | Recessed channel, banks, bed, water surface footprint | No accidental walk-through of deep water |
| **T05 — Bridge anchors** | Matching approach levels on both riverbanks | A provisional bridge deck can connect without a gap |
| **T06 — Waterfall cliff** | Height drop, impact area, downstream continuation | Waterfall geometry does not block route or z-fight |
| **T07 — Castle ridge / plateau** | Raised destination with switchback/stair footprint | Reachable, stable walking surface and coherent silhouette |
| **T08 — World horizon** | Distant terrain tiers/mountain proxies and hidden section boundaries | No visibly cut-off map edge during normal views |

**Terrain/prop boundary:** A tree may occupy a marked planting area, but modeling the tree belongs to Phase 02. Likewise, the bridge deck may be a temporary blockout mesh until architectural models are defined. Do not mix final character modeling into terrain delivery.

## 4. GLB and modular terrain asset contract

**GLB** is the binary packaging of glTF 2.0, useful for 3D meshes, transforms, materials and optional textures. It does **not**, by itself, prove that engine collision, navmesh, gameplay triggers, water simulation or world streaming work. Those must be authored/configured in the target runtime.

Recommended proposed asset paths (no files yet created at these paths):

```text
assets/3d/terrain/
  terrain_chunk_cx0_cz0.glb
  terrain_chunk_cx1_cz0.glb
  pieces/
    ground_grass_1m.glb
    ground_stone_1m.glb
    road_straight_4m.glb
    road_turn_4m.glb
    cliff_step_1m.glb
    riverbed_straight_4m.glb
    bank_transition_4m.glb
    stair_ramp_4m.glb
```

**Contract:**
- Chunks have an agreed local origin and identity keyed by integer `(chunk_x, chunk_z)`; world transform is resolved by chunk coordinates, not baked twice.
- Keep terrain collision geometry separate from visual detail; sloped walkable surfaces may need simple colliders rather than every visible voxel as a collision step.
- No T-junction cracks, overlapping z-fighting faces, floating edge strips or unpredictable scaled transforms at seams.
- Apply transforms before export and use consistent units, orientation, material naming and pivot placement.
- Preserve original authoring sources separately; GLB is an interchange/delivery artifact, not a substitute for editable sources.
- Use lightweight materials and intentional mesh batching/instancing; don't export every block as a unique draw call.
- Asset names and internal node IDs should remain stable for references and future model integration.

## 5. River, waterfall, traversal and collision rules

- Carve real riverbed depth and bank transitions into the terrain rather than painting blue over walkable ground.
- Use a distinct render plane/material for water; collision, buoyancy, swimming and damage remain **design decisions**.
- Keep shoreline collision/entry rules coherent so a player cannot pass through cliff walls or silently walk on deep water.
- Use an explicit bridge deck collider or placeholder walkway; never rely on visual water/bridge pixels to provide physics.
- Walkable paths must support first-person turning, backward motion and crossing each seam without collision oscillation.
- In the waterfall area, avoid a physically impossible river upstream/downstream topology; confirm elevations and flow direction before final art.
- Use simple ramp-like collision under voxel stair silhouettes where the engine's step/climb mechanics need it.
- Distant terrain is visual until a traversable area is connected and loaded; don't pretend a backdrop is reachable.

## 6. Performance and streaming assumptions

The initial **16-chunk, 64 × 64 m** test scene is a validation slice. Expanding to an open world requires measured performance and streaming semantics.

- Load visible/nearby terrain chunks; unload distant chunks only after occupants, jobs, positions and objects are persisted.
- Generate seam-compatible deterministic ground layouts or store authored terrain chunk data.
- Keep collision and navigable surfaces available ahead of the player; do not unload ground while a player or NPC stands on it.
- Do not place all decorative voxels in separate rendering objects.
- Capture frame time, draw calls, triangles, RAM use and load spikes on the actual Android target if mobile is selected.
- No fixed performance threshold has been verified; a nominal 30 FPS budget corresponds to 33.3 ms/frame and 60 FPS to 16.7 ms/frame, including all engine work.

## 7. Ordered terrain-only production tasks

| Order | Task | Artifact | Done when |
| --- | --- | --- | --- |
| 01 | [Scale calibration](STEP01_SCALE_CALIBRATION.md) | World scale note and GLB test capsule **generated; 6 geometry tests pass** | **Engine-based walkthrough still pending** |
| 02 | Graybox 64 × 64 m terrain | 16 identifiable test chunks | All terrain chunks placed and connected |
| 03 | Lay village path and castle approach | Walkable route graph | Spawn-to-plateau-to-spawn loop possible |
| 04 | Sculpt terraces and cliff faces | Heightfield/block mesh | No unreachable required terrain destinations |
| 05 | Cut river and waterfall channel | Waterbed + boundaries | Coherent banks, no floating river plane |
| 06 | Reserve bridge crossing | Bridge foundation/deck proxy | Reachable both directions with proper clearance |
| 07 | Build simplified colliders | Terrain physics | No falling through, snagging or cliff penetration |
| 08 | Define nav/traversable surfaces | Nav build or equivalent | NPC-sized agent can traverse selected destinations |
| 09 | Export one test terrain GLB | .glb with known mesh/pivot/materials | Reloaded in target runtime at matching scale |
| 10 | Run mobile and seam tests | Screenshots, logs, measured metrics | Visual route and performance evidence recorded |

**Smallest useful milestone:** graybox the village spawn, a path bend, **one** riverbank and a provisional bridge anchor; test first-person scale and collision before making the full valley.

## 8. Verification checklist — all pending

- [ ] Target engine and exact version inspected.
- [ ] Editable terrain source project exists and can be reopened.
- [ ] At least one terrain GLB exists and imports with expected orientation, materials and dimensions.
- [ ] 1 m calibration cube and player eye height verified in-engine.
- [ ] Main route is continuous, including ascent and bridge connection.
- [ ] No fall-through holes, floating tiles, invisible obstacles or unintended water walking.
- [ ] All four sides of a test chunk have clean visual/collision seams.
- [ ] Main route works moving both forward and backward in first person.
- [ ] Waterfall source is higher than the receiving river and does not visually clip.
- [ ] No abrupt visible map edge from intended first-person viewpoints.
- [ ] Android or chosen target frame-time and memory measurements captured.
- [ ] Reload/save or chunk unload does not lose terrain/world state.

Terrain-specific runtime checks remain pending. Step 01 now has a separate [scale calibration GLB generator and test report](STEP01_SCALE_CALIBRATION.md): a calibration GLB was exported and round-trip tested, but no in-engine navigation or collision test has run.

## 9. Phase boundary and next work

**Phase 01 = ground, elevation, river channel, collision, navigation and terrain GLB interoperability.** Decorative architecture and human/creature meshes are deliberately not included.

**Phase 02 = 3D model production** after terrain geometry/scale are stable. Prioritize a single reusable **character model** with an explicit GLB mesh, rig/animation requirement, scale and first-person visibility rules, then modular environment props and buildings. Use measured terrain proportions to size every model. Do not claim that the reference PNG itself contains a rigged 3D character.

### Handoff record

- **Confirmed:** 2D source image exists; image uploaded privately to Drive and metadata verified.
- **Completed:** Terrain design specification and terrain-only ordered task definitions.
- **Completed since initial plan:** Step 01 scale calibration GLB generator, 1 m reference cube, player proxy and six offline geometry tests.
- **Not completed:** Actual terrain chunks, terrain-model GLBs, collision runtime, camera controls and an engine build/test.
- **Next action:** Inspect actual engine/repository when available; implement and verify the smallest terrain graybox milestone before modeling.
