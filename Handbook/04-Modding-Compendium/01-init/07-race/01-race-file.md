# The race file

Each file directly inside `init/race` defines one race. This page covers the race file's tags, except for the two largest blocks, which have pages of their own: [`PREFERRED`](02-preferences.md) and [`STATS`](03-stats.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/race/` |
| **Files** | One `.txt` file per race, e.g. `HUMAN.txt` |
| **Key** | The file name without `.txt`, e.g. `HUMAN`. Other files use this key to refer to the race. |
| **Adding new files** | Yes. Every file in the folder (not in its sub-folders) is loaded as a race. There must be at least one. |
| **Text file** | `assets/text/race/<KEY>.txt`, which must exist and have the same name. |

Vanilla has eight races: `ARGONOSH`, `CANTOR`, `CRETONIAN`, `DONDORIAN`, `GARTHIMI`, `HUMAN`, `Q_AMEVIA` and `TILAPI`. Argonosh and Cantor aren't playable.

## Tags

The examples below come from the vanilla `HUMAN.txt` unless stated otherwise.

### PLAYABLE

Whether the race is playable. Only playable races can be chosen when you start a game, and only playable races live in the regions of the world map: the races of AI factions and regional populations all come from this list.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
PLAYABLE: true,
```

### PROPERTIES

A block of the race's basic physical and economic properties. The block is required, and so is every tag in it.

```text
PROPERTIES: {
	HEIGHT: 6,
	WIDTH: 9,
	BABY_DAYS: 12,
	CHILD_DAYS: 80,
	CORPSE_DECAY: true,
	SLEEPS: true,
	SLAVE_PRICE: 11,
	SLAVE_PRICE_RECOVERY: 0.5,
	RAID_MERCINARY: 1.0,
},
```

| Tag | Meaning | Type and range |
|---|---|---|
| `HEIGHT` | How tall members of the race are. Each individual varies up to 25% either side of this. Children are shorter, and grow towards full height as they age. | Integer, 0 or more. The code names a maximum of 200, but doesn't enforce it. |
| `WIDTH` | How wide a member of the race is. This sets the space each one takes up: how closely they can pass each other, the size of their corpse, and how widely spaced soldiers stand in formation. | Integer, 5 or more. The code names a maximum of 15, but doesn't enforce it. |
| `BABY_DAYS` | How many days a newborn spends as a baby, carried by its parent. If it's `0`, the race doesn't reproduce naturally at all. | Integer |
| `CHILD_DAYS` | How many days a child takes to grow up after being a baby. A member of the race is an adult after `BABY_DAYS` plus `CHILD_DAYS`. | Integer |
| `CORPSE_DECAY` | Whether the race's corpses rot. | True/false |
| `SLEEPS` | Whether members of the race lie down to sleep in their beds. | True/false |
| `SLAVE_PRICE` | The worth of a slave of this race in the game's economy, measured in the same units of work the game uses to value goods. | Decimal, 0 to 2147483647 |
| `SLAVE_PRICE_RECOVERY` | How quickly AI factions' stocks of slaves of this race recover after you trade with them. At `0`, they don't recover at all. | Decimal, 0 to 10 |
| `RAID_MERCINARY` | How likely members of this race are to become raiders and mercenaries, compared with other races. Note the game's spelling. | Decimal, 0 to 100000 |

`RAID_MERCINARY` works as a weight. When the game decides which race a band of raiders belongs to, each race's chance is in proportion to this value, and for raiders coming from a region of the world map, to how many of the race live there. Mercenaries offered to you are chosen in a similar way.

`GARTHIMI.txt` also has an `ADULT_AT_DAY` tag in this block. The game doesn't read it.

### BIO_FILE

The name of the biography file the race uses, from `assets/text/race/bio/`. Biographies are the descriptions and opinions shown when you inspect a subject. Several races can share one file.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
BIO_FILE: Normal,
```

Unlike most text files, biography files are **not** [layered over vanilla](../../../02-Getting-Started.md#changing-a-vanilla-file). If your mod has a file of the same name, the game uses yours whole, so it must be complete.

### BIO_FILE_SPECIFIC

An extra biography file from `assets/text/race/bio/specific/`, with lines that only this race uses. Like `BIO_FILE`, it's used whole, without layering.

| | |
|---|---|
| **Type** | File name |
| **Required** | No |

```text
BIO_FILE_SPECIFIC: Human,
```

### KING_FILE

The name of the file in `assets/text/race/king/` holding what AI rulers of this race say to you in diplomacy: greetings, threats, declarations of war and so on.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
KING_FILE: Normal,
```

### WORLD_NAME_FILE

The name of the file in `assets/text/names/world/` that supplies names for this race's factions and rulers on the world map.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
WORLD_NAME_FILE: Misc,
```

### RAID_TEXT_FILE

The name of the file in `assets/text/race/raider/message/` holding the messages raiders of this race send you.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
RAID_TEXT_FILE: Normal,
```

### RAIDER_NAME_FILE

The name of the file in `assets/text/race/raider/name/` holding names for raider leaders of this race.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
RAIDER_NAME_FILE: Normal,
```

### TOURIST

Whether, and how, members of this race visit your settlement as tourists.

| Tag | Meaning | Type and range |
|---|---|---|
| `OCCURENCE` | How often tourists of this race come, compared with other races. Note the game's spelling. | Decimal, 0 to 100000 |
| `CREDITS` | How generous these tourists are: it scales the money they pay. | Decimal, 0 to 100000 |
| `TOURIST_TEXT_FILE` | The file in `assets/text/race/tourist/` holding their reviews and other text. | File name |

All three are required if the block is present. Without the block, the race never comes as tourists.

```text
TOURIST: {
	OCCURENCE: 1.0,
	CREDITS: 0.75,
	TOURIST_TEXT_FILE: NORMAL,
},
```

The attractions tourists of a race look for aren't set here. They're taken from the race's [work preferences](02-preferences.md#work): of the rooms that can serve as tourist attractions, the five (at most) the race most likes to work in, ignoring any it doesn't like at all.

### HOME

The name of the file in [`init/race/home/`](04-home.md) that sets the furniture and floors of this race's homes.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
HOME: HUMAN,
```

### TECH

Three vanilla races (`HUMAN`, `GARTHIMI` and `Q_AMEVIA`) have a `TECH` list, but the game never reads it.

| | |
|---|---|
| **Type** | List |
| **Required** | No |
| **Effect** | Unread |

```text
TECH: [
	*,
],
```

### MILITARY_SUPPLY_USE

How much of each army supply soldiers of this race use. Army supplies are defined in `assets/init/resource/supply/`, and each supply file lists the races that use it. This block overrides that list for this race: `0` means the race doesn't use the supply, and higher numbers multiply how much it uses.

| | |
|---|---|
| **Type** | Block of integers, keyed by supply |
| **Range** | Each value 0 or more. The code names a maximum of 10000, but doesn't enforce it. |
| **Required** | No |

From `GARTHIMI.txt`:

```text
MILITARY_SUPPLY_USE: {
	DRINK: 0,
},
```

### PREFERRED

The race's preferences: its favourite foods and drinks, the buildings, roads and jobs it likes, how it gets on with other races, and its views on crime and punishment. See [Race preferences](02-preferences.md).

### POPULATION

How the race spreads across the world map, and how well it thrives in different places.

| Tag | Meaning | Type and range |
|---|---|---|
| `MAX` | How numerous the race can be. It scales the most members of this race that can live in your settlement, and is also used in working out the race's population in world regions. | Decimal, 0 to 1 |
| `GROWTH` | How quickly the race's population grows in world regions. | Decimal, 0.0001 to 1 |
| `CLIMATE` | How well the race does in each climate: `COLD`, `TEMPERATE` and `HOT`. A climate missing from the block counts as `0`. | Block of decimals, each 0 to 1 |
| `TERRAIN` | How well the race does on each type of terrain: `OCEAN`, `WET`, `MOUNTAIN`, `FOREST` and `NONE` (open land). A terrain missing from the block counts as `0`. | Block of decimals, each 0 to 100 |

`MAX` and `GROWTH` are required if the block is present.

```text
POPULATION: {
	MAX: 1.0,
	GROWTH: 0.075,
	CLIMATE: {
		COLD: 0.8,
		TEMPERATE: 1.0,
		HOT: 0.8,
	},
	TERRAIN: {
		MOUNTAIN: 0.2,
		FOREST: 0.2,
		NONE: 1.5,
	},
},
```

In world regions, a race's population is set by both blocks together: its climate values weighted by the region's climate, multiplied by its terrain values weighted by the region's terrain. The climate value for your own settlement's climate also affects how readily the race immigrates to you, and is a need in its own right (see [Race stats](03-stats.md)).

Without a `POPULATION` block, every climate and terrain counts as `0`. Vanilla's two non-playable races have none.

### TRAITS

Every vanilla race has a `TRAITS` block, but the game doesn't read it, so it has no effect. Its entries (`FIGHTER`, `GLUTTON` and `SPRINTER`) aren't even current traits.

```text
TRAITS: {
	FIGHTER: 0.1,
	GLUTTON: 0.1,
	SPRINTER: 0.1,
},
```

| | |
|---|---|
| **Type** | Block of decimals |
| **Required** | No |
| **Effect** | Unread |

To set trait chances for a race, use [`TRAIT`](#trait) instead.

### TRAIT

The chance, from 0 to 1, that a member of this race has each [personality trait](07-trait.md), overriding the default chance set in the trait's own file. Note the singular name: vanilla's `TRAITS` block is a different, unread tag. Vanilla doesn't use `TRAIT`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by trait |
| **Range** | Each value 0 to 1 |
| **Required** | No |

### RESOURCE

What a corpse of this race yields when it's butchered in a cannibal room. Each listed resource is produced in proportion to the number given.

| | |
|---|---|
| **Type** | Block of numbers, keyed by resource |
| **Range** | Each value 0 to 100000 |
| **Required** | No |

```text
RESOURCE: {
	MEAT: 30,
	LEATHER: 10,
},
```

### RESOURCE_GROOMING

Resources produced each time a member of this race is groomed at a barber, as whole numbers. Dondorians shed cotton, for example. A resource name the game doesn't recognise is silently ignored.

| | |
|---|---|
| **Type** | Block of integers, keyed by resource |
| **Required** | No |

From `DONDORIAN.txt`:

```text
RESOURCE_GROOMING: {
	COTTON: 1,
},
```

### STATS

How much each of the race's needs and wants matters to each class. This decides what makes members of the race happy, loyal or submissive. See [Race stats](03-stats.md).

### STATS_ON_SPAWN

Starting values for some stats, given to each new member of the race. Vanilla uses it to make Dondorians arrive already educated. The keys are stat names, as in the [`STATS` block](03-stats.md).

| | |
|---|---|
| **Type** | Block of decimals, keyed by stat |
| **Required** | No |

From `DONDORIAN.txt`:

```text
STATS_ON_SPAWN: {
	EDUCATION_EDUCATION: 1.0,
},
```

In v0.71.44 the values given aren't what you might expect. Each new member gets a random value between `0` and one fifth of the number, and about half of them get `0`. With `1.0`, Dondorians arrive between 0% and 20% educated.

### SPRITE_FILE

The name of the file in [`init/race/sprite/`](06-sprite/00-sprite.md) that sets the race's appearance.

| | |
|---|---|
| **Type** | File name |
| **Required** | Yes |

```text
SPRITE_FILE: HUMAN,
```

### ICON_SMALL and ICON_BIG

The race's icons, written as icon paths. Vanilla uses 24-pixel icons for `ICON_SMALL` and 32-pixel icons for `ICON_BIG`.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path |
| **Required** | Yes, both |

```text
ICON_SMALL: 24->race->Human->0,
ICON_BIG: 32->race->Human->0,
```

### ROOM_FLOOR_OVERRIDE

Floors that rooms use when **you** are playing this race, in place of their usual floors. Each entry names a room and lists floors, one for each of the room's upgrade levels in turn. Rooms or levels not covered keep their normal floor.

This only affects the race you play. It doesn't depend on who uses or builds the room.

| | |
|---|---|
| **Type** | Block of lists, keyed by room |
| **Required** | No |

From `GARTHIMI.txt` (shortened):

```text
ROOM_FLOOR_OVERRIDE: {
	_BENCH: [DARK1, DARK2, DARK3,],
	_EXECUTION: [DARK1, DARK2, DARK3,],
	...
	ARENAG_NORMAL: [DARK3,],
},
```

### BOOST

The race's bonuses and penalties. Each line names a stat, `>MUL` or `>ADD`, and a value, and a `*` at the end of a name applies the line to every stat whose name begins with what comes before it. A name the game doesn't recognise is ignored, and the first time this happens the game shows a warning listing the available names.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	PHYSICS_RESISTANCE_COLD>ADD: -0.15,
	PHYSICS_RESISTANCE_HOT>ADD: -0.15,
	PHYSICS_DEATH_AGE>MUL: 0.8,
	BATTLE_BLUNT_ATTACK>ADD: 10,
	CIVIC_IMMIGRATION>MUL: 1.5,
	ROOM_UNIVERSITY*>MUL: 1.5,
	ROOM_SCHOOL*>MUL: 1.5,
	BEHAVIOUR_LAWFULNESS>MUL: 0.75,
	BEHAVIOUR_SANITY>MUL: 0.8,
	
	ROOM_FARM*>MUL: 1.1,
	ROOM_ORCHARD*>MUL: 1.1,
	ROOM_LIBRARY_NORMAL>MUL: 1.25,
	ROOM_ADMIN_NORMAL>MUL: 1.25,
	ROOM_LABORATORY_NORMAL>MUL: 1.25,
},
```

### EQUIPMENT_NOT_ENABLED and EQUIPMENT_ENABLED

Which equipment the race can use. Every piece of equipment is allowed by default. `EQUIPMENT_NOT_ENABLED` lists equipment the race can't use, and `EQUIPMENT_ENABLED` lists equipment it can.

The game always applies `EQUIPMENT_NOT_ENABLED` first, whatever order they appear in. That lets you disable everything with `*` and then enable a few items, as the Argonosh do:

| | |
|---|---|
| **Type** | Lists of equipment keys |
| **Required** | No |

From `ARGONOSH.txt`:

```text
EQUIPMENT_NOT_ENABLED: [
	*,
],

EQUIPMENT_ENABLED: [
	BATTLE_ARMOUR_LEATHER,
	BATTLE_ARMOUR_PLATE,
],
```

Equipment keys are formed from the files in [`assets/init/stats/equip/`](../13-stats/04-equip/00-equip.md), as described under [EQUIPMENT in init/battle/divType](../02-battle/01-divType.md#equipment).

## The text file

Each race needs a file of the same name in `assets/text/race/`. It holds the race's names and descriptions, and words its members use when they speak.

| Tag | Meaning | Required |
|---|---|---|
| `NAME`, `NAMES` | The race's name, singular and plural. | `NAME` yes; `NAMES` no |
| `POSSESSIVE`, `POSSESSIVES` | The adjective forms, as in "a Human house". | Yes |
| `DESC` | The short description. | Yes |
| `DESC_LONG` | The long description. | Yes |
| `CHALLENGE` | How difficult the race is to play, such as `"Medium"`. | No |
| `PROS`, `CONS` | Lists of the race's strengths and weaknesses. | No |
| `PRONOUN_HE`, `PRONOUN_HIM`, `PRONOUN_HIS`, `PRONOUN_HIMSELF`, `PRONOUN_CHILD`, `PRONOUN_HEC`, `PRONOUN_HIMC`, `PRONOUN_HISC`, `PRONOUN_HIMSELFC`, `PRONOUN_CHILDC` | Pronouns, as lists: the first entry is used for males and the second for females. A name ending in `C` is the capitalised version. | Yes |
| `ARMY_NAMES` | Names for the race's armies. At least 1 and at most 255. | Yes |
| `HELLO`, `GOODBYE`, `CURSE`, `INSULT`, `INSULTING`, `LORD`, `CITY`, `OTHERS`, `SELVES`, `SELF`, `CHILDREN` | Lists of words and phrases members of the race use when they speak. | Yes |
| `WIKI` | An article about the race in the in-game wiki, in the format described under [`WIKI` in init/animal](../01-animal.md#wiki). | No |

From `HUMAN.txt` in `assets/text/race/` (shortened):

```text
NAME: "Human",
NAMES: "Humans",
POSSESSIVE: "Human",
POSSESSIVES: "Human",
PRONOUN_HE: ["he", "she",],
PRONOUN_HEC: ["He", "She",],
...
LORD: [
	"Lord",
	"Liege",
	"Master",
],
```

## Notes

### Wildcards in blocks keyed by name

Several blocks in race files are keyed by the names of other things: rooms, floors, races, resources. In these blocks, `*` on its own applies a value to everything, and a name ending in `*` applies it to every name beginning with what comes before the `*`. Entries are applied in the order they're written, so put the wildcard first and the exceptions after it.

Names beginning with an underscore, such as `_ASYLUM`, can be written with or without the underscore.

## Related

- [init/race](00-race.md)
- [Race preferences](02-preferences.md)
- [Race stats](03-stats.md)
- [init/race/sprite](06-sprite/00-sprite.md)
- [Your First Mod](../../../03-Your-First-Mod.md)
