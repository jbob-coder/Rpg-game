# 02 — RPG Statistics: Taxonomy and Design Contracts

**Status:** Cross-genre catalog, not a required final stat list.

## What counts as a stat?

A stat is a value or tag that changes what the game can do, what it can show, or what it can remember. Do not treat every stat as a levelable attribute.

| Category | Definition | Examples | Persistence |
| --- | --- | --- | --- |
| **Identity** | Stable reference/descriptive data | entity_id, species, origin, occupation | Mostly permanent |
| **Primary attributes** | Broad base capabilities | STR, DEX, WIL, PER, intellect, empathy | Persist; modify rarely |
| **Skills/proficiencies** | Learned activity competence | surgery, swordplay, negotiation, masonry | Persist/progress |
| **Resources** | Current quantities with spending/recovery rules | HP, MP, stamina, AP, mana, currency | Current/max as appropriate |
| **Derived stats** | Calculated from other values | attack accuracy, armor, carry limit, walk speed | Usually recomputable |
| **Conditions** | Temporary modifiers/permissions | wounded, stunned, soaked, invisible, downed | Persist if ongoing |
| **Traits/tags** | Discrete qualities and narrative constraints | oathbound, night-blind, wanted, licensed | Persist as relevant |
| **Relationships** | Directed ties to specific entities | trust, loyalty, fear, debt | Persist with IDs |
| **Reputation/legal standing** | Public or institutional assessment | faction reputation, crime heat, citizenship | Persist by faction/region |
| **Knowledge** | Known facts with source and certainty | map discovered, secret learned, recipe known | Persist |
| **Economic/world state** | Entity ownership, production and conditions | stock, prices, land, territory, crop quality | Persist in world |
| **Progression** | Growth-related accounting | level, XP, perks, skill XP, mastery | Persist |
| **Control/runtime** | Simulation-specific data | cooldown timer, action queue, next wake tick | Persist if necessary |

### Primary-attribute candidates — examples, not a universal list

| Candidate | Measures | Risk of overlap |
| --- | --- | --- |
| Strength / Power | Force, lifting, physical impact | Weapon damage |
| Agility / Dexterity | Coordination, balance, precision | Speed, aim, evasion |
| Endurance / Constitution | Physical hardiness and capacity | HP, stamina, resistances |
| Intelligence / Reason | Analysis, memory, formal learning | Knowledge, crafting |
| Perception / Awareness | Detecting environmental signals | Wisdom, survival |
| Wisdom / Judgment | Interpretation and practical choices | Perception, will |
| Willpower / Resolve | Resistance to coercion, fear or temptation | Morale, stress |
| Charisma / Presence | Public influence and expression | Persuasion, leadership |
| Empathy / Social insight | Understanding others | Charisma, perception |
| Luck / Fortune | Randomness modifier or fate-like budget | Generic success chance |
| Spirit / Attunement | Supernatural affinity, if relevant | Willpower, magic capacity |

**Rule:** only add a candidate if it has independent gameplay effects and the player can understand what decisions it changes. Physical, social and mental stats are not required to share a numerical scale.

### Derived/combat catalog

**Offense:** base damage, hit chance/accuracy, weapon reach, attack speed, penetration, stagger, critical chance, critical effect, damage type, area of effect, spell power.

**Defense:** armor, guard/block, dodge/evasion, resistance by damage type, status resistance, poise, shield capacity, healing received, cover.

**Mobility/utility:** movement rate, acceleration, jump/climb, carrying capacity, encumbrance, stealth, detection, vision, noise, crafting throughput, gathering speed, interaction reach.

**Recovery/economy:** HP regeneration, stamina recovery, MP regeneration, cooldown recovery, durability, vendor price adjustment, income, upkeep, inventory weight.

These are names only; a particular rules engine must specify units, ranges and interactions.

### Social/life/world catalog

- **Personal:** health/injury, hunger, thirst, exhaustion, stress, mood, safety, age and life stage (if the game models them).
- **Capabilities:** education, expertise, profession proficiency, learned languages, licenses, tool access.
- **Social:** relationship-by-target, family/household membership, influence, rank, reputation by faction, favor, obligations, reputation decay.
- **Economic:** money, assets, debts, supply, production rate, transport capacity, maintenance cost, labor availability.
- **Spatial:** location ID, region, world coordinate, current destination, route, movement mode, loaded/unloaded simulation tier.
- **Information:** known facts, information provenance, fog of war, witnessed acts, rumors with confidence.
- **Institutional:** citizenship, legal rights, titles, territory control, organization role, law/permissions.

**Guardrail:** mental-health or social traits should not be confused with biological certainties or used as deterministic predictions of real human behavior. These are fictional game mechanics.

## Required stat contract (template)

For any stat added to an actual game, document:

| Field | Example for HP (illustrative) |
| --- | --- |
| Stable key / namespace | resource.hp_current |
| Owner / scope | individual actor |
| Data type and unit | integer hit points |
| Valid range | 0 through resource.hp_max |
| Default and source | character creation/base form; no assumption about class |
| Calculation | resource.hp_max from explicit selected ruleset |
| Writers | damage resolver, healing resolver, status expiration |
| Readers | combat, AI survival behavior, UI, death rules |
| Dependencies | max HP, injury conditions, armor mitigation |
| Update timing | committed action/tick |
| Persistence policy | store current; validate max on load |
| Modifier and stacking rule | ordered, named categories; one contribution per source |
| Display rule | current/max; visible to player only when intended |
| Test rule | never below zero or above max |

**Not all fields are numeric:** reputation may be a per-faction score; allegiance may be an enum; a profession may be a set of qualifications.

## Dependency graph example [Illustrative]

- constitution -> maximum HP -> survival budget -> healing strategy
- dexterity -> accuracy + evasion -> expected combat survival
- skill.masonry + workstation + materials + time -> construction action
- trust(target) + witnessed_event + current law -> willingness to cooperate
- carry_capacity + inventory_weight -> encumbrance -> speed

These are **possible**, not imposed, dependencies. If a value influences nothing, remove it or make its purpose explicit. If a modifier reaches the same derived value along multiple paths, check double-counting.

## Stacking/priority policy

Document the exact order: **base -> additive modifiers -> multiplicative modifiers -> caps -> rounding** (or an explicitly different policy). Each source should have an ID. Mutually exclusive states (e.g. burning and soaked, if designed as such) need reconciliation rules. Do not round between steps without explaining the effect.

Example [Illustrative]: base speed 5 m/s + flat 1 m/s, then a 0.8 slow gives (5+1)*0.8 = 4.8 m/s. Multiplying before adding produces 5 m/s; that is a different ruleset, not a small display difference.

## Example character *not adopted*

An illustrative character has Identity (ID "demo-1"), 3 broad attributes (Power 2, Insight 3, Resolve 1), 2 skills (Masonry 3, Mediation 1), resources (HP 12/12, stamina 6/6), location (settlement-1), and relationship trust with actor "npc-2" of +1. This makes clearer sense for a town-building social RPG than adding a mandatory critical-hit stat.

## Failure cases to test

- Negative quantities, zero denominator, missing max values, stale derived caches.
- Loading a save after a stat definition changes or disappears.
- Multiple modifiers from one item applied more than once.
- Unknown entity IDs in relationships/ownership.
- Infinite/NaN floating values in derived calculations.
- Resource cap reduced below current resource; define clamp or overflow policy.
- Implicit coupling of UI labels to stat lookup keys.
- Permanent character values mixed with temporary status modifiers.

See [mathematical rules](03_RESOLUTION_MATH_AND_BALANCE.md), [architecture contracts](06_ARCHITECTURE_CONTRACTS.md), and [test plan](07_TESTING_AND_VALIDATION.md).
