# text/names/WorldAreas.txt

This file holds the names of regions on the world map. The game looks at what a region's land is mostly made of, and picks from the matching list.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/names/WorldAreas.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### MOUNTAIN, FOREST, RIVER, OCEAN, LAKE, STEPPE, DESERT and MISC

One list of names for each kind of land, all required. A kind counts once its share of the region's tiles passes the figure below, and the one furthest over its figure gives the name. If none passes, the region uses `MISC`.

| List | Share needed |
|---|---|
| `MOUNTAIN` | 20% |
| `FOREST` | 40% |
| `RIVER` | 10% |
| `OCEAN` | 15% |
| `LAKE` | 15% |
| `STEPPE` | 60%, counting dry ground in the top half of the map |
| `DESERT` | 60%, counting dry ground in the bottom half of the map |

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
MOUNTAIN: [
	"Johi",
	"Pirvatz",
],
```

### ISLAND_ADDONS

Wording for regions surrounded by water, as a list. The game picks one at random, and puts the region's name in place of `{0}`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
ISLAND_ADDONS: [
	"Isle of {0}",
	"{0} Island",
],
```

## Related

- [text/names](00-names.md)
- [init/world](../../01-init/15-world/00-world.md)
