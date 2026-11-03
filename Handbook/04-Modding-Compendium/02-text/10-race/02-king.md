# text/race/king

These files hold what AI rulers say to you in diplomacy. A race names one with [`KING_FILE`](../../01-init/07-race/01-race-file.md#king_file), and all vanilla races share `Normal.txt`.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/race/king/` |
| **Files** | One `.txt` file per set of speech, e.g. `Normal.txt` |
| **Adding new files** | Yes. A race file must name it. |

## Tags

Every tag here is required, and each is a list of text the game picks from at random. The examples come from the vanilla `Normal.txt`.

If a line uses a placeholder the game doesn't know, it shows a warning naming it, and the first such warning also lists the placeholders available. [Event text](../../01-init/05-event/04-text.md#placeholders) explains how placeholders work. Here they cover the ruler speaking, their faction, and yours under `PLAYER_`, such as `{PLAYER_FACTION_RULER}`. `{WAR_CAUSE}` and `{COALITION}` show the two names below.

### Speech

| Tag | When the ruler says it | Type and range | Required |
|---|---|---|---|
| `GREETING_GOOD`, `GREETING_BAD` | Greeting you for the first time, with a deal to offer or without one. | List of text | Yes |
| `STANCE_UP`, `STANCE_DOWN`, `STANCE_WARNING` | Relations are improving, they're cancelling an agreement, or they're warning you and asking for a deal. | List of text | Yes |
| `PEACE_GOOD`, `PEACE_BAD` | Offering peace. `PEACE_GOOD` is used when the deal has a positive value in credits. | List of text | Yes |
| `THREAT_NORMAL`, `THREAT_ALLY`, `THREAT_VASSAL` | Making demands, as a normal faction, one with transit rights, or your vassal. | List of text | Yes |
| `WAR_NORMAL`, `WAR_ALLY`, `WAR_VASSAL` | Declaring war, as a normal faction, your ally or your vassal. | List of text | Yes |
| `WAR_JOIN_NORMAL`, `WAR_JOIN_ALLY`, `WAR_JOIN_VASSAL` | Joining a war against you, in the same three ways. | List of text | Yes |

```text
WAR_JOIN_ALLY: [
	"Sorry old friend. They gave me no choice. I too will join {COALITION}.",
],
```

### Names and rumours

These aren't speech, so they don't use placeholders.

| Tag | What it is | Type and range | Required |
|---|---|---|---|
| `COALITION_NAME` | The name your enemies give their alliance. | List of text | Yes |
| `WAR_CAUSE_AGRESSION` | The name of the war when you started it. `{0}` shows the other faction. | List of text | Yes |
| `WAR_CAUSE_DEFEND` | The name of the war when the other side started it. `{0}` shows your faction. | List of text | Yes |
| `RUMOUR` | Completes the sentence "It has come to our attention that a rumour has been spread. That you ...". | List of text | Yes |
| `NGO` | The name of an organisation opposing your rule in a region. | List of text | Yes |

```text
RUMOUR: [
	"have drunk milk on occasion",
	"keep an Onx mistress",
],
```

## Related

- [text/race](00-race.md)
- [KING_FILE in the race file](../../01-init/07-race/01-race-file.md#king_file)
