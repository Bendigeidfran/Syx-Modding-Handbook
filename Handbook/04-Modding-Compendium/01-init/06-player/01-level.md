# init/player/level

Each file in `init/player/level` defines one **level**: a rank your ruler holds, such as Mir or Emir. You start the game at the first level and are promoted through the others in order as your settlement meets their requirements. Each level can give bonuses and unlock buildings.

Your current level appears with your ruler's name, in the form "Mir *ruler* of *faction*".

## At a glance

| | |
|---|---|
| **Location** | `assets/init/player/level/` |
| **Files** | One `.txt` file per level, e.g. `010_MIR.txt` |
| **Key** | The file name without `.txt`, e.g. `010_MIR` |
| **Order** | Levels are ordered by file name. The first file is the level you start at. |
| **Adding new files** | Yes. Every file in the folder is loaded as a level, and its file name decides where it falls in the order. There must be at least one. |
| **Text file** | `assets/text/player/level/<KEY>.txt`, which must exist and have the same name. |

Vanilla has fourteen levels. In order: `010_MIR`, `020_EMIR`, `021_AMARIR`, `030_PRONTIX`, `031_APPRONTIX`, `032_APPRONTIX_RAY`, `040_LEGATI`, `045_LEGATI_RAY`, `050_DAKORI`, `060_DAKORI_RAY`, `070_SORAX`, `080_SORAX_RAY`, `090_ASTA` and `100_ASTA_RAY`.

The numbers at the start of the names are only there to set the order. Files are sorted character by character, not by numerical value, which is why vanilla pads its numbers to three digits. To add a level between two vanilla ones, give it a name that sorts between theirs, such as `025_MYLEVEL` to fall between `021_AMARIR` and `030_PRONTIX`.

## Tags

The examples below come from the vanilla `030_PRONTIX.txt` unless stated otherwise.

### REQUIRES

The conditions your settlement must meet to be promoted to this level, in the same [condition format](../05-event/02-occurrence.md#conditions) as events. The values checked are your faction's.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No. A level without requirements is reached as soon as you reach the level before it. |

```text
REQUIRES: {
	GREATERE: {
		POPULATION_CITIZEN: 200,
	},
},
```

The first level's requirements are never checked, because you start there.

### UNLOCKS_FACTION

Things that stay locked until you reach this level, as a list of names. Vanilla uses it for rooms: `030_PRONTIX` holds back the Training Ground, the Army Supply Depot and the Stockade until you're a Prontix.

| | |
|---|---|
| **Type** | List of names |
| **Required** | No |

```text
UNLOCKS_FACTION: [

	ROOM_BARRACKS_VANILLA,
	ROOM_MILITARY_SUPPLY,
	ROOM_STOCKADE,
],
```

The names that can go in this list include:

| Name | Locks |
|---|---|
| `ROOM_<room>` | A room. `<room>` is the name of the room's file in `assets/init/room/`, without a leading underscore: `BARRACKS_VANILLA.txt` gives `ROOM_BARRACKS_VANILLA`, and `_STOCKADE.txt` gives `ROOM_STOCKADE`. |
| `ROOM_<room>_UPGRADE_<n>` | A room's upgrade, numbered from 1. |
| `ROOM_<room>_RECIPE_<n>` | One of a workshop's recipes, numbered from 1. |
| `FLOOR_<floor>` | A type of floor. |
| `FORTIFICATION_<key>` | A type of wall or fortification. |

These are the same names that technologies list under their own `UNLOCKS_FACTION`.

The lock only applies to you. AI factions are never held back by your level.

If a name doesn't match anything, the entry is ignored. The first time this happens, the game shows a warning that lists **every name available**, so as with condition values, you can use a deliberately wrong name to get the full list.

### UNLOCKS_REGION

Things on the world map that stay locked until you reach this level, as a list of names. These are region buildings, named `BUILDING_<category>_<building>_<level>`. Vanilla's lists are all empty.

The lock only applies to regions you hold.

| | |
|---|---|
| **Type** | List of names |
| **Required** | No |

```text
UNLOCKS_REGION: [
],
```

The game also reads an `UNLOCKS_HUMAN` list, but in v0.71.44 nothing can be locked through it.

### BOOST

Bonuses that come with the level, written in the same way as a race's `BOOST` block: each line names a stat, `>MUL` or `>ADD`, and a value.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No. Several vanilla levels have an empty block. |

```text
BOOST: {
	CIVIC_INNOVATION>ADD: 10,
	CIVIC_KNOWLEDGE>ADD: 35,
},
```

Level boosts **add up** as you rise. Each level keeps applying its boosts once you've reached it, so at the fifth level you have the boosts of all five. They only apply to you, not to AI factions.

When several levels multiply the same stat, the game adds their effects together rather than multiplying them. Two levels with `CIVIC_INNOVATION>MUL: 1.2` give `1.4`, not `1.44`.

A boost name the game doesn't recognise is ignored. The first time this happens, the game shows a warning listing the available names.

## The text file

Each level needs a file of the same name in `assets/text/player/level/`. From `010_MIR.txt`:

```text
MALE: "Mir",
FEMALE: "Miress",
DESC: "A Mir is the head of the lowest of noble houses. The people who follow you know not to expect much.",
```

| Tag | Meaning | Required |
|---|---|---|
| `MALE` | The level's name. This is the name the game shows. | Yes |
| `FEMALE` | A feminine form of the name. The game reads it, but in v0.71.44 never shows it. | Yes |
| `DESC` | The description. | Yes |

## Notes

### Promotion

The game only ever checks the **next** level's requirements. Once your settlement meets them, you're promoted, and a message announces your new level and what it brings. Levels are always gained one at a time and in order, and you're never demoted.

### AI rulers

The rulers of AI factions are given titles from the same list of level names. An AI ruler's title depends on how many regions their faction holds: the list of levels is spread across 0 to 20 regions, so a faction with 20 or more regions has the last level's name. If you add or remove levels, AI rulers' titles shift to match.

### The throne

Your throne room's appearance changes as you rise. It depends on how far through the list of levels you are, so with more levels, each one changes it less.

## Related

- [init/player](00-player.md)
- [Occurrence and conditions](../05-event/02-occurrence.md)
- [init/player/titles](03-titles.md)
