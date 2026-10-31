# init/config/GenerationSettlement.txt

`GenerationSettlement.txt` controls how the map is generated when you found a new settlement: how many caves there are, how large mountains and lakes are, how wide rivers run, and how much forest and food there is.

These settings only apply when a settlement's map is first generated. Changing them has no effect on an existing settlement.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/GenerationSettlement.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | None |

## File structure

All the settings sit inside a single `GENERATION` block:

```text
GENERATION: {
	CAVE_AMOUNT: 0.16,
	CAVE_SIZE: 0.5,
	CAVE_TUNNELS: 0.2,
	MOUNTAIN_SIZE: 0.2,
	MOUNTAIN_RANDOM: 0.2,

**	1-6 valid
	RIVER_WIDTH: 10,
	LAKE_SIZE: 0.2,
	LAKE_SMALL: 0.5,
	LAKE_ISLANDS: 0.3,
	FOREST_AMOUNT: 0.7,
	FOREST_DENSITY: 0.8,
	MINERALS_AMOUNT: 0.3,
	EDIBLES_AMOUNT: 1.0,
}
```

Four of these tags have no effect; see [Tags that have no effect](#tags-that-have-no-effect) below.

## Tags

### CAVE_AMOUNT

How many caves the generator tries to create. The value is multiplied by 300 to give the number of attempts; not every attempt produces a cave.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### CAVE_SIZE

How large each cave can grow.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### CAVE_TUNNELS

How many tunnels are dug out from the caves. Higher values allow more tunnels; the exact number is random.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### MOUNTAIN_SIZE

How large mountains are.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.1 to 1 |
| **Required** | Yes |

### RIVER_WIDTH

How wide rivers are.

The vanilla comment says only 1 to 6 are valid, but the vanilla value is 10 and the game's code allows more.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 15, but doesn't enforce it. |
| **Required** | Yes |

### LAKE_SIZE

How large lakes are.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.1 to 1 |
| **Required** | Yes |

### LAKE_ISLANDS

How many islands lakes have. The value is multiplied by 100 to give the number of islands the generator tries to place.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### FOREST_AMOUNT

How much of the map is covered by forest.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### EDIBLES_AMOUNT

How much wild food the map has.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

## Notes

### Tags that have no effect

`MOUNTAIN_RANDOM`, `LAKE_SMALL`, `FOREST_DENSITY` and `MINERALS_AMOUNT` appear in the vanilla file, but the game never reads them. Changing them has no effect, and they can be left out.

### Battle maps

When the generator builds a battle map rather than a settlement, it uses three quarters of the `FOREST_AMOUNT` value.

## Related

- [init/config](00-config.md)
