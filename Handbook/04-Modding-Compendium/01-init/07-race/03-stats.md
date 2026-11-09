# Race stats

Every subject has a large set of **stats**: how well furnished their home is, how much space and quiet they have, which services they can reach, how often they see monuments, and many more. For this purpose, each stat is read as a value between 0 and 1.

The `STATS` block in a [race file](01-race-file.md) decides which of these stats matter to the race, and how much, for each class of subject. It's why Human citizens want gems in storage while Garthimi want meat.

## How stats become happiness

Each class adds up its stats differently:

- **Citizens** (called Plebeians in game): the values make up their **fulfilment**, which drives their happiness and loyalty.
- **Slaves**: the values make up their fulfilment in the same way, which drives their submission.
- **Nobles**: the game doesn't calculate a fulfilment for nobles. Their values are only used for a few things, such as which graves they're buried in.

For citizens and slaves, each number in the block is the **most** that stat can add. The game compares what a subject's situation achieves with the total possible, so what matters is how large each number is compared with the others. A stat given `3.5` matters seven times as much as one given `0.5`.

A class can only use a service, such as an eatery or a temple, if its value for that service's stat is above 0. The same applies to the types of grave the dead are buried in. (Nobles can use any service.)

Every race needs at least one stat above 0 for citizens and one for slaves, or the game stops with an error.

## Format

Each entry in the block names a stat and contains these tags:

| Tag | Meaning | Type and range | Default |
|---|---|---|---|
| `CITIZEN`, `SLAVE`, `NOBLE` | The most the stat can add for that class. | Decimal, 0 to 1000000 | `0` |
| `OTHER` | The same value for the game's fourth class, which holds prisoners, tourists, enemies, rioters, the deranged and children. Vanilla never uses it. A value above 0 gives this class permission for the stat's service or grave type. | Decimal, 0 to 1000000 | `0` |
| `MULTIPLIER` | Multiplies the stat's value before it's used. Values above 1 make the stat easier to satisfy fully. | Decimal, 0 to 100000 | `1` |
| `EXPONENT` | Applied to the value after `MULTIPLIER`. Above 1, the stat is harder to satisfy; below 1, easier. | Decimal, 0.01 to 10 | `1` |
| `INVERTED` | If `true`, the stat counts against the race: a value of 0 gives the full amount and a value of 1 gives nothing. | True/false | `false` |
| `PRIO` | How prominently subjects mention this stat when they voice their opinions, together with the class's number. | Decimal, 0 to 100000 | The game's own priority for the stat |
| `DISMISS` | If `true`, the stat only ever adds. It counts towards fulfilment when it's met, but isn't counted in the total possible, so it never counts against the subject. | True/false | `false` |
| `CHILD` | If `true`, children can use this service too, provided their parent's class can. | True/false | `false` |

The value a stat adds works out as: the stat's value, times `MULTIPLIER`, capped at 1, raised to the power of `EXPONENT`, flipped if `INVERTED`, and finally multiplied by the class's number.

From `HUMAN.txt`:

```text
STATS: {


	ACCESS_NOISE: {
		CITIZEN: 0.5,
		INVERTED: true,
	},
	ACCESS_SPACE: {
		CITIZEN: 0.5,
	},

	STORED_GEM: {
		CITIZEN: 1,
		SLAVE: 0,
		NOBLE: 1,
		PRIO: 10,
	},
	MONUMENTS_MONUMENT_SCULPTURE: {
		CITIZEN: 0.5,
		SLAVE: 0.5,
		PRIO: 10,
		MULTIPLIER: 8,
	},
	MONUMENTS_MONUMENT_NATURE: {
		CITIZEN: 0.5,
		SLAVE: 0.5,
		PRIO: 10,
		MULTIPLIER: 8,
	},
},
```

Here, noise counts against Human citizens, space counts for them, and citizens want gems in storage. Monuments need only a small amount (one eighth) of their stat to be fully satisfied.

Any other tag in an entry is ignored.

## Stat names

A stat's name is the name of its group followed by the stat's own name, such as `HOME_FURNITURE`, `SERVICE_COURT` or `MONUMENTS_MONUMENT_SCULPTURE`. Many are built from the keys of other things, like rooms and resources.

The simplest way to find the right name is to let the game tell you. The first time the block uses a name that doesn't exist, the game shows a warning that lists **every name available**. After that, unknown names are only written to the game's log. You can use a deliberately wrong name to get the list, then correct it.

## Notes

### Listing a stat replaces the game's default

The game has its own default for every stat. A stat that isn't in the block keeps that default. A stat that **is** in the block uses only what the entry says, so a class left out of the entry gets `0`.

That means an empty entry switches a stat off for the race entirely. Vanilla does this for the Garthimi, among others:

```text
POPULATION_WRONGFUL_DEATHS: {

},
```

### Wildcards

A name containing `*` applies the entry to every stat whose name contains the text before the `*`, anywhere in the name. Entries are applied in the order they're written, so a later entry overrides an earlier one for the same stat.

From `GARTHIMI.txt`:

```text
ACCESS*: {
	
},
```

This switches off every stat with `ACCESS` in its name. Later in the block, the Garthimi list a few `ACCESS` stats again to switch those back on with their own values.

### Dismissed stats

From `GARTHIMI.txt`:

```text
BATTLE_CHIVALRY: {
	CITIZEN: 1.0,
	SLAVE: 0,
	PRIO: 10,
	DISMISS: true,
	INVERTED: true,
},
```

Because the entry is inverted, Garthimi citizens gain from a **lack** of chivalry. Because it's also dismissed, chivalry never makes them unhappy; a lack of it only makes them happier.

### Multipliers in the warning list

The warning's list of available names includes some multiplier names as well as stats. The race `STATS` block accepts these without an error, but they have no effect there.

## Related

- [init/race](00-race.md)
- [The race file](01-race-file.md)
- [Race preferences](02-preferences.md)
