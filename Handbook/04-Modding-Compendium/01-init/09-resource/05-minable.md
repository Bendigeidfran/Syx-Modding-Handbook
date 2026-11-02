# init/resource/minable

Each file in `init/resource/minable` defines one kind of mineral deposit: which resource it yields, how it looks on the ground, and how much of it appears depending on the terrain.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/minable/` |
| **Files** | One `.txt` file per deposit, e.g. `CLAY.txt` |
| **Key** | The file name without `.txt`. Mine rooms use this key, e.g. `MINABLE: CLAY,` in `assets/init/room/MINE_CLAY.txt`. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded. There must be at least 1 and at most 31. |
| **Images** | In `assets/sprite/resource/minable/`, named by the `SPRITE` tag. |

Vanilla has six deposits: `CLAY`, `COAL`, `GEM`, `ORE`, `SITHILON` and `STONE`. The deposit's name in the game is built from its resource's name.

## Tags

The examples below come from the vanilla `CLAY.txt`.

### RESOURCE

The resource this deposit yields, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: CLAY,
```

### ON_EVERY_MAP

Whether the deposit appears on every map. The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
ON_EVERY_MAP: true,
```

### COLOR

A colour written as `RED_GREEN_BLUE`. The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
COLOR: 255_255_255,
```

### MINIMAP_COLOR

The colour of the deposit on the minimap, written as `RED_GREEN_BLUE`. It's blended with the colour of the ground, at most half and half. In v0.71.44 the richer the deposit, the closer it is to the ground's colour, so rich deposits show this colour least.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
MINIMAP_COLOR: 120_70_50,
```

### FERTILITY_INCREASE

How the deposit changes the soil's fertility, judging by its name. The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | -1 to 1 |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
FERTILITY_INCREASE: 1,
```

### SPRITE

The image the deposit is drawn from: the name of a file in `assets/sprite/resource/minable/`, without `.png`. Several deposits can share one image.

The image must be exactly 364 pixels wide and at least 94 pixels tall, or the game stops loading with an error. If the file doesn't exist, that's also an error. The game cuts it up using a fixed layout, so the safest way to make a new one is to copy a vanilla image and paint over it.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/resource/minable/`) |
| **Required** | Yes |

```text
SPRITE: Clay,
```

### TERRAIN

How strongly the deposit is linked to each type of terrain. The block can contain `OCEAN`, `WET`, `MOUNTAIN`, `FOREST` and `NONE` (open land), and `*` sets every terrain at once. A terrain that's missing counts as 0.

The game scales the values so they add up to 1, so only their sizes relative to each other matter. They're used when your settlement's map is created:

- **How much is placed.** The game's measure of the amount is 38 + 2000 × `OCCURENCE` × the total of each terrain's share of your capital's region multiplied by its value here. It then adds a fixed amount of 1000 at the lowest quality.
- **Where it's placed.** Deposits go first to the parts of the map with the most of the terrains they favour.

In v0.71.44 these values don't affect the world map. The game means to use them to choose which regions get a prospect for this mine, but because of a fault it multiplies them all by one terrain's share of the region, which gives the same result whatever they are.

| | |
|---|---|
| **Type** | Block of decimals, keyed by terrain |
| **Range** | Each value 0 to 1 |
| **Required** | No. Unverified: with no value above 0, the game divides by zero when scaling them, so include at least one. |

```text
TERRAIN: {
	WET: 0.8,
	NONE: 0.05,
},
```

### OCCURENCE

How much of the deposit is placed on your settlement's map, as described under `TERRAIN`. It also sets how many world map regions get a prospect for this mine, compared with other industries. Note the game's spelling. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | No. Default `1`. |

## Related

- [init/resource](00-resource.md)
- [The resource file](01-resource-file.md)
