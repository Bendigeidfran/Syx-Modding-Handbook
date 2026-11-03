# init/room: infrastructure rooms

These rooms keep the settlement running: administration, storage and logistics, gates, monuments, inns and the throne. Besides the tags on this page, they use the [common tags](01-common.md), and those with workers use [employment](02-employment.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `ADMIN_*`, `GATEHOUSE_*`, `MONUMENT_*`, `RESTHOME_*`, `_BENCH`, `_BUILDER`, `_EMBASSY`, `_EXPORT`, `_HAULER`, `_IMPORT`, `_INN`, `_JANITOR`, `_STATION`, `_STOCKPILE`, `_THRONE` and `_TRANSPORT` |
| **Adding new rooms** | Yes for `ADMIN`, `GATEHOUSE`, `MONUMENT` and `RESTHOME`. The others are single rooms. |
| **Text file** | `assets/text/room/<KEY>.txt` |

## ADMIN

An administration room's workers build up a value that feeds a boost, which vanilla uses for `CIVIC_ADMIN`. It has exactly three `ITEMS`, in this order: the clerk station (at least one per room), the shelf and the carpet. It has three statistics. Vanilla's text file also has `BOOST_NAME` and `UNLOCK_MESS`, which the game doesn't read.

The examples come from the vanilla `ADMIN_NORMAL.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. It must be `WORK`, because this room's value tags only work with that block, not `EMPLOYMENT`. This example comes from the vanilla `ADMIN_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.375,
	SOUND: work->Paper*,
	USES_TOOL: true,
	FULFILLMENT: 0.5,
},
```

### VALUE_PER_WORKER

The value each worker can build up.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | Yes |

```text
VALUE_PER_WORKER: 1,
```

### VALUE_DEGRADE_PER_YEAR

How much of the value is lost per year.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes |

```text
VALUE_DEGRADE_PER_YEAR: 1.0,
```

### VALUE_WORK_SPEED

How quickly workers build up the value.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
VALUE_WORK_SPEED: 4,
```

### BOOST

The boost this value feeds, by its name. Unlike most `BOOST` tags, this is a single name, not a block.

| | |
|---|---|
| **Type** | Key (a boost) |
| **Required** | No. Without it, the value feeds nothing. |

```text
BOOST: CIVIC_ADMIN,
```

### CONSUMPTION

Resources the room can consume to work better. Each entry names a resource by its key, and holds `RATE` and `BONUS`.

| | |
|---|---|
| **Type** | Block of blocks, keyed by resource |
| **Required** | No |

```text
CONSUMPTION: {
	PAPER: {
		RATE: 1,
		BONUS: 2,
	},
},
```

#### RATE

How much of the resource is consumed.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | Yes |

```text
RATE: 1,
```

#### BONUS

How much having this resource adds to the room's output.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
BONUS: 2,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `ADMIN_ONTOP_1X1` | Things on the tables. | `1x1` |
| `WORK_UNUSED_1X1` | A work spot, free. | `1x1` |
| `WORK_USED_1X1` | A work spot, in use. | `1x1` |
| `WORK_USED_TOP_1X1` | The top of a work spot in use. | `1x1` |
| `STOOL_1X1` | The stools. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_TOP_1X1` | Things on the shelves. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## GATEHOUSE

A gate in a wall. It has no workers, no tags of its own and no `SPRITES` block. It has exactly one `ITEMS` block and no statistics.

## MONUMENT

A decorative monument, which subjects value for being near it. It has no workers. The file's `ITEMS` list sets how many kinds it has, rather than the game's code, and each has no statistics. A monument with `TYPE: TORCH` works differently from the others, including in its `SPRITES`.

The examples come from the vanilla `MONUMENT_TORCH.txt` unless stated otherwise.

### TYPE

If this is `TORCH`, the room is a torch: it's drawn differently and reads different `SPRITES`. Any other value, or none, gives a normal monument.

| | |
|---|---|
| **Type** | Text |
| **Required** | No |

```text
TYPE: TORCH,
```

### SOLID

Whether the monument blocks the way. If `false`, subjects can walk through it. This example comes from the vanilla `MONUMENT_BLOB.txt`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `true`. |

```text
SOLID: true,
```

### MAX_VALUE

The amount of this monument nearby that counts as full value. The game measures a tile's value as a share of this number.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes |

```text
MAX_VALUE: 1,
```

### STANDING

How much access to this monument matters to subjects. It's in the same format as an entry in a race's [`STATS`](../07-race/03-stats.md#format) block, and it's at the top level of the file.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

```text
STANDING: {
	CITIZEN: 1.5,
	NOBLE: 1,
	SLAVE: 1,
	PRIO: 75,
	MULTIPLIER: 1.5,
},
```

### STANDING_UPGRADE

A further `STANDING` block, inside this block, for the monument's upgrades.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

```text
STANDING_UPGRADE: {
	STANDING: {
		CITIZEN: 0.5,
		NOBLE: 0,
		SLAVE: 0,
		PRIO: 25,
	},
},
```

### FULFILLMENT_BONUS

Bonuses from access to the monument, in the same form as a race's [`BOOST`](../07-race/01-race-file.md#boost) block. They're scaled by how much access subjects have.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
FULFILLMENT_BONUS: {
	CIVIC_LAW>ADD: 0.05,
},
```

### SPRITES

The images the room is drawn with. A normal monument has a list of blocks, one for each entry in `ITEMS`. Each block must have `FLOOR_COMBO`, and at least one of the others. A torch has a single block with `SMALL_1X1` and `COMBO`.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FLOOR_COMBO` | The floor under the monument. Normal monuments only. | `combo` |
| `1x1` | A small monument. Normal monuments only. | `1x1` |
| `2x2` | A medium monument. Normal monuments only. | `2x2` |
| `3x3` | A large monument. Normal monuments only. | `3x3` |
| `SMALL_1X1` | A small torch. Torches only. | `1x1` |
| `COMBO` | A large torch. Torches only. | `combo` |

| | |
|---|---|
| **Type** | List of blocks, or a block for a torch |
| **Required** | Yes |

## RESTHOME

A home for the elderly. It uses an `EMPLOYMENT` block rather than `WORK`. It has exactly four `ITEMS`, in this order: the tables (at least one per room), the dance floor (at least one per room), the decorations and the carpets. It has two statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with, except where the table says otherwise.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CHAIR_1X1` | The chairs. | `1x1` |
| `TABLE_1X1` | A single table. | `1x1` |
| `TABLES_COMBO` | Larger tables. | `combo` |
| `ON_TOP_DECOR_1X1` | Decoration on a table. | `1x1` |
| `ON_TOP_CARDS_1X1` | Cards on a table. | `1x1` |
| `STAGE_COMBO` | The dance floor. Despite its name, this is a `box` entry. | `box` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_ON_TOP_1X1` | Things on the shelves. | `1x1` |
| `NICKNACK_1X1` | Clutter. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _BENCH

A bench. It has no workers. It has exactly one `ITEMS` block and no statistics.

The examples come from the vanilla `_BENCH.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: BENCH,
```

### SPRITES

The images the room is drawn with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BENCH_1X1` | The bench. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _BUILDER

The builders' room. It has no `ITEMS` or statistics, and vanilla writes `ITEMS` as an empty list.

### SPRITES

The images the room is drawn with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `1x1` | The room's object. Note that this is the whole name. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _EMBASSY

An embassy's workers build up a value in the same way as an administration room. Vanilla gives it no `BOOST`, but the game would read one here as it does for `ADMIN`. It has exactly three `ITEMS`, in this order: the workstation, the nicknacks and the carpets. It has two statistics.

The examples come from the vanilla `_EMBASSY.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. It must be `WORK`, because this room's value tags only work with that block, not `EMPLOYMENT`. This example comes from the vanilla `_EMBASSY.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.375,
	USES_TOOL: false,
	FULFILLMENT: 0.75,
},
```

### VALUE_PER_WORKER

The value each worker can build up.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | Yes |

```text
VALUE_PER_WORKER: 1.0,
```

### VALUE_DEGRADE_PER_YEAR

How much of the value is lost per year.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes |

```text
VALUE_DEGRADE_PER_YEAR: 0.2,
```

### VALUE_WORK_SPEED

How quickly workers build up the value.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
VALUE_WORK_SPEED: 6,
```

### CONSUMPTION

Resources the room can consume to work better. Each entry names a resource by its key, and holds `RATE` and `BONUS`.

| | |
|---|---|
| **Type** | Block of blocks, keyed by resource |
| **Required** | No |

```text
CONSUMPTION: {
	FABRIC: {
		RATE: 1,
		BONUS: 1,
	},
	JEWELRY: {
		RATE: 0.1,
		BONUS: 1,
	},
	SITHILON: {
		RATE: 0.1,
		BONUS: 1,
	},
},
```

#### RATE

How much of the resource is consumed.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | Yes |

```text
RATE: 1,
```

#### BONUS

How much having this resource adds to the room's output.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
BONUS: 1,
```

### INDUSTRY

The game never reads this block for embassies. `CONSUMPTION` is what counts.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
INDUSTRY: {
	IN: {
		JEWELRY: 0.1,
		FABRIC: 2,
	},
},
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_1X1` | A single table. | `1x1` |
| `TABLE_TOP_1X1` | Things on the tables. | `1x1` |
| `DECOR_1X1` | Decoration. | `1x1` |
| `STOOL_1X1` | The stools. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _EXPORT

The export depot. It has exactly one `ITEMS` block and one statistic.

The examples come from the vanilla `_EXPORT.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: STONE2,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CRATE_1X1` | The crates. | `1x1` |
| `ROOF_COMBO` | The roof. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _HAULER

The hauling station. It has exactly one `ITEMS` block and no statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CRATE_1X1` | The crates. | `1x1` |
| `FENCE_COMBO` | The fence. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _IMPORT

The import depot. It has no workers. It has exactly one `ITEMS` block and one statistic.

The examples come from the vanilla `_IMPORT.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: STONE2,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CRATE_1X1` | The crates. | `1x1` |
| `POST_1X1` | The posts. | `1x1` |
| `FENCE_1X1` | The fence. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _INN

Where tourists stay. Its `SERVICE` block only reads `RADIUS`, and its text file only needs `SERVICE.VERB`. It has exactly three `ITEMS`, in this order: the room (at least one per room), the decorations and the carpets. It has three statistics.

The examples come from the vanilla `_INN.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: STONE_BRICK,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BED_UNMADE_HEAD_1X1` | The head of an unmade bed. | `1x1` |
| `BED_UNMADE_TAIL_1X1` | The foot of an unmade bed. | `1x1` |
| `BED_MADE_HEAD_1X1` | The head of a made bed. | `1x1` |
| `BED_MADE_TAIL_1X1` | The foot of a made bed. | `1x1` |
| `BED_CLAIMED_1X1` | A marker on a claimed bed. | `1x1` |
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_TOP_1X1` | Things on the tables. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_TOP_1X1` | Things on the shelves. | `1x1` |
| `CHEST_1X1` | The chests. | `1x1` |
| `NICKNACK_1X1` | Clutter. | `1x1` |
| `WALLS_COMBO` | The walls between rooms. | `combo` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _JANITOR

The janitors' room. It has exactly two `ITEMS`, in this order: the work stations and the utilities, with at least one of each per room. It has two statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_MISC_1X1` | Things on the tables. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |
| `STORAGE_1X1` | The storage. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _STATION

The unloading station. It has exactly one `ITEMS` block and no statistics.

The examples come from the vanilla `_STATION.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: DIRT,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `WORK_1X1` | The work spot. | `1x1` |
| `WORK_TOP_1X1` | The top of the work spot. | `1x1` |
| `ANIMAL_TOP_1X1` | The animals' basin. | `1x1` |
| `ANIMAL_BOTTOM_1X1` | The water in the basin. | `1x1` |
| `ROOF_MID_1X1` | The middle of the roof. | `1x1` |
| `ROOF_EDGE_1X1` | The edge of the roof. | `1x1` |
| `CRATE_BOTTOM_1X1` | The crates. | `1x1` |
| `CRATE_TOP_1X1` | The tops of the crates. | `1x1` |
| `TORCH_1X1` | The torches. | `1x1` |

| Tag | Meaning | Effect |
|---|---|---|
| `GROUND_THING_1X1` | Never read here, though vanilla has it. | Unread |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _STOCKPILE

The stockpile. It has exactly one `ITEMS` block, the crates (at least one per room), and one statistic.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CRATE_BOTTOM_1X1` | The crates. | `1x1` |
| `CRATE_TOP_1X1` | The tops of the crates. | `1x1` |
| `CRATE_TOP_FOOD_1X1` | The tops of crates holding food. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _THRONE

The throne. It's a special case in the game's code, with its own loader, and the only tags it reads are `ICON`, `MINI_COLOR` and `SPRITES`. It also reads an image, `assets/sprite/room/_THRONE.png`, which must be exactly 264 pixels wide and at least 240 pixels tall. Its text file only needs `NAME`, `DESC` and, optionally, `NAMES` and `WIKI`.

Vanilla also writes `RESOURCES`, `AREA_COSTS` and `FLOOR`, which the game doesn't read for this room.

### ICON

The throne's icon. The value is an icon path, as described under [`ICON` on the init/animal page](../01-animal.md#icon).

| | |
|---|---|
| **Type** | Icon path, or a block |
| **Required** | Yes |

### MINI_COLOR

The throne's colour on the minimap, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

### SPRITES

The images the room is drawn with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TORCH_1X1` | The torches. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _TRANSPORT

The loading station. It has exactly one `ITEMS` block and one statistic.

The examples come from the vanilla `_TRANSPORT.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: DIRT,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `GROUND_THING_1X1` | A marker on the ground. | `1x1` |
| `TORCH_1X1` | The torches. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## The text file

Monuments can also have these lists at the top level of their text file.

### MORE

Things subjects say when they want more of this monument. This example comes from the vanilla `MONUMENT_BLOB.txt`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No. Without it, the game uses standard wording. |

```text
"The air is too dry. More humidifiers would solve that quickly.",
```

### LESS

Things subjects say when they want less of this monument. Vanilla's `MONUMENT_DEATH.txt` has this list.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No. Without it, the game uses standard wording. |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Employment](02-employment.md)
