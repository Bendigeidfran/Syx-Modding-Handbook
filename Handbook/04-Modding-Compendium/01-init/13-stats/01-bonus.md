# init/stats/bonus

These files tie bonuses and penalties to a stat. They're why combat experience makes a soldier fight better, and why handouts raise a subject's loyalty.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/bonus/` |
| **Files** | Any number of `.txt` files. Vanilla has one, `VANILLA.txt`. |
| **Adding new files** | Yes. The game reads every file in the folder whose name doesn't start with `_`. |
| **Text file** | None |

## File format

Each entry in a file names a stat and holds a block of boosts, written in the same way as a race's [`BOOST`](../07-race/01-race-file.md#boost) block: a boost name, then `>MUL` or `>ADD`, then a value. A line without `>MUL` or `>ADD` stops the game with an error.

This example comes from the vanilla `VANILLA.txt`:

```text
BATTLE_COMBAT_EXPERIENCE: {
	BATTLE_OFFENCE_SKILL>ADD: 1.0,
	BATTLE_DEFENCE_SKILL>ADD: 1.0,
	BATTLE_MORALE>ADD: 2.0,
},
```

The file's entries can also be wrapped in an outer `STATS` block. Vanilla doesn't do this.

### How strong a bonus is

The value is what the bonus reaches when the stat is at its full value of 1, and the bonus scales with the stat on the way there. At a stat value of 0, an `>ADD` adds nothing and a `>MUL` multiplies by 1, which also changes nothing.

For example, `BATTLE_MORALE>ADD: 2.0` above adds 1 morale to a soldier halfway to the most combat experience. A `>MUL` below 1 is a penalty, like this one from the same file:

```text
ENVIRONMENT_UNBURRIED: {
	PHYSICS_HEALTH>MUL: 0.25,
},
```

### Which stats can be named

Besides ordinary stats, this folder also accepts six event stats that [`loyalty`](05-loyalty.md#event-stats) doesn't: `EVENT_PROSECUTION`, `EVENT_HANDOUT`, `EVENT_DAY_OFF`, `EVENT_SLAVES_FREED`, `EVENT_SERIAL_KILLER` and `EVENT_OVERTIME`.

A stat name containing `*` applies its entry to every stat whose name contains the text before the `*`.

The first time a file names a stat or a boost that doesn't exist, the game shows a warning listing the names available. After that, an unknown stat is only written to the game's log, and so is an unknown boost. The stat and boost warnings are separate, so you can get one of each.

## Notes

### Several files add together

Each entry adds its bonuses to whatever the stat already has. A new file in this folder therefore adds to vanilla's bonuses. It can't remove them: to change a value in `VANILLA.txt`, use a file of that same name, as described under [Changing a vanilla file](../../../02-Getting-Started.md#changing-a-vanilla-file).

### Other sources of the same bonus

[Equipment](04-equip/00-equip.md) and [environment effects](../12-settlement/01-environment.md#boost) carry `BOOST` blocks of their own, so they don't need an entry here.

## Related

- [init/stats](00-stats.md)
- [init/stats/loyalty](05-loyalty.md)
- [BOOST in the race file](../07-race/01-race-file.md#boost)
