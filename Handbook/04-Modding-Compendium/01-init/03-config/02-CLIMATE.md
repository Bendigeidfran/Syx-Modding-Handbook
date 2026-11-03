# init/config/CLIMATE.txt

`CLIMATE.txt` configures the game's three climates: cold, temperate and hot. Every region of the world has a mix of climates, and your settlement takes its climate from where you found it. The settings here decide how warm each climate is through the year, how its ground looks, and what bonuses or penalties come with it.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/CLIMATE.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new climates** | No. The three climates, `COLD`, `TEMPERATE` and `HOT`, are built into the game. You can change their settings but not add, remove or rename them. |
| **Companion files** | None. The climates' names and descriptions don't come from a file in `text/config`. |

## File structure

The file has one block for each climate. Every block uses the same tags:

```text
COLD: {
	ICON: 32->SEASONS->3,
	SEASONAL_CHANGE: 1.0,
	TEMP_COLD: -0.36,
	TEMP_WARM: 0.31,
	COLOR: 0_100_255,
	GROUND: {
		DRY: 193_181_135,
		WET: 74_55_55,
	},
	BOOST: {
		PHYSICS_HEALTH>MUL: 1.5,
	},
	FERTILITY: 0.65,
},
```

All three blocks are required.

## Tags

### ICON

The icon representing the climate in the interface, written as an icon path.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path |
| **Required** | Yes |

```text
ICON: 32->SEASONS->3,
```

### SEASONAL_CHANGE

How strongly the seasons show on the world map. It affects two things there: how much the map's appearance changes with the seasons, and how often farms appear when the world is generated (more seasonal areas get fewer).

It doesn't affect your settlement's temperature through the year, which comes from `TEMP_COLD` and `TEMP_WARM`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
SEASONAL_CHANGE: 1.0,
```

### TEMP_COLD and TEMP_WARM

The settlement's temperature at the coldest and warmest points of the year. `TEMP_COLD` applies in winter and `TEMP_WARM` in summer. Spring and autumn are a blend of the two, three quarters of the way towards `TEMP_WARM`, and the game moves smoothly between seasons. On top of that, each day's temperature varies by chance, and nights are cooler.

On this scale, `0` is a comfortable temperature, negative values are cold and positive values are hot. The further from `0`, the more your subjects suffer from exposure to cold or heat unless they're protected.

Together, these two values also affect how often droughts come: warmer climates have them more often.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | -1 to 1 |
| **Required** | Yes, both |

```text
TEMP_COLD: -0.36,
TEMP_WARM: 0.31,
```

### COLOR

The colour that represents the climate on the world map's climate overlay and in the region interface, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR: 0_100_255,
```

### GROUND

The colours of the ground in a settlement with this climate. The block holds two colours, `DRY` and `WET`, and the game uses them for dry and moist ground when it generates a new settlement map.

| | |
|---|---|
| **Type** | Block of two colours |
| **Required** | Yes, with both `DRY` and `WET` |

```text
GROUND: {
	DRY: 193_181_135,
	WET: 74_55_55,
},
```

### BOOST

Bonuses or penalties that come with the climate, written in the same way as a race's `BOOST` block: each line names a stat, `>MUL` or `>ADD`, and a value.

A climate's boosts apply to a region according to how much of the region has that climate, and to your settlement according to its location.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No. Vanilla's temperate climate has none. |

```text
BOOST: {
	PHYSICS_HEALTH>MUL: 1.5,
},
```

### FERTILITY

The game reads this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | Yes. The tag must be present even though it has no effect. |

```text
FERTILITY: 0.65,
```

### TEMP_SPAN

This tag appears at the end of the vanilla file, outside the climate blocks. The game never reads it, so it has no effect and can be left out.

```text
TEMP_SPAN: 60,
```

## Notes

### Climate keys elsewhere

Other files refer to the climates by their keys, `COLD`, `TEMPERATE` and `HOT`, usually in a block that weights something by climate. For example, [an animal's CLIMATE block](../01-animal.md#climate) sets how common it is in each one.

## Related

- [init/config](00-config.md)
- [init/animal](../01-animal.md)
