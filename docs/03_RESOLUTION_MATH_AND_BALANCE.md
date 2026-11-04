# 03 — Action Resolution, Probability and Balancing

**Status:** Comparative research + original, explicitly **illustrative** models. Never copy a formula into a game without choosing its scope, exception rules and test cases.

## Five resolution families

1. **Deterministic threshold** [Pattern]: requirements + attribute/skill total >= target. Best when careful planning should eliminate randomness. For example 8 skill points against requirement 6 succeeds.
2. **Uniform d20 checks** [Observed in D&D/PF2e]: d20 + bonuses vs DC; the value of +1 depends on caps and rules for natural rolls.
3. **Percentile roll-under** [Observed in Basic Roleplaying]: roll 1..100 and succeed if roll <= adjusted skill chance, subject to system-specific critical/fumble exceptions.
4. **Dice pool** [Observed in Blades]: roll multiple d6, choose highest, outcome bands. The number of dice changes the outcome distribution nonlinearly.
5. **Fiction-first/aspect-influenced** [Observed in Fate]: evaluate fictional permission and consequences; a currency can influence a check. Fate Core uses four Fate dice with skill and aspects.

**No single option is automatically more realistic or fair.** Choose based on player feedback, failure frequency, pacing and control.

## Worked probability calculations [Illustrative, *not* official rules]

### d20 threshold without automatic 1/20 behavior

For a uniform integer roll R in {1,...,20}, modifier M and target DC:

P(success) = clamp((21 - (DC - M))/20, 0, 1), **when DC-M is an integer**.

For R+3 >= 15, R must be 12 through 20: 9 successful faces / 20 = **45%**.

If natural 1 or natural 20 change results, the formula must incorporate those separate rules; neither D&D nor PF2e should be assumed to use this simplified probability in every circumstance.

### Percentile roll-under without exception rules

For chance 65 and uniform R in {1,...,100}: P(R <= 65) = **65%**. This teaching example ignores BRP-specific rules governing criticals, fumbles, modifiers and edge cases.

### Largest die in a d6 pool

For n independent fair d6 and success defined as "at least one six": P = 1 - (5/6)^n. With 3 dice, P = 1 - 125/216 = 91/216 = **42.13%**.

With two dice, P(highest >= 4) = 1 - (3/6)^2 = **75%** and P(at least one six) = 1 - (5/6)^2 = **30.56%**. This counts success **bands** only; it does not account for costs, effects, stress or position in Blades.

### Four Fate dice (context)

Four dice with faces -1, 0, +1 create a nonuniform sum between -4 and +4; near-zero sums occur more often. See the Fate rules for its exact distribution. Do **not** substitute uniform rolls when porting the model.

## Worked damage example [Illustrative]

A very simple tactical ruleset might define:

- Hit separately: attack roll against defense target.
- If hit: raw = base_attack + relevant_attribute_bonus + weapon_bonus.
- After defense: damage = max(0, raw - flat_armor).
- Apply HP := max(0, HP - damage), once.

Example: base_attack 10, attribute_bonus 3, weapon_bonus 2, armor 4 -> raw 15, damage **11**. A miss deals 0 unless a separate explicit effect says otherwise. Criticals, penetration, resistance, block and minimum-damage rules are deliberately unspecified.

**Do not double-reduce** damage using armor twice through two pipelines unless explicitly chosen and balanced.

## Progression curves [Original proposal examples]

These are examples of cost *curves*, not RPG facts:

- Linear cost per level: XP_needed(L) = 100 * L. L=3 -> 300 XP for next level.
- Quadratic cost per level: XP_needed(L) = 100 * L^2. L=3 -> 900 XP for next level.
- Diminishing return: effective_stat = 100 * x/(100+x), for x >= 0. At x=100, effective_stat=50.

For each curve distinguish **XP to next level** from **cumulative XP total**. Document caps and integer rounding. Simulate early, mid and late game before adopting; exponential progression without pacing measurements can render late game inaccessible.

## Balancing measures and dependencies

- **Combat:** expected damage per second/turn, average time-to-defeat, survival margin, healing-to-damage ratio, crowd control uptime, burst-versus-sustain, encounter variance.
- **Skills:** success probability at novice/intermediate/expert tiers, meaningful failure rate, time cost, rewards, exploit resistance, accessibility of prerequisites.
- **Economy:** resource inflows/outflows, time to acquire materials, supply deficits, wealth concentration, price feedback, transaction integrity, scarcity.
- **Social:** rate of relationship change, decay, recoverability, evidence thresholds, options for nonviolent success.
- **World simulation:** NPC throughput per tick, travel realism, off-screen event reconciliation, memory/cpu budget, persistence size.

Avoid balancing exclusively around average values: test unlucky streaks, high-power builds, groups, resource starvation and edge-case combinations.

## Design checks

| Issue | What to measure | Correction candidate |
| --- | --- | --- |
| Attribute dominates all roles | Top attribute's marginal benefit across major loops | Split effects, add tradeoffs or reduce scaling |
| Infinite healing / resource loop | Net resource gain per action cycle | Time cost, caps, ingredient loss, no-repeat flags |
| Critical damage one-shots early content | 95th/99th percentile incoming damage | Crit cap, defenses, telegraphs |
| High accuracy makes evasion irrelevant | Hit probabilities across level deltas | Caps, alternative defense, level scaling |
| Long progression grind | Actions/time needed for next meaningful choice | Milestones, alternate rewards, curve adjustment |
| NPC economics creates free items | Material balance over production actions | Transaction contracts, conservation ledger |

## Implementation ordering (if later selected)

Define value units and rounding; define roll distribution; validate preconditions; compute outcome once; atomically apply effects; emit explanation; then test with exact seeds and boundary cases. Arithmetic alone is not proof of a balanced game.

See [statistics](02_STATISTICS_TAXONOMY.md) and [verification](07_TESTING_AND_VALIDATION.md).
