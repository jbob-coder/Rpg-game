# 05 — Character Development, NPC Autonomy and Persistent World

**Status:** Simulation systems reference, not a claim of existing AI behavior.

## Character lifecycle models

Characters can be adults at the start, progress from childhood, age over time, or exist outside biological lifecycles. Optional state includes birth/origin, family IDs, education, learned abilities, social roles, injury, disease, aging, occupation and death/inheritance.

Keep **identity** independent from current role and stats. A stable ID survives name changes, movement, job changes and save/load. No mandatory progression model applies to every RPG.

**Important separation:** player-accessible information is not identical to character knowledge. Native NPCs need not possess the player's interface to make world-valid decisions.

## NPC autonomy spectrum

| Tier | Capability | Suitable scope | Failure mode |
| --- | --- | --- | --- |
| 0 — Decorative | Plays idle animations/dialogue | Background crowds | Feels lifeless if relied on for world |
| 1 — Routine | Follows schedules and destinations | Shops, town ambience | No response to unexpected events |
| 2 — Reactive | Responds to threats, needs and dialogue | Small local encounters | State oscillation or repetitive loops |
| 3 — Goal-based | Chooses goals and prerequisite tasks | Workers, merchants, guards | Impossible goals or resource cheating |
| 4 — Social/economic agent | Coordinates, trades, learns, negotiates | Living settlements | Deadlocks, runaway wealth/politics |
| 5 — Multi-scale simulation | Plans at local and regional resolution with persistence | Large worlds | Off-screen continuity illusions |

A high tier is not automatically better. Choose based on game experience, predictability, budget and player observability.

## Intent -> plan -> action -> outcome

1. **Perceive:** sample visible/audible events and retained memories only within NPC's information constraints.
2. **Assess:** internal needs, safety, obligations, relationships, faction constraints, time and available resources.
3. **Choose a goal:** safety, food, shelter, work, socialization, learning, trade, construction or leadership, scored by urgency/utility.
4. **Plan prerequisites:** gather materials -> obtain tool -> travel to site -> work -> complete.
5. **Validate:** legal permission, ownership, reachability, transport, workspace, time and task reservations.
6. **Execute incrementally:** move, craft, negotiate or work using the same world-state APIs as relevant player actions.
7. **Observe/replan:** handle blocked paths, missing resources, contested targets, failure or new dangers.
8. **Record:** actual state transitions, memories, ownership changes and whether others could witness them.

**Example:** A hungry woodworker cannot instantly build a house upon collecting enough logs. The plan also requires land/access, compatible tools and construction recipes, stone if prescribed, reachable site, staged work and elapsed world time.

## Goal-choice design

**Illustrative** utility score: 3*safety_urgency + 2*hunger_urgency + relationship_need - travel_cost - resource_shortfall. Scores need normalization; always specify time and units. A high score does not bypass preconditions.

Use explicit priority for emergencies, hysteresis/cooldowns for goals, failed-plan backoff, and a stuck-state recovery path. NPCs must not execute the same failed action every frame.

**Autonomy ≠ arbitrary randomness.** A useful NPC exhibits agency within identity, knowledge, preferences, available means, law and consequences.

## Knowledge, relationships and social propagation

- NPC knowledge must have a provenance (direct observation, conversation, institution, inference), time and optional uncertainty.
- Relationships are directional records with target IDs; they can conflict.
- Rumor propagation requires a sender, recipient, event, latency and possible distortion; do not give instant omniscience by default.
- Professions require competence, access to inputs, customers and reasons to work.
- Leaders can be selected by rules, election/appointment, prestige, violence or inheritance depending on fictional institutions, not by globally scripted titles alone.
- Settlements require land, structures, population, material flows, food and governance states; rendered buildings alone are insufficient.

## Spatial simulation and pathfinding

Track region/section, local coordinates, intended destination, movement progress, current nav version and failed-route count. Collision and obstacles must be authoritative; visual animation cannot stand in for actual position changes.

For failure to move: confirm target is reachable -> request alternate path -> retry with budget -> choose another task or report blocked. Do not infinite-loop.

### Multi-scale world updates [Option]

- **Tier A:** Close/visible entities simulated with physics/animation and frequent decisions.
- **Tier B:** Nearby off-screen entities with movement and jobs simulated at lower tick rate.
- **Tier C:** Distant entities represented by planned arrival, production jobs, stock transfers and event timestamps.
- **Tier D:** Dormant regions rehydrated from saved state using explicit rules for elapsed time.

Moving between tiers must preserve **time, position plausibility, material ownership, event order, survival, and identity**. A distant town cannot both consume and spend the same inventory twice during reactivation.

Simulate world hours explicitly; cap catch-up to a bounded budget if the device was offline for long periods. Use clear approximation policies, not fabricated step-by-step traces.

## Core consistency properties

- One item at one owner/location at a time; no free creation through state rehydration.
- One authoritative alive/dead state and coherent condition transitions.
- No ungrounded teleportation, instant building, or instant global knowledge.
- Time spent traveling, building and crafting must be accounted for.
- A change to an NPC's profession or location must not change their entity ID.
- Decisions made off-screen must be replayable/reconcilable or explicitly marked approximate.
- The player can observe at least some causal consequences of the simulated world.

## Simulation quality metrics

Measure: tasks completed per NPC-hour, idle-without-reason %, path failures and recovery time, material balance errors, house construction duration, settlement supply deficits, population/occupation ratios, faction interaction density, CPU ms/tick, and save/reload divergence.

Do not infer "alive world" from NPC count. Demonstrate causality with an observable trace: an NPC needs shelter -> acquires resources legally -> transports materials -> constructs over time -> occupies and maintains the building.

See [mechanics](04_GAMEPLAY_SYSTEMS.md), [architecture](06_ARCHITECTURE_CONTRACTS.md) and [test cases](07_TESTING_AND_VALIDATION.md).
