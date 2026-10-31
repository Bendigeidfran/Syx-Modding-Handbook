# init/event

The `init/event` folder holds the game's events: the festivals, discoveries, disasters, diplomatic incidents and other happenings that interrupt the running of your settlement. Events are written in a small scripting format of their own. Each event says when it can happen, what it does, how long it lasts, what choices it offers, and what happens when it ends.

Because the format is large, it's covered over several pages:

- this page explains how events work overall, how the files are organised, and the `_CONFIG.txt` settings;
- [Event structure](01-structure.md) covers the tags that make up an event;
- [Occurrence and conditions](02-occurrence.md) covers when an event can happen, and the condition format used throughout events.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/event/` |
| **Files** | Any number of `.txt` files, each holding any number of events. Vanilla groups its events by theme: `ARTI`, `CIVIC`, `DIPLO`, `EARLY`, `ENVIRO`, `HINT`, `PROD`, `REGION`, `RELIGION`, `SLAVES` and `TEST`. There's also `_CONFIG.txt`. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded, and its events are added to the pool. |
| **Text files** | `assets/text/event/<FILE>.txt`, with the same name as the event file. Optional. |

## Files and event keys

Each event file is a list of events. Every top-level block in the file is one event:

```text
COAL_GOOD: {
	ICON: { ... },
	DURATION: { ... },
	OCCURENCE: { ... },
	TAGS: { ... },
	ON_SPAWN: { ... },
},

CLAY_GOOD: {
	...
},
```

An event's full **key** is the file name, an underscore, and the block's name. The `COAL_GOOD` block in `PROD.txt` has the key `PROD_COAL_GOOD`.

When one event refers to another, for example to start it, the game first looks for the name exactly as written, then tries it with the current file's name in front. So inside `CIVIC.txt`, `FESTIVAL_BIG_YES` finds `CIVIC_FESTIVAL_BIG_YES`. To refer to an event in a different file, use its full key.

The file name is only a prefix. You can split your events across as many files as you like, and a mod can add events by adding a new file, without changing any of the vanilla ones.

A mod file with the same name as a vanilla event file is [laid over it](../../../02-Getting-Started.md#changing-a-vanilla-file). Each block in your file replaces the vanilla event of the same name, and the vanilla events you don't mention are kept. To change one vanilla event, your `PROD.txt` only needs that event's block. Don't put `_JSON_ADD` or `_ARRAY_ADD` in an event file: the game reads every top-level tag as an event, and stops with an error when it reaches one that isn't a block.

## How events run

Only one event can be active at a time. The game's event system works in a cycle:

1. **Eligibility.** Every event is regularly checked to see whether it could happen now: its conditions must be met, it mustn't have reached its spawn limit, enough time must have passed since it last happened, and its tags must allow it. See [Occurrence and conditions](02-occurrence.md).
2. **Building up.** Each eligible event gains weight over time, at a rate set by its occurrence values. Events that are likely in your settlement build up faster.
3. **Starting.** When it's time for a new event and none is running, the game tries the events with the most weight built up, starting with the highest. An event can still fail to start if it needs to select something, such as a number of subjects, and can't find enough. Once an event starts, its built-up weight resets to zero.
4. **Running.** The event's starting actions take effect, and if it has message text, a message appears with any choices. While it runs, the game watches for anything that should end it early.
5. **Ending.** The event ends when the player makes a choice, when an early-ending condition is met, or when its duration runs out. Whatever ends it, the matching actions take effect, and those can start another event, letting you chain events together.

An event with no occurrence settings never builds up weight, so it never starts on its own. It only happens when another event starts it. Vanilla uses this for the follow-up events in its chains.

## _CONFIG.txt

`_CONFIG.txt` sets how often the game tries to start a new event. Because its name starts with an underscore, it isn't read as an event file.

```text
DAYS_BETWEEN_EVENTS_POP_0: 64,
DAYS_BETWEEN_EVENTS_POP_5000: 8,
```

### DAYS_BETWEEN_EVENTS_POP_0

How many days pass between events when your settlement has no population.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

### DAYS_BETWEEN_EVENTS_POP_5000

How many days pass between events in a large settlement.

Despite the name, this value is reached at a population of **10,000**, not 5,000. Between no population and 10,000, the rate of events rises steadily from one setting to the other, so at 5,000 subjects it's halfway between them.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

## Notes

### Mistakes in event files

The game is forgiving about some mistakes in event files and strict about others, so it's worth testing new events with the launcher's **Debug** option turned on:

- A tag the event format doesn't recognise is noted in the game's error output and otherwise ignored. The event still loads, but the tag does nothing.
- A reference to an event that doesn't exist is logged as an error, and the reference is dropped.
- An unknown value in a condition produces a warning on screen, and the condition no longer works as written.
- A mistake in the basic syntax, such as a missing comma, stops the game from loading, as in any other file.

### The text files

An event file's messages, names and choice labels come from the text file of the same name in `assets/text/event/`. Each event has its own block there, under the same name as in the event file. An event without text shows no message. See [Event text](04-text.md).

## Sections

- [Event structure](01-structure.md)
- [Occurrence and conditions](02-occurrence.md)
- [Event actions](03-actions.md)
- [Event text](04-text.md)

## Related

- [init](../00-init.md)
