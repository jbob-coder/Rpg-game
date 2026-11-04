# 06 — Engine-Neutral RPG Rules Architecture

**Status:** [Option] design contracts for later implementation; no project engine selected.

## Design objectives

- One authoritative model of character, NPC and world state.
- Deterministic replay **where gameplay uses a seeded resolver**, not a claim that all physics is deterministic.
- Strict action validation and controlled mutation paths.
- Explicit identity, location, time, random generator, item ownership and event ordering.
- Versioned persistence that can evolve without breaking saves.
- Bounded simulation work for mobile devices or large worlds.
- Minimal coupling between rules, UI rendering, input and audio.

## Boundaries

| Module | Owns | Must not own |
| --- | --- | --- |
| Definition registry | Versioned stat/skill/item/recipe/rules definitions | Current character HP or inventory |
| Entity state | Stable IDs, mutable characters/items/relationships | Rules calculations |
| Action gateway | Input normalization, identity and permission validation | UI layout |
| Resolver | Explicit rules, randomness, effects | Persistent side-effect writes before commit |
| Transaction/state store | Atomic effect commit and invariant enforcement | Arbitrary user interface controls |
| World simulator | Time, NPC goals, jobs, movement and environment updates | Direct unvalidated resource creation |
| Persistence | Save schema, migrations, integrity and backup policy | Business/rules decisions |
| Presentation | Display, camera, animations, audio and input mapping | Independent shadow stats |
| Diagnostics/QA | Trace IDs, metrics, tests, replay facilities | Altering gameplay outcomes to hide errors |

## Stable-ID and reference contract

- Entities, item definitions, item instances, quests, abilities, jobs, regions and factions need separate ID namespaces.
- References must not use translated display names, array offsets, or temporary scene instance indexes.
- A removed entity requires a documented tombstone/cleanup policy.
- Item ownership must be single-valued at any committed point.
- Different NPCs referring to the same entity must resolve to the same authoritative record.

## Action command example [Illustrative JSON, not schema/API]

~~~json
{
  "command_id": "cmd-102",
  "actor_id": "npc-17",
  "action_type": "craft",
  "target_id": "workstation-9",
  "recipe_id": "foundation-woodstone",
  "submitted_tick": 901,
  "expected_state_version": 41
}
~~~

A robust flow validates the command, calculates a proposed transition, checks the current state version, applies all effects atomically, increments version and emits a single result event. Duplicate command IDs return a documented no-op or same previous result rather than duplicating materials.

## Outcome event example [Illustrative JSON]

~~~json
{
  "event_id": "evt-707",
  "caused_by_command_id": "cmd-102",
  "tick": 902,
  "actor_id": "npc-17",
  "kind": "craft_job_started",
  "job_id": "job-53",
  "reserved_inputs": [{"item_def_id": "wood", "quantity": 2}],
  "result_state_version": 42
}
~~~

These JSON payloads are **examples**; they are not executable schema definitions and are not installed APIs.

## Mutation and derived stat handling

A mutation should come from one validated command/system tick. Stage all state effects, validate invariants, commit once and notify subscribers. Derived stats can be computed on demand or cached with an invalidation graph; they should not become independent competing sources of truth.

For stacking modifiers use stable source IDs and phase order. Example: base + equipment + condition, then multipliers, then caps/rounding. Do not let combat and UI disagree about the final number.

## Time, randomness and ordering

- Declare tick duration and ordering: environment -> NPC planning -> movement/jobs -> effects/expiration -> persistence hooks (or another chosen order).
- Use a seedable PRNG and record its state for mechanics requiring reproducible outcomes.
- Avoid drawing random numbers during UI refresh or logging.
- For physics-dependent games, test reproducible *gameplay invariants* instead of claiming frame-perfect determinism across all devices.
- Use stable conflict resolution for simultaneous item claims or occupation of scarce workstations.

## Save and migration contract

Required persisted concepts depend on selected game but may include: schema version, world clock, PRNG state, entity IDs/state, regions/locations, inventory/ownership, quest progression, active status effects, jobs/reservations, relationships, and event checkpoints.

Save via temporary complete snapshot + validation + atomic swap when supported. Never truncate the sole good save before the replacement is durable. Provide backups/checksums where useful. Migrate old schema through versioned transforms; preserve unknown values only under an explicit compatibility policy.

### Loaded world reconciliation

1. Check schema version/parse and integrity.
2. Migrate known versions.
3. Validate references (missing locations/items/NPCs).
4. Restore jobs, reservations and resource caps.
5. Rebuild derived indexes/caches from authoritative state.
6. Resume ticks with bounded off-screen catch-up.
7. Compare invariants before exposing controls.

## Interfaces for future implementation

Before coding, formally decide and document:

- Stat registry schema (key, type, unit, caps, dependencies, writer, persistence).
- Command schema and failure codes.
- Event and save schema/version conventions.
- Timing model and authoritative tick policy.
- What state UI may read but must not mutate.
- Inter-module ownership and test harness strategy.

## Deployment and platform independence

This repository is a design reference; do not assume Python, Kotlin, Godot, Unity or JavaScript. Interface concepts transfer, but code and lifecycle APIs must be verified against the actual chosen project, engine version and branch.

See [validation](07_TESTING_AND_VALIDATION.md) and [open decisions](08_DECISIONS_AND_ROADMAP.md).
