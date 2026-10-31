# Occurrence and conditions

This page covers two related things: the `OCCURENCE` block, which decides when and how often an event happens on its own, and the **condition format**, which events use wherever something must be checked: in `OCCURENCE`, choices, `CONDITION`, `ABORTS` and selection filters.

## OCCURENCE

Note the game's spelling, with a single R. An event without this block never starts on its own; it only happens when another event starts it.

```text
OCCURENCE: {
	CLIMATE: {
		*: 1.0,
	},
	TERRAIN: {
		*: 1.0,
	},
	RACE: {
		*: 1.0,
	},
	REQUIRES: {
		GREATER: {
			EMPLOYED_MINE_COAL: 100,
		},
	},
},
```

### CLIMATE, TERRAIN and RACE

How likely the event is, depending on your settlement's climate, the terrain around it, and the races living in it. Each is a block of weights:

- `CLIMATE` is keyed by climate: `COLD`, `TEMPERATE` and `HOT`.
- `TERRAIN` is keyed by terrain: `OCEAN`, `WET`, `MOUNTAIN`, `FOREST` and `NONE`.
- `RACE` is keyed by race, such as `HUMAN` or `DONDORIAN`.

`*` sets every entry at once. Anything missing from a block counts as `0`, and so does a missing block.

| | |
|---|---|
| **Type** | Blocks of decimals |
| **Range** | `CLIMATE` and `RACE`: each 0 to 10000000. `TERRAIN`: each 0 to 100000. |
| **Required** | No, but all three are needed for the event to happen: if any is missing or zero, the event never starts on its own. |

The three combine into the event's occurrence:

- for **terrain**, the game multiplies each terrain's weight by how much of your settlement's area is that terrain, and takes the highest result;
- for **race**, it multiplies each race's weight by that race's share of your population, and takes the highest result;
- the occurrence is the terrain result × the climate weight for your settlement's climate × the race result.

The higher the occurrence, the faster the event builds up weight while it's eligible, and so the sooner and more often it happens.

### REQUIRES

Conditions that must be met for the event to be eligible at all, in the [condition format](#conditions) below. Vanilla uses this to tie events to your settlement's state: `COAL_GOOD` can only happen once more than 100 people are employed in coal mines.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No |

### MAX_SPAWNS

How many times the event can happen in a game. Vanilla uses `MAX_SPAWNS: 1` for one-off events.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more |
| **Required** | No. Default: no limit. |

```text
MAX_SPAWNS: 1,
```

### ONLY_AFTER_DAYS

The fewest days that must pass after the event last started before it can start again. Before the event has happened for the first time, the days are counted from the start of the game.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | No. Default `0`. |

```text
ONLY_AFTER_DAYS: 32,
```

### TYPE

The game reads a `TYPE` tag in `OCCURENCE`, apparently to share out occurrence between events of the same type. Vanilla doesn't use it, and in v0.71.44 it doesn't work as intended: the game counts the events of each type incorrectly, so every event with a `TYPE` has its climate weights divided by zero. **Don't use this tag.**

## Conditions

Conditions check values from the game. The same format is used in every part of an event that tests something: `REQUIRES` blocks (in `OCCURENCE`, `CHOICES`, `CONDITION` and `ABORTS`) and the entries in a selection's `FILTERS`.

A condition block contains one or more **comparisons**. Each comparison is a block listing values and the numbers to compare them with:

```text
REQUIRES: {
	GREATER: {
		EMPLOYED_MINE_COAL: 100,
	},
	LESS: {
		POPULATION_WRONGFUL_DEATHS: 0.15,
	},
},
```

This reads: "more than 100 people employed in coal mines, and wrongful deaths below 0.15". **Every** comparison in a block must be true for the condition to be met.

### Comparisons

| Comparison | True when the game's value is |
|---|---|
| `GREATER` | greater than the number |
| `GREATERE` | greater than or equal to the number |
| `LESS` | less than the number |
| `EQUAL` | equal to the number |
| `NEQUAL` | not equal to the number |

There is no "less than or equal" comparison. Use `LESS` with a slightly higher number instead.

A comparison name that isn't in this list stops the game from loading.

### Values

The values a condition can check are supplied by many different parts of the game, so there's no fixed list. Many are built from the keys of other things. For example:

- `EMPLOYED_MINE_COAL` is the number of people employed in the `MINE_COAL` room;
- `POPULATION_DONDORIAN_CITIZEN_F` is the number of Dondorian citizens as a fraction of your whole population, and `POPULATION_DONDORIAN_CITIZEN_I` is the number itself.

A name ending in `_F` is often a fraction from 0 to 1, and one ending in `_I` a whole number, but check each value rather than relying on this.

Which values are available depends on what the condition is checking:

| Where | Checks values of |
|---|---|
| `REQUIRES` in `OCCURENCE`, `CHOICES`, `CONDITION` and `ABORTS` | Your faction |
| `FILTERS` under `SUBJECTS` | Each subject |
| `FILTERS` under `REGIONS` | Each region |
| `FILTERS` under `FACTIONS` | Each faction |
| `FILTERS` under `ROYALTIES` | Each member of royalty |

### Finding value names

The simplest way to find the right name is to let the game tell you. The first time a condition uses a value that doesn't exist, the game shows a warning that names it and **lists every value available** in that place. You can use a deliberately wrong name to get the list, then correct it.

Until it's corrected, an unknown value doesn't work as written: the game compares `0` against `1`, ignoring the number you gave. With `GREATER` the condition is never met, and with `LESS` it always is.

## Related

- [init/event](00-event.md)
- [Event structure](01-structure.md)
- [init/config/CLIMATE.txt](../03-config/02-CLIMATE.md)
- [init/config/TERRAIN.txt](../03-config/13-TERRAIN.md)
