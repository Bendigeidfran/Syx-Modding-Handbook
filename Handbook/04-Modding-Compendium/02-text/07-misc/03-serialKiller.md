# text/misc/serialKiller

These files hold the serial killer event: the messages the player gets as the case unfolds, and the killers themselves.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/misc/serialKiller/` |
| **Files** | One `.txt` file per killer, e.g. `TheCollector.txt`, plus `_INFO.txt` |
| **Adding new killers** | Yes. Every file not starting with `_` is loaded as a killer. |

## Tags

These tags are in each killer's file. The examples come from the vanilla `TheCollector.txt`.

### NAME

The name the killer goes by. `{KILLER_ALIAS}` in a message shows it.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "The Collector",
```

### METHOD

What the killer leaves on the bodies. `{KILLER_SIGNATURE}` in a message shows it.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
METHOD: "hearts removed",
```

### MESSAGES

What the killer says after each murder, in order, as a list of text. The length of the list also sets how many victims it takes before the killer stops: the last message goes with the last murder. The game names a suspect at the murder halfway through the list.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 2 to 100 |
| **Required** | Yes |

```text
MESSAGES: [
	"Another one added to the collection. You shouldn't have resisted me. Now your organs will never serve their original purpose.",
],
```

## _INFO.txt

This file holds the messages the player gets. The game loads it by name.

### FIRST, SECOND, AGAIN, SUSPECT, SUSPECT_FAIL, CAUGHT and COLD

One block for each message, all required. `FIRST` and `SECOND` go with those murders, `AGAIN` with later ones. `SUSPECT` names a suspect, `SUSPECT_FAIL` says they were innocent and `CAUGHT` that they were guilty, and `COLD` says the trail has gone cold.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `TITLE` | The message's title. | Text | Yes |
| `BODY` | The message's text, which can use the placeholders below. | Text | Yes |

The example leaves out the `BODY`.

```text
AGAIN: {
	TITLE: "Another Killing",
},
```

The placeholders are `{VICTIM_NAME}`, `{VICTIM_AGE}`, `{VICTIM_RACE}`, `{KILLER_SIGNATURE}`, `{KILLER_ALIAS}`, `{KILLER_NAME}` and `{SUSPECT_NAME}`.

## Related

- [text/misc](00-misc.md)
