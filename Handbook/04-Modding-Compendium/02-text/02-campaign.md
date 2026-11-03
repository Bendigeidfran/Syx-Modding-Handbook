# text/campaign

These files hold the wording of the campaigns on the game's campaign menu, which in vanilla are its two tutorials. Each one pairs with a file of the same name in the game's `data/campaigns/` folder, which sits beside `assets` in `base/data.zip`.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/campaign/` |
| **Files** | One `.txt` file per campaign, e.g. `000_Tutorial.txt` |
| **Key** | The file name, e.g. `000_Tutorial` |
| **Companion file** | `data/campaigns/<KEY>.txt` |

## The text file

The examples come from the vanilla `000_Tutorial.txt`.

### NAME

The campaign's name on the menu.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "New Cretonia #1 (Tutorial)",
```

### NAMES

The plural of the name. Vanilla doesn't use it here.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

### DESC

The campaign's description on the menu.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Learn the very basics of the game as you partake in Hotam Greattusk's struggle to build a new settlement for his Cretonian tribe.",
```

### CUTSCENE

The words of the scene shown when the campaign starts. Both tags are required.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `TITLE` | The scene's title. | Text | Yes |
| `BODY` | The scene's text. | Text | Yes |

```text
TITLE: "The struggles of Hotam Greattusk",
```

### MISSIONS

The tutorial's steps, as a block for each step holding `NAME`, `DESC` and `GOAL`. The example leaves out the `DESC`.

Unverified: the game's source code never reads this block. It's presumably read by the campaign's script, which the source doesn't include, so the tag names and which are needed couldn't be checked.

| | |
|---|---|
| **Type** | Block |

```text
ZOOM: {
	NAME: "Zoom & Minimap",
	GOAL: "Zoom all the way out and back in again.",
},
```

## Notes

### The file in data/campaigns

The companion file holds the rest of the campaign, and it's read when the menu opens. Vanilla's look like this:

| Tag | Meaning |
|---|---|
| `REQUIRES` | The campaigns that must be completed first. |
| `SCRIPTS` | The scripts the campaign runs. The game stops with an error if one doesn't exist. |
| `SAVE_LOCAL` | Which saved game the campaign starts from: the player's own save for it if `true`, or the one shipped with the game if `false`. |
| `CUTSCENE` | The scene's `IMAGE` and `MUSIC`. |

Unverified: with mods active, the code appears to look for this folder in only one mod, rather than adding to the game's own. Where a mod should put it, and what that does to vanilla's tutorials, wasn't confirmed.

## Related

- [text](00-text.md)
