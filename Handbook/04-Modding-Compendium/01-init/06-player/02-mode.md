# init/player/mode

Each file in `init/player/mode` defines one **play mode**. When you start a new game, the menu shows every mode as a large icon, alongside a **Custom Settings** option. A mode is a ready-made set of bonuses and penalties that applies to your realm for the whole game, in place of custom settings.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/player/mode/` |
| **Files** | One `.txt` file per mode, e.g. `40_CONQUERER.txt` |
| **Key** | The file name without `.txt`, e.g. `40_CONQUERER` |
| **Order** | Modes appear in the menu in file name order. |
| **Adding new files** | Yes. Every file in the folder is loaded as a mode. |
| **Text file** | `assets/text/player/mode/<KEY>.txt`, which must exist and have the same name. |

Vanilla has six modes. The file names don't always match the names shown in game, which come from the text files:

| File | Name in game |
|---|---|
| `00_FIRST_NAME` | Utopia |
| `10_GREAT` | Despot |
| `20_HOMESTEAD` | Homestead |
| `30_TRADER` | Merchant Prince |
| `40_CONQUERER` | Warlord |
| `50_RULER_OF_RULER` | Ruler of Kings |

## Tags

The examples below come from the vanilla `40_CONQUERER.txt`:

```text
ICON_I: 13,
TITLE: THE_CONQUERER,
BOOST: {
	CIVIC_GOV>MUL: 1.6,
	CIVIC_TRUST>MUL: 0.8,	
	CIVIC_RAIDING>MUL: 0.7,
	CIVIC_OPINION>MUL: 0.7,	
	BEHAVIOUR_LOYALTY>MUL: 1.2,
},
```

### ICON_I

The mode's icon in the menu, as a number. Modes use the same set of icons as titles: the sheet `assets/sprite/ui/Titles.png`, with its icons numbered from 0, left to right along each row and then row by row. Vanilla gives each mode the icon of the title that goes with it.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 to 34. A number outside this range causes an error when the menu is built. |
| **Required** | Yes |

```text
ICON_I: 13,
```

### TITLE

Vanilla names the [title](03-titles.md) that goes with each mode here, but the game never reads this tag, so it has no effect. The real link between a mode and its title is made in the title's own file, which requires the mode to be active (see [Notes](#notes)).

```text
TITLE: THE_CONQUERER,
```

### BOOST

The mode's bonuses and penalties, written in the same way as a race's `BOOST` block: each line names a stat, `>MUL` or `>ADD`, and a value. They apply to you only, never to AI factions, for the whole game.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | Yes. Without it, the game fails when you start a game in this mode. |

```text
BOOST: {
	CIVIC_GOV>MUL: 1.6,
	CIVIC_TRUST>MUL: 0.8,	
	CIVIC_RAIDING>MUL: 0.7,
	CIVIC_OPINION>MUL: 0.7,	
	BEHAVIOUR_LOYALTY>MUL: 1.2,
},
```

**Check your spelling carefully.** Unlike most `BOOST` blocks, a mode's block gives no warning for a boost name the game doesn't recognise. The line is silently ignored.

## The text file

Each mode needs a file of the same name in `assets/text/player/mode/`. Its name and description are shown when you hover over the mode in the menu. From `40_CONQUERER.txt`:

```text
NAME: "Warlord",
DESC: "See your enemies driven before you. Other despots will oppose you, but your subjects are used to hardship.

You can develop more regions, but also attract stronger raiders.",
```

| Tag | Meaning | Required |
|---|---|---|
| `NAME` | The mode's name. | Yes |
| `DESC` | The description. | Yes |

## Notes

### Checking the mode

Every mode creates a value named `PLAY_MODE_` followed by its key, such as `PLAY_MODE_40_CONQUERER`. It's `1` while you're playing that mode and `0` otherwise, and it's `0` for every mode if you chose custom settings. Conditions that check your faction's values can use it, in titles, levels and events alike.

Vanilla uses this to tie a title to each mode. The requirements in `THE_CONQUERER.txt` in `init/player/titles` include:

```text
EQUAL: {
	PLAY_MODE_40_CONQUERER: 1,
},
```

so The Conquerer title can only be earned while playing the Warlord mode.

### Saved games

The mode is saved with the game, but its boosts aren't. Each time a save is loaded, the game reads the mode's file again and applies the boosts it finds there. Changing a mode's `BOOST` block therefore changes existing saves that use it, and if the mode's file is missing, a save that used it loads without any mode boosts.

## Related

- [init/player](00-player.md)
- [init/player/titles](03-titles.md)
- [Occurrence and conditions](../05-event/02-occurrence.md)
