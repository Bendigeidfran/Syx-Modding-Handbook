# text/player

These files hold the wording of the things defined in [`init/player`](../01-init/06-player/00-player.md), plus the names of noble ranks.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/player/` |

| File or sub-folder | Holds | Format |
|---|---|---|
| `level/` | The name and wording of each player level. | [Player levels](../01-init/06-player/01-level.md#the-text-file) |
| `mode/` | The name and description of each game mode. | [Game modes](../01-init/06-player/02-mode.md#the-text-file) |
| `titles/` | The name and description of each title. | [Titles](../01-init/06-player/03-titles.md#the-text-file) |
| `noble/_RANKS.txt` | The names of noble ranks. | Below |

## noble/_RANKS.txt

This file names the ranks a noble can be promoted through. The game loads it by name.

### RANKS

The rank names, from lowest to highest. The length of this list sets how many ranks there are.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
RANKS: [
	"Sparabar",
	"Taxmari",
	"Asbari",
	"Sardar",
	"Grand Sardar",
	"Padaan",
	"Grand Padaan",
	"Anguiri",
	"Grand Anguiri",
	"Anarii Ray",
],
```

## Notes

### A vanilla file the game doesn't read

`_STATISTICS.txt` lists names such as `TIME_PLAYED`, but nothing reads it. The game takes those names from its dictionary instead.

## Related

- [text](00-text.md)
- [init/player](../01-init/06-player/00-player.md)
