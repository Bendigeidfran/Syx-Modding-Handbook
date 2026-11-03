# init/room: food rooms

These rooms grow, raise, catch or butcher things: farms, orchards, pastures, fisheries, hunters and the Cannibal room. Besides the tags on this page, they use the [common tags](01-common.md), [employment](02-employment.md) and [production](03-production.md) tags.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `FARM_*.txt`, `ORCHARD_*.txt`, `PASTURE_*.txt`, `FISHERY_*.txt`, `HUNTER_*.txt` and `_CANNIBAL.txt` |
| **Adding new rooms** | Yes for all of these types except `_CANNIBAL`, which is a single room. |

Vanilla has seven farms, one orchard, six pastures, one fishery and one hunter.

## FARM

A farm grows one [crop](../09-resource/04-growable.md). Its `INDUSTRY` block sets its yield. A farm has no `ITEMS` or `SPRITES`: the player paints an area of soil, the plants are drawn from the crop's own settings, and the soil is the fixed sheet `_FARM_DIRT` in `assets/sprite/game/1x1/`. It has four statistics. Moisture and soil fertility affect its output.

The examples come from the vanilla `FARM_GRAIN.txt`.

### GROWABLE

The crop this farm grows, by its key in `assets/init/resource/growable/`.

Each file names the one before it, so create them in this order: the [resource](../09-resource/01-resource-file.md), then the [crop](../09-resource/04-growable.md), then this farm. The game doesn't mind which you write first, as long as they're all there when it loads. A name that doesn't match stops loading with an error listing the available ones.

| | |
|---|---|
| **Type** | Key (a crop) |
| **Required** | Yes |

```text
GROWABLE: GRAIN,
```

### ICON

The farm's icon in the interface, written as an icon path, a block that combines icons, or a list of blocks. Every vanilla farm uses a block, with the background `32->BG->3`, or `32->BG->6` for the indoor mushroom farm, and the crop's resource icon on top. A single icon path such as `24->resource->Grain->0` also works.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom. A block has `BG`, the background icon path, and `FG`, an icon path drawn on top, and any `SHADOW` other than `0` draws a shadow behind `FG`.

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | Yes |

```text
ICON: {
	BG: 32->BG->3,
	FG: 24->resource->Grain->0,
	SHADOW: 2,
},
```

### RESOURCES

The resources the farm is built from, as a list of resource keys, in the same order as `AREA_COSTS`. Each vanilla farm lists only the resource it grows.

| | |
|---|---|
| **Type** | List of keys (resources) |
| **Range** | 4 at most |
| **Required** | No. If it's missing, the farm costs no resources, and `AREA_COSTS` must be an empty list. |

```text
RESOURCES: [GRAIN,],
```

### AREA_COSTS

How much of each resource in `RESOURCES` the farm costs for its area, in the same order. Every vanilla farm uses `0.1`.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have the same number of entries as `RESOURCES` |
| **Required** | Yes |

```text
AREA_COSTS: [0.1,],
```

### MINI_COLOR

The farm's colour on the minimap, written as `RED_GREEN_BLUE`. Vanilla's farms use `74_119_14`, except the cotton farm with `100_119_14`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
MINI_COLOR: 74_119_14,
```

### MINI_COLOR_PATTERN

A pattern that shades the farm's colour on the minimap, repeated across the farm. Each string is a row, and each character is a tile. A digit from `0` to `9` shades that tile, from half brightness up to full. All the strings must be the same length. Every vanilla farm uses the pattern in this example.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 to 32 rows |
| **Required** | No. Without it, the whole farm is one colour. |

```text
MINI_COLOR_PATTERN: [
	"44444444",
	"99999999",
	"00000000",
	"44444444",
],
```

### BONUS

Multiplies the farm's production by climate, as a `CLIMATE` block that can contain `COLD`, `TEMPERATE` and `HOT`, with `*` setting every climate at once. A climate that's missing stays at 1. Vanilla's values run from `0.5` to `2`, and its grain, fruit and vegetable farms have no bonus at all. This example comes from the vanilla `FARM_COTTON.txt`.

| | |
|---|---|
| **Type** | Block |
| **Range** | Each value 0 to 2000 |
| **Required** | No |

```text
BONUS: {
	CLIMATE: {
		COLD: 0.5,
		TEMPERATE: 1,
		HOT: 1.5,
	},
},
```

### INDOORS

Whether the farm must be built indoors. If `false`, it must be outdoors. Vanilla's mushroom farm is the only indoor one.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
INDOORS: false,
```

### WORK

The farm's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. A farm can't do without it: the game crashes during play if it's missing.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.125,
	SOUND: impact->Dig*,
	USES_TOOL: true,
	FULFILLMENT: 0,
},
```

### INDUSTRY.OUT

What the farm yields, in the form described on the [production](03-production.md#industryout) page. It must have an entry, or the game crashes while loading.

Vanilla's `PLAYER` and `AI_RATE` values are `4` and `3.64` for grain, `3` and `2.86` for cotton, `2.1` and `1.4` for fruit and vegetables, `1.1` and `0.88` for mushrooms, `0.25` and `0.208` for herbs, and `0.25` and `0.25` for `FARM_SPICES`, which grows opiates.

| | |
|---|---|
| **Type** | Block, keyed by resource |
| **Range** | A plain rate is 0 to 10000 |
| **Required** | Yes |

```text
OUT: {
	GRAIN: {
		PLAYER: 4,
		AI_RATE: 3.64,
	},
},
```

## ORCHARD

An orchard grows trees that yield its `INDUSTRY` output. Felling a tree also gives an extra resource. It has exactly two `ITEMS`, in this order: the storage (exactly one per room) and the tree. It has four statistics. Moisture and soil fertility affect its output.

The examples come from the vanilla `ORCHARD_FRUIT.txt`.

### INDOORS

Whether the orchard must be built indoors. If `false`, it must be outdoors.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
INDOORS: false,
```

### WORK

The orchard's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. An orchard can't do without it: the game crashes during play if it's missing.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

### INDUSTRY.OUT

What the orchard yields, in the form described on the [production](03-production.md#industryout) page. It must have an entry, or the game crashes while loading.

| | |
|---|---|
| **Type** | Block, keyed by resource |
| **Range** | A plain rate is 0 to 10000 |
| **Required** | Yes |

### EXTRA_RESOURCE

The extra resource a tree gives when it's felled, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
EXTRA_RESOURCE: WOOD,
```

### EXTRA_RESOURCE_AMOUNT

How much of `EXTRA_RESOURCE` a tree gives when it's felled.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes |

```text
EXTRA_RESOURCE_AMOUNT: 8,
```

### DAYS_TILL_GROWTH

How many days a tree takes to grow.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 8 or more. The game's code names a maximum of 1024, but doesn't enforce it. |
| **Required** | Yes |

```text
DAYS_TILL_GROWTH: 64,
```

### RIPE_AT_PART_OF_YEAR

When in the year the fruit ripens, as a share of the year.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
RIPE_AT_PART_OF_YEAR: 0.60,
```

### SPRITES

The images an orchard is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TREE_2X2` | The grown tree. | `2x2` |
| `TREE_1X1` | The young tree. | `1x1` |
| `FRUIT_1X1` | The fruit on the tree. | `1x1` |
| `STORAGE_1X1` | The storage. | `1x1` |
| `EDGE_COMBO` | The edge of the orchard. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## PASTURE

A pasture keeps one [animal](../01-animal.md), and its `INDUSTRIES` recipes set what it yields. A pasture's storage only has room for three outputs. It has exactly two `ITEMS`, in this order: the gate (exactly one per room) and the hut. It has four statistics.

The examples come from the vanilla `PASTURE_AUR.txt` unless stated otherwise.

### ANIMAL

The animal this pasture keeps, by its key in `assets/init/animal/`. The animal's `MASS` decides how many fit: the heavier it is, the fewer there are per tile.

Each file names the one before it, so create them in this order: any new [resources](../09-resource/01-resource-file.md) the animal yields, then the [animal](../01-animal.md), then this pasture. The game doesn't mind which you write first, as long as they're all there when it loads. A name that doesn't match stops loading with an error listing the available ones.

| | |
|---|---|
| **Type** | Key (an animal) |
| **Required** | Yes |

```text
ANIMAL: AUROCH,
```

### INDOORS

Whether the pasture is indoors. An indoor pasture has a storage in place of the outdoor gate. Vanilla only uses this for `PASTURE_BALTI`, which this example comes from.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
INDOORS: true,
```

### INDUSTRIES.INDUSTRY.OUT

What each recipe produces, in the form described on the [production](03-production.md#industryout) page. Every recipe must have an entry, or the game stops loading with an error. A pasture's storage only has room for three outputs.

| | |
|---|---|
| **Type** | Block, keyed by resource |
| **Range** | A plain rate is 0 to 10000 |
| **Required** | Yes |

### FENCE

The game never reads this tag. A pasture's fence is drawn by its `SPRITES`.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
FENCE: WOOD,
```

### SPRITES

The images a pasture is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with, unless the table says otherwise.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FENCE_COMBO` | The fence. | `combo` |
| `FENCE_D_COMBO` | The fence on a diagonal. | `combo` |
| `STORAGE_1X1` | The storage. | `1x1` |
| `GATE_TOP_3X3` | The gate. Only outdoor pastures read this. | `3x3` |
| `AUX_MID_1X1` | The middle of the hut. | `1x1` |
| `AUX_EDGE_1X1` | The edge of the hut. | `1x1` |
| `AUX_BIG_2X2` | A larger part of the hut. | `2x2` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## FISHERY

A fishery catches fish from the water it's built beside. Its own tiles can't be on water, but its shape has to contain enough water tiles to work. Its `INDUSTRY` block sets its yield. It has exactly two `ITEMS`, in this order: the storage (exactly one per room) and the auxiliaries. It has five statistics.

The examples come from the vanilla `FISHERY_NORMAL.txt`.

### STORAGE

The game never reads this tag for fisheries. A fishery's storage holds 31 per tile, fixed in the game's code.

| | |
|---|---|
| **Type** | Integer |
| **Required** | No |
| **Effect** | Unread |

```text
STORAGE: 70,
```

### SPRITES

The images a fishery is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `STORAGE_BOTTOM_1X1` | The storage. | `1x1` |
| `STORAGE_TOP_1X1` | The top of the storage. | `1x1` |
| `WORKTABLE_1X1` | The work table. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |
| `MISC_TOP_1X1` | Clutter on top. | `1x1` |
| `MISC_GROUND_1X1` | Clutter on the ground. | `1x1` |
| `CANDLE_1X1` | The candles. | `1x1` |
| `AUX_MID_1X1` | The middle of an auxiliary. | `1x1` |
| `AUX_EDGE_1X1` | The edge of an auxiliary. | `1x1` |
| `AUX_BIG_2X2` | A large auxiliary. | `2x2` |
| `EDGE_COMBO` | The edge of the room. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## HUNTER

A Hunter room's workers hunt wild animals. Its `INDUSTRIES` recipes set its yield. These recipes don't count towards a resource having a [producer](../09-resource/01-resource-file.md#every-resource-needs-a-producer). It has exactly two `ITEMS`, in this order: the butcher table and the utilities. It has three statistics.

The examples come from the vanilla `HUNTER_NORMAL.txt`.

### INDUSTRIES.INDUSTRY.OUT

What each recipe produces, in the form described on the [production](03-production.md#industryout) page. Every recipe must have an entry, or the game stops loading with an error.

| | |
|---|---|
| **Type** | Block, keyed by resource |
| **Range** | A plain rate is 0 to 10000 |
| **Required** | Yes |

```text
OUT: {
	MEAT: 2.2,
},
```

### MAX_EMPLOYED

How many hunters the settlement can have before each becomes less effective. Above this number, the room's output is divided by 1 + (employed − this value) ÷ (this value × 4).

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 10000, but doesn't enforce it. |
| **Required** | Yes |

```text
MAX_EMPLOYED: 15,
```

### SPRITES

The images a Hunter room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The butcher table. | `combo` |
| `STORAGE_1X1` | The storage. | `1x1` |
| `NICKNACK_1X1` | Clutter. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _CANNIBAL

The room where people are butchered. It has no `INDUSTRY` block: what it yields comes from the [`RESOURCE`](../07-race/01-race-file.md#resource) block of each race. It has exactly one `ITEMS` block, the work bench, and one statistic.

The examples come from the vanilla `_CANNIBAL.txt`.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The work bench. | `combo` |
| `ON_TABLE_1X1` | Things on the work bench. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |
| `CAGE_1X1` | The cage. | `1x1` |
| `CAGE_TOP_1X1` | The top of the cage. | `1x1` |
| `CANDLE_BASE_1X1` | The base of the candles. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Production](03-production.md)
- [init/resource/growable](../09-resource/04-growable.md)
- [init/animal](../01-animal.md)
