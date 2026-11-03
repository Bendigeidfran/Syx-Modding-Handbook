# init/room: industry rooms

These rooms make or extract resources: workshops and refiners turn resources into other resources, mines dig up deposits, and the woodcutter fells trees. Besides the tags on this page, they use the [common tags](01-common.md), [employment](02-employment.md) and [production](03-production.md) tags.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `WORKSHOP_*.txt`, `REFINER_*.txt`, `MINE_*.txt` and `_WOODCUTTER.txt` |
| **Adding new rooms** | Yes for workshops, refiners and mines. `_WOODCUTTER` is a single room. |

Vanilla has ten workshops, five refiners and six mines.

## WORKSHOP

Workshops have one or more recipes in `INDUSTRIES`. They have exactly three `ITEMS`, in this order: the storage (exactly one per room), the work bench (at least one per room) and an auxiliary station. They have three statistics, for workers, efficiency and output. Workers are counted from the work tiles, and the game calculates output. Efficiency is the statistic that items add to.

The examples come from the vanilla `WORKSHOP_SMITHY.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. This example comes from the vanilla `WORKSHOP_SMITHY.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.325,
	SOUND: impact->Metal*,
	ACCIDENTS_PER_YEAR: 0.025,
	FULFILLMENT: 0,
},
```

### STORAGE

The game never reads this tag for workshops, though every vanilla workshop has it. A workshop's storage holds 31 per tile, fixed in the game's code.

| | |
|---|---|
| **Type** | Integer |
| **Required** | No |
| **Effect** | Unread |

```text
STORAGE: 25,
```

### SPRITES

The images a workshop is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CHAIR_1X1` | The workers' chairs. | `1x1` |
| `TABLE_COMBO` | The tables of the work bench and storage. | `combo` |
| `TABLE_TOP_COMBO` | The table tops, drawn over `TABLE_COMBO`. | `combo` |
| `WORK_BELOW_1X1` | The work spot, drawn under whatever's being made. Animates while someone works. | `1x1` |
| `WORK_ABOVE_1X1` | The work spot, drawn over it. Animates while someone works. | `1x1` |
| `TOOL_1X1` | Objects on the auxiliary tables. | `1x1` |
| `MISC_BELOW_1X1` | Clutter on the bench, on some tiles only. | `1x1` |
| `MISC_ABOVE_1X1` | Clutter drawn over `MISC_BELOW_1X1`. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

```text
CHAIR_1X1: [
	{
		SHADOW_HEIGHT: 4,
		FRAMES: [
			CHAIRS: 10,
			CHAIRS: 11,
		],
	},
],
```

## REFINER

Refiners have one or more recipes in `INDUSTRIES`. They have exactly three `ITEMS`, in this order: the machine (at least one per room), the storage (exactly one per room) and an auxiliary machine. They have three statistics, for workers, efficiency and output, which work as they do for workshops.

The example comes from the vanilla `REFINER_BAKERY.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. This example comes from the vanilla `REFINER_BAKERY.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.125,
	SOUND: work->Machine*,
	FULFILLMENT: 0,
	ACCIDENTS_PER_YEAR: 0.05,
},
```

### STORAGE

How much of its output each storage tile can hold.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 8 or more. The game's code names a maximum of 500, but doesn't enforce it. |
| **Required** | Yes |

```text
STORAGE: 350,
```

### SPRITES

The images a refiner is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with, except where the table says otherwise.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `MAIN_MACHINE_COMBO` | The main machine. | `combo` |
| `MAIN_MACHINE_COMBO_TOP` | The top of the main machine. | `combo` |
| `MAIN_MACHINE_COMBO_TOP_MACHINE` | Moving parts on top of some machine tiles. Despite its name, this is a `1x1` entry. | `1x1` |
| `STORAGE_IN_1X1` | Where workers fetch the room's ingredients. | `1x1` |
| `WORK_1X1` | The work spot. Animates while someone works. | `1x1` |
| `CONVEYOR_1X1` | The conveyor at the start of the storage. | `1x1` |
| `STORAGE_1X1` | The storage. Despite its name, it's a row of tiles. | `1x1` |
| `NICKNACK_BOTTOM_1X1` | Clutter on the machine. | `1x1` |
| `NICKNACK_TOP_1X1` | Clutter drawn over `NICKNACK_BOTTOM_1X1`, on some tiles only. | `1x1` |
| `MACHINE_1X1` | Small animated machines. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## MINE

A mine extracts one [deposit](../09-resource/05-minable.md), and has to be built at least partly on it. It can't be built on a different deposit. Mines don't use `INDUSTRY` or `INDUSTRIES`: their output is set by `YEILD_WORKER_DAILY`, and the resource comes from the deposit. They have exactly two `ITEMS`, in this order: the storage (exactly one per room) and the auxiliaries. They have four statistics, for workers, deposits, efficiency and output. The game calculates workers, deposits and output from the room, so efficiency is the statistic that items add to.

The examples come from the vanilla `MINE_CLAY.txt`.

### MINABLE

The deposit this mine extracts, by its key in `assets/init/resource/minable/`.

| | |
|---|---|
| **Type** | Key (a deposit) |
| **Required** | Yes |

```text
MINABLE: CLAY,
```

### FLOOR

The floor laid in the mine. Unlike other rooms, a mine must have one, and it must be a single floor by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR: MINE_MUD,
```

### YEILD_WORKER_DAILY

How much of the resource each worker extracts per day, before bonuses. Note the game's spelling.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
YEILD_WORKER_DAILY: 1.5,
```

### STORAGE

How much of its output each storage tile can hold.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 4 or more. The game's code names a maximum of 500, but doesn't enforce it. |
| **Required** | Yes |

```text
STORAGE: 75,
```

### SPRITE

The game never reads this tag, though every vanilla mine has it.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
SPRITE: MINE_TYPE_MUD,
```

### SPRITES

The images a mine is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CONVEYOR_1X1` | The conveyor beside the storage. Animates while the mine works. | `1x1` |
| `STORAGE_1X1_TOP` | The first tile of a storage row. | `1x1` |
| `STORAGE_1X1_MID` | The middle tiles of a storage row. | `1x1` |
| `STORAGE_1X1_END` | The last tile of a storage row. | `1x1` |
| `SLAB_1X1` | A storage of a single tile, and the slabs showing the resource's icon. | `1x1` |
| `AUX_1X1` | Small auxiliary machines. Animates while the mine works. | `1x1` |
| `AUX_MEDIUM_A_1X1` | The first half of a medium auxiliary machine. | `1x1` |
| `AUX_MEDIUM_B_1X1` | The second half of a medium auxiliary machine. | `1x1` |
| `AUX_BIG_2X2` | Large auxiliary machines. | `2x2` |
| `WORK_1X1` | The work spot. Animates while someone works. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _WOODCUTTER

The woodcutter's own room. Its `INDUSTRY` block sets how much wood it yields. It has exactly two `ITEMS`, in this order: the storage (exactly one per room) and the auxiliaries. It has four statistics, for workers, efficiency, moisture and output. Moisture affects its output, and a world map region's forest decides its prospect for this industry.

The examples come from the vanilla `_WOODCUTTER.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: FISHERY,
```

### STORAGE

How much wood each storage tile can hold.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 8 or more. The game's code names a maximum of 500, but doesn't enforce it. |
| **Required** | Yes |

```text
STORAGE: 200,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `EDGE_COMBO` | The edge of the room. | `combo` |
| `STORAGE_1X1_TOP` | The first tile of a storage row. | `1x1` |
| `STORAGE_1X1_MID` | The middle tiles of a storage row. | `1x1` |
| `STORAGE_1X1_END` | The last tile of a storage row. | `1x1` |
| `SLAB_1X1` | A storage of a single tile. | `1x1` |
| `AUX_1X1` | Small auxiliary objects. | `1x1` |
| `AUX_MEDIUM_A_1X1` | The first half of a medium auxiliary object. | `1x1` |
| `AUX_MEDIUM_B_1X1` | The second half of a medium auxiliary object. | `1x1` |
| `AUX_BIG_2X2` | Large auxiliary objects. | `2x2` |
| `WORK_1X1` | The work spot. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Production](03-production.md)
- [init/resource/minable](../09-resource/05-minable.md)
