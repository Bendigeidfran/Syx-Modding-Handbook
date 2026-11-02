# init/room: service rooms

These rooms serve your subjects: places to eat, drink, wash and be entertained, along with nurseries and breeders. Besides the tags on this page, they use the [common tags](01-common.md) and [services](04-services.md) tags, and those with workers use [employment](02-employment.md).

Many rooms here have a fixed need in the game's code, so a `NEED` tag written in their `SERVICE` block is ignored. Where a room reads `NEED`, the section below says so.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `ARENAG_*`, `BARBER_*`, `BATH_*`, `BREEDER_*`, `CANTEEN_*`, `EATERY_*`, `FIGHTPIT_*`, `LAVATORY_*`, `MARKET_*`, `NURSERY_*`, `PLEASURE_*`, `SPEAKER_*`, `STAGE_*`, `TAVERN_*`, `WELL_*` and `_HEARTH.txt` |
| **Adding new rooms** | Yes for every type except `_HEARTH`, which is a single room. |
| **Text file** | `assets/text/room/<KEY>.txt` |

## ARENAG

The grand arena. Its `SERVICE` block reads `NEED`. It has exactly one `ITEMS` block, the entrance, and two statistics.

The examples come from the vanilla `ARENAG_NORMAL.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: ARENA_G,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CONSTRUCT_1X1` | The room's construction marker. | `1x1` |
| `WALL_1X1` | The walls. | `1x1` |
| `TOWER_1X1` | The towers. | `1x1` |
| `TORCH_1X1` | The torches. | `1x1` |
| `TORCH_TOP_1X1` | The tops of the torches. | `1x1` |
| `STAIRS_SINGLE_1X1` | Stairs one tile wide. | `1x1` |
| `STAIRS_LEFT_1X1` | The left of the stairs. | `1x1` |
| `STAIRS_CENTRE_1X1` | The centre of the stairs. | `1x1` |
| `STAIRS_RIGHT_1X1` | The right of the stairs. | `1x1` |
| `SEAT_BOX` | The seats. | `box` |
| `RIM_BOX` | The rim of the arena. | `box` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## BARBER

Its `SERVICE` block reads `NEED`. It has exactly two `ITEMS`, in this order: the booth and the carpet. It has three statistics.

The examples come from the vanilla `BARBER_NORMAL.txt`.

### WORK_TIME_IN_DAYS

How long a barber's work on one subject takes, in days of work time.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
WORK_TIME_IN_DAYS: 0.2,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_CENTRE_1X1` | The centre of a table. | `1x1` |
| `TABLE_CENTRE_TOP_1X1` | Things on the centre of a table. | `1x1` |
| `CHAIR_1X1` | The chairs. | `1x1` |
| `SEPARATOR_1X1` | The separators between booths. | `1x1` |
| `NICKNACK_1X1` | Clutter. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## BATH

Its `SERVICE` block reads `NEED`. Its `INDUSTRY` block has `IN` entries for what it consumes to heat the water, with no output. It has exactly two `ITEMS`, in this order: the basin and the benches. It has two statistics. Its text file needs some extra tags, listed under [The text file](#the-text-file).

The examples come from the vanilla `BATH_NORMAL.txt`.

### WATER_COLOR

The colour of the water, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
WATER_COLOR: 20_40_100,
```

### WATER_OPACITY

How opaque the water is. The game halves this value before drawing the water.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
WATER_OPACITY: 0.75,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FRAME_COMBO` | The edge of the basin. | `combo` |
| `POOL_FLOOR_TEXTURE` | The floor of the basin. | `texture` |
| `ENTRANCE_1X1` | The way into the basin. | `1x1` |
| `WORK_1X1` | The work spot. | `1x1` |
| `OVEN_1X1` | The oven. | `1x1` |
| `PIPE_1X1` | The pipes. | `1x1` |
| `BENCH_1X1` | The benches. | `1x1` |
| `TORCH_1X1` | The torches. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## BREEDER

A room where a race breeds new members. Its `INDUSTRY` block must have at least one `IN` resource, as food, or the game stops loading with an error. It has exactly two `ITEMS`, in this order: the breeding spot and the humidifier. It has two statistics.

The examples come from the vanilla `BREEDER_GARTHIMI.txt`.

### RACE

The race this room breeds, by its key.

| | |
|---|---|
| **Type** | Key (a race) |
| **Required** | Yes |

```text
RACE: GARTHIMI,
```

### INCUBATION_DAYS

How many days it takes to breed a new member, before bonuses. Don't use `0`, because the game divides by this value.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 127, but doesn't enforce it. |
| **Required** | Yes |

```text
INCUBATION_DAYS: 8,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries). In this room, the kind comes at the start of the name.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `1x1_RIM_CORNER` | The corners of a breeding spot's rim. | `1x1` |
| `1x1_RIM_EDGE` | The edges of a breeding spot's rim. | `1x1` |
| `1x1_RIM_DECOR` | Decoration on the rim. | `1x1` |
| `1x1_WORM` | The creature in a breeding spot. | `1x1` |
| `1x1_CORNER` | The corner of the humidifier. | `1x1` |
| `1x1_DECOR` | Small decoration. | `1x1` |
| `2x2_DECOR` | Large decoration. | `2x2` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## CANTEEN

Its need is fixed to hunger. Its `INDUSTRY` block has `IN` entries for what it consumes as fuel. It has exactly two `ITEMS`, in this order: the cooking station and the tables. It has three statistics. Vanilla gives it a low `SERVICE.USAGE` of `0.125`, which makes subjects less inclined to eat here.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `PLATE_1X1` | The plates. | `1x1` |
| `OVEN_1X1` | The ovens. | `1x1` |
| `OVEN_BENEATH_1X1` | Beneath an oven. | `1x1` |
| `OVEN_BENEATH_USED_1X1` | Beneath an oven in use. | `1x1` |
| `TOOLS_1X1` | Tools. | `1x1` |
| `STOOL_1X1` | The stools. | `1x1` |
| `DECOR_1X1` | Decoration. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## EATERY

Its need is fixed to hunger. It has exactly one `ITEMS` block, the stall, and two statistics.

The examples come from the vanilla `EATERY_NORMAL.txt`.

### USAGE

The game never reads this tag at the top level of the file. `SERVICE.USAGE` is the one that counts.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
USAGE: 1.0,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `STALL_BOTTOM_1X1` | The stalls. | `1x1` |
| `STALL_TOP_1X1` | The tops of the stalls. | `1x1` |
| `CRATE_BOTTOM_A_1X1` | The crates. | `1x1` |
| `CRATE_TOP_1X1` | The tops of the crates. | `1x1` |
| `MISC_BOTTOM_1X1` | Clutter. | `1x1` |
| `MISC_1X1` | Clutter on top. | `1x1` |
| `CARPET_COMBO` | The carpet. | `combo` |

| Tag | Meaning | Effect |
|---|---|---|
| `CRATE_BOTTOM_B_1X1` | Never read, though vanilla has it. | Unread |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## FIGHTPIT

The fight pit. Its `SERVICE` block reads `NEED`. It has exactly one `ITEMS` block and two statistics.

The examples come from the vanilla `FIGHTPIT_NORMAL.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: ARENA,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `WALL_1X1` | The walls. | `1x1` |
| `TOWER_1X1` | The towers. | `1x1` |
| `TORCH_1X1` | The torches. | `1x1` |
| `TORCH_TOP_1X1` | The tops of the torches. | `1x1` |
| `STAIRS_LEFT_1X1` | The left of the stairs. | `1x1` |
| `STAIRS_CENTRE_1X1` | The centre of the stairs. | `1x1` |
| `STAIRS_RIGHT_1X1` | The right of the stairs. | `1x1` |
| `SEAT_BOX` | The seats. | `box` |
| `RIM_BOX` | The rim of the pit. | `box` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## LAVATORY

Its `SERVICE` block reads `NEED`. It has exactly two `ITEMS`, in this order: the latrine and the basins. It has three statistics.

The examples come from the vanilla `LAVATORY_NORMAL.txt`.

### DEFAULT_STANDING

The game never reads this block.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
DEFAULT_STANDING: {
	FROM: 1.0,
	TO: 3.0,
	EXPONENT: 0.8,
	MULTIPLIER: 1,
},
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `SIT_COMBO` | The seats. | `combo` |
| `SIT_ONTOP_COMBO` | The tops of the seats. | `combo` |
| `SHITHOLE_1X1` | The hole in a seat. | `1x1` |
| `SHIT_1X1` | Its contents. | `1x1` |
| `SHIT_LID_1X1` | Its lid. | `1x1` |
| `TABLE_COMBO` | The tables holding the basins. | `combo` |
| `BASIN_1X1` | The basins. | `1x1` |
| `BASIN_WATER_1X1` | The water in a basin. | `1x1` |
| `NICKNACK_1X1` | Clutter. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## MARKET

Its need is fixed to shopping, so vanilla's `NEED: SHOPPING` is ignored. It has exactly one `ITEMS` block, the stall, and two statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `STALL_BOTTOM_COMBO` | The stalls. | `combo` |
| `STALL_TOP_1X1` | The tops of the stalls. | `1x1` |
| `CRATE_1X1` | The crates. | `1x1` |
| `MISC_BOTTOM_1X1` | Clutter. | `1x1` |
| `MISC_1X1` | Clutter on top. | `1x1` |
| `CARPET_COMBO` | The carpet. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## NURSERY

Its `SERVICE` block only reads `RADIUS`, and its text file only needs `SERVICE.VERB`. It has exactly three `ITEMS`, in this order: the play station, the carpets and the storage. It has three statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries).

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `1x1_CHAIR` | The chairs. Note the order of this name. | `1x1` |
| `STUFF_1X1` | Toys and clutter. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

### INDUSTRY

The game never reads this block for nurseries, though vanilla has one. The examples come from the vanilla `NURSERY_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
INDUSTRY: {
	IN: {
		FRUIT: 0.5,
	},
	OUT: {
	
	},
},
```

### SPRITES2

The game never reads this block, though vanilla has one.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

## PLEASURE

Its `SERVICE` block reads `NEED`. It has exactly three `ITEMS`, in this order: the booth, the decorations and the carpets. It has three statistics.

The examples come from the vanilla `PLEASURE_NORMAL.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: WOOD,
```

### COLOR_PIXEL_BASE

A base colour, written as `RED_GREEN_BLUE`, that the room builds a range of colours from.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR_PIXEL_BASE: 103_80_60,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BED_HEAD_1X1` | The head of a bed. | `1x1` |
| `BED_TAIL_1X1` | The foot of a bed. | `1x1` |
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_TOP_1X1` | Things on the tables. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_TOP_1X1` | Things on the shelves. | `1x1` |
| `NICKNACK_1X1` | Clutter. | `1x1` |
| `WALLS_COMBO` | The walls of a booth. | `combo` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## SPEAKER

Its `SERVICE` block reads `NEED`. It has exactly one `ITEMS` block and two statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CENTER_COMBO` | The centre. | `combo` |
| `FRAME_COMBO` | The frame. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## STAGE

Its `SERVICE` block reads `NEED`. It has exactly one `ITEMS` block and two statistics.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `A_BOX` | The first part of the stage. | `box` |
| `B_BOX` | The second part of the stage. | `box` |
| `C_BOX` | The third part of the stage. | `box` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## TAVERN

Its need is fixed to thirst, so vanilla's `NEED: THIRST` is ignored. It has exactly three `ITEMS`, in this order: the table, the nicknacks and the carpets. It has two statistics. The colour of the drink in its jugs comes from [init/resource/drinkable](../09-resource/02-drinkable.md).

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_DECOR_1X1` | Things on the tables. | `1x1` |
| `JUG_1X1` | The jugs. | `1x1` |
| `JUG_FILL_1X1` | The drink in a jug. | `1x1` |
| `CHAIR_1X1` | The chairs. | `1x1` |
| `STORAGE_1X1` | The storage. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |
| `MISC_DECOR_1X1` | Clutter on top. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## WELL

It has no workers. Its `SERVICE` block reads `NEED`. It has exactly one `ITEMS` block and one statistic.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `STONE_RING_COMBO` | The ring of stone around the well. | `combo` |
| `STONE_RING_STENCIL_COMBO` | A shape used with the ring. | `combo` |
| `ROOF_EDGE_1X1` | The edge of the roof. | `1x1` |
| `ROOF_MID_1X1` | The middle of the roof. | `1x1` |
| `FOUNTAIN_1X1` | The fountain. | `1x1` |
| `BUCKET_1X1` | The buckets. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _HEARTH

It has no workers. Its `SERVICE` block reads `NEED`. It has exactly one `ITEMS` block and one statistic.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `HEARTH_COMBO` | The hearth. | `combo` |
| `BENCH_1X1` | The benches. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## The text file

Bathhouses need these extra tags at the top level of their text file. The examples come from the vanilla `BATH_NORMAL.txt`.

### HEATING

The name of the heating statistic in the room's panel.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, for bathhouses |

```text
HEATING: "Heating",
```

### HEATING_DESC

The description of the heating statistic.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, for bathhouses |

```text
HEATING_DESC: "Current Heating of the basins. Make sure coal is nearby",
```

### HEATING_PROBLEM

The warning shown when the water is too cold.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, for bathhouses |

```text
HEATING_PROBLEM: "Low heating decreases the experience!",
```

### WATER_PROBLEM

The game must find this tag, but the warning that would use it is switched off in v0.71.44.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, for bathhouses |
| **Effect** | None |

```text
WATER_PROBLEM: "A bath need access to fresh water to function properly.",
```

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Services](04-services.md)
- [init](../00-init.md)
