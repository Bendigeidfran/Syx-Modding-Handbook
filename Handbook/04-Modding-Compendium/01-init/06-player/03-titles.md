# init/player/titles

Each file in `init/player/titles` defines one **title**, such as The Artisan or The Builder. Titles are earned by achievements: when your settlement meets a title's requirements, the title is unlocked for good and recorded in your player profile. When you start a new game, you can choose up to five of your unlocked titles, and their bonuses apply to your realm for that game.

Unlike levels and modes, titles last beyond a single game. They're how the game rewards you for what you've achieved in past games.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/player/titles/` |
| **Files** | One `.txt` file per title, e.g. `ARTISAN.txt` |
| **Key** | The file name without `.txt`, e.g. `ARTISAN`. Your profile records unlocked titles by this key. |
| **Adding new files** | Yes. Every file in the folder is loaded as a title. |
| **Text file** | `assets/text/player/titles/<KEY>.txt`, which must exist and have the same name. |
| **Icons** | `assets/sprite/ui/Titles.png`, chosen by `ICON_I`. |

Vanilla has 34 titles.

## Tags

The examples below come from the vanilla `ARTISAN.txt` unless stated otherwise:

```text
ICON_I: 0,
REQUIRES: {
	GREATERE: {
		COUNT_CRAFTED_GAME: 100000,
	},
},
UNLOCKS_FACTION: [
],
UNLOCKS_REGION: [
],
BOOST: {
	ROOM_WORKSHOP*>ADD: 0.2,
},
```

### ICON_I

The title's icon, as a number. The icons come from the sheet `assets/sprite/ui/Titles.png`, numbered from 0, left to right along each row and then row by row. The vanilla sheet has 35 icons, numbered 0 to 34.

[Modes](02-mode.md) use the same icons, and vanilla gives each mode the same icon as the title that goes with it.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 to 34 with the vanilla sheet |
| **Required** | Yes |

```text
ICON_I: 0,
```

### REQUIRES

The conditions for unlocking the title, in the same [condition format](../05-event/02-occurrence.md#conditions) as events. The values checked are your faction's. The Artisan, for example, is unlocked once the current game's **Goods Crafted** count reaches 100,000.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No. A title without requirements is always available. |

```text
REQUIRES: {
	GREATERE: {
		COUNT_CRAFTED_GAME: 100000,
	},
},
```

A condition can check which [mode](02-mode.md) you're playing, using the mode's `PLAY_MODE_` value. Vanilla uses this to make some titles available only in a particular mode. From `THE_CONQUERER.txt`:

```text
REQUIRES: {
	GREATERE: {
		WORLD_REGIONS: 10.0,
** # of vassals > 5
	},
	EQUAL: {
		PLAY_MODE_40_CONQUERER: 1,
	},
},
```

### UNLOCKS_FACTION and UNLOCKS_REGION

Things that stay locked unless you chose this title for the current game, as lists of names. The names are the same as for [levels](01-level.md#unlocks_faction): rooms, room upgrades, recipes and so on for `UNLOCKS_FACTION`, and region buildings for `UNLOCKS_REGION`.

Listing a room here makes it available **only** in games where you've chosen this title. AI factions aren't affected. Vanilla's lists are all empty.

| | |
|---|---|
| **Type** | Lists of names |
| **Required** | No |

```text
UNLOCKS_FACTION: [
],
UNLOCKS_REGION: [
],
```

### BOOST

The title's bonuses, written in the same way as a race's `BOOST` block: each line names a stat, `>MUL` or `>ADD`, and a value. A `*` at the end of a name applies the boost to every stat whose name begins with what comes before it. The Artisan's `ROOM_WORKSHOP*` boosts every workshop.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	ROOM_WORKSHOP*>ADD: 0.2,
},
```

The boosts apply only to you, and only in games where you've chosen the title. They're also not always at full strength; see [How strong a title is](#how-strong-a-title-is) below.

A boost name the game doesn't recognise is ignored. The first time this happens, the game shows a warning listing the available names.

## The text file

Each title needs a file of the same name in `assets/text/player/titles/`. From `ARTISAN.txt`:

```text
NAME: "The Artisan",
DESC: "Gained by workshop output. Increases productivity of all workshops.",
```

| Tag | Meaning | Required |
|---|---|---|
| `NAME` | The title's name. | Yes |
| `NAMES` | A plural name. | No. If it's missing, `NAME` is used. |
| `DESC` | The description. Vanilla uses it to say how the title is earned and what it does. | Yes |

As with animals, the tags can also be wrapped in an `INFO` block.

## Notes

### Unlocking

The game checks your titles one at a time as you play. When your settlement meets a title's requirements, and keeps meeting them for about a quarter of a day, the title is unlocked and a message announces it.

The unlock is recorded in your player profile, not in your save, so it stays unlocked in every future game. The profile also records **which race** you were playing when you unlocked it. You can unlock the same title again with a different race, and each race you unlock it with makes it stronger.

Titles can't be unlocked while playing one of the game's showcase saves.

### Choosing titles

When you start a new game, a **Select Titles** step lets you pick up to five titles. You can choose any title you've unlocked, as well as any whose requirements your new realm already meets.

### How strong a title is

A chosen title's boosts are scaled by how many races you've unlocked it with. They start at half strength and rise evenly to full strength once you've unlocked the title with every playable race:

> strength = 50% + 50% × (races unlocked with ÷ playable races)

With vanilla's playable races, a title unlocked with just one race gives a little over half its boosts.

When several chosen titles multiply the same stat, the game adds their effects together rather than multiplying them, as it does for levels.

### Renaming titles

Because your profile stores unlocked titles by key, renaming a title's files makes the game treat it as a new title that you haven't unlocked yet.

## Related

- [init/player](00-player.md)
- [init/player/mode](02-mode.md)
- [init/player/level](01-level.md)
- [Occurrence and conditions](../05-event/02-occurrence.md)
