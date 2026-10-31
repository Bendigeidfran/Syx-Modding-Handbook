# Colours and extras

This page covers the middle of a [sprite file](00-sprite.md): the headwear drawn on certain portraits (`CROWN`, `MERC` and `RAIDER`), and the race's colours (`COLOR_CLOTHES`, `COLOR_BLOOD` and `COLORS`). All six tags are required.

The examples below come from the vanilla `HUMAN.txt` unless stated otherwise.

## Headwear

`CROWN`, `MERC` and `RAIDER` add a piece of headwear to the portraits of three kinds of leader. It's drawn over the finished portrait, and only for these leaders, so it doesn't change how ordinary subjects look.

| Tag | Drawn on the portrait of | Which variant |
|---|---|---|
| `CROWN` | The reigning ruler of a faction, when the ruler is of this race. It appears in the faction and royalty screens, diplomacy messages and events. Heirs are marked with a star instead. | Always the first. |
| `MERC` | The leader of a mercenary company of this race. | One at random for each leader. |
| `RAIDER` | The leader of a band of raiders of this race. | One at random for each leader. |

Each tag holds either one entry (a block) or several (a list of blocks). Vanilla uses a block for `CROWN` and `MERC`, and a list for `RAIDER`. Each entry has the same three tags:

| Tag | Meaning | Type and range |
|---|---|---|
| `FILE` | The image, from `assets/sprite/race/face/addon/`. | File name |
| `OFFX` | Moves the image left (negative) or right (positive) on the portrait. | Integer, -48 or more. The code names a maximum of 48, but doesn't enforce it. |
| `OFFY` | Moves the image up (negative) or down (positive) on the portrait. | Integer, -48 or more. The code names a maximum of 48, but doesn't enforce it. |

All three are required in each entry. The offsets scale with the portrait, so they work at every size the portrait is drawn.

An image can hold several **variants**, one above another, each 36 pixels high. Vanilla's `Helm.png` is 288 pixels high, so it holds 8 helmets. A tag's variants are all the variants of all its entries, in order. A mercenary or raider leader is given one of them at random. A ruler always wears the first variant of the first `CROWN` entry, so any others are never seen.

If `FILE` names an image that doesn't exist, the game logs an error and leaves that entry out.

### CROWN

```text
CROWN: {
	FILE: CrownHuman,
	OFFX: 0,
	OFFY: -7,
},
```

### MERC

```text
MERC: {
	FILE: Helm,
	OFFX: 0,
	OFFY: 0,
},
```

### RAIDER

Shortened:

```text
RAIDER: [
	{
		FILE: RaidHat_H,
		OFFX: 0,
		OFFY: -6,
	},
	{
		FILE: RaidHat_L,
		OFFX: 0,
		OFFY: 0,
	},
	...
	{
		FILE: Helm,
		OFFX: 0,
		OFFY: 0,
	},
],
```

## Colours

### COLOR_CLOTHES

The colours of the clothes worn by ordinary members of the race in the settlement. Each subject is given one of the colours at random, and keeps it.

| | |
|---|---|
| **Type** | List of colour blocks |
| **Range** | 1 to 15 entries. Only the first 8 are ever used. |
| **Required** | Yes |

Each entry must be written as a block (`{R: …, G: …, B: …,}`); the `R_G_B` form isn't accepted here. With fewer than 8 entries, the list is repeated to fill 8 places, so some colours become more common than others.

The colour you give is the one worn by subjects with the best clothing. At each lower level of clothing, the colour is greyer, so poorly clothed subjects wear duller clothes.

These colours are only used for the race's ordinary subjects. Enemies, slaves, prisoners, nobles and tourists wear colours set by the game itself, whatever their race.

```text
COLOR_CLOTHES: [
	{R: 114, G: 101, B: 35,},
	{R: 142, G: 126, B: 44,},
	{R: 83, G: 181, B: 94,},
	{R: 62, G: 135, B: 70,},
	{R: 105, G: 125, B: 239,},
	{R: 79, G: 94, B: 181,},
	{R: 53, G: 64, B: 122,},
	{R: 193, G: 77, B: 0,},
],
```

### COLOR_BLOOD

The colour of the race's blood. It's used for the blood drawn on injured subjects and their portraits, the blood and gore left when they're hurt, killed or executed, and the remains of sacrifices and butchering.

| | |
|---|---|
| **Type** | [Single colour](00-sprite.md#a-single-colour) |
| **Required** | Yes |

```text
COLOR_BLOOD: 123_20_17,
```

From `ARGONOSH.txt`:

```text
COLOR_BLOOD: {R: 70, G: 40, B: 40,},
```

### COLORS

The race's **colour collections**: named sets of colours for skin, hair, eyes and anything else that varies from one subject to the next. Types, add-ons and face parts refer to the collections by name, so the names are yours to choose. Vanilla's include `SKIN`, `HAIR`, `EYE`, `LEG`, `LIPS`, `FEATURE`, `PAINT1`, `JEWELLERY`, `ARMOUR` and `ARMOUR_LEATHER`. Cretonians have separate `SKIN_M` and `SKIN_F` collections for their two types.

| | |
|---|---|
| **Type** | Block of colour collections, keyed by name |
| **Required** | Yes |

Each subject is given one colour from each collection, and keeps it for life, so a subject's hair stays the same colour from one day to the next. Where a collection is used on both the body and the portrait, both show the same colour.

If a type, add-on or face part names a collection that isn't in `COLORS`, the game stops loading with an error listing the names that are.

Shortened:

```text
COLORS: {
	SKIN: {
		TURNS_WHITE_WHEN_DEAD: true,
		VALUES: [
			{R: 210, G: 169, B: 151,},
			{R: 204, G: 158, B: 137,},
			...
			{R: 150, G: 127, B: 96,},
		],
	},
	...
	HAIR: {
		TURNS_GRAY_WHEN_OLD: true,
		VALUES: [
			**Dark
			{R: 52, G: 51, B: 53,},
			...
		],
	},
	...
},
```

Each collection is a block with these tags:

#### VALUES

The collection's colours.

| | |
|---|---|
| **Type** | [List of colours](00-sprite.md#a-list-of-colours) |
| **Range** | 1 to 16 colours. More than 16 crashes the game. |
| **Required** | Yes |

Each collection has 16 places to choose from, and each subject is given one at random. The collection's colours are spread evenly over those places, so each colour is about equally likely. With 3 colours, for example, the first takes six places and the other two take five each.

#### GENERATE_RANDOMIZE

Fills the collection's spare places with darker copies of its colours, instead of spreading the colours out. The listed colours each take one place, and the rest are filled with copies that get darker place by place. The number sets how much darker: with `0.2`, the last copy is about 80% as bright as the colour it was copied from.

This gives a race a wider spread of shades from a few colours. Note that only the listed colours keep their full brightness, so with few colours, most subjects get a darker copy.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |

From `TILAPI.txt`:

```text
SKIN: {
	GENERATE_RANDOMIZE: 0.2,
	TURNS_WHITE_WHEN_DEAD: true,
	TURNS_SICKLY: true,
	VALUES: [
		{R: 209, G: 230, B: 188,},
		{R: 209, G: 225, B: 188,},
		{R: 209, G: 219, B: 188,},
		{R: 209, G: 219, B: 148,},
		{R: 209, G: 219, B: 158,},
		{R: 209, G: 219, B: 168,},
	],
},
```

#### TURNS_GRAY_WHEN_OLD

When `true`, retired subjects show a fixed grey in place of their usual colour. Vanilla uses it for hair.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. The default is `false`. |

#### TURNS_WHITE_WHEN_DEAD

When `true`, the colour fades part of the way towards a pale, bluish white in the portrait of a dead subject, such as a defeated raider leader. Vanilla uses it for skin.

It doesn't affect corpses in the settlement. Their colours blend towards a dark brown as they decay, whatever this tag says.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. The default is `false`. |

#### TURNS_SICKLY

When `true`, the colour is tinted while the subject is ill, with the colour of their disease, or while an event marks them with a colour of its own.

On the body seen in the settlement, the skin of a sick subject is tinted in this way whether or not its collection sets `TURNS_SICKLY`. The tag controls every other use of the collection, such as portraits, add-ons and legs.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. The default is `false`. |

#### PICK_BY_STAT

Chooses the colour by one of the subject's stats instead of at random. The lowest value of the stat gives the collection's first place, and the highest its last. Vanilla uses it so that the colour of plate armour follows the subject's `EQUIP_BATTLE_ARMOUR_PLATE` stat:

```text
ARMOUR: {
	PICK_BY_STAT: EQUIP_BATTLE_ARMOUR_PLATE,

	VALUES: [
		090_090_080,
		099_099_099,
		168_168_180,
		209_159_054,
	],
},
```

| | |
|---|---|
| **Type** | Stat name |
| **Required** | No |

A stat name the game doesn't recognise is silently ignored, and the colour is picked at random as usual.

## Notes

### The first seven collections

In v0.71.44, how many collections a race has, and their order in `COLORS`, affects how well the colours are mixed. Each collection's random choice comes from its own part of a random number the subject is given when they're created, chosen by the collection's position in the block. Only the first seven positions get a full, independent choice:

- the **8th** collection only ever chooses from the first half of its places, which means the first half of its colours;
- from the **9th** on, each collection makes the same choice as the one eight places above it, so their colours go together instead of varying separately.

Collections that use `PICK_BY_STAT` aren't affected, since they don't choose at random.

This affects vanilla Humans: `ARMOUR_LEATHER` is their 8th collection, so only the first two of its four colours appear. If a collection's colours matter to you, put it among the first seven.

## Related

- [init/race/sprite](00-sprite.md)
- [Types and faces](02-types-and-faces.md)
- [init/race](../00-race.md)
