# RPG Stats and Core Fundamentals

> **Document type:** Genre reference and starter-system proposal.
> **Status:** Documentation only. The examples in this document are **not implemented game mechanics**, and no final RPG ruleset has been approved.
> **Scope:** General-purpose role-playing games (tabletop, text-based, turn-based, action, and open-world). This repository does not yet identify a specific game or engine.
> **Last reviewed:** 2026-11-04.

## 1. What defines an RPG?

A role-playing game gives the player a character (or party), a role in a world, and consequential decisions. Progression is usually represented by changing character capabilities, relationships, equipment, resources, or access to new opportunities.

Not every RPG needs levels, classes, turn-based combat, random loot, or a fantasy setting. The important foundations are **character identity**, **actions with rules**, **meaningful outcomes**, **progression**, and **persistent consequences**.

### Core gameplay loop

1. **Observe:** Learn the current situation, goals, threats, resources, and available actions.
2. **Decide:** Choose how to explore, interact, solve a problem, or fight.
3. **Resolve:** Apply the rules, context, character abilities, and potentially randomness.
4. **Change state:** Update health, inventory, relationships, quests, world objects, and NPCs.
5. **Receive feedback:** Explain the outcome and why it happened.
6. **Progress:** Unlock opportunities, improve abilities, and return to exploration.

This loop must remain understandable even when combat is absent.

## 2. Stat categories and meanings

A **stat** is any tracked quantity or classification that determines or describes game state. Do not mix permanent attributes, temporary resources, derived values, and world-state variables in one undifferentiated collection.

### 2.1 Primary attributes

Primary attributes represent relatively stable capabilities. These are a **common example set**, not a genre-wide requirement:

| Attribute | Abbreviation | Represents | Example uses |
| --- | --- | --- | --- |
| Strength | STR | Physical power | Heavy attacks, carrying, forcing doors |
| Dexterity | DEX | Precision and coordination | Aiming, dodging, lockpicking |
| Constitution | CON | Physical resilience | HP, resistance to fatigue, poison |
| Intelligence | INT | Learned knowledge and analytical skill | Research, engineering, spell formulas |
| Wisdom | WIS | Awareness and practical judgment | Perception, intuition, survival |
| Charisma | CHA | Social presence and influence | Persuasion, negotiation, leadership |

Common alternatives include **Agility (AGI)**, **Endurance (END)**, **Perception (PER)**, **Willpower (WIL)**, **Spirit (SPI)**, and **Luck (LUK)**. Choose a set appropriate to the game's fiction. For instance, an action RPG may need AGI but not WIS; a social RPG may emphasize empathy, reputation, and negotiation rather than attack power.

**Design rule:** Every primary attribute should influence multiple real decisions. If two stats always produce the same result, merge or differentiate them. Avoid a universal “best” stat.

### 2.2 Resources (current and maximum)

| Resource | Meaning | Typical change |
| --- | --- | --- |
| Health / Hit Points (HP) | Capacity to survive injury | Damage lowers current HP; healing raises it up to max HP |
| Mana / Magic Points (MP) | Fuel for magic or supernatural abilities | Abilities spend MP; rest or recovery restores it |
| Stamina (SP) | Short-term physical exertion | Sprinting, blocking, climbing, attacking consume stamina |
| Energy / Action Points (AP) | Number or cost of actions | Recovered each turn, encounter, or time interval |
| Hunger / Thirst | Survival requirements | Rise over time; food and water mitigate them |
| Fatigue / Sleep | Longer-term exhaustion | Accumulates with activity; recovers with rest |
| Morale / Stress | Psychological state | Social events, fear, danger, successes and losses |
| Currency | Purchasing power | Earned, traded, stolen or spent |

Distinguish **current HP** from **maximum HP**. Define whether a resource regenerates in combat, outside combat, after rest, or never automatically. Use only resources that produce meaningful trade-offs.

### 2.3 Derived combat and utility stats

Derived stats come from primary attributes, gear, level, conditions, or explicit bonuses.

| Derived stat | Meaning |
| --- | --- |
| Attack power / damage | Potential damage when an attack connects |
| Accuracy / hit chance | Likelihood or ability to connect with an attack |
| Evasion | Ability to avoid a hit |
| Armor / defense | Reduction or mitigation of incoming damage |
| Critical chance | Likelihood of an enhanced hit |
| Critical damage | Strength of a critical hit |
| Attack speed | Frequency of attack opportunities |
| Movement speed | Ground covered per unit of time |
| Initiative | Relative action order in turn-based encounters |
| Resistances | Reduction or avoidance of fire, poison, fear, etc. |
| Carry capacity / encumbrance | How much equipment can be carried before penalties |
| Perception / detection | Ability to discover creatures, clues, traps, and hidden paths |
| Crafting efficiency | Time, success rate, or material efficiency for crafting |

Avoid double-counting the same modifier (for example, applying armor to hit chance **and** damage reduction without intentionally balancing both effects).

### 2.4 Noncombat and social stats

- **Skills:** Swordplay, medicine, stealth, persuasion, farming, construction, research, cooking, and similar learned proficiencies.
- **Reputation:** Standing with a faction, settlement, profession, or the public.
- **Relationships:** Trust, affection, respect, fear, loyalty, rivalry, obligations, and known history with specific NPCs.
- **Profession / trade:** Economic or occupational capabilities, licenses, and experience.
- **Knowledge:** What the character actually knows, distinct from what the player knows.
- **Alignment / values:** Optional descriptors of beliefs; do not use them as a substitute for recorded actions.
- **Status and condition:** Alive, injured, poisoned, stunned, wet, hidden, wanted, employed, indebted, and so on.
- **World influence:** Property, leadership, territory, organizational roles, legal standing, or political power.

Social systems work better when actions change specific relationships and factions, rather than a single global “good/bad” score.

## 3. Character identity and lifecycle

At minimum, a persistent character needs:

- A **stable unique ID** that never depends on display name or list position.
- A name and appropriate identity/customization fields.
- A current location and a valid spatial or narrative context.
- Base attributes, acquired skills, and any active modifiers.
- Resource values and maximums.
- Inventory, equipped items, and currency.
- Conditions, cooldowns, abilities, and quest flags.
- Relationships/faction standing where applicable.
- Progression data (level, experience, talents, achievements).
- A clear alive/downed/dead state if mortality exists.

Optional systems include origin, age, culture, species, class, occupation, background, appearance, traits, needs, injuries, personality, and lifespan. Do not assume every RPG requires a class or fantasy race.

**Separation of concerns:** Character identity, rules resolution, and presentation/UI should be separate. The UI reads authoritative game state; it does not invent or independently update stats.

## 4. Progression: how characters get stronger

Possible approaches:

| Model | How progression works | Primary trade-off |
| --- | --- | --- |
| Level and XP | Actions/quests grant XP; levels unlock upgrades | Easy to communicate; can encourage grinding |
| Skill-based | Using/training a skill increases proficiency | Organic growth; can be exploited by repetitive actions |
| Milestone | Story or world achievements unlock upgrades | Strong pacing; less granular progression |
| Equipment-based | Gear determines most capabilities | Clear loot incentive; fragile balance/gear dependency |
| Talent / perk tree | Choices grant distinct actions or advantages | Builds feel unique; requires careful prerequisites |
| Hybrid | Combines selected models | Flexible but needs clear ownership of rewards |

A level is not the same thing as a skill rank. Track them separately if both exist. Growth must have understandable causes and bounded effects. Include soft caps, hard caps, diminishing returns, or costs only where the design needs them.

Key decisions: whether respec is allowed, whether NPCs progress under the same rules, whether abilities have prerequisites, and whether the world scales with the player.

## 5. Actions, checks, and outcomes

All meaningful gameplay actions should have:

1. An **actor** (stable entity ID).
2. A **verb** (move, speak, attack, craft, trade, heal, inspect, etc.).
3. An optional **target**.
4. **Preconditions** (valid location, adequate resources, permissions, range).
5. A **cost** (time, MP, AP, stamina, durability, item quantity).
6. A **resolver** (deterministic rule or seeded randomness).
7. An **outcome** (state changes plus feedback).
8. An auditable **reason** for success, failure, or rejection.

Typical resolutions are: automatic success, threshold check, contested check, random roll with modifiers, or real-time collision/physics outcome.

### Example skill check (optional proposal)

For a d20-style game:

- Attribute modifier = `floor((attribute - 10) / 2)`.
- Total = `d20 + attribute_modifier + skill_bonus + contextual_modifiers`.
- Succeed when `total >= difficulty`.

This is **one illustrative ruleset**, not a universal RPG formula. A real-time action game may instead use input timing, attack arcs, line of sight, hitboxes, and physics. For seeded tabletop/text resolutions, record the random-number generator's state for reproducibility.

Failures should still be meaningful: a failed lockpick might consume time, break a tool, attract attention, or reveal new information.

## 6. Combat fundamentals

Combat can be turn-based, real-time, tactical, party-based, or absent entirely. If combat is included, define:

- **Encounter start/finish:** Threat detection, aggression, disengagement, fleeing, and surrender.
- **Turn/action economy:** Initiative and action limits, or time-based recovery and cooldowns.
- **Target validation:** Range, line of sight, visibility, faction hostility, and whether the target still exists.
- **Hit resolution:** Accuracy versus evasion, or physically detected hitboxes.
- **Damage:** Base power, scaling, damage type, armor, resistances, criticals, blocking, and minimum damage policy.
- **Control effects:** Stuns, knockback, slows, taunts, roots, interrupts, immunities, and stacking rules.
- **Survival:** Healing, downed state, death, revival, injury persistence, and defeat consequences.
- **AI behavior:** Threat evaluation, positioning, retreat, coordination, and resource consumption.
- **Player feedback:** Telegraphs, damage cues, clear hit/miss reasons, and readable effects.

### Example minimal turn-based formula (optional proposal)

`damage = max(0, attack_base + relevant_attribute_bonus + weapon_bonus - armor_mitigation)`

Damage is applied **only after** a successful hit. Resistances may be applied as a later distinct step. Ensure damage types, rounding, and effects are deterministic. This is not suitable as-is for every game.

**Required invariants:**

- `0 <= current_HP <= max_HP` at every state transition.
- Spend resources only when the action is accepted, unless failed-attempt costs are explicitly designed.
- One hit should not secretly deal damage twice.
- Dead or invalid targets must not accept ordinary actions.
- Status effects need explicit application, tick timing, stacking, duration, and removal rules.
- Combat and noncombat actions must follow the same authoritative state-update approach.

## 7. Inventory, items, crafting, and equipment

Items should have **stable definition IDs** (what an item is) and optionally **instance IDs** (which particular item it is). A sword template and an individual sword with durability are different concepts.

Define:

- **Item kinds:** Consumables, equipment, tools, materials, quest items, currencies.
- **Stacking:** Quantity limits, stack compatibility, weight/volume, unique instances.
- **Equipment:** Slots, requirements, bonuses, restrictions, durability, unequip rules.
- **Use effects:** Preconditions, costs, effects, and what happens when interrupted.
- **Ownership:** Character, NPC, container, merchant, world drop, or organization.
- **Crafting:** Recipe ID, input materials, workstation/tools, required skill, time, output quantity and quality, and failure/cancellation handling.
- **Trade:** Ownership transfer, currency deduction, stock, pricing, legality, and atomic transactions.

**Conservation rule:** Crafting and trading must not accidentally duplicate items or currency. Never consume ingredients and then lose the output due to an interrupted state update; commit the entire transaction or roll it back.

## 8. Exploration, quests, dialogue, and world state

A world becomes an RPG world when character choices produce persistent effects.

**Exploration:** locations, movement/travel, discoverable information, hazards, interactable objects, travel costs, maps, and fast-travel restrictions.

**Quests:** stable quest IDs, objectives, requirements, progress, mutually exclusive branches, rewards, failure states, and replayability rules. Avoid relying on display-text comparisons for quest logic.

**Dialogue:** speakers, topics, knowledge constraints, relationship conditions, choices, checks, consequences, and memory of previous interactions.

**World simulation:** in-game time, day/night, weather, schedules, resource production/consumption, settlement changes, faction conflicts, and NPC goals where required.

**NPC autonomy (advanced option):** distinguish an NPC's intent, available information, resources, plan, and actual world actions. NPCs must obey inventory, travel, construction, and time constraints rather than spawning completed results instantly. Use simulation levels of detail for large worlds; do not pretend unloaded NPCs have physically traveled unless a deterministic, accountable approximation covers their movement.

## 9. Game architecture and state integrity

An implementation-ready RPG typically needs separate responsibilities:

| Layer | Responsibilities |
| --- | --- |
| Data definitions | Immutable archetypes: items, skills, enemies, abilities, recipes |
| Entity state | Current characters, NPCs, items, relationships, locations |
| Rules engine | Validate actions, calculate outcomes, update authoritative state |
| Simulation | In-game time, schedules, world changes, NPC decisions |
| Persistence | Versioned save/load, migrations, backups, integrity |
| Presentation | UI, camera, controls, animation, audio, accessibility |
| Diagnostics/tests | Logs, seeded scenarios, assertions, profiling |

Recommended practices:

- Use **stable IDs** for entities and references.
- Prefer a **single authoritative state** over independent copies in UI, NPC logic, and saves.
- Centralize changes through **validated commands/events**.
- Use **seeded randomness** when reproducible encounters or simulations are required.
- Distinguish **game time**, **real time**, and **simulation ticks**.
- Version saved data and provide migrations before changing a shipped save schema.
- Handle missing data, deleted entities, interrupted saves, and backward compatibility.
- Record sufficient reasons/events to debug a surprising outcome.
- Keep simulation work bounded for mobile devices; unloaded areas need explicit policy.

These are architecture recommendations, **not claims that the repository currently implements them**.

## 10. Minimum viable RPG systems

A simple but complete playable slice should demonstrate:

1. Create a character with an ID, name, and a few well-defined stats.
2. Display the current situation and at least two meaningful actions.
3. Resolve an action through one consistent rule.
4. Apply an outcome to authoritative character/world state.
5. Use a resource or inventory item.
6. Progress a skill, relationship, or quest after a meaningful event.
7. Save and reload without changing results or losing state.
8. Display accurate feedback and recover gracefully from invalid actions.

**Example design-only starter stat block:**

```text
Character: Example Adventurer [stable ID: char-001]
Level: 1        XP: 0
STR: 12  DEX: 12  CON: 12  INT: 10  WIS: 10  CHA: 10
HP: 24/24       MP: 10/10        Stamina: 24/24
Equipment: training sword
Skills: melee 1, survival 1, persuasion 0
Location: village-square
Conditions: none
```

Numbers are illustrative. They are not approved balancing targets.

## 11. Quality and validation checklist

The following should be tested **when the mechanics exist**:

- [ ] All resources remain within defined boundaries.
- [ ] Attribute and item modifiers apply exactly once.
- [ ] Requirements reject invalid actions without unintended side effects.
- [ ] Deterministic actions give the same outcome with the same state/input/seed.
- [ ] Leveling and skill progression cannot be exploited by obvious duplicate reward paths.
- [ ] Equipment and consumables cannot duplicate or disappear during trades.
- [ ] Status conditions expire and stack according to documented rules.
- [ ] Quests preserve progress and branching consequences after loading.
- [ ] NPCs do not create resources, buildings, or travel without valid simulation rules.
- [ ] Save/load round-trips preserve IDs, state, active effects, and relationships.
- [ ] UI reports actual state; changing screens does not change gameplay state.
- [ ] Mobile performance remains bounded with many entities or world regions.

**Verification status:** This document has no executable tests. The boxes are future test cases, not evidence of passed tests.

## 12. Open design decisions before implementation

No option below is an adopted project decision. Record explicit owner decisions before implementing irreversible or expensive architecture:

| Decision | Options / implications |
| --- | --- |
| RPG format | Text, 2D, 3D; single-character or party; online/offline |
| Primary focus | Combat, roleplay, simulation, exploration, story, survival, or hybrid |
| Core stats | Six-attribute example above, smaller set, or custom thematic set |
| Progression | Levels/XP, skills-by-use, milestones, perks, or hybrid |
| Combat model | Turn-based, real-time, tactical, or none |
| Randomness | Seeded dice, deterministic thresholds, physics/input-driven |
| Survival needs | None, light stamina/rest, or full needs |
| Failure/death | Retry, checkpoint, injury, permanent consequence, permadeath |
| NPC simulation | Scripted, schedule-based, goal-based, or autonomous |
| Game world | Scene-based, hub-based, continuous, or streamed by region |
| Saves | Slots/autosave, serialization format, schema versioning |
| Engine/runtime | Choose only after confirming the actual project technology |

## 13. Suggested implementation sequence

**Stage A: Rules core.** Define canonical stats, IDs, character state, action schemas, validation, and tests.

**Stage B: Playable loop.** Add one location, two to three actions, resources, UI feedback, save/load, and regression tests.

**Stage C: Gameplay depth.** Add skills, progression, inventory, dialogue/quests, and either combat or another primary conflict system.

**Stage D: Living world.** Add NPC goals, time, economy, travel, simulation budgets, world-state persistence, and performance tests only after the core loop is reliable.

Treat each stage as a milestone with measurable acceptance criteria rather than a promise that it is already built.

## 14. Glossary

- **Attribute:** Broad inherent capability (STR, DEX, etc.).
- **Skill:** Trained proficiency at a narrower activity.
- **Resource:** Spendable or depletable quantity (HP, MP, stamina).
- **Derived stat:** Value calculated from other data (armor, max HP).
- **Modifier:** Contextual adjustment to a check or derived stat.
- **Condition:** Time-bound or persistent effect on an entity.
- **Action economy:** Rules governing how many actions are possible.
- **Progression:** Persistent growth in capabilities or opportunities.
- **Authoritative state:** The single reliable representation of what is true.
- **Persistence:** Storing and restoring game state correctly.

---

**Repository note:** This document records RPG fundamentals and a reversible proposed starting approach. It does not contain project-specific canon, implemented classes, configured balance, engine assumptions, or validated gameplay code. Maintain a separate decisions log when a game-specific ruleset is chosen.
