# init/resource/growable

Each file in `init/resource/growable` defines one crop: which resource it yields, when it's harvested, how much of it grows wild on new maps, and how the plants look.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/growable/` |
| **Files** | One `.txt` file per crop, e.g. `COTTON.txt` |
| **Key** | The file name without `.txt`. Farm rooms use this key, e.g. `GROWABLE: GRAIN,` in `assets/init/room/FARM_GRAIN.txt`. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded. There must be at least one. |
| **Images** | In `assets/sprite/resource/growable/`, named by `SPRITE.SPRITE`. |

Vanilla has seven crops: `COTTON`, `FRUIT`, `GRAIN`, `HERB`, `MUSHROOM`, `OPIATES` and `VEGETABLE`.

## Tags

The examples below come from the vanilla `COTTON.txt`.

### RESOURCE

The resource this crop yields, by its key. Two crops can't yield the same resource: that stops the game from loading with an error.

Each file names the one before it, so create them in this order: the [resource](01-resource-file.md), then this crop, then the [farm](../10-room/05-food.md#farm) that names it. The game doesn't mind which you write first, as long as they're all there when it loads. A name that doesn't match stops loading with an error listing the available ones.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: COTTON,
```

### SEASONAL_OFFSET

When in the year the crop is harvested, as a share of the year: `0` is the start and `0.5` is halfway through. Farms plant the crop three eighths of a year before this. The same day sets when a world map region delivers the crop.

Vanilla uses `0.375` (`HERB`, `VEGETABLE`), `0.4375` (`FRUIT`), `0.5` (`COTTON`), `0.5625` (`GRAIN`, `OPIATES`) and `0.75` (`MUSHROOM`).

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
SEASONAL_OFFSET: 0.5,
```

### GROWTH_VALUE

How much of this crop grows wild when a new map is created, together with `CLIMATE_BONUS`. The game uses the square root of this value, so `0.25` gives half as much as `1`.

This doesn't affect what farms produce.

Vanilla uses `0.1` (`OPIATES`), `0.3` (`MUSHROOM`), `0.35` (`COTTON`), `0.5` (`FRUIT`, `HERB`, `VEGETABLE`) and `1.0` (`GRAIN`).

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
GROWTH_VALUE: 0.35,
```

### MINIMAP_COLOR

A colour written as `RED_GREEN_BLUE`. The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
MINIMAP_COLOR: 255_127_0,
```

### CLIMATE_BONUS

How much of this crop grows wild in each climate when a new map is created, multiplied with `GROWTH_VALUE`. The block can contain `COLD`, `TEMPERATE` and `HOT`, and `*` sets every climate at once. A climate that's missing counts as 0.

This doesn't affect what farms produce.

Vanilla's values run from `0.1` to `1.1`. `GRAIN` has `1` in every climate, while `HERB` has `COLD` 1, `TEMPERATE` 0.2 and `HOT` 0.1.

| | |
|---|---|
| **Type** | Block of decimals, keyed by climate |
| **Range** | Each value 0 to 10000 |
| **Required** | No. Without it, the crop doesn't grow wild. |

```text
CLIMATE_BONUS: {
	COLD: 0.2,
	TEMPERATE: 0.8,
	HOT: 1.1, 
},
```

### SPRITE

How the plants look.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

### SPRITE.SPRITE

The image the plants are drawn from: the name of a file in `assets/sprite/resource/growable/`, without `.png`. Several crops can share one image.

The image must be exactly 460 pixels wide and at least 34 pixels tall, or the game stops loading with an error. The game cuts it up using a [fixed layout](../../03-sprite/08-resource.md#growable), so the safest way to make a new one is to copy a vanilla image and paint over it. The vanilla `_Flower.png` is used for wild flowers, not for a crop.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/resource/growable/`) |
| **Required** | Yes |

```text
SPRITE: Cotton,
```

### SPRITE.WIND_SWAY

How much the plants move in the wind. Vanilla uses `0` to `1.5`, with `GRAIN` the highest.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | No. Default `1`. |

```text
WIND_SWAY: 0.5,
```

### SPRITE.POLLEN

How much pollen drifts from ripe plants. With `0`, there's none. Vanilla uses `0` for every crop except `OPIATES`, which has `1`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes |

```text
POLLEN: 0,
```

### SPRITE.COLOR_POLLEN

The colour of the pollen, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes, even if `POLLEN` is `0`. |

```text
COLOR_POLLEN: 255_255_255,
```

### SPRITE.STEM and SPRITE.GROWTH

The two parts of the plant, each coloured separately: the stem, and the growth at the top of it. Both blocks are required, and both use the same tags. These examples come from the `STEM` block.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

#### DEAD, LIVE and RIPE

The part's colours as it grows, written as `RED_GREEN_BLUE`. It moves from `DEAD` towards `LIVE` as it grows, and from `LIVE` towards `RIPE` as it ripens.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes, all three. |

```text
DEAD: 99_76_33,
```

#### SHADOW_LENGTH

The length of the shadow this part casts. Vanilla uses `0` to `6`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 32 |
| **Required** | Yes |

```text
SHADOW_LENGTH: 0,
```

#### SHADOW_HEIGHT

How far above the ground this part's shadow starts. Vanilla uses `0` to `7`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 32 |
| **Required** | Yes |

```text
SHADOW_HEIGHT: 6,
```

#### WIND_SWAY

How much this part moves in the wind, multiplied with `SPRITE.WIND_SWAY`. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | No. Default `0.8` for the stem and `1` for the growth. |

## Related

- [init/resource](00-resource.md)
- [The resource file](01-resource-file.md)
