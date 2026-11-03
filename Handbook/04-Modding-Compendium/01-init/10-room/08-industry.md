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

Each file names the one before it, so create them in this order: the [resource](../09-resource/01-resource-file.md), then the [deposit](../09-resource/05-minable.md), then this mine. The game doesn't mind which you write first, as long as they're all there when it loads. A name that doesn't match stops loading with an error listing the available ones.

| | |
|---|---|
| **Type** | Key (a deposit) |
| **Required** | Yes |

```text
MINABLE: CLAY,
```

### FLOOR

The floor laid in the mine. Unlike other rooms, a mine must have one, and it must be a single floor by its key. Vanilla's mines use `MINE`, except the clay mine with `MINE_MUD`.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR: MINE_MUD,
```

### YEILD_WORKER_DAILY

How much of the resource each worker extracts per day, before bonuses. Note the game's spelling.

Vanilla uses `0.1` for sithilon, `0.2` for gems, `1.5` for clay and ore, `4.0` for coal and `4.5` for stone.

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

Vanilla uses `25` for sithilon and gems, `75` for clay and ore, `200` for coal and `225` for stone. Apart from the two slowest, that's 50 times `YEILD_WORKER_DAILY`.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 4 or more. The game's code names a maximum of 500, but doesn't enforce it. |
| **Required** | Yes |

```text
STORAGE: 75,
```

### ICON

The mine's icon in the interface, written as an icon path, a block that combines icons, or a list of blocks. Every vanilla mine uses a block, with the background `32->BG->4` and its resource's icon on top, but a single icon path such as `24->resource->Clay->0` also works.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom. A block has `BG`, the background icon path, and `FG`, an icon path drawn on top, and `SHADOW` sets the size of the shadow under `FG`.

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | Yes |

```text
ICON: {
	BG: 32->BG->4,
	FG: 24->resource->Clay->0,
	SHADOW: 2,
},
```

### RESOURCES

The resources the mine is built from, as a list of resource keys. `AREA_COSTS`, `ITEMS.COSTS` and `UPGRADES.RESOURCE_MASK` all follow this list's order. Every vanilla mine uses the list in this example, except the stone mine, which has `WOOD` in place of `STONE`. Here `STONE` means the resource in `_STONE.txt`, because a key starting with `_` also works without it.

| | |
|---|---|
| **Type** | List of keys (resources) |
| **Range** | 4 at most |
| **Required** | No. If it's missing, the mine costs no resources, and `AREA_COSTS` must be an empty list. |

```text
RESOURCES: [STONE,FURNITURE,METAL,MACHINERY,],
```

### AREA_COSTS

How much of each resource in `RESOURCES` the mine costs for its floor area, in the same order. Every vanilla mine uses `0` for all of them, so a mine only costs resources for its items.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have the same number of entries as `RESOURCES` |
| **Required** | Yes |

```text
AREA_COSTS: [0,0,0,0,],
```

### MINI_COLOR

The mine's colour on the minimap, written as `RED_GREEN_BLUE`. Every vanilla mine uses `80_80_80`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
MINI_COLOR: 80_80_80,
```

### WORK

The mine's workers, in the form described on the [employment](02-employment.md#work-and-employment) page.

Every vanilla mine has `SHIFT_OFFSET: 0.125` and `ACCIDENTS_PER_YEAR: 0.075`. `FULFILLMENT` is `-4`, or `-2` for the clay mine. `HEALTH_FACTOR` is `0.5` for coal, `0.65` for ore, `0.75` for gems, sithilon and stone, and `0.85` for clay.

| | |
|---|---|
| **Type** | Block |
| **Required** | Keep it. Unverified: the game doesn't check for it while loading, but a mine's job code expects it, so leaving it out should crash during play. |

```text
WORK: {
	SHIFT_OFFSET: 0.125,
	SOUND: impact->Dig*,
	FULFILLMENT: -2,
	HEALTH_FACTOR: 0.85,
	ACCIDENTS_PER_YEAR: 0.075,
},
```

### ITEMS

The furniture the player can place in the mine, as a list of exactly two blocks: the storage, then the auxiliaries. The wrong number is a loading error. Each block has its name and description in the text file.

| | |
|---|---|
| **Type** | List of blocks |
| **Range** | Exactly 2 |
| **Required** | Yes |

```text
ITEMS: [
	{
		COSTS: [1,1,1,3.75,],
		STATS: [0,0,0,0,],
	},
	{
		COSTS: [1,1,1,3.75,],
		STATS: [0,0,2,0,],
	},
],
```

#### COSTS

How much of each resource in `RESOURCES` one of these items costs, in the same order. Items that come in several sizes multiply this by a figure set in the game's code. Every vanilla mine uses `[1,1,1,3.75,]` for both items.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have the same number of entries as `RESOURCES` |
| **Required** | Yes |

```text
COSTS: [1,1,1,3.75,],
```

#### STATS

What one of these items adds to the mine's four statistics, in this order: workers, deposits, efficiency and output. Only efficiency uses the number written here, because the game calculates the other three from the room. Every vanilla mine uses `[0,0,0,0,]` for the storage and `[0,0,2,0,]` for the auxiliaries.

Efficiency starts at 50% and rises with the total the items add: it's 0.5 + 0.5 × total ÷ workers, up to 100%. A mine's workers are its deposit tiles with no item on them, divided by 1.5 and rounded down.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have 4 entries |
| **Required** | Yes |

```text
STATS: [0,0,2,0,],
```

### UPGRADES

The mine's upgrade levels, as a list of blocks. The first block is the mine as first built, and each later block is one upgrade. Every vanilla mine has three levels, with the `RESOURCE_MASK` and `BOOST` values in this example. `RESOURCE_MASK` multiplies the costs at that level, one number for each resource in `RESOURCES`, and `0` means the level doesn't use that resource. `BOOST` is the bonus the level gives to production. `AI` has no effect.

| | |
|---|---|
| **Type** | List of blocks |
| **Range** | 1 or more |
| **Required** | No. Without it, the mine can't be upgraded. |

```text
UPGRADES: [
	{
		RESOURCE_MASK: [3,2.5,0,0,],
		BOOST: 0,
	},
	{
		RESOURCE_MASK: [3,5.5,6,0,],
		BOOST: 1.0,
		AI: 0.8,
	},
	{
		RESOURCE_MASK: [3,5.5,6,1,],
		BOOST: 2.0,
		AI: 1.3,
	},
],
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

Each name holds a list of sprite entries, and each entry's `FRAMES` names images as `FILE: ROW`. This example is the `WORK_1X1` entry from the vanilla `MINE_CLAY.txt`:

```text
WORK_1X1: [
	{
		ROTATES: false,
		SHADOW_LENGTH: 2,
		FRAMES: [
			STORAGE: 5,
		],
	},
	{
		ROTATES: false,
		FPS: 15,
		SHADOW_LENGTH: 4,
		CIRCULAR: true,
		FRAMES: [
			MECH_WORK: 0,
			MECH_WORK: 1,
			MECH_WORK: 2,
			MECH_WORK: 3,
		],
	},
],
```

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
