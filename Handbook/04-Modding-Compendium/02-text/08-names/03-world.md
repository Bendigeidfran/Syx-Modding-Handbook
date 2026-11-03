# text/names/world

These files hold the names of factions and their rulers on the world map. A race chooses one with [`WORLD_NAME_FILE`](../../01-init/07-race/01-race-file.md#world_name_file), and all vanilla races share `Misc.txt`.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/names/world/` |
| **Files** | One `.txt` file per set of names, e.g. `Misc.txt` |
| **Adding new files** | Yes. A race file must name it. |

## Tags

The examples come from the vanilla `Misc.txt`.

### INTRO

What comes before a faction's name.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 to 128 |
| **Required** | Yes |

```text
INTRO: [
	"The Glorious Nation of",
	"The Dominion of",
],
```

### NAMES

The names of factions.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 to 512 |
| **Required** | Yes |

```text
NAMES: [
	"Opriud",
	"Sre",
],
```

### RULER_INTRO

What comes before a ruler's name. `{TITLE}` shows their title.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 to 128 |
| **Required** | Yes |

```text
RULER_INTRO: [
	"Supervised by {TITLE}",
	"Ruled by {TITLE}",
],
```

### RULER

The names of rulers.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 to 512 |
| **Required** | Yes |

```text
RULER: [
	"Jackster",
],
```

### DIPLOMACY_GREETING

The game never reads this tag. AI rulers' greetings come from the file named by [`KING_FILE`](../../01-init/07-race/01-race-file.md#king_file).

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |
| **Effect** | Unread |

```text
DIPLOMACY_GREETING: [
	"What do you propose, exalted one?",
],
```

## Related

- [text/names](00-names.md)
- [WORLD_NAME_FILE in the race file](../../01-init/07-race/01-race-file.md#world_name_file)
