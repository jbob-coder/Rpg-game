# RPG Systems Reference — Index

**Purpose:** Cross-genre research and design reference for role-playing systems; not a playable game, engine, or approved ruleset.

**Status:** Reference material and explicitly marked design proposals. Repo currently has no verified gameplay implementation. **Revision:** 2026-11-04.

## Start here

| Topic | Document | Question answered |
| --- | --- | --- |
| Genre and system comparison | [01 — RPG models](01_COMPARATIVE_RPG_MODELS.md) | Which RPG paradigm suits a design goal? |
| Stat catalog and definitions | [02 — Statistics taxonomy](02_STATISTICS_TAXONOMY.md) | What stats exist and how do they differ? |
| Resolution, formulas, and balancing | [03 — Mathematics](03_RESOLUTION_MATH_AND_BALANCE.md) | How do actions and numbers resolve? |
| Player-facing mechanics | [04 — Gameplay systems](04_GAMEPLAY_SYSTEMS.md) | What gameplay contracts depend on what? |
| Character/NPC/world continuity | [05 — Living world](05_CHARACTER_NPC_WORLD.md) | How do agency, knowledge, and time interact? |
| Engine-neutral implementation | [06 — Architecture](06_ARCHITECTURE_CONTRACTS.md) | How can a rules engine preserve consistent state? |
| Testable design & QA | 07 — Validation (planned, not yet written) | How do we detect broken or exploitative systems? |
| Decisions and delivery plan | 08 — Decisions (planned, not yet written) | What remains open before project-specific code? |
| Primary research and source limits | Sources (planned, not yet written) | What evidence supports comparative claims? |
| Earlier introductory overview | [Legacy RPG overview](RPG_STATS_AND_FUNDAMENTALS.md) | What was originally documented? |
| First-person 3D world | [Phase 01 — Terrain blueprint](3d/01_TERRAIN_BLUEPRINT.md) | How to build the terrain before character/models? |
| Terrain Step 01/10 | [Scale calibration](3d/STEP01_SCALE_CALIBRATION.md) | What meter scale, player height and path widths were generated and tested? |

## Voxel RPG reference asset

[First-person concept PNG (private Google Drive)](https://drive.google.com/file/d/1EGEBCBMkPnbnE63yqvxn3rAMol3w3hPJ/view?usp=drivesdk). The concept is not a GLB. The terrain blueprint defines phase 01; 3D models are phase 02 and remain pending.

## Classification labels

- **[Observed]**: sourced example in a published system; check edition/source.
- **[Pattern]**: generalization based on multiple RPG approaches, not universal law.
- **[Option]**: one viable design choice; not adopted by owner.
- **[Illustrative]**: invented example/formula for teaching; not an official rule or implemented code.
- **[Decision needed]**: design cannot be locked without project requirements.
- **[Verified implementation]**: requires actual source inspection and executable evidence; none claimed in this reference repository.

## Usage rules

1. Start with the genre, intended experience and player loop; do not start by copying D&D attributes.
2. Select a resolution model and decide which **kinds** of stats it needs.
3. Write an explicit contract for each statistic: ID, scope, type/unit, range, origin, calculation, update event, persistence, stacking, use cases and display.
4. Link mechanics via a dependency map; test boundaries, exploits and save/load.
5. Adopt rules **per game**, version decisions, and document deviations. Do not silently turn these examples into universal canon.
6. Keep copyrighted game text out of this repository. Summarize rules briefly, link to primary sources, and distinguish our original templates.

## Out of scope / current evidence

- No actual RPG engine, API, mobile build, stat implementation, save migration or runtime test is established here.
- No universal "complete list" of RPG stats exists: stat names and meanings vary by game.
- These notes can inform separate projects, but they do **not** change rules in other game repositories.
- The earlier overview is retained for traceability; the specialized documents above are the preferred detailed reference.

## Maintenance

When adding a rule example, state its model, assumptions, source/edition (where external), formula, worked input/output, and a testable invariant. Keep references internal and update the index if adding a new domain. 
