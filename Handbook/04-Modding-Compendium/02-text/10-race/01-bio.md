# text/race/bio

These files hold what you read when you inspect a subject: their biography, and the opinions they have about your rule. A race names one with [`BIO_FILE`](../../01-init/07-race/01-race-file.md#bio_file), and can add a second with [`BIO_FILE_SPECIFIC`](../../01-init/07-race/01-race-file.md#bio_file_specific).

## At a glance

| | |
|---|---|
| **Location** | `assets/text/race/bio/` |
| **Files** | One `.txt` file per biography set, e.g. `Normal.txt`, plus race-specific files in `specific/`, e.g. `specific/Human.txt` |
| **Adding new files** | Yes. A race file must name it. |
| **Layering** | None. Unlike most files, your file replaces the vanilla one whole. |

## Specific files

A file in `specific/` uses the same tags. A line it has replaces the same line from `BIO_FILE`, and anything it leaves out comes from there. A trait it doesn't list gets the lines from both. Its `TRAIT`, `STATS_MORE` and `STATS_LESS` blocks must still be present, even if empty, as they are in vanilla's `specific/Human.txt`.

## Tags

Each biography line is a list of text, and a subject always gets the same pick from the list. A line that's missing or empty is left out.

If a line uses a placeholder the game doesn't know, it shows a warning naming it, and the first such warning also lists the placeholders available. [Event text](../../01-init/05-event/04-text.md#placeholders) explains how placeholders work. The placeholders here cover the subject, with their friend under `FRIEND_` and the player's faction under `FACTION`.

### Biography lines

The examples come from the vanilla `Normal.txt`.

| Tag | Shown for | Type and range | Required |
|---|---|---|---|
| `INFO_OTHER` | Subjects who aren't yours. | List of text | No |
| `INFO_GENERAL`, `INFO_TITLE`, `INFO_GENERAL2`, `INFO_GENERAL3` | Your subjects, joined up as the start of the biography. | List of text | No |
| `ORIGIN_NATIVE`, `ORIGIN_IMMI`, `ORIGIN_FREED`, `ORIGIN_PAROLE`, `ORIGIN_SOLDIER`, `ORIGIN_INSANE` | Citizens, by how they arrived: born here, immigrated, freed, paroled, returned from soldiering or cured of insanity. | List of text | No |
| `HOME`, `HOME_ALONE` | Those with a home, shared or alone. | List of text | No |
| `HOME_NONE_WORK`, `HOME_NONE`, `HOME_NONE_SEARCH` | Those without a home, who have a job, have no job, or haven't looked yet. | List of text | No |
| `DIVISION`, `DIVISION_RECRUIT`, `DIVISION_NONE` | Soldiers, recruits and everyone else. | List of text | No |
| `WORK_NOBLE`, `WORK_EMPLOYED`, `WORK_UNEMPLOYED`, `WORK_LEISURE` | Nobles, the employed, the unemployed and those off work. | List of text | No |
| `FRIEND`, `FRIEND_ENEMY`, `FRIEND_OTHER` | Those with a friend of a race they like, of a race they don't, or an animal. | List of text | No |
| `DREAMS` | Your subjects. | List of text | No |
| `DREAMS_CHILD`, `DREAMS_CRIMINAL`, `DREAMS_ENEMY`, `DREAMS_RIOTEER`, `DREAMS_INSANE`, `DREAMS_SLAVE` | Children, prisoners, enemies, rioters, the deranged and slaves. | List of text | No |

```text
INFO_TITLE: [
	"proudly serving you as a {TITLE}.",
],
```

### HOME_NOBLE

The game never reads this tag, because the code that used it is commented out.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |
| **Effect** | Unread |

### TRAIT

Biography lines for subjects with a trait, as a block of lists keyed by trait. A trait left out uses its own [`BIO_DESC`](../../01-init/07-race/07-trait.md). The block must be present, and vanilla's `Normal.txt` leaves it empty.

| | |
|---|---|
| **Type** | Block of lists, keyed by trait |
| **Required** | Yes |

```text
TRAIT: {

},
```

### HAPPY, HAPPY_SOSO and HAPPY_NO

The heading above a subject's demands, by how content they are: `HAPPY` above 0.95, `HAPPY_SOSO` above 0.8, and `HAPPY_NO` for anything lower. Without one, there's no heading.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

```text
HAPPY: [
	"Pleased with the city. Demands:",
],
```

### FUNNY

Lines used in place of a demand, for about one subject in 32. Keep at least one, because an empty list crashes the game when it tries to pick one.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 or more |
| **Required** | Yes |

```text
FUNNY: [
	"Show the gods more respect. Straighten your back, chin up.",
],
```

### NOTHING

Meant for a subject with no demands. Unverified: the code's check for this appears never to be true, so this line may never show. Keep at least one, as with `FUNNY`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
NOTHING: [
	"For the time being, nothing.",
],
```

### STATS_MORE and STATS_LESS

What subjects say when they want more or less of a stat, as a block of lists keyed by [stat](../../01-init/13-stats/00-stats.md#stat-names). `*` in a name works as it does for [race stats](../../01-init/07-race/03-stats.md#wildcards). A stat left out uses its [`MORE` or `LESS`](../../01-init/13-stats/07-NAMES.md#more) from `NAMES.txt`. Both blocks must be present.

| | |
|---|---|
| **Type** | Block of lists, keyed by stat |
| **Required** | Yes |

```text
BURIAL_DESECRATION: [
	"Stop the desecration of the dead.",
],
```

## Related

- [text/race](00-race.md)
- [init/race/trait](../../01-init/07-race/07-trait.md)
- [text/stats/NAMES.txt](../../01-init/13-stats/07-NAMES.md)
