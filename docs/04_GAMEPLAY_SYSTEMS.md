# 04 — RPG Gameplay Systems and Dependencies

**Status:** Architectural reference: *what* a mechanic must answer, not a claim that it exists in this repository. For stat contracts see [02](02_STATISTICS_TAXONOMY.md).

## Action lifecycle — shared contract

Regardless of whether the game is text, real-time, turn-based, or simulation-led:

1. **Intent:** actor ID, action kind, target ID/position, context, selected options.
2. **Eligibility:** actor alive/valid, permission, knowledge, ownership, range, resources, location, timing.
3. **Cost/risk declaration:** stamina/time/materials, possible failure consequences, collision or check type.
4. **Resolution:** model-specific deterministic calculation or saved-seed roll/physics.
5. **Atomic outcome:** apply state changes once; consume resources once; either complete transaction or revert.
6. **Feedback:** explain what happened with accessible cues; do not leak hidden game knowledge.
7. **Persistence/events:** record relevant facts, transactions, cooldowns, quest triggers and observed consequences.

**Invariants:** No rejected action mutates state unless the rejection itself has an explicit rule; no invalid target should silently succeed. Repeat submission must not duplicate unique rewards.

## Combat and conflict

**Design choices:** turn-based / real-time / tactical / noncombat; PvE / cooperative / PvP; lethal / nonlethal; deterministic / stochastic; single-character / party.

| Layer | Required definition | Frequent defect |
| --- | --- | --- |
| Encounter | Detection, hostile status, entry/exit, surrender | Eternal aggro without exit path |
| Timing | Initiative/AP or simulation time, cooldown policy | Double action or desync |
| Targeting | Reach, visibility, collision, friendly fire | Attacking dead/invisible targets |
| Accuracy | Hit rules, dodge, block and counters | Multiple independent chances not balanced |
| Harm | Damage type, armor, resistances, wounds, healing | Double mitigation or negative HP |
| Effects | Application, stacking, duration, expiration, immunity | Buff lasts forever |
| Defeat | Downed, death, retreat, respawn, looting | Rewards twice after reload |
| Enemy behavior | Intent, telegraph, threat, spacing and recovery | Enemy stuck at wall or instant action |

**Other conflict models:** debates, legal disputes, competitions, negotiations, and survival crises can use stakes, clocks, relationships and resources without HP damage.

## Ability, class, talent and progression

Separate **access** (may a character invoke this ability?) from **capability** (how effectively?) and **cost** (what is consumed?). Class may define an archetype, but **classlessness is valid**. Record prerequisites, effect, cooldown, cost, training rule, respec rule and presentation.

A skill rank should not silently stand in for character level; keep distinct if both appear. Choose how NPCs progress, whether time-based learning counts, and whether repeated trivial actions can be exploited.

## Inventory, equipment, loot and economy

- **Definitions vs instances:** item definition "iron_sword" can spawn many instances with separate IDs/durability.
- **Containers:** stable owners, item counts, quantity precision, weight/volume and capacity.
- **Equipment:** explicit slot constraints, requirements, equip/unequip events and modifier sources.
- **Loot:** drop generation seed, reward entitlement, pickup rights, loot persistence and anti-duplication.
- **Trade:** debit and credit in one operation; validate balance, available stock, ownership and price snapshot.
- **Currency:** distinguish physical coins, account balance, faction credit, and debt if relevant.
- **Economy:** production, consumption, transport, taxes, wages, storage, scarcity and economic sinks are separate systems. Wealth should not appear without a defined source unless configured as deliberate world generation.

### Crafting/construction transaction example [Illustrative]

**Recipe:** 2 wood + 1 stone + 10 minutes -> 1 foundation component (not an instant complete house).

Preconditions: worker knows recipe, tools/workstation valid, required materials available and reserved, construction site reachable, enough work time. Start action reserves materials; progress is tracked over time; completion consumes reserved inputs and creates output once. Interruption follows documented cancellation/refund policy. Persist job and reservations to prevent load/save duplication.

**Balance equation:** inventory_before - consumed + produced = inventory_after for each item type, accounting for world drops/trades explicitly.

## Exploration/navigation/world interaction

- Space: region ID, coordinate system, traversability, path cost, portals, streaming boundaries, interior links.
- Movement: input intent, collision, dynamic obstacles, movement capabilities, navigation recalculation, stuck recovery.
- Discovery: player knowledge and NPC knowledge may differ; persist fog of war and examined objects.
- Time: explicit seconds/ticks/turns and advancement triggers; moving through unloaded regions must have a time/cost explanation.
- Encounters: spawn budgets, uniqueness, persistence, despawn rules and save/load boundaries.
- Environments: hazards, weather, lighting, temperature, visibility and environmental interactions only where they matter.

Avoid the appearance of a large world composed only of random empty terrain: traversal should lead to distinct decisions, discoveries or relationships.

## Quests, dialogue and narrative consequences

**Quest contract:** stable quest ID, eligibility, objectives, progress event sources, branches, success/fail/abandoned states, rewards paid once, persistent consequences. Quest flags must not rely on mutable UI text.

**Dialogue contract:** speaker/listener, available knowledge, interpersonal relation, legal/social context, skill/ability preconditions, costs/risks, outcome and memory. Branches should be allowed to alter the world, not just flavor text.

**Decision consequence contract:** affected entity IDs, timestamp, observed witnesses, legal/faction implications, reversible/irreversible effects, save-state impact, and how the player learns about it.

## Social systems

Relations should be directional and person-specific: A trusting B does not imply B trusting A. Distinguish familiarity, trust, friendship, affection, loyalty, fear, respect, debt and public reputation. Define who witnessed an act; do not globally notify every NPC unless the fiction supports global communication.

## Audio, UX, accessibility and input

Document combat telegraphs, UI latency, controller/mobile mapping, touch hit targets, readable stat descriptions, alternatives to color-only feedback, sound cues, pause behavior and screen-size scaling. Stat meaning should be discoverable without requiring players to read the source.

## Dependency map

| If introducing... | Also design... |
| --- | --- |
| Weapon durability | Repair, failure, UI, economy and persistence |
| Hunger/thirst | Food/water sources, costs, rest, off-screen time and fairness |
| Classes | Progression, skills, prerequisites, enemy/party balance and respec |
| Stealth | Visibility, hearing, NPC perception, detection states and memory |
| Crafting/building | Recipes, material conservation, job progress, pathing and ownership |
| Reputation | Witnesses, rumor propagation, privacy, factions and consequences |
| Open-world travel | Coordinates, streaming, pathing, persistence and performance budgets |
| Death/permadeath | Save handling, recovery/continuity, quest failure and NPC inheritance |

## Reference vs implementation

This file supplies contracts and failure modes. It does **not** select an engine, combat model, class list or skill names. See [architecture](06_ARCHITECTURE_CONTRACTS.md) and [verification](07_TESTING_AND_VALIDATION.md).
