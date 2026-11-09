# init/race/sprite

A race's sprite file decides how its members look. It names the images used for their bodies and portraits, sets the colours of their skin, hair, eyes and clothes, chooses what crowns and helmets their leaders wear, and picks the art used for the race's towns, villages and farms on the world map.

The file is large, so it's described over three pages:

- this page covers how the file is organised, the images it uses, how colours are written, and the file-level tags `SLEEP_FILE`, `SPRITE_EXTRA_FILE`, `NAMESET_FILE_NOBLE` and `WORLD`;
- [Colours and extras](01-colours-and-extras.md) covers the headwear drawn on portraits (`CROWN`, `MERC` and `RAIDER`) and the race's colours (`COLOR_CLOTHES`, `COLOR_BLOOD` and `COLORS`);
- [Types and faces](02-types-and-faces.md) covers the body types (`TYPES`), the child type (`CHILD`), and how bodies and portraits are built up from add-ons and face parts.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/race/sprite/` |
| **Files** | One `.txt` file per appearance. Vanilla has one for each race, e.g. `HUMAN.txt`. |
| **Key** | The file name without `.txt`. A race file names its sprite file with [`SPRITE_FILE`](../01-race-file.md#sprite_file). |
| **Adding new files** | Yes. A sprite file is only loaded when a race's `SPRITE_FILE` names it, and several races can share one. |
| **Images** | In `assets/sprite/race/` and `assets/sprite/world/centre/`. See [Images](#images) below. |
| **Text files** | Name lists in `assets/text/names/nameset/`. See [Name-set files](#name-set-files) below. |

## How the file is organised

The file's tags, in the order vanilla files use them:

```text
SLEEP_FILE: Blanket,
SPRITE_EXTRA_FILE: Normal,
NAMESET_FILE_NOBLE: StdLastNoble,

WORLD: { ... },

CROWN: { ... },
MERC: { ... },
RAIDER: [ ... ],
COLOR_CLOTHES: [ ... ],
COLOR_BLOOD: 123_20_17,

COLORS: { ... },
CHILD: { ... },

TYPES: [ ... ],
```

Every one of these tags is required.

The game draws a member of a race in two quite different ways:

- **In the settlement**, subjects are small sprites seen from above, built from a body image, add-ons such as hair and armour, and extras such as tools and blankets.
- **In portraits**, shown when you select a subject and in many menus, a face is built up in layers from separate face parts: skull, ears, eyes, hair and so on.

Both are set per **type** in `TYPES`, and children have a type of their own in `CHILD`. See [Types and faces](02-types-and-faces.md).

## Images

The sprite file refers to images by file name, without `.png`. Each kind of image lives in its own folder and must have a set width. An image of the wrong width, or one that's too short, stops the game from loading with an error naming the image. Images may be taller than the minimum height, and some kinds, such as face parts and headwear, use the extra height for more variants.

| Named by | Folder | Width | Height, at least |
|---|---|---|---|
| `SPRITE_FILE` in a type | `assets/sprite/race/` | 448 | 546 |
| `SPRITE_SKELLETON_FILE` in a type | `assets/sprite/race/skelleton/` | 316 | 120 |
| `FRAMES` in a face part | `assets/sprite/race/face/` | 416 | 60 |
| `INFANT_FILE` in `CHILD` | `assets/sprite/race/infant/` | 352 | 22 |
| `SLEEP_FILE` | `assets/sprite/race/sleep/` | 164 | 44 |
| `SPRITE_EXTRA_FILE` | `assets/sprite/race/extra/` | 428 | 310 |
| `FILE` in `CROWN`, `MERC` and `RAIDER` | `assets/sprite/race/face/addon/` | 104 | 36 |
| `TOWN` in `WORLD` | `assets/sprite/world/centre/town/` | 460 | 62 |
| `VILLAGE` in `WORLD` | `assets/sprite/world/centre/village/` | 460 | 34 |
| `OVERLAY` in `WORLD` | `assets/sprite/world/centre/overlay/` | 236 | 34 |
| `WALL` and `WALL_VILLAGE` in `WORLD` | `assets/sprite/world/centre/wall/` | 600 | 120 |
| `TERRAIN` in `WORLD` | `assets/sprite/world/centre/terrain/` | 152 | 76 |
| `FARM` in `WORLD` | `assets/sprite/world/centre/farm/` | 364 | 50 |

The layout inside each image is fixed by the game, and [sprite/race](../../../03-sprite/07-race/00-race.md) describes the ones in `assets/sprite/race/`. The simplest way to make a new one is to copy a vanilla image of the same kind from `base/data.zip` and paint over it.

## Writing colours

Colours appear throughout the sprite file, and the game accepts them in several forms.

### A single colour

Used by `COLOR_BLOOD` and the `_COLOR` tags in `WORLD` (except `FARM_COLOR`). Write it either as red, green and blue numbers joined by underscores, or as a block:

```text
COLOR_BLOOD: 123_20_17,
```

```text
COLOR_BLOOD: {R: 70, G: 40, B: 40,},
```

The first example is from `HUMAN.txt`, the second from `ARGONOSH.txt`. Vanilla always uses numbers from 0 to 255.

Many colours in the sprite file tint an image. `255_255_255` is plain white, and vanilla uses it for most of the `WORLD` images.

### A list of colours

Used by the `VALUES` of each colour in `COLORS`, and by `FARM_COLOR` in `WORLD`. You can write:

- a list of colours, all written in the same single-colour form (a list mixing the two forms stops the game from loading):

  ```text
  VALUES: [
  	090_090_080,
  	099_099_099,
  	168_168_180,
  	209_159_054,
  ],
  ```

- a single colour, which makes a list of one;
- a block that generates a smooth range of colours, with `GENERATE` colours running evenly from `FROM` to `TO`. From `GARTHIMI.txt`:

  ```text
  VALUES:{
  	GENERATE: 16,
  	FROM: 100_100_75,
  	TO: 95_115_100,
  },
  ```

`COLOR_CLOTHES` is a list too, but stricter: every entry must be a block (`{R: …, G: …, B: …,}`). See [COLOR_CLOTHES](01-colours-and-extras.md#color_clothes).

## Tags

The examples below come from the vanilla `HUMAN.txt`.

### SLEEP_FILE

The image drawn over members of the race while they lie asleep. Vanilla races all use `Blanket`.

| | |
|---|---|
| **Type** | File name, from `assets/sprite/race/sleep/` |
| **Required** | Yes |

```text
SLEEP_FILE: Blanket,
```

### SPRITE_EXTRA_FILE

The image holding the extras drawn with a subject's body in the settlement, such as the tools they hold while working.

It holds:

- the tools they hold while working;
- the trolley they push when carrying more than 4 units of a resource;
- the water drawn over a subject, or a body, that is in water.

Vanilla races all use `Normal`.

| | |
|---|---|
| **Type** | File name, from `assets/sprite/race/extra/` |
| **Required** | Yes |

```text
SPRITE_EXTRA_FILE: Normal,
```

### NAMESET_FILE_NOBLE

A [name-set file](#name-set-files) of surnames, used when the game names this race's camps on the world map. A camp's name is taken from the camp's own list of names, with a random surname from this file put in place of `{0}`. See [init/race/worldcamp](../08-worldcamp.md#the-text-file).

Despite the tag's name, these surnames aren't given to nobles in your settlement. Subjects' names, nobles included, come from their type's `NAMESET_FILE_FIRST` and `NAMESET_FILE_SURNAME` (see [Types and faces](02-types-and-faces.md#nameset_file_first-and-nameset_file_surname)).

| | |
|---|---|
| **Type** | File name, from `assets/text/names/nameset/` |
| **Required** | Yes |

```text
NAMESET_FILE_NOBLE: StdLastNoble,
```

### WORLD

The art used for the race's settlements on the world map. Every tag in the block is required.

Each tag names an image, and each has a matching `_COLOR` tag that tints it:

| Tag | What it draws |
|---|---|
| `TOWN` | The houses at the centre of a region. |
| `VILLAGE` | The small villages scattered across a region's land. |
| `OVERLAY` | A layer drawn over the houses at a region's centre. |
| `WALL` | The walls round the centre of a faction's capital. |
| `WALL_VILLAGE` | The walls round the centre of any other region. |
| `TERRAIN` | The ground beneath a region's centre. |
| `FARM` | The fields round a region's centre and beside villages. |

| Tag | Meaning | Type | Required |
|---|---|---|---|
| `TOWN_COLOR`, `VILLAGE_COLOR`, `OVERLAY_COLOR`, `WALL_COLOR`, `WALL_VILLAGE_COLOR`, `TERRAIN_COLOR` | The tint for the image named by the tag without `_COLOR`. | A [single colour](#a-single-colour) | Yes |
| `FARM_COLOR` | The tints for `FARM`. Each field picks one from the list. | A [list of colours](#a-list-of-colours) | Yes |

```text
WORLD: {
	TOWN: Human,
	TOWN_COLOR: 255_255_255,
	VILLAGE: Human,
	VILLAGE_COLOR: 255_255_255,
	OVERLAY: Human,
	OVERLAY_COLOR: 255_255_255,
	WALL: Human,
	WALL_COLOR: 255_255_255,
	WALL_VILLAGE: Human_Village,
	WALL_VILLAGE_COLOR: 255_255_255,
	TERRAIN: Human,
	TERRAIN_COLOR: 140_110_100,
	FARM: Farm,
	FARM_COLOR: [
		194_218_194,
		180_180_180,
		...
		208_232_208,
	],
},
```

Which race's art a region shows depends on who lives there. A region's centre uses the art of the race with the largest population in it. Its villages are shared out between its races in proportion to their numbers, so a mixed region shows a mix of village styles. The fields beside villages are an exception: each uses the `FARM` art of a playable race chosen at random.

Only playable races live in world regions, so a non-playable race's `WORLD` art never appears. The block is still required.

## Name-set files

A name-set file in `assets/text/names/nameset/` is a list of names. Sprite files use them for first names, surnames and the noble surnames used by camps.

| Tag | Meaning | Required |
|---|---|---|
| `NAMES` | The names, as a list of text. At least one. | Yes |

From `StdLastNoble.txt` (shortened):

```text
NAMES: [
	"of Pheelonia",
	"Nicklowden",
	"Kellarere",
	...
],
```

Like most data files, a name-set file in your mod is [laid over the vanilla one](../../../../02-Getting-Started.md#changing-a-vanilla-file). Because `NAMES` is a list, your list replaces vanilla's whole unless your file uses `_JSON_ADD` and `_ARRAY_ADD`.

## Notes

### Changing a vanilla sprite file

A sprite file in your mod with the same name as a vanilla one is [laid over it](../../../../02-Getting-Started.md#changing-a-vanilla-file). Most of the file is made of blocks and lists (`WORLD`, `COLORS`, `TYPES` and so on). Each one in your file replaces vanilla's whole, unless your file uses `_JSON_ADD`. For a new race, it's usually simpler to make a new sprite file with its own name.

## Sections

- [Colours and extras](01-colours-and-extras.md)
- [Types and faces](02-types-and-faces.md)

## Related

- [init/race](../00-race.md)
- [The race file](../01-race-file.md)
- [sprite/race](../../../03-sprite/07-race/00-race.md)
