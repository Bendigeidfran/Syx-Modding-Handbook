# text/race/tourist

These files hold the reviews tourists leave after visiting your city. A race names one with `TOURIST_TEXT_FILE`, inside its [`TOURIST`](../../01-init/07-race/01-race-file.md#tourist) block.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/race/tourist/` |
| **Files** | One `.txt` file per set of reviews, e.g. `NORMAL.txt`, plus `_WIKI.txt` |
| **Adding new files** | Yes. A race file must name it. |

## Tags

The examples come from the vanilla `NORMAL.txt`.

If a line uses a placeholder the game doesn't know, it shows a warning naming it, and the first such warning also lists the placeholders available. [Event text](../../01-init/05-event/04-text.md#placeholders) explains how placeholders work. Here they cover the tourist and your faction, plus the ones listed below.

### RATING, ATTRACTION, SERVICE and INN

One block for each part of a review, all required. The game picks a line by the tourist's rating: `BAD` below 0.375, `OK` below 0.875, and `GOOD` from there up.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `BAD` | Lines for a poor visit. | List of text | Yes |
| `OK` | Lines for an average visit. | List of text | Yes |
| `GOOD` | Lines for a good visit. | List of text | Yes |

```text
INN: {
	BAD: [
		"Could not even get a room.",
	],
},
```

| Placeholder | Shows |
|---|---|
| `{ATTRACTION}`, `{ATTRACTIONS}` | The room the tourist came to see, singular and plural. |
| `{ATTRACTION_EMPLOYEE}` | The title of that room's workers. |
| `{SERVICE}` | A service the tourist used. |
| `{INN_NAME}`, `{INN_HOST}` | The name of the inn, and one of its workers. |

## _WIKI.txt

The game loads this file by name, so it must exist. It holds a wiki article about tourism, in the [`WIKI`](../../01-init/01-animal.md#wiki) format.

## Related

- [text/race](00-race.md)
- [TOURIST in the race file](../../01-init/07-race/01-race-file.md#tourist)
