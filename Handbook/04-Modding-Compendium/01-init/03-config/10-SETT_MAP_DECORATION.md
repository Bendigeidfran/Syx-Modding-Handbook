# init/config/SETT_MAP_DECORATION.txt

`SETT_MAP_DECORATION.txt` sets the small decorative details scattered across a settlement map: pebbles and plants on the ground, objects on beaches, and things floating on fresh water. Each entry is a sprite definition listing the images the game can pick from.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/SETT_MAP_DECORATION.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new entries** | No. The game reads exactly the five entries below. |
| **Companion files** | Images in `assets/sprite/game/1x1/` |

## Entries

| Entry | Where it appears |
|---|---|
| `BEACH_1X1` | Placed along ocean shores when a settlement map is generated. |
| `WATER_SWEET_1X1` | Drawn on top of about one in eight tiles of fresh water. |
| `MID_FERTILITY_1X1` | Scattered on moist open ground (about one tile in 50) when a settlement map is generated. |
| `INFERTILE_1X1` | Scattered on dry open ground (about one tile in 200) when a settlement map is generated. |
| `WOOD_1X1` | Placed by woodcutters' work and by the growth of trees. |

All five are required.

## Tags

Each entry is a sprite definition. This is the same format the game uses for sprites in other files, such as rooms, so it supports more tags than the four vanilla uses here. Those four are described below; the full format will be covered in the sprite chapter.

```text
WATER_SWEET_1X1: {
	SHADOW_LENGTH: 1,
	ROTATES: false,
	TINT: true,
	FRAMES: [
		NATURE: 6,
		NATURE: 7,
		NATURE: 8,
		NATURE: 9,
	],
},
```

### FRAMES

The images to choose from. Each entry is the name of an image in `assets/sprite/game/1x1/` (without `.png`), a colon, and the row of that image to use, counting from `0`. An entry of `-` means "nothing".

For each tile, the game picks one entry from the list at random. Listing the same entry several times makes it more likely to be picked; vanilla does this in `MID_FERTILITY_1X1`, where `NATURE: 11` and `NATURE: 12` appear many times.

| | |
|---|---|
| **Type** | List of `IMAGE: ROW` entries |
| **Required** | Yes |

### SHADOW_LENGTH

How long a shadow the decoration casts.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 to 100 |
| **Required** | No |

### ROTATES

Whether the decoration can be drawn rotated to add variety.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `true`. |

### TINT

Whether the game gives each decoration a slightly varied shade. If `false`, decorations are drawn in their original colours.

This has no effect on `WATER_SWEET_1X1`, which is always coloured using the game's tree colours.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `true`. |

## Related

- [init/config](00-config.md)
- [init/config/GameSprites.txt](05-GameSprites.md)
