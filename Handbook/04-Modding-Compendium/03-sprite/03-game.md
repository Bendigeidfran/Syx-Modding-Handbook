# sprite/game

The `sprite/game` folder holds the sprite sheets for objects drawn on the settlement map: furniture in homes and rooms, decorations, monuments, fences and the like. The images are sliced into tile-sized sprites, and data files in `init` choose sprites from them with a small block called a **sprite entry**.

This page covers both halves: how the images are laid out, and how a sprite entry is written. Race homes ([init/race/home](../01-init/07-race/04-home.md)) and rooms use sprite entries.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/game/`, in six sub-folders, one for each kind of sheet |
| **Files** | `.png` images. Each image holds several sprites, one per row. |
| **Name** | The file name without `.png`, e.g. `2xBED`. Sprite entries refer to images by this name. |
| **Adding new files** | Yes. New images can be added to any of the sub-folders. |
| **Used by** | Sprite entries in `init` files, such as [init/race/home](../01-init/07-race/04-home.md). |

## The kinds of sheet

The game reads each sheet according to its kind, and each kind has its own sub-folder. The thing that uses a sprite entry decides the kind. A sprite entry only looks for images in the folder of its kind: a 1×1 piece of furniture can't use an image from `2x2`.

| Folder | What its sprites are | Cell size, in pixels |
|---|---|---|
| `1x1` | Single tiles. | 22 × 22 |
| `2x2` | Objects 2 tiles square. | 44 × 44 |
| `3x3` | Objects 3 tiles square. | 60 × 60 |
| `combo` | Objects that join up with their neighbours, such as tables and carpets. Each cell holds the pieces used to join up with neighbouring tiles. | 72 × 72 |
| `box` | Areas that join up into boxes with edges and corners. | 76 × 76 |
| `texture` | Surface textures. These use a different layout; see below. | |

A tile on the settlement map is 16 pixels square. Each cell is larger than the sprite it holds, because every sprite sits inside a frame. Vanilla images draw that frame in solid colours, so the sprites are easy to tell apart.

## How an image is laid out

Every image is made of two halves side by side:

- the **left half** holds the sprites in colour;
- the **right half** holds a matching normal map for each sprite, which the game uses to light it.

Each half is a grid of cells of the size in the table above:

- each **row** is a different sprite, numbered from 0 at the top;
- each **column** in a row is a **variation** of that sprite. Every row in an image has the same number of variations.

The game works out the number of rows and variations from the image's size. Half the image's width must be an exact multiple of the cell width, and its height an exact multiple of the cell height. If not, the game stops loading with an error naming the image.

The vanilla `1x1/2xBED.png`, for example, is 352 pixels wide: each half is 176 pixels, or 8 cells of 22, so every row has 8 variations.

You only draw each sprite facing one way. The game makes the rotated versions itself.

### Taller 1×1 sprites

A `1x1` image can hold sprites more than one tile tall, such as beds. The game decides the height from the image's height: it uses the smallest number of tiles *N*, from 1 to 8, for which the image's height is an exact multiple of 16 × *N* + 6 pixels. Each band of that height is then split into *N* rows of one tile each, numbered from the top.

`2xBED.png`, for example, is 494 pixels tall: 13 bands of 38 pixels (16 × 2 + 6), giving 26 rows. Row 0 is the top half of the first bed and row 1 its bottom half, row 2 the top half of the second bed, and so on.

Because the smallest *N* that fits is used, an image whose height also happens to be a multiple of 22 is read as single tiles. If a tall image is read wrongly, add or remove a band.

### Shadow variations

In `1x1`, `2x2`, `3x3` and `combo` images, when a row has an odd number of variations, more than one, the **last variation is a shadow**. It isn't drawn as a variation. Instead, it's the shape the game uses to cast the object's shadow, so a sprite can cast a shadow that differs from its outline. With an even number of variations, or just one, every variation is drawn, and the shadow is cast from the sprite itself.

Either way, a shadow is only cast if the sprite entry gives it a [`SHADOW_LENGTH`](#shadow_length) or [`SHADOW_HEIGHT`](#shadow_height) above 0.

### Textures

Sheets in `texture` are laid out differently. Half the image's width must be 16 × *n* + 12 pixels, and the height a multiple of 28, with one sprite per 28-pixel row. Copy a vanilla texture to see the layout.

### Making an image

The arrangement inside each cell is fixed by the game, and it differs between kinds: `combo` and `box` cells hold many joining pieces. The simplest way to make a new image is to copy a vanilla one of the same kind from `base/data.zip`, paint over it, and give it a new name.

New images go in the same sub-folder in your mod, for example `V71/assets/sprite/game/1x1/MY_BEDS.png`. An image in your mod with the same name as a vanilla one is used instead of the vanilla one.

Files whose names start with `_` are used by the game itself. `_OVERLAY.png` in `1x1`, `2x2` and `3x3` holds the outlines shown while you place furniture.

## Sprite entries

A sprite entry is a block that chooses sprites from an image and sets how they're drawn. From the vanilla `init/race/home/HUMAN.txt`:

```text
{
	RESOURCES: {
		WOOD: 3,
	},
	FPS: 0,
	SHADOW_LENGTH: 2,
	SHADOW_HEIGHT: 0,
	FRAMES : [
		2xBED: 2,
	],
},
```

Only the tags below are allowed in a sprite entry. Any other tag stops the game from loading with an error that lists the allowed ones. `RESOURCES` is allowed too, but only some files use it; see [init/race/home](../01-init/07-race/04-home.md).

### FRAMES

The sprites to draw, as a list. Each entry is written as `FILE: ROW`: the name of an image in the folder for this kind of sheet, and a row number in it.

When there's more than one entry, each object picks one of them at random and keeps it. An entry of `-` on its own draws nothing, so it can be used to leave some objects empty.

| | |
|---|---|
| **Type** | List of `FILE: ROW` entries, or `-` |
| **Required** | Yes |

```text
FRAMES : [
	2xBED: 2,
],
```

If an image doesn't exist, the game shows a warning that lists the images available and skips the entry. A row number past the end of the image also produces a warning, and the entry is skipped. An entry that isn't in the `FILE: ROW` form stops the game from loading with an error.

### FPS

How fast the sprite animates, in variations per second. An animated sprite steps through the variations in its row.

At `0`, the sprite doesn't animate: each object shows one variation of its row, chosen at random.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | No. Default `0`. |

```text
FPS: 0,
```

### FPS_INTERVAL

Makes an animation pause. The animation plays for this fraction of every 64 steps, then holds still for the rest. At `1`, the animation never pauses. Each object's cycle starts at a random point, so nearby objects don't pause together.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `1`. |

From the vanilla `init/room/BREEDER_GARTHIMI.txt`:

```text
FPS_INTERVAL: 0.5,
```

### CIRCULAR

If `true`, an animation runs back and forth through its variations instead of jumping from the last one back to the first.

| | |
|---|---|
| **Type** | `true` or `false` |
| **Required** | No. Default `false`. |

```text
CIRCULAR: true,
```

### SHADOW_LENGTH

How long a shadow the object casts. At `0`, together with a `SHADOW_HEIGHT` of `0`, it casts no shadow.

| | |
|---|---|
| **Type** | Decimal, used as a whole number |
| **Range** | 0 to 100 |
| **Required** | No. Default `0`. |

```text
SHADOW_LENGTH: 2,
```

### SHADOW_HEIGHT

How high above the ground the object's shadow is cast from, for things that hang or float.

| | |
|---|---|
| **Type** | Decimal, used as a whole number |
| **Range** | 0 to 100 |
| **Required** | No. Default `0`. |

```text
SHADOW_HEIGHT: 0,
```

### ROTATES

Whether the sprite turns to face the way the object was placed. If `false`, the sprite is drawn turned a random way instead.

| | |
|---|---|
| **Type** | `true` or `false` |
| **Required** | No. Default `true`. |

```text
ROTATES: true,
```

Not every object uses it. Single-tile furniture in homes always faces the way it was placed, and `combo` sheets don't rotate at all.

### COLOR

A colour, or several, to tint the sprite with. With several, each object picks one at random. It takes the same forms as the [lists of colours](../01-init/07-race/06-sprite/00-sprite.md#a-list-of-colours) in race sprite files: a single colour, a list, or a `GENERATE` block.

| | |
|---|---|
| **Type** | Colour, or list of colours |
| **Required** | No. See `TINT`. |

From the vanilla `init/race/home/HUMAN.txt`:

```text
COLOR: {R: 10, G: 150, B: 10,},
```

### TINT

What to do when there's no `COLOR`. If `true`, each object is darkened slightly by a random amount, so that rows of the same object don't look identical. If `false`, the sprite is drawn in its own colours.

| | |
|---|---|
| **Type** | `true` or `false` |
| **Required** | No. Default `true`. |

```text
TINT: false,
```

### OVERWRITE

Changes the settings for some of the `FRAMES` entries. It's a list of blocks: the first block applies to the first entry in `FRAMES`, the second to the second, and so on. A block can hold any of the tags above except `FRAMES`, and the tags it leaves out keep the entry's own values. Entries with no block, or an empty one, use the entry's settings.

There's one exception: colours are not kept. A block without `COLOR` goes back to the random tint, unless it has `TINT: false`, in which case it keeps the entry's colours. An empty block `{}` therefore drops any `COLOR` the entry has.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | No |

From the vanilla `init/race/home/AMEVIA.txt`, where the second of two frames gets three colours to choose from:

```text
OVERWRITE: [
	{},
	{COLOR: [127_80_80,80_127_80,80_80_127,],},
],
```

## Notes

### The developer's note

The vanilla `sprite/game` folder includes a short `_Note.txt` from the developer. It's a good introduction, but parts of it no longer match the game:

- It describes a `SHADOW_SPRITE` tag. The game no longer accepts it, and a sprite entry containing it stops the game from loading. Shadow variations are now chosen automatically, as described in [Shadow variations](#shadow-variations).
- It says that several `FRAMES` make an animation. In the current game, each object picks one of the `FRAMES` entries, and animations run through the variations in a row.
- It says that a `1x1`, `2x2` or `3x3` sprite whose file is missing is looked for in `combo`. The game only looks in the folder for the sprite's own kind, and a missing file produces a warning.

## Related

- [sprite](00-sprite.md)
- [init/race/home](../01-init/07-race/04-home.md)
