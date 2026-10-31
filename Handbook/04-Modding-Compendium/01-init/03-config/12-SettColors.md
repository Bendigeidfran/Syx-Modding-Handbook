# init/config/SettColors.txt

`SettColors.txt` sets several colours used on the settlement map: the colours shown on the minimap, the colour of water through the year, and the colours of rocky and sandy ground.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/SettColors.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | None |

## Colour format

Colours in this file are written as blocks with `R`, `G` and `B` values, each from 0 to 255:

```text
TREE: {R:58, G:104, B:26,},
```

## Tags

### MINIMAP

The colours used for features on the minimap. The block must contain all six of these colours:

| Tag | Used for |
|---|---|
| `TREE` | Trees |
| `WATER` | Water |
| `WATER_DEEP` | Deep water |
| `ROCK` | Rocks |
| `GROWABLE` | Wild crops and other things that can be harvested |
| `MOUNTAIN` | Mountains, and (slightly lighter) caves |

| | |
|---|---|
| **Type** | Block of colours |
| **Required** | Yes |

```text
MINIMAP: {
	TREE: {R:58, G:104, B:26,},
	WATER: {R:60, G:80, B:100,},
	WATER_DEEP: {R:45, G:65, B:82,},
	ROCK: {R:63, G:53, B:53,},
	GROWABLE: {R:255, G:216, B:10,},
	MOUNTAIN: {R:63, G:56, B:42,},
},
```

### WATER

The colour of water on the settlement map. `NORMAL` is used during the growing season and `WINTER` outside it, with the game blending between the two. Shallow water by the shore uses the colour as given; open and deep water use progressively darker versions of it.

| | |
|---|---|
| **Type** | Block of two colours, `NORMAL` and `WINTER` |
| **Required** | Yes, with both colours |

```text
WATER: {
	NORMAL: {R:60, G:150, B:200,},
	WINTER: {R:60, G:140, B:160,},
},
```

### GROUND_SAND and GROUND_ROCK

The colours of sandy and rocky ground. Each block holds a `DRY` and a `WET` colour, used for dry and moist ground.

Other kinds of ground take their colours from the climate instead; see [GROUND in CLIMATE.txt](02-CLIMATE.md#ground).

| | |
|---|---|
| **Type** | Block of two colours, `DRY` and `WET` |
| **Required** | Yes, both blocks |

```text
GROUND_SAND: {
	DRY: {R:208, G:194, B:142,},
	WET: {R:150, G:126, B:102,},
},
```

## Notes

### Tags that have no effect

The vanilla file also contains `GROUND_WOODS` and `GROUND_PASTURE` blocks. The game never reads them, so changing them has no effect, and they can be left out.

## Related

- [init/config](00-config.md)
- [init/config/CLIMATE.txt](02-CLIMATE.md)
