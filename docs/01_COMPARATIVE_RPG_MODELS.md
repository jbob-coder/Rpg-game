# 01 — Comparative RPG Models

**Scope:** Research-based comparisons. Published systems provide *examples*, not a mandate to reproduce their intellectual property. Links and edition notes: [Sources](SOURCES.md).

## Why no universal RPG stat sheet exists

An RPG can emphasize tactical optimization, expressive characterization, skill practice, survival, a social economy or a fictional world that remembers choices. Numeric attributes are **a tool**, not the defining requirement. Some designs do not use combat stats or character levels at all.

## Published examples

| Model and source | Character representation | Action resolution | Consequence/progression emphasis | Trade-off |
| --- | --- | --- | --- | --- |
| **D&D Fifth Edition (2024 Basic Rules)** [Observed] | Six abilities; skills/proficiency, class/background; HP and features | d20 + modifiers versus target | Class features and level-based progression | Readable character builds; balance and level scaling need care |
| **Pathfinder Second Edition** [Observed] | Attribute modifiers and proficiency ranks; features and equipment | d20 against DC; four degrees of success | Tactical choices, degrees and proficiencies | Deep tactical expression; large rule surface |
| **Basic Roleplaying, Universal Game Engine** [Observed] | Characteristics and rated skills | d100 roll against a percentage rating | Practice/experience-based skill advancement is prominent | Intuitive success percentages; advancement and opposed rules need care |
| **Fate Core** [Observed] | Skills, descriptive aspects, stunts, stress/consequences and fate points | Four Fate dice + skill; invoke aspects for resource-based influence | Dramatic consequences and fiction-first aspects | Flexible fiction; less granular physical simulation |
| **Blades in the Dark** [Observed] | Action ratings, stress, load, contacts, crew-level structures | d6 pools; result determines outcome; position sets risk, effect sets impact | Complications, progress clocks, stress and fiction | Strong risk/reward pacing; less emphasis on conventional attack/armor |

**Important edition distinction:** The D&D source in this table refers to the **2024 Basic Rules**; do not apply 2014 rules to 2024 without checking changes. Pathfinder Remaster maintains PF2e's core identity while changing some terminology. Read the cited edition before exact mechanical implementation.

## Genre lenses (design patterns, not named-game rules)

| RPG focus | Questions players optimize | Useful stats/records | Often unnecessary |
| --- | --- | --- | --- |
| Tactical/party CRPG | Position, action economy, party synergy | Initiative, AP, range, accuracy, defenses, status durations | Detailed survival simulation |
| Real-time action RPG | Timing, build synergy, movement and risk | HP, stamina, cooldowns, hitboxes, resistances, movement state | Universal d20 checks |
| Story/narrative RPG | Stakes, relationships, identity, obligations | Aspects/tags, skills, trust, stress, clocks, consequences | Damage-per-second |
| Life/social simulation RPG | Career, household, opportunity, social consequences | Needs, traits, education, finances, knowledge, relationships | Classes, magic, critical hit chance |
| Survival/sandbox RPG | Logistics, travel, crafting, settlement choices | Capacity, materials, needs, durability, position, time | Fixed campaign milestones |
| Kingdom/economy simulation RPG | Scarcity, production, legitimacy, coordination | Ownership, stock, throughput, population, trust, law | Individual attack animation speed |

An actual game may combine lenses, but each additional tracked variable must have a meaningful effect and a player-facing explanation.

## Choosing a model: compare before coding

For each candidate model, score 0–3 on: **fit for the core loop**, player comprehensibility, support for meaningful choices, system interoperability, implementation/test complexity, ability to support NPC rules, and performance on target hardware. Weight the fit for core loop most heavily; the smallest model meeting the target is generally safer than a hybrid of everything.

### Design comparison — three example choices

- [Option A] **Compact narrative model:** 3–6 broad approaches + tags + consequences, no levels. Favor when decisions/story matter more than quantitative gear power.
- [Option B] **Tactical numeric model:** distinct attributes, combat resources, skills, ability prerequisites, action economy and progression. Favor when combat and builds drive play.
- [Option C] **Living-world model:** occupation/skill/knowledge, needs, relationships, material stocks, agency and time; combat may use a lightweight module. Favor when NPCs and settlement continuity drive play.

These are proposed patterns, **not** actual mechanics in this repository.

## Anti-patterns

- **Cargo-cult six stats:** Copying STR/DEX/CON/INT/WIS/CHA for an RPG whose core game is politics or crafting.
- **Duplicate stats:** Evasion and dodge each grant the same independent defense without a clear distinction.
- **Dominant attribute:** One stat controls almost every high-value interaction.
- **Excessive granularity:** Tracking dozens of variables that never affect choices.
- **Incompatible mixes:** D&D's d20 values inserted directly into percentile checks without normalizing and documenting conversion.
- **Genre blindness:** Reusing real-time combat cooldowns in a turn-based game without revisiting action economy.

## Questions before adopting a ruleset

1. What are the player's three most common consequential actions?
2. Should outcomes be more influenced by build, planning, skillful inputs, randomness or narrative choices?
3. What information can the character know that the player does not, and vice versa?
4. Must NPCs follow identical mechanics? If not, which invariants are shared?
5. How are failure, recovery and persistent consequence supposed to feel?
6. What must be simulated exactly, and what can be approximated?

See [statistics](02_STATISTICS_TAXONOMY.md) and [decisions](08_DECISIONS_AND_ROADMAP.md).
