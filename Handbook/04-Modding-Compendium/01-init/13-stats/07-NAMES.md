# text/stats/NAMES.txt

This file holds the names and descriptions of most stats, along with what subjects say about them. It sits in the text folder rather than in `init/stats`, but this chapter is where its keys come from.

Each entry is named after a stat's key, and adding an entry doesn't create a new stat.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/stats/NAMES.txt` |
| **Files** | This one file |
| **Key** | The stat's key, e.g. `BURIAL_DESECRATION` |
| **Adding new files** | No. Only this file is read. |

## Tags

The examples come from the vanilla entries for `EVENT_HANDOUT` and `BURIAL_DESECRATION`. A stat that gets its name from this file must have an entry, or the game stops with an error.

### NAME

The stat's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Handouts",
```

### NAMES

The plural of the stat's name. Vanilla doesn't use it here.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

### DESC

The stat's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Handouts are 400 Denari in cash that have been handed out to a subject.",
```

### WIKI

Adds an article about the stat to the in-game wiki. Vanilla doesn't use it here. The tags inside it are described under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

### VERB

The word for the action, shown in the decree and subject menus. Only the `EVENT_` stats listed under [`bonus`](01-bonus.md#which-stats-can-be-named) read it, and they must have it, though it can be empty.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, for those stats |

```text
VERB: "Handout",
```

### MORE

Things subjects say when they want more of this stat, as a list of text. Without it, the game uses a short line of its own. The example is shortened.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

```text
MORE: [
	"Stop the desecration of our dead. Let {RACES} rest in peace!",
],
```

### LESS

Things subjects say when they want less of this stat, in the same form as `MORE`. Without it, the game uses a short line of its own. This shortened example comes from the vanilla entry for `EDUCATION_EDUCATION`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

```text
LESS: [
	"Education is foreign to our way of life and usually unsuited to our favorite work.",
],
```

## Notes

### Entries the game doesn't read

Some stats get their name from elsewhere, so their entries here aren't read. Vanilla has entries for `EQUIP_CIVIC_CLOTHES` and `EQUIP_CIVIC_JEWELRY`, which take their names from the resource, and for `BATTLE_BARRACKS_VANILLA`, `BATTLE_ARCHERY_VANILLA`, `BURIAL_GRAVEYARD_NORMAL` and `BURIAL_TOMB_NORMAL`, which take theirs from the room.

## Related

- [init/stats](00-stats.md)
- [init/stats/bonus](01-bonus.md)
- [init/stats/loyalty](05-loyalty.md)
