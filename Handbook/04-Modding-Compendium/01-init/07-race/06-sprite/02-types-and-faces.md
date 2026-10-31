# Types and faces

This page covers the end of a [sprite file](00-sprite.md): the race's body types (`TYPES`) and its child type (`CHILD`). Together they decide what each member of the race looks like, both as a sprite in the settlement and in their portrait, and which names they're given. Both tags are required.

The examples below come from the vanilla `HUMAN.txt` unless stated otherwise.

## TYPES

A list of the race's **types**. In vanilla, `HUMAN.txt`, `CRETONIAN.txt` and `Q_AMEVIA.txt` have two types each, and the other five sprite files have one. Humans use theirs for men and women.

| | |
|---|---|
| **Type** | List of type blocks |
| **Range** | 1 to 3 types |
| **Required** | Yes |

Each new member of the race is given one of the types when they're created, chosen at random in proportion to each type's [`OCCURRENCE`](#occurrence), and keeps it for life. The type sets their body, portrait, colours and names. Children are given their type at birth too: it chooses their names straight away, but they only look like it once they've grown up. Until then, they use the [`CHILD`](#child) block.

```text
TYPES: [

	** M A L E S
	
	{
		OCCURRENCE: 0.3,
		COLOR_SKIN: SKIN,
		COLOR_LEG: LEG,
		
		SPRITE_FILE: Human,
		SPRITE_SKELLETON_FILE: Humanoid,
		NAMESET_FILE_FIRST: StdFirst,
		NAMESET_FILE_SURNAME: StdLast,
		PORTRAIT_FILE: Human,
	
		ADDONS: [ ... ],
		
		FACE: [ ... ],
	},
	
	** F E M A L E S

	{
		...
	},
],
```

## Type tags

Each type is a block with the tags below.

### OCCURRENCE

How common the type is, compared with the race's other types. Humans have `0.3` for both their types, so each is equally likely.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No. The default is `0.5`. |

```text
OCCURRENCE: 0.3,
```

### COLOR_SKIN and COLOR_LEG

The [colour collections](01-colours-and-extras.md#colors) used for the skin and the legs of the type's body in the settlement. Each names a collection in the file's `COLORS` block.

| | |
|---|---|
| **Type** | Colour collection names |
| **Required** | Yes, both |

```text
COLOR_SKIN: SKIN,
COLOR_LEG: LEG,
```

These only colour the body. Portraits are coloured part by part, by each face part's own [`COLOR`](#color).

### SPRITE_FILE

The image of the type's body in the settlement, from `assets/sprite/race/`. The same image also holds the type's [add-ons](#addons). Several types, and several races, can share one image.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
SPRITE_FILE: Human,
```

### SPRITE_SKELLETON_FILE

The image used for the skeletons of the race's dead, from `assets/sprite/race/skelleton/`. Note the game's spelling.

In v0.71.44, this tag doesn't work as you'd expect; see [Skeletons](#skeletons) below.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
SPRITE_SKELLETON_FILE: Humanoid,
```

### NAMESET_FILE_FIRST and NAMESET_FILE_SURNAME

The [name-set files](00-sprite.md#name-set-files) that members of this type take their first names and surnames from. Humans have different first names for their two types but share the surnames.

| | |
|---|---|
| **Type** | File names, from `assets/text/names/nameset/` |
| **Required** | Yes, both |

```text
NAMESET_FILE_FIRST: StdFirst,
NAMESET_FILE_SURNAME: StdLast,
```

### PORTRAIT_FILE

Every vanilla type has a `PORTRAIT_FILE`.

> **TODO:** What this tag does hasn't been confirmed yet. Portraits are built from the type's [`FACE`](#face) parts.

```text
PORTRAIT_FILE: Human,
```

### ADDONS

Extra pieces drawn on the type's body in the settlement. Vanilla uses them for things such as armour, which is only drawn on subjects wearing it. Each add-on can have conditions, so it's only drawn on some subjects.

| | |
|---|---|
| **Type** | List of add-on blocks |
| **Required** | No |

Each add-on has these tags:

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `ADDON_INDEX` | Which add-on to draw. The type's `SPRITE_FILE` image has 8 add-on rows, numbered 0 to 7. | Integer, 0 to 7. 8 or more crashes the game. | Yes |
| `BELOW_HEAD` | Whether the add-on is drawn before the head (`true`), so the head covers it, or after it (`false`). | True/false | Yes |
| `COLOR` | The [colour collection](01-colours-and-extras.md#colors) that tints the add-on. Without it, the add-on is drawn untinted. | Colour collection name | No |
| `CONDITIONS` | When the add-on is drawn, in the [condition format](#conditions) described below. Without it, the add-on is always drawn. | Block of conditions | No |

Two Human add-ons. The first is coloured from the `HAIR` collection and drawn on about three quarters of subjects; the second is drawn on anyone wearing plate armour:

```text
{
	BELOW_HEAD: false,
	ADDON_INDEX: 3,
	CONDITIONS: {
		GREATER: {
			RANDOM_2_F: 0.25,
		},
	},
	COLOR: HAIR,
},
{
	BELOW_HEAD: false,
	ADDON_INDEX: 0,
	CONDITIONS: {
		GREATER: {
			EQUIP_BATTLE_ARMOUR_PLATE_I: 0,
		},
	},
	COLOR: ARMOUR,
},
```

### FACE

The parts the type's portrait is built from, in drawing order: the first part is drawn at the back, and each later part goes on top. A Human portrait is built up from the chest, ears, skull, mouth, nose, eyes, eyebrows and hair, along with parts that only some subjects have: wrinkles, beards, a slave collar, a noble's cloak.

| | |
|---|---|
| **Type** | List of face-part blocks |
| **Required** | No. Without it, the portrait is blank. |

The tags of a face part are described in [Face parts](#face-parts) below. Two Human parts, the chest, and the eyes of living subjects:

```text
**Chest
{
	FRAMES: [
		Chest: 0,
		Chest: 1,
		Chest: 2,
		Chest: 3,
	],
	COLOR: SKIN,
	STAINS: false,
	OFF_Y: 2,
},
```

```text
**Eyes_A
{
	CONDITIONS: {
		EQUAL: {
			APPEARANCE_DEAD_I: 0,
		},
	},
	FRAMES: [
		Eyes: 4,
		Eyes: 5,
		Eyes: 6,
		Eyes: 7,
	],
	OFF_Y: -1,
	FRAME_RANDOM: 8,
	STAINS: false,
},
```

### OCCURRENCE_EXTRA1, OCCURRENCE_EXTRA2, COLOR_EXTRA1, COLOR_EXTRA2 and SET_APPEARANCE_STATS

The female type in `HUMAN.txt` has these five tags:

```text
OCCURRENCE_EXTRA1: 0,
OCCURRENCE_EXTRA2: 0.95,
COLOR_EXTRA1: HAIR,
COLOR_EXTRA2: HAIR,
```

```text
SET_APPEARANCE_STATS: {
	**hair
	EXTRA1: 0.95,
	EXTRA2: 0.5,
	EXTRA4: 0.5,
},
```

> **TODO:** What these tags do hasn't been confirmed yet.

## Face parts

Each entry in a `FACE` list is one part of the portrait. If a face part contains a tag that isn't one of these, the game shows a warning listing the valid ones.

Portraits are 40 pixels wide and 64 high. Face parts are drawn in a 40 × 48 area, 8 pixels from the top.

### FRAMES

The images the part can show. Each subject is shown one of them, chosen at random, and always sees the same one.

Each entry is a face image and a frame number, joined by a colon. The images are in `assets/sprite/race/face/`. Each row of an image is 60 pixels high and holds 4 frames, numbered from 0, left to right along each row and then row by row. Vanilla's `Hair.png` is 960 pixels high, so it has 16 rows and 64 frames, numbered 0 to 63.

| | |
|---|---|
| **Type** | List of `File: number` entries |
| **Required** | Yes |

```text
FRAMES: [
	Ears: 0,
	Ears: 1,
	Ears: 2,
	Ears: 3,
],
```

An entry naming an image that doesn't exist, or a frame number past the end of the image, gives a warning and is drawn blank. An entry that can't be read as `File: number` gives a warning and is left out.

### COLOR

The [colour collection](01-colours-and-extras.md#colors) that tints the part. Without it, the part uses plain white. Either way, the game brightens the colour by 20% before drawing the part.

| | |
|---|---|
| **Type** | Colour collection name |
| **Required** | No |

### CONDITIONS

When the part is drawn, in the [condition format](#conditions) described below. Without it, the part is always drawn.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No |

A Human man's beard is only drawn past a certain age, and only on some men:

```text
CONDITIONS: {
	GREATER: {
		POPULATION_AGE_F: 0.25,
		RANDOM_2_F: 0.1,
	},
},
```

### OFF_X and OFF_Y

Move the part right (positive) or left (negative), and down (positive) or up (negative), in portrait pixels.

| | |
|---|---|
| **Type** | Integers |
| **Range** | `OFF_X` -40 or more, `OFF_Y` -48 or more. The code names maximums of 40 and 48, but doesn't enforce them. |
| **Required** | No. The default for both is `0`. |

```text
OFF_Y: 2,
OFF_X:12,
```

### OFF_X_RANDOM and OFF_Y_RANDOM

Add a random extra shift to the right and downwards, different for each subject, of up to the number given.

| | |
|---|---|
| **Type** | Integers |
| **Range** | 0 or more. The code names maximums of 40 and 48, but doesn't enforce them. |
| **Required** | No. The default for both is `0`. |

In v0.71.44, `OFF_X_RANDOM` doesn't work as intended: the shift can be up to about 17 times the number given, which can move the part right out of the portrait. Vanilla doesn't use either tag.

### FRAME_RANDOM

Links the random choices of parts that should match. Parts with the same `FRAME_RANDOM` number share the same random roll, so they choose matching frames (when they have the same number of frames) and the same random shifts.

Vanilla Humans give the open eyes of the living and the closed eyes of the dead the same number, `8`, so a subject's eyes keep their shape when they die.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The code names a maximum of 16, but doesn't enforce it. |
| **Required** | No. Without it, each part uses its own position in the `FACE` list. |

```text
FRAME_RANDOM: 8,
```

### FRAME_OCCURRENCE

The chance, from 0 to 1, that the part is shown at all, worked out separately for each subject in steps of one sixteenth.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. The default is `1`, always shown. |

In v0.71.44, the game checks face parts against a list of valid tags that spells this one `FRAME_OCCURENCE`. `FRAME_OCCURRENCE` works, but the game shows a warning that it isn't valid. Vanilla doesn't use it; it uses `RANDOM_` values in `CONDITIONS` instead.

### OPACITY

How opaque the part is, from `0` (invisible) to `255` (solid).

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. Anything above 255 counts as 255. |
| **Required** | No. The default is `255`. |

### STAINS

Whether dirt and blood are drawn over the part when the subject is grimy or injured. Blood is drawn in the race's [`COLOR_BLOOD`](01-colours-and-extras.md#color_blood).

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. The default is `true`. |

```text
STAINS: false,
```

## Conditions

Add-ons and face parts use the same condition format as events: comparisons such as `GREATER` and `EQUAL`, each listing values and numbers. See [Conditions](../../05-event/02-occurrence.md#conditions) for the format. As there, a value name the game doesn't recognise gives a warning that lists every value available.

The values checked are the subject's own. Vanilla uses, among others:

| Value | Used for |
|---|---|
| `RANDOM_0_F` to `RANDOM_7_F` | Eight random numbers from 0 to 1, fixed for each subject when they're created. `GREATER: { RANDOM_2_F: 0.25, }` picks about three quarters of subjects. |
| `POPULATION_AGE_F` | The subject's age. |
| `APPEARANCE_DEAD_I` | Whether the subject is dead (`1`) or alive (`0`). |
| `CLASS_NOBLE` | Whether the subject is a noble. |
| `TYPE_SLAVE` | Whether the subject is a slave. |
| `EQUIP_BATTLE_ARMOUR_PLATE_I` | How much plate armour the subject wears. |

## CHILD

A single type for the race's children. While a subject is a child, including a child slave, their body in the settlement and their portrait come from this block. It has the same tags as the blocks in `TYPES`, plus `INFANT_FILE`, but some of them don't work the same way:

- `OCCURRENCE` has no effect, since there's only one child type.
- `NAMESET_FILE_FIRST` and `NAMESET_FILE_SURNAME` are required and must name existing files, but children's names come from the type in `TYPES` they'll grow up into.
- In v0.71.44, `ADDONS` here are loaded but never drawn. Children are drawn with the add-ons of the type they'll grow up into, so that type's conditions decide which of its add-ons a child shows.
- `COLOR_SKIN` and `COLOR_LEG` colour free children's bodies. A child slave's body takes its skin and leg colours from their type in `TYPES` instead.

Vanilla's Human children (shortened):

```text
CHILD: {

	INFANT_FILE: Human,

	COLOR_SKIN: SKIN,
	COLOR_LEG: LEG,
	
	SPRITE_FILE: ChildHumanoid,
	SPRITE_SKELLETON_FILE: Humanoid_small,
	NAMESET_FILE_FIRST: StdFirst,
	NAMESET_FILE_SURNAME: StdLast,
	
	ADDONS: [
		{
			BELOW_HEAD: false,
			ADDON_INDEX: 3,
			COLOR: HAIR,
		},
	],
	FACE: [
		**baby
		{
			CONDITIONS: {
				
			},
			FRAMES: [
				Baby: 1,
			],
			OFF_Y: 0,
			OFF_X: 0,
			STAINS: true,
		},
		...
	],
},
```

The simplest child, from `ARGONOSH.txt`, has no add-ons, face parts or infant:

```text
CHILD: {
	COLOR_SKIN: SKIN,
	COLOR_LEG: LEG,
	
	SPRITE_FILE: Argonosh,
	SPRITE_SKELLETON_FILE: Argonosh,
	NAMESET_FILE_FIRST: LzmFirst,
	NAMESET_FILE_SURNAME: LzmLast,
},
```

### INFANT_FILE

The image of a baby, drawn with a subject who is carrying one (see the race's [`BABY_DAYS`](../01-race-file.md#properties)), from `assets/sprite/race/infant/`. Without it, no baby is drawn. Four vanilla sprite files have one: `HUMAN.txt`, `CRETONIAN.txt`, `TILAPI.txt` and `Q_AMEVIA.txt`.

| | |
|---|---|
| **Type** | File name |
| **Required** | No |

```text
INFANT_FILE: Human,
```

## Notes

### Skeletons

In v0.71.44, skeletons are drawn from the wrong blocks:

- adults' skeletons use the `SPRITE_SKELLETON_FILE` of the **`CHILD`** block;
- children's skeletons use the `SPRITE_SKELLETON_FILE` of the **first** type in `TYPES`.

The skeleton files of the other types aren't used. In vanilla, this means Human adults decay to the small `Humanoid_small` skeleton. To give adults a full-sized skeleton in your own race, you would need to name it in `CHILD`.

### How random choices are shared

Several of a subject's random choices are drawn from the same random number, so they can be linked in ways that aren't obvious:

- `FRAME_RANDOM` numbers that differ by 8 behave as the same number. Without `FRAME_RANDOM`, this means the 1st and 9th face parts share their random choices, as do the 2nd and 10th, and so on.
- `FRAME_RANDOM` numbers 4, 5, 6 and 7 (and so 12 to 15) use the same random rolls as `RANDOM_0_F`, `RANDOM_2_F`, `RANDOM_4_F` and `RANDOM_6_F`.
- `RANDOM_0_F` to `RANDOM_3_F` come from the same part of the random number as the picks of the first eight [colour collections](01-colours-and-extras.md#colors), two collections to each. A condition on `RANDOM_0_F`, for example, partly depends on which colours the 1st and 2nd collections picked.

If two things on your race seem to go together more often than they should, this is the likely cause.

## Related

- [init/race/sprite](00-sprite.md)
- [Colours and extras](01-colours-and-extras.md)
- [Occurrence and conditions](../../05-event/02-occurrence.md)
- [The race file](../01-race-file.md)
