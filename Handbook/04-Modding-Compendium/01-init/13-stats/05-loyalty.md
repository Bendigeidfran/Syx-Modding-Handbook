# init/stats/loyalty

These files set the game's defaults for how much each stat matters to a subject's happiness. A race can then override them for itself in its [`STATS`](../07-race/03-stats.md) block, which explains in full how these values become happiness.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/loyalty/` |
| **Files** | Any number of `.txt` files. Vanilla has one, `VANILLA.txt`. |
| **Adding new files** | Yes. The game reads every file in the folder whose name doesn't start with `_`, in alphabetical order. |
| **Text file** | None |

## Tags

Each entry in a file names a stat and holds the tags below. A name containing `*` applies the entry to every stat whose name contains the text before the `*`. The file's entries can also be wrapped in an outer `STATS` block, which vanilla doesn't do.

This example comes from the vanilla `VANILLA.txt`:

```text
POPULATION_NOBLES: {
	MULTIPLIER: 500,
	CITIZEN: 1.0,
	PRIO: 1.000,
},
```

| Tag | Meaning | Type and range | Required | Default |
|---|---|---|---|---|
| `CITIZEN`, `SLAVE`, `NOBLE` | The most the stat can add for that class. | Decimal, 0 to 1000000 | No | `0` |
| `MULTIPLIER` | Multiplies the stat's value before it's used. | Decimal, 0 to 100000 | No | `1` |
| `EXPONENT` | Applied to the value after `MULTIPLIER`. | Decimal, 0.01 to 10 | No | `1` |
| `INVERTED` | If `true`, the stat counts against subjects: a value of 0 gives the full amount and a value of 1 gives nothing. | True/false | No | `false` |
| `PRIO` | How prominently subjects mention this stat in their opinions. The game drops anything after the decimal point. | Decimal, 0 to 100000 | No | `1` |
| `DISMISS` | If `true`, the stat only ever adds, and never counts against the subject. | True/false | No | `false` |
| `CHILD` | If `true`, children can use this service too. It only applies to service stats. | True/false | No | `false` |

### ICON

Replaces the stat's icon, written as an icon path.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path, or a block |
| **Required** | No |

```text
ICON: 16->Stats->12,
```

## Notes

### An entry replaces the whole default

An entry takes the place of any earlier one for that stat, so anything it leaves out goes back to the defaults above, including `0` for a class. If two files name the same stat, the file later in alphabetical order wins. A stat with an empty entry counts for nothing:

```text
EDUCATION_EDUCATION: {
	
},
```

### Stats with no entry

A stat that no file names keeps what the game's code gives it. For most stats that means it counts for nothing, but some, such as graves, get their values from elsewhere.

### Event stats

This folder doesn't accept the `EVENT_` stats listed under [`bonus`](01-bonus.md#which-stats-can-be-named), and naming one counts as naming a stat that doesn't exist. Other names are looked up as usual, and the first unknown one shows a warning that lists the names available. After that, unknown names are only written to the game's log.

### Unknown tags

The game doesn't check the tags in these entries, so a misspelt tag is silently ignored. That includes `MUL`, which [some vanilla environment files](../12-settlement/01-environment.md#mul) use by mistake for `MULTIPLIER`.

## Related

- [init/stats](00-stats.md)
- [Race stats](../07-race/03-stats.md)
- [init/stats/bonus](01-bonus.md)
