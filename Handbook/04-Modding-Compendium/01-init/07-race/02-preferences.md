# Race preferences

The `PREFERRED` block in a [race file](01-race-file.md) describes what the race likes: its favourite food and drink, the buildings and roads it likes to live among, the jobs it enjoys, how it gets on with other races, and how it feels about crime and punishment.

The block is required, and must contain at least `FOOD` and `DRINK`.

## Tags

The examples below come from the vanilla `HUMAN.txt` unless stated otherwise.

### FOOD

The race's favourite foods, as a list of edible resources. Members of the race choose these when they eat at eateries and canteens. At least one is required.

| | |
|---|---|
| **Type** | List of resource keys (edible resources) |
| **Required** | Yes, with at least one entry |

```text
FOOD: [
	BREAD,
	MEAT,
	MUSHROOM,
	EGG,
],
```

### DRINK

The race's favourite drinks, as a list of drinkable resources, chosen when they drink at taverns. `*` means every drink. At least one is required.

| | |
|---|---|
| **Type** | List of resource keys (drinks) |
| **Required** | Yes, with at least one entry |

```text
DRINK: [
	*,
],
```

### ROAD

How much the race likes each kind of road floor, from 0 to 1. When a subject walks on a road outside any room, their liking for that road (less if the road is worn) gradually becomes their rating of the roads around them, which is one of their stats. A road that isn't listed keeps its default for the race, set by [`ROAD.PREFERENCE`](../12-settlement/03-floor.md#preference) in its floor file.

| | |
|---|---|
| **Type** | Block of decimals, keyed by road floor |
| **Range** | Each value 0 to 1 |
| **Required** | No |

```text
ROAD: {
	*: 0.1,
	STONE1 : 0.5,
	STONE2 : 0.8,
	DECOR1: 1.0,
},
```

### STRUCTURE

How much the race likes each kind of building structure, from 0 to 1. The keys are `MOUNTAIN`, `OUTDOORS`, `MUD`, and one for each structure file in `assets/init/settlement/structure/` (`GRAND`, `STONE` and `WOOD` in vanilla).

Wherever a subject is, the game rates the structure of the tiles around them by this preference. Over time this becomes the subject's building-preference stat (`ENVIRONMENT_BUILDING_PREF`). The structure of a worker's workplace also affects how readily they stay in that job.

A structure missing from the block keeps its default for the race. The defaults are set in the structure files themselves, in their `PREFERENCE` blocks.

| | |
|---|---|
| **Type** | Block of decimals, keyed by structure |
| **Range** | Each value 0 to 1 |
| **Required** | No |

```text
STRUCTURE: {
	MOUNTAIN: 0.2,
	STONE: 0.7,
	GRAND: 1,
	WOOD: 0.5,
	OUTDOORS: 0.3,
},
```

### POOL

How much the race likes each kind of pool room, from 0 to 1, used when a subject bathes in one. A pool that isn't listed counts as `0`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by pool room |
| **Range** | Each value 0 to 1 |
| **Required** | No |

```text
POOL: {
	POOL_STONE: 1,
},
```

### WORK

How much the race likes working in each room. Positive values are jobs they enjoy and negative values are jobs they dislike. A room that isn't listed keeps the default set by the room's own `FULFILLMENT` tag, or `0.5` if it has none.

| | |
|---|---|
| **Type** | Block of decimals, keyed by room |
| **Range** | Each value -10000 to 10000 |
| **Required** | No |

Each key must be a room that employs workers. Any other room name causes an error.

From `GARTHIMI.txt` (shortened):

```text
WORK: {
	_ASYLUM: 0.75,
	_CANNIBAL: 4.0,
	_COURT: -100.0,
	...
	HUNTER_NORMAL: 4.0,
	...
	WORKSHOP_SMITHY: 0.25,
},
```

These values are used in several ways:

- **Job satisfaction.** A subject's liking for their job is one of their stats, which the race's [`STATS`](03-stats.md) can make matter for their happiness.
- **Work priorities.** The game's default employment priorities for the race follow these values.
- **Tourism.** Tourists of this race are drawn by the attraction rooms the race most likes to work in.
- **Retirement.** Retirees of the race only use retirement homes the race likes (a value above 0), and how much the race likes the home is one of the retiree's stats.

### OTHER_RACES

How much the race likes living alongside each other race, from 0 to 1. A race that isn't listed counts as `1` (unless another race's `OTHER_RACES_REVERSE` says otherwise), and a race's opinion of itself is always `1`.

Within the block, an entry naming a race directly beats a `*` entry, whichever comes first.

| | |
|---|---|
| **Type** | Block of decimals, keyed by race |
| **Range** | Each value 0 to 1 |
| **Required** | No |

```text
OTHER_RACES: {
	GARTHIMI: 0.75,
	CRETONIAN: 0.75,
	CANTOR: 0.75,
	Q_AMEVIA: 0.75,
	DONDORIAN: 0.75,
	ARGONOSH: 0.75,
	TILAPI: 0.2,
},
```

The race's opinion of other races is used in several places:

- how happy subjects are to live among the other races in your settlement;
- how conversations between subjects of different races go;
- how mixed the populations of world regions become;
- how AI royalty of this race regard you, depending on the race you play.

### OTHER_RACES_REVERSE

How much **other** races like this race, from 0 to 1. Each entry sets the named race's opinion of this one, as if it had been written in that race's own `OTHER_RACES`. This lets a modded race fit in with the vanilla races without changing their files.

| | |
|---|---|
| **Type** | Block of decimals, keyed by race |
| **Range** | Each value 0 to 1 |
| **Required** | No |

```text
OTHER_RACES_REVERSE: {
	*: 1,
},
```

The game applies every race's `OTHER_RACES_REVERSE` first, and every race's `OTHER_RACES` after. An entry in a race's own `OTHER_RACES` that names another race directly therefore always has the final say on that race's opinion.

### WORLD_BUILDING

How strongly this race responds to region buildings on the world map. Each entry names a region building and gives a multiplier for the building's effect on this race's loyalty, population target and population growth in the region. Values above 1 make the building matter more to the race, and values below 1 less.

| | |
|---|---|
| **Type** | Block of decimals, keyed by region building |
| **Required** | No |

From `GARTHIMI.txt`:

```text
WORLD_BUILDING: {
	CIVIC_L_ARENA: 1.5,
},
```

`HUMAN.txt` has a block called `BUILDING_OVERRIDE` in this position instead. The game doesn't read that name, so it has no effect.

### CRIME

The race's own views on each crime, overriding the defaults set in [`init/config/LAW.txt`](../03-config/07-LAW.md). Each entry names a crime and can contain `FREEDOM` and `LAW`, with the same meanings as in `LAW.txt`. A tag left out keeps the default.

| | |
|---|---|
| **Type** | Block of blocks, keyed by crime |
| **Range** | `FREEDOM` and `LAW` each 0 to 1 |
| **Required** | No |

From `CRETONIAN.txt`:

```text
CRIME: {
	FLASHING: {
		FREEDOM: 0.75,
	},
},
```

Cretonians resent punishment for flashing far more than the default.

### PUNISHMENT

How severe the race considers each punishment, from 0 to 1, overriding the `VALUE` set in [`init/config/LAW.txt`](../03-config/07-LAW.md).

| | |
|---|---|
| **Type** | Block of decimals, keyed by punishment |
| **Range** | Each value 0 to 1 |
| **Required** | No |

From `Q_AMEVIA.txt`:

```text
PUNISHMENT: {
	BANISH: 0.3,
	PRISON: 1,
	EXECUTE: 0,
},
```

### RESOURCE_RPICE_MUL and RESOURCE_RPICE_CAP

Two blocks the game reads that vanilla doesn't use. Note the game's spelling, `RPICE`.

- `RESOURCE_RPICE_MUL` multiplies the price AI factions ruled by this race ask for each resource. Each value is from 0 to 100, and a resource that isn't listed keeps the default set in its resource file.
- `RESOURCE_RPICE_CAP` is shown in the world map's trade information, but in v0.71.44 it doesn't change any price. Each value is from 0 to 1.

Both are keyed by resource.

## Related

- [init/race](00-race.md)
- [The race file](01-race-file.md)
- [Race stats](03-stats.md)
- [init/config/LAW.txt](../03-config/07-LAW.md)
