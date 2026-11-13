# init/room: production

Rooms that turn resources into other resources describe it with an `INDUSTRY` block, or with `INDUSTRIES` if they offer several recipes for the player to choose between. Some rooms, such as bathhouses, only consume resources, and have just an `IN` block. Which of these forms a room reads depends on its type.

Rates are per worker, per day, before bonuses.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | One `.txt` file per room |

## Tags

### INDUSTRY

One recipe: what the room consumes and what it produces. These examples come from the vanilla `FARM_GRAIN.txt` unless stated otherwise, with a comment left out.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, for room types that read it |

```text
INDUSTRY: {
	OUT: {
		GRAIN: {
			PLAYER: 4,
			AI_RATE: 3.64,
		},
	},
},
```

### INDUSTRIES

Several recipes, as a list of blocks, each holding an `INDUSTRY` block with the same tags. The player chooses between them for each room. Every recipe must have at least one `OUT` resource, or the game stops loading with an error. This example comes from the vanilla `WORKSHOP_SMITHY.txt`.

When a room has more than one recipe, each gets an unlock, `ROOM_<KEY>_RECIPE_<N>`, counting from 0.

| | |
|---|---|
| **Type** | List of blocks |
| **Range** | 1 or more |
| **Required** | Yes, for room types that read it |

```text
INDUSTRIES: [
	{
		INDUSTRY: {
			IN: {
				COAL: 2.0,
				METAL: 0.4,
			},
			OUT: {
				TOOL: {
					PLAYER: 2.0,
				},
			
			},
		},
	},
],
```

### INDUSTRY.IN

What the recipe consumes: each entry names a resource by its key, with its rate. This example comes from the vanilla `BATH_NORMAL.txt`.

A canteen must have at least one entry, because its cooks fetch the first entry as fuel, and the game crashes without it. See [CANTEEN](13-service.md#canteen).

| | |
|---|---|
| **Type** | Block of decimals, keyed by resource |
| **Range** | Each value 0 to 10000 |
| **Required** | No, except for canteens |

```text
IN: {
	COAL: 1.5,
},
```

### INDUSTRY.OUT

What the recipe produces: each entry names a resource by its key. An entry can be written as a plain rate, or as a block that gives AI factions a different rate.

Every resource needs at least one room producing it at a rate above 0, whose ingredients can also be produced, or the game crashes while it's running. See [Every resource needs a producer](../09-resource/01-resource-file.md#every-resource-needs-a-producer).

Whether it's needed depends on the room type. Every recipe in `INDUSTRIES` must have an entry, or the game stops loading with an error. That covers workshops, refiners, pastures and hunters. Farms and orchards must have one too, or the game crashes while loading. Rooms that only consume resources, such as bathhouses, leave it out. A canteen must have no entries at all: any entry crashes the game while it loads.

| | |
|---|---|
| **Type** | Block, keyed by resource |
| **Range** | A plain rate is 0 to 10000 |
| **Required** | Depends on the room type, as described in this entry. |

```text
OUT: {
	GRAIN: {
		PLAYER: 4,
		AI_RATE: 3.64,
	},
},
```

#### PLAYER

The rate of production in your settlement, when the entry is written as a block.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | Yes |

```text
PLAYER: 4,
```

#### AI_RATE

The rate for AI factions. This is also the rate that decides whether the room counts as a producer of the resource, so if it's the only room making a resource, this must be above 0, or the game crashes while it's running.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | No. If it's missing, `PLAYER` is used. |

```text
AI_RATE: 3.64,
```

#### AI_RECOVERY

A recovery rate for AI factions. Unverified: the game passes this on to its recipes, but what it changes hasn't been confirmed. Vanilla uses `0.5` for pasture meat.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | No. Default `1`. |

```text
AI_RECOVERY: 0.5,
```

### INDUSTRY.ICON

An icon for the recipe. Without it, the game builds one from the icons of the resources produced. This example comes from the vanilla `WORKSHOP_RATION.txt`.

It's written like a room's [`ICON`](01-common.md#icon). An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | No |

```text
ICON: 24->resource->Recipe->3,
```

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Employment](02-employment.md)
- [init/resource](../09-resource/00-resource.md)
