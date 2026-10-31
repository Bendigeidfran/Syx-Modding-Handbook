# init/race/trait

Traits are personality traits that individual subjects can have, such as Cruel, Lazy or Competent. Each trait gives bonuses or penalties to the subjects who have it, and adds a line about it to their biography. The kings of other factions have traits too, and theirs are shown as titles, such as "The Merciless".

Traits aren't tied to one race. Each trait file sets how common the trait is in every race.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/race/trait/` |
| **Files** | One `.txt` file per trait, e.g. `CRUEL.txt`. Vanilla has 12. |
| **Key** | The file name without `.txt`, e.g. `CRUEL` |
| **Adding new files** | Yes. Every file in the folder is loaded as a trait. |
| **Text file** | `assets/text/race/trait/<KEY>.txt`, which must exist and have the same name. See [The text file](#the-text-file). |

## How traits are given out

When a subject is created, the game goes through every trait in a random order. For each one, the subject gets the trait with the chance set for their race. A subject who gets a trait has it at a random strength between 0 and 1. Any traits it [disables](#disables_others) can't be given to them afterwards.

A trait's bonuses are scaled by its strength: a subject who has a trait at half strength gets half of each bonus. The trait is only mentioned in their biography if its strength is above 0.35.

## Tags

The examples below come from the vanilla `CRUEL.txt` unless stated otherwise.

### BOOST

The trait's bonuses and penalties, in the same form as a race's [`BOOST`](01-race-file.md#boost) block. Each is scaled by how strongly the subject has the trait.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	NOBLE_MERCY>ADD: -1.0,
},
```

From `COMPETENT.txt`:

```text
BOOST: {
	NOBLE_COMPETENCE>ADD: 0.5,
	PHYSICS_SPEED>ADD: 0.1,
},
```

### DEFAULT_RACE_OCCURANCE

The chance, from 0 to 1, that a member of each race has this trait. Keys are race names, and `*` sets every race at once. Entries are applied in the order they're written, so put `*` first and the exceptions after it, as vanilla does (see [Wildcards in blocks keyed by name](01-race-file.md#wildcards-in-blocks-keyed-by-name)). A race left out has no chance of the trait.

Note the spelling: `OCCURANCE`, not `OCCURRENCE`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by race |
| **Range** | Each value 0 to 1 |
| **Required** | No. Without it, no race has the trait. |

```text
DEFAULT_RACE_OCCURANCE: {
	*: 0.3,
	TILAPI: 0.6,
	CRETONIAN: 0.1,
	DONDORIAN: 0.2,
	GARTHIMI: 0.8,
	Q_AMEVIA: 0.1,
	CANTOR: 0.3,
	ARGONOSH: 0.3,
},
```

A race file can override these chances for its own race with a [`TRAIT`](01-race-file.md#traits) block. This is the simplest way to give a new race its own mix of traits without changing the trait files.

### DISABLES_OTHERS

Traits that a subject with this trait can't also have.

| | |
|---|---|
| **Type** | List of trait keys |
| **Required** | No |

```text
DISABLES_OTHERS: [
	MERCIFUL,
],
```

A trait key that doesn't exist stops the game from loading with an error that lists the traits available.

This only works one way. If `CRUEL` disables `MERCIFUL`, a subject who is given `MERCIFUL` first, because of the random order, can still be given `CRUEL` afterwards, unless `MERCIFUL` also disables `CRUEL`. Every vanilla trait is paired with its opposite in both directions: Cruel and Merciful, Lazy and Competent, and so on. When you add an opposing pair, list each in the other's file.

## The text file

Each trait needs a text file of the same name in `assets/text/race/trait/`.

| Tag | Meaning | Required |
|---|---|---|
| `NAME` | The trait's name. | Yes |
| `DESC` | A short description. | Yes |
| `TITLE` | The title shown for a faction king with this trait, such as "The Merciless". | Yes |
| `BIO_DESC` | Lines for the biographies of subjects with the trait, as a list of text. | Yes |

From `text/race/trait/CRUEL.txt`:

```text
NAME: "Cruel",
TITLE: "The Merciless",
DESC: "Rules should be enforced by fear. Opposition should be ruthlessly destroyed.",

BIO_DESC: [
	"{HEC} likes to steal sweets from the children at a nearby nursery.", 
	"{NAME} reserves his empathy for those not in {HIS} way.", 
	"{HEC} is utterly vicious if given the chance.", 
	"Considers the merciful ways of {HIS} kin a weakness.",
	"Is an unusually vicious {RACIAN} specimen.",
],
```

`BIO_DESC` lines can use the same `{…}` placeholders as biography files, such as `{NAME}`, `{HEC}` and `{HIS}`. A race's biography file (its [`BIO_FILE`](01-race-file.md#bio_file)) can replace these lines for that race with a `TRAIT` block of its own, keyed by trait.

## Notes

- Changing a vanilla trait file in your mod [lays it over the vanilla one](../../../02-Getting-Started.md#changing-a-vanilla-file). Because `DEFAULT_RACE_OCCURANCE` is a block, your block replaces vanilla's whole unless your file uses `_JSON_ADD`. To make a vanilla trait possible for a new race, use `_JSON_ADD` and add a line for your race, or set the chance in your race file's `TRAIT` block instead.
- A new trait with no `DEFAULT_RACE_OCCURANCE` block, and no `TRAIT` entry in any race file, is loaded but never given to anyone.

## Related

- [init/race](00-race.md)
- [The race file](01-race-file.md)
