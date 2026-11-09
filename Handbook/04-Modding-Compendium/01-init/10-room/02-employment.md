# init/room: employment

Rooms that employ workers have a `WORK` or `EMPLOYMENT` block, setting when they work and what the job is like. `WORK` is the normal form, and the player can set hiring priorities for these rooms. A few rooms, such as guardhouses and universities, use `EMPLOYMENT` instead. If a file has both, `WORK` is used.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | One `.txt` file per room |
| **Text file** | `assets/text/room/<KEY>.txt` |

## Tags

### WORK and EMPLOYMENT

How the room employs its workers. Both blocks use the same tags. The examples for these tags come from the vanilla `MINE_COAL.txt` unless stated otherwise.

Whether a room needs one depends on its type, so keep the block if the vanilla room of that type has one. These types use their workers while loading, so the game crashes without it: `ADMIN`, `ARENAG`, `BATH`, `BREEDER`, `CANTEEN`, `FIGHTPIT`, `LABORATORY`, `LIBRARY`, `REFINER`, `SCHOOL`, `SPEAKER`, `STAGE`, `WORKSHOP`, `_EMBASSY` and `_HOSPITAL`. Farms, orchards, pastures, fisheries, mines and woodcutters crash without it later, during play, within about a game day, even if none has been built. `ADMIN`, `LABORATORY`, `LIBRARY` and `_EMBASSY` must use `WORK` specifically. Apart from fisheries and woodcutters, each of these types has its own entry too.

| | |
|---|---|
| **Type** | Block |
| **Required** | No for some room types, such as wells. Many types need it, as listed in this entry. |

```text
WORK: {
	SHIFT_OFFSET: 0.125,
	SOUND: impact->Mine*,
	FULFILLMENT: -4,
	HEALTH_FACTOR: 0.5,
	ACCIDENTS_PER_YEAR: 0.075,
},
```

#### SHIFT_OFFSET

When in the day the shift starts, as a share of the day.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 0.99 |
| **Required** | Yes |

```text
SHIFT_OFFSET: 0.125,
```

#### NIGHT_SHIFT

Whether the room works a night shift. This example comes from the vanilla `SPEAKER_NORMAL.txt`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
NIGHT_SHIFT: true,
```

#### FULFILLMENT

How satisfying the job is to workers, as the default for every race. A race's `PREFERRED.WORK` block can override it. Negative values are allowed, and vanilla uses them for hard jobs like coal mining.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | -100000 to 100000 |
| **Required** | No. Default `0.5`. |

```text
FULFILLMENT: -4,
```

#### ACCIDENTS_PER_YEAR

How likely workers are to have an accident. The game halves this value when it reads it.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | No. Default `0`. |

```text
ACCIDENTS_PER_YEAR: 0.075,
```

#### HEALTH_FACTOR

How healthy the job is. Unverified: `1` appears to mean the job does no harm, with lower values worse for workers' health. Vanilla gives mines values below 1, and coal mines the lowest.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `1`. |

```text
HEALTH_FACTOR: 0.5,
```

#### LARGE_WORKFORCE

The game reads this value, but in v0.71.44 nothing uses it: changing it has no effect. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 10 or more. The game's code names a maximum of 10000, but doesn't enforce it. |
| **Required** | No |
| **Effect** | None |

#### SOUND

The game never reads this tag. A room's work sound comes from the entry `ROOM_WORK_<KEY>` in the audio files.

| | |
|---|---|
| **Type** | Sound path |
| **Required** | No |
| **Effect** | Unread |

```text
SOUND: impact->Mine*,
```

#### USES_TOOL

The game never reads this tag. Which rooms can use tools is set in [init/resource/work](../09-resource/07-work.md). This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No |
| **Effect** | Unread |

```text
USES_TOOL: false,
```

#### DEFAULT_RACE_WORKSKILL

The game never reads this tag. This example comes from the vanilla `PASTURE_BALTI.txt`, the only file that has it.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
DEFAULT_RACE_WORKSKILL: 0.1,
```

#### FULLFILLMENT

A misspelling of `FULFILLMENT` found in the vanilla `BARRACKS_VANILLA.txt` and `_COURT.txt`. The game doesn't read this spelling here, so those two rooms use the default of `0.5` instead of the value written. Use `FULFILLMENT`.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
FULLFILLMENT: 0.75,
```

### BONUS

Multiplies the room's production by climate, for room types that have a production bonus.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

```text
BONUS: {
	CLIMATE: {
		TEMPERATE: 1.25,
		COLD: 0.75,
		HOT: 0.75,
	},
},
```

#### CLIMATE

The multiplier in each climate. The block can contain `COLD`, `TEMPERATE` and `HOT`, and `*` sets every climate at once. A climate that's missing stays at 1. This example comes from the vanilla `PASTURE_AUR.txt`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by climate |
| **Range** | Each value 0 to 2000 |
| **Required** | No |

```text
TEMPERATE: 1.25,
```

### EXPERIENCE_BONUS

A bonus to the room's production that grows as your total number of employees in this kind of room rises, for the room types that read it. It starts at 50 employees and reaches its full value at `MAX_EMPLOYEES`. These examples come from the vanilla `LABORATORY_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Default a bonus of `1` at 1000 employees, for the room types that use experience. |

```text
EXPERIENCE_BONUS: {
	BONUS: 2.5,
	MAX_EMPLOYEES: 2000,
},
```

#### BONUS

The size of the bonus at its full value.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
BONUS: 2.5,
```

#### MAX_EMPLOYEES

The number of employees at which the bonus reaches its full value.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 50 or more |
| **Required** | Yes |

```text
MAX_EMPLOYEES: 2000,
```

## The text file

A room with a `WORK` block needs a `WORK` block in its text file, and a room with `EMPLOYMENT` needs an `EMPLOYMENT` block. Both use the same tags. These examples come from the vanilla `WORKSHOP_SMITHY.txt`.

### WORK and EMPLOYMENT

The wording for the room's workers.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, if the room file has the block |

```text
WORK: {
	TITLE: "Blacksmith",
	VERB: "Forging",
},
```

#### TITLE

The workers' job title.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
TITLE: "Blacksmith",
```

#### VERB

What the workers are doing.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
VERB: "Forging",
```

## Notes

### Tools

Which rooms can use tools, and how many, is set in [init/resource/work](../09-resource/07-work.md).

### Other files

A race's [`PREFERRED.WORK`](../07-race/02-preferences.md#work) block sets how much that race likes each job.

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
