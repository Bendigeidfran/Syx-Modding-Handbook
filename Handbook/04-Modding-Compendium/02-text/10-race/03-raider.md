# text/race/raider

These files hold the raiders that demand tribute from you: what they say, and what they're called. A race names one of each with [`RAID_TEXT_FILE`](../../01-init/07-race/01-race-file.md#raid_text_file) and [`RAIDER_NAME_FILE`](../../01-init/07-race/01-race-file.md#raider_name_file).

## At a glance

| | |
|---|---|
| **Location** | `assets/text/race/raider/message/` |
| **Files** | One `.txt` file per set of messages, e.g. `Normal.txt`, and one per set of names in `raider/name/` |
| **Adding new files** | Yes. A race file must name it. |

## Tags

Every tag in a message file is required, and each is a list of text the game picks from at random. The examples come from the vanilla `message/Normal.txt`.

If a line uses a placeholder the game doesn't know, it shows a warning naming it, and the first such warning also lists the placeholders available. [Event text](../../01-init/05-event/04-text.md#placeholders) explains how placeholders work. Here they include `{RAIDER_NAME}`, the raider's details, and your faction.

### FIRST and REPEAT

The demand a raider sends, the first time and on later visits. The game builds it from one line of each of these lists, in this order.

| Tag | Part of the message | Type and range | Required |
|---|---|---|---|
| `GREETING` | The greeting. | List of text | Yes |
| `INTROS` | Who the raider is. | List of text | Yes |
| `BODIES` | What's happening. | List of text | Yes |
| `ENDS` | What they want. | List of text | Yes |

```text
GREETING: [
	"{RACE_HELLO}",
],
```

### REJECTED, PAYED and AFTER_RAID

The raider's reply when you refuse, when you pay, and after a raid.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

### HELP, HELP_FIGHT and HELP_DESTROYED

Messages about a raider near another faction. `HELP` and `HELP_FIGHT` use the file of that other faction's race, and `HELP_DESTROYED` the file of the raider's race.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
HELP_FIGHT: [
	"{RACE_CURSE}! {HEC} attacked me! Can you believe that? What did you do to this guy? My army is blooded, the border regions lay in ruins, and it's all because of you! Thanks a bunch, {RACE_INSULT}!",
],
```

## Name files

Each file in `assets/text/race/raider/name/` holds one tag.

### NAMES

The raiders' names, where `{0}` shows the raider's first name.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
NAMES: [
	"{0} the Merciless",
	"{0} the Defiler",
],
```

## Related

- [text/race](00-race.md)
- [init/race: the race file](../../01-init/07-race/01-race-file.md)
