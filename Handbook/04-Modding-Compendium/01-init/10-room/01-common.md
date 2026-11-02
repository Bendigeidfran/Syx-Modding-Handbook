# init/room: common tags

These tags are used by most rooms, whatever their type: what a room costs, how it appears in the interface, its furniture and its upgrades.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | One `.txt` file per room |
| **Text file** | `assets/text/room/<KEY>.txt` |

## Tags

### ICON

The room's icon in the interface. The value can be an icon path, as described under [`ICON` on the init/animal page](../01-animal.md#icon), or a block that combines icons, as described under [`ICON` on the event page](../05-event/01-structure.md#icon). This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | Icon path, or a block |
| **Required** | Yes |

```text
ICON: 32->SERVICE->2,
```

### RESOURCES

The resources the room is built from, as a list of resource keys. `AREA_COSTS`, `ITEMS.COSTS` and `UPGRADES.RESOURCE_MASK` all follow this list's order. More than four is a loading error. This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | List of keys (resources) |
| **Range** | 4 at most |
| **Required** | No. If it's missing, the room costs no resources, and `AREA_COSTS` must be an empty list. |

```text
RESOURCES: [STONE,STONE_CUT,METAL,],
```

### AREA_COSTS

How much of each resource in `RESOURCES` the room costs for its floor area, in the same order. The list must have exactly as many entries as `RESOURCES`. This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have the same number of entries as `RESOURCES` |
| **Required** | Yes |

```text
AREA_COSTS: [0,0,0,],
```

### FLOOR

The floor laid in the room, by its key. It can be a single floor, or a list with one floor for each upgrade level. If the room has more upgrades than floors, the higher upgrades use the last floor. A race's [`ROOM_FLOOR_OVERRIDE`](../07-race/01-race-file.md#room_floor_override) can replace it when you're playing that race. This example comes from the vanilla `WELL_NORMAL.txt`.

| | |
|---|---|
| **Type** | Key (a floor), or a list of keys |
| **Required** | No. Without it, the room lays no floor. |

```text
FLOOR: [DIRT,STONE1,STONE2,],
```

### MINI_COLOR

The room's colour on the minimap, written as `RED_GREEN_BLUE`. This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
MINI_COLOR: 70_0_255,
```

### MINI_COLOR_PATTERN

A pattern that shades the room's colour on the minimap, repeated across the room. Each string is a row, and each character is a tile. A digit from `0` to `9` shades that tile, from half brightness up to full. Any other character leaves it at full brightness. All the strings must be the same length, which is a loading error otherwise. This example comes from the vanilla `TEMPLE_AMINION.txt`.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 to 31 rows |
| **Required** | No. Without it, the whole room is one colour. |

```text
MINI_COLOR_PATTERN: [
	"--------",
	"-0----0-",
	"---00---",
	"--0440--",
	"-04--40-",
	"-04--40-",
	"--4--4--",
	"--------",	
],
```

### ITEMS

The furniture the player can place in the room, as a list of blocks. For most room types, the game's code fixes how many there must be and what each one is, so the list must keep the same length and order as the vanilla file for that type. The wrong number is a loading error. Each block has its name and description in the text file. These examples come from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | Yes, for room types that have items |

```text
ITEMS: [
	{
		COSTS: [0,2,1,],
		STATS: [1,0,],
	},
	{
		COSTS: [1,1,0,],
		STATS: [0,4,],
	},
],
```

#### COSTS

How much of each resource in `RESOURCES` one of these items costs, in the same order. The list must have exactly as many entries as `RESOURCES`. Items that come in several sizes multiply this by a figure set in the game's code.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have the same number of entries as `RESOURCES` |
| **Required** | Yes |

```text
COSTS: [0,2,1,],
```

#### STATS

What one of these items adds to the room's statistics, such as how many workers it fits or how many people it serves. There's one number for each statistic the room type has, in the order of the `STATS` list in the text file. Items that come in several sizes multiply this by a figure set in the game's code.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have one entry for each statistic of this room type |
| **Required** | Yes |

```text
STATS: [1,0,],
```

### SPRITES

The images the room is drawn with. It's a block of named sprite entries, in the format described on the [sprite/game](../../03-sprite/03-game.md#sprite-entries) page. The game's code decides which names each room type reads, and they're listed with each room type. Vanilla's monuments write this as a list of blocks instead. This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block of sprite entries, or a list of blocks |
| **Required** | Yes, for most room types |

```text
TORCH_1X1: [
	{	
		ROTATES: false,
		TINT: true,
		SHADOW_LENGTH: 4,
		FRAMES: [
			TABLES: 4,	
		],
	},
],
```

### ENVIRONMENT_EMIT

What the room gives off into its surroundings, such as noise. Each entry names an environment effect, by a key from `assets/init/settlement/environment/`: `_GUARD`, `_LIGHT`, `_NOISE`, `_PUNISHMENT`, `_SPACE`, `_URBANISATION`, `_WATER_SALT` or `_WATER_SWEET`. A key that doesn't match is skipped, and only reported when Debug is on. Some room types may set these effects in their own code. This example comes from the vanilla `_GUARD.txt`.

| | |
|---|---|
| **Type** | Block of blocks, keyed by environment effect |
| **Required** | No |

```text
ENVIRONMENT_EMIT: {
	_GUARD: {
		VALUE: 1,
		RADIUS: 1,
	},
},
```

#### VALUE

How strong the effect is.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
VALUE: 1,
```

#### RADIUS

How far the effect reaches. With `0`, the room doesn't give off the effect at all.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
RADIUS: 1,
```

### DEGRADE_RATE

How quickly the room wears out and needs maintenance. Some room types set this in the game's code and ignore the tag: farms never degrade, for example. This example comes from the vanilla `_DUMP_CORPSE.txt`, the only vanilla room that uses it.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `0.75`. |

```text
DEGRADE_RATE: 0,
```

### REQUIRES

Conditions that must be met before the room can be built, in the [condition format](../05-event/02-occurrence.md#conditions). Vanilla doesn't use this tag: it unlocks rooms through technologies and other unlocks instead, as described in the notes on this page.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No |

### UPGRADES

The room's upgrade levels, as a list of blocks. The first block is the room as first built, and each later block is one upgrade. Without this tag, the room can't be upgraded. These examples come from the vanilla `_HEARTH.txt`.

| | |
|---|---|
| **Type** | List of blocks |
| **Range** | 1 or more |
| **Required** | No |

```text
UPGRADES: [
	{
		RESOURCE_MASK: [2,0,0,0,],
		BOOST: 0,
	},
	{
		RESOURCE_MASK: [4,4,3,0,],
		BOOST: 1.0,
	},
	{
		RESOURCE_MASK: [6,8,11,10,],
		BOOST: 1.0,
	},
],
```

#### RESOURCE_MASK

Multiplies the room's costs at this level, one number for each resource in `RESOURCES`, in the same order. It applies to both `AREA_COSTS` and `ITEMS.COSTS`. A `0` means the level doesn't use that resource. If the list is shorter than the longest one in `UPGRADES`, the missing entries count as `1`.

| | |
|---|---|
| **Type** | List of decimals |
| **Required** | Yes |

```text
RESOURCE_MASK: [2,0,0,0,],
```

#### BOOST

The bonus this level gives to the room's production, where the room type uses one.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
BOOST: 0,
```

#### AI

The game reads this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | No |
| **Effect** | None |

## The text file

Each room needs a file of the same name in `assets/text/room/`. `NAME`, `NAMES`, `DESC` and `WIKI` go inside an `INFO` block in vanilla, but can also be written at the top level of the file. The other tags stay at the top level. Room types can read further tags of their own, which are listed with each type. These examples come from the vanilla `BATH_NORMAL.txt` and `WORKSHOP_SMITHY.txt`.

### NAME

The room's singular name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Bathhouse",
```

### NAMES

The room's plural name.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

```text
NAMES: "Bathhouses",
```

### DESC

The room's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Where subjects can get clean and relax.",
```

### WIKI

Adds an article about the room to the in-game wiki, opened from a button in the room's panel. The tags inside it are described in full under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Without it, the room has no article. |

### ITEMS

The names and descriptions of the room's furniture, as a list of blocks in the same order as `ITEMS` in the room file. It must have the same number of blocks.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | Yes, for room types that have items |

#### NAME

The item's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Storage",
```

#### DESC

The item's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "The internal storage for produce.",
```

### STATS

The names and descriptions of the room's statistics, as a list of blocks. The game's code fixes how many each room type has. Some are named by the game itself, so vanilla files can have an empty block in their place. The wrong number of blocks is a loading error.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | Yes, for room types with statistics named here |

```text
STATS: [
	{
		NAME: "Baths",
		DESC: "Available bathing spots",
	},
	{
		NAME: "Relaxation",
		DESC: "Where people can relax afterwards.",
	},
],
```

### UPGRADES

Optional text for each upgrade level, as a list of text.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

### BONUS

The game never reads this block from the text file, though many vanilla rooms have one. A room's bonus takes its name from the room itself. This example comes from the vanilla `WORKSHOP_SMITHY.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
BONUS: {
	NAME: "Metallurgy",
	DESC: "Increases effectiveness of smithies",
},
```

## Notes

### Unlocking rooms

The game creates an unlock for each room, its upgrades and, where a room has several recipes, each recipe. Technologies and other files name these in their unlock lists:

- `ROOM_<KEY>` for the room, e.g. `ROOM_BARRACKS_VANILLA`;
- `ROOM_<KEY>_UPGRADE_<N>` for an upgrade, counting from 1, e.g. `ROOM_SPEAKER_NORMAL_UPGRADE_1`;
- `ROOM_<KEY>_RECIPE_<N>` for a recipe, counting from 0.

For rooms whose key starts with `_`, the name has a single underscore: `_HOME` gives `ROOM_HOME_UPGRADE_1`.

### Unused text file

`assets/text/room/_MINE.txt` has no matching room, and the game doesn't read it. Each mine has its own text file.

### Sound

A room's sounds aren't set in its file. The game looks them up by name in the files in `assets/audio/config/`, using `ROOM_<KEY>`, `ROOM_CLICK_<KEY>`, `ROOM_WORK_<KEY>` and `ROOM_SERVICE_<KEY>`. If an entry is missing, the room is silent, and the game only reports it when Debug is on.

## Related

- [init/room](00-room.md)
- [Employment](02-employment.md)
- [Production](03-production.md)
- [Services](04-services.md)
