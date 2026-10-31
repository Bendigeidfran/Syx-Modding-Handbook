# Event text

The words an event shows the player, such as its title, its message and the labels on its choices, live in a separate text file. This page covers that file and the placeholders that let messages mention the subjects, regions and factions an event involves.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/event/<FILE>.txt` |
| **Matching** | Each event file in `assets/init/event/` can have a text file with the same name. Inside it, each event's text is a block with the same name as the event's block. |
| **Required** | No. An event without text has no name or message, and shows no message window when it starts. |

## File structure

From `assets/text/event/ARTI.txt` (the message is shortened here):

```text
VOLCANO: {
	NAME: "Promising artifact",
	DESC: "A decision awaits.",
	MESSAGE: [
		"As the ruler of the land, you lay claim to all artifacts found in it. ...",
	],
	CHOICES: [
	"Depress the panel",
	"Sell it",
	],
},
```

Text can run over several lines inside its quotes. The line breaks are kept and appear in the message.

## Tags

### NAME

The event's title. It heads the message window and names the event elsewhere, for example in the descriptions of any permanent boosts it gives.

| | |
|---|---|
| **Type** | Text |
| **Required** | No |

### DESC

A short description, shown when the player hovers over the running event.

| | |
|---|---|
| **Type** | Text |
| **Required** | No |

### MESSAGE

The message shown when the event starts, as a list of text. **Every** entry is shown, each as its own paragraph, in order.

An event without a `MESSAGE` shows no message window. Because choices are buttons in that window, an event with `CHOICES` must have a `MESSAGE`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

### CHOICES

The labels for the event's choice buttons, as a list of text in the same order as the choices in the event file.

If this is missing, an event with one or two choices labels them **Accept** and **Decline**. An event with more choices and no labels shows them numbered from `0`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

### SUBJECT

A line of text attached to each subject the event has selected, for as long as the event runs. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Text |
| **Required** | No |

## Placeholders

Messages can include details that are only known when the event happens, such as the name of a selected subject or region. Write a placeholder in curly brackets, and the game replaces it with the right text. From a vanilla message in `ARTI.txt`:

```text
"Disaster has struck your capital! A janitor by the name of {SUBJECT1_NAME} has discovered something concerning while repairing a section of wall. ...
```

Placeholders are made of a **prefix** that says what the text is about, followed by a **detail**.

### Prefixes

| Prefix | Refers to |
|---|---|
| `SUBJECT1_`, `SUBJECT2_` | The first and second subjects the event selected |
| `REGION1_`, `REGION2_` | The first and second regions the event selected |
| `FACTION1_`, `FACTION2_` | The first and second factions the event selected |
| `ROYALTY1_`, `ROYALTY2_` | The first and second members of royalty the event selected |
| `PLAYER_` | Your own faction, and some details picked at random for the event (such as `PLAYER_RND_REGION_FAR`) |

### Details

The details available depend on the prefix. These are the ones vanilla uses most:

| Placeholder | Inserts |
|---|---|
| `{REGION1_NAME}` | The selected region's name |
| `{SUBJECT1_NAME}` | The selected subject's name |
| `{SUBJECT1_HE}`, `{SUBJECT1_HIM}`, `{SUBJECT1_HIS}`, `{SUBJECT1_HIMSELF}` | Pronouns for the selected subject |
| `{ROYALTY1_NAME}` | The selected royal's name |
| `{ROYALTY1_FACTION_FACTION}` | The name of the royal's faction |
| `{ROYALTY1_FACTION_FACTION_RULER}` | The ruler of the royal's faction |
| `{PLAYER_FACTION_RULER}` | Your ruler |
| `{PLAYER_RND_REGION_FAR}`, `{PLAYER_RND_REGION_CLOSE}` | A random region, far from or close to you |
| `{PLAYER_RND_FACTION_FAR}`, `{PLAYER_RND_FACTION_CLOSE}` | A random faction, far from or close to you |

Some prefixes chain together, as in `ROYALTY1_FACTION_FACTION`: `ROYALTY1_` leads to the royal, `FACTION_` to their faction, and `FACTION` gives that faction's name.

### Other placeholders

| Placeholder | Inserts |
|---|---|
| `{SELECTED_AMOUNT}` | The total number of targets the event selected |
| `{ACTION_AMOUNT_F}` | The share of animals or orchard affected by the event's last `PASTURE` or `ORCHARD` action, as a decimal |
| `{ACTION_AMOUNT_I}` | The same value rounded down to a whole number, which for a share is usually `0` |

### Finding the right placeholder

As with condition values, the game will tell you what's available. When it loads, it checks the placeholders in every event's `DESC` and `MESSAGE`. An unknown placeholder produces a warning naming it, and the first such warning also **lists every placeholder available**. A deliberately wrong placeholder is a quick way to get the full list.

## Notes

### Unknown tags

A tag the text format doesn't recognise is noted in the game's error output and otherwise ignored.

## Related

- [init/event](00-event.md)
- [Event structure](01-structure.md)
- [Event actions](03-actions.md)
