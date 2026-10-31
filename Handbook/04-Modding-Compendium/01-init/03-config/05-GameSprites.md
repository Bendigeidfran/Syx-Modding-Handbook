# init/config/GameSprites.txt

`GameSprites.txt` tells the game which images to use for a few special decorations that it assembles itself: severed heads on spikes, and mounds of skulls. These are used by the vanilla Monument of Death room.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/GameSprites.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new entries** | No. The game reads exactly the four entries below and ignores anything else. |
| **Companion files** | Images in `assets/sprite/game/1x1/` |

## File structure

The file has four blocks, each pointing at a row of an image:

```text
HEAD_SPIKE_1X1: {
	FILE: MISC2,
	ROW: 0,
},

SKULL_SMALL_1X1: {
	FILE: DEATH,
	ROW: 3,
},

SKULL_MEDIUM_1X1: {
	FILE: DEATH,
	ROW: 4,
},

SKULL_BIG_1X1: {
	FILE: DEATH,
	ROW: 2,
},
```

All four are required.

## Tags

Each block contains the same two tags.

### FILE

The image to take the sprite from: the name of a file in `assets/sprite/game/1x1/`, without `.png`. `1x1` means the sprites in it are one tile (16 × 16 pixels) in size.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/game/1x1/`) |
| **Required** | Yes |

### ROW

Which row of the image to use, counting from `0` at the top. Each row of a sprite image is a separate sprite, and the images side by side within a row are random variations of it.

If the row doesn't exist in the image, the game shows a warning and the sprite is left blank.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes |

## Notes

### What the entries build

The game uses these images to build sprites of its own, which room files can then use like any other sprite:

| Entry | Used to build |
|---|---|
| `HEAD_SPIKE_1X1` | `SEVERED_HEAD_1X1` |
| `SKULL_SMALL_1X1`, `SKULL_MEDIUM_1X1`, `SKULL_BIG_1X1` | `SKULL_MOUND_1X1`, `SKULL_MOUND_2X2` and `SKULL_MOUND_3X3` |

In vanilla, these are used by `assets/init/room/MONUMENT_DEATH.txt`.

## Related

- [init/config](00-config.md)
