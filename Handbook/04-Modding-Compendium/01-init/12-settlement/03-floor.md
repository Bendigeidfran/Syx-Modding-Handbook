# init/settlement/floor

These files define the floors of the city. A floor with a `ROAD` block is a road the player can build. A floor without one isn't a road, but other files can still use it by its key, such as a room's `FLOOR` tag.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/settlement/floor/` |
| **Files** | One `.txt` file per floor, e.g. `STONE1.txt`, plus `_DEFAULT_ROAD.txt` and `_MAIN_ROAD.txt` |
| **Key** | The file name, e.g. `STONE1` |
| **Adding new floors** | Yes, up to 62 files, not counting `_DEFAULT_ROAD.txt` and `_MAIN_ROAD.txt`. More stops the game with an error. |
| **Text file** | `assets/text/settlement/floor/<KEY>.txt`, required for floors with a `ROAD` block |
| **Sprites** | Images in `assets/sprite/game/texture/`, named by `GAME_TEXTURE`. All floors also share [`_FloorExtra.png`](../../03-sprite/10-settlement/01-floor.md). |

## Tags

The examples come from the vanilla `STONE1.txt` unless stated otherwise.

### GAME_TEXTURE

The image the floor is drawn with. See [Textures](../../03-sprite/03-game.md#textures) for how these images are laid out.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
GAME_TEXTURE: {
	FILE: STONE,
	ROW: 5,
},
```

#### FILE

The name of an image in `assets/sprite/game/texture/`.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
FILE: STONE,
```

#### ROW

The row to use in the image, counting from 0. A row past the end of the image draws nothing, and the game only reports it when Debug is on.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes |

```text
ROW: 5,
```

### COLOR_MASK

The colour the floor's texture is tinted with, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR_MASK: 255_255_255,
```

### IS_GRASS

If `true`, the floor takes the colour of the map's grass instead of its `COLOR_MASK`. This example comes from the vanilla `GRASS.txt`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
IS_GRASS: true,
```

### ROAD

Makes the floor a road, with its own name, cost and effects. All the tags below go inside this block.

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Without it, the floor isn't a road. |

```text
ROAD: {
	ENVIRONMENT: {
		
	},
	PREFERENCE: {
		*: 0.5,
	},
	SPEED: 2,
	RESOURCE: STONE,
	RESOURCE_AMOUNT: 1,
	DURABILITY: 0.5,
},
```

#### ENVIRONMENT

How much the road adds to [environment effects](01-environment.md) on its own tile. Each entry names an effect by its key, and `*` covers every effect. The road adds nothing once it's fully worn or if it's inside a room. All the vanilla roads with this block leave it empty.

| | |
|---|---|
| **Type** | Block of decimals, keyed by environment effect |
| **Range** | Each value 0 to 1 |
| **Required** | No. A missing effect counts as `0`. |

```text
ENVIRONMENT: {
	
},
```

#### PREFERENCE

How much each race likes this road by default, from 0 to 1. Each entry names a race by its key, and `*` covers every race. A race's own [`PREFERRED.ROAD`](../07-race/02-preferences.md#road) block overrides this for any road it lists.

| | |
|---|---|
| **Type** | Block of decimals, keyed by race |
| **Range** | Each value 0 to 1 |
| **Required** | No. A missing race counts as `0`. |

```text
PREFERENCE: {
	*: 0.5,
},
```

#### SPEED

How much the road speeds up walkers, as a level from 0 to 4. Level 0 adds nothing, and each level adds 5%, up to 20% at level 4.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 to 4. The game's range check only enforces the minimum, but a higher value crashes the game while loading. |
| **Required** | Yes |

```text
SPEED: 2,
```

#### RESOURCE

The resource the road is built from, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | No. Without it, the road costs nothing. A name that doesn't match counts as no resource, and is only reported when Debug is on. |

```text
RESOURCE: STONE,
```

#### RESOURCE_AMOUNT

How much of the resource each tile of road costs. Maintenance uses it too, so a higher amount costs more to maintain.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes, if the road has `RESOURCE` |

```text
RESOURCE_AMOUNT: 1,
```

#### DURABILITY

How well the road resists wear, from 0 to 1. Higher values need less maintenance.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DURABILITY: 0.5,
```

## The text file

Each floor with a `ROAD` block needs a file of the same name in `assets/text/settlement/floor/`. Other floors don't use one. These examples come from the vanilla `STONE1.txt`.

### NAME

The road's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Paved Road",
```

### DESC

The road's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "The road of choice for your subjects. Durable, but requires stone to construct.",
```

## _DEFAULT_ROAD.txt

This file doesn't define a floor. It names an existing one as the game's default road. The game uses its icon for some tools, and puts it in place of any floor in a saved game that no longer exists.

### FILE

The key of the floor to use.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FILE: DIRT,
```

## Notes

### _MAIN_ROAD.txt

`_MAIN_ROAD.txt` defines the road laid when a settlement's map is generated. It uses the tags above, and vanilla gives it no `ROAD` block.

### Unlocks

Each road gets an unlock named `FLOOR_<KEY>`.

## Related

- [init/settlement](00-settlement.md)
- [Environment effects](01-environment.md)
- [Race preferences](../07-race/02-preferences.md)
- [sprite/game](../../03-sprite/03-game.md)
- [sprite/settlement/floor](../../03-sprite/10-settlement/01-floor.md)
