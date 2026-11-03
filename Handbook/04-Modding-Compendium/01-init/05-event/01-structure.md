# Event structure

Every event is a block of tags. None of the tags is strictly required, but an event needs at least some of them to do anything useful. This page describes each one. When an event can happen is covered separately, in [Occurrence and conditions](02-occurrence.md).

Here is a complete vanilla event, `COAL_GOOD` from `PROD.txt`, which boosts coal mining for eight days:

```text
COAL_GOOD: {
	ICON: {
		BG: 32->BG->4,
		FG: 24->resource->Coal->0,
		SHADOW: 2,
	},
	DURATION: {
		DAYS: 8.0,
	},
	
	OCCURENCE: {
		CLIMATE: {
			*: 1.0,
		},
		TERRAIN: {
			*: 1.0,
		},
		RACE: {
			*: 1.0,
		},
		REQUIRES: {
			GREATER: {
				EMPLOYED_MINE_COAL: 100,
			},
		},
	},
	
	TAGS: {
		ALLOW_NOT: [
			CHAIN_ONGOING,
		],
	},	
	
	ON_SPAWN: {
		ACTIONS: [
			{
				TYPE: BOOST,

				PLAYER: {
					ROOM_MINE_COAL>MUL: 3,
				},
			},
		],
	},
},
```

## Actions

Several tags below contain an `ACTIONS` list: the things that happen at a particular moment, such as giving resources, applying a boost or starting another event. Each action is a block with a `TYPE` and the settings for that type. All the action types are described in [Event actions](03-actions.md).

## Tags

### ICON

The icon shown for the event. If it's missing, the game uses its standard event icon.

The value can be a simple icon path or a block that combines two icons. An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

The tags in a block are:

| Tag | Meaning | Required |
|---|---|---|
| `BG` | The background icon, as an icon path. | Yes |
| `FG` | An icon drawn on top. | No |
| `SHADOW` | Any value other than `0` draws a shadow behind `FG`. The number itself makes no difference. | No. Default `0`. |
| `OFFX`, `OFFY` | Moves the smaller of the two icons sideways or up and down, or `FG` if they're the same size. | No. Default `0`. |
| `SCALE` | Enlarges both icons. | No. Default `1`. |
| `COLOR` | A colour applied to `BG`. Only used when there's no `FG`. | No |

```text
ICON: {
	BG: 32->BG->4,
	FG: 24->resource->Coal->0,
	SHADOW: 2,
},
```

### SHOW_TIME

Whether the event shows how much time it has left. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `true`. |

### DURATION

How long the event lasts, and what happens when it runs out.

| Tag | Meaning | Required |
|---|---|---|
| `DAYS` | How many days the event lasts, from 0 to 1000000. | No. Default `1` if the `DURATION` block is present. |
| `ACTIONS` | What happens when the time runs out. | No |

An event without a `DURATION` block lasts no time at all: it ends as soon as it starts, after its starting actions have taken effect. That leaves the player no time to pick a choice, so any event with `CHOICES` needs a `DURATION`. Every vanilla event with choices has one.

```text
DURATION: {
	DAYS: 8.0,
},
```

When the duration runs out, the game checks the event's `CONDITION`, if it has one. If that condition is met, the condition's actions take effect instead of the duration's.

### ON_SPAWN

What happens when the event starts, as an `ACTIONS` list. These are the event's main effects. Some kinds of action, such as boosts, also keep applying for as long as the event lasts.

```text
ON_SPAWN: {
	ACTIONS: [
		{
			TYPE: BOOST,

			PLAYER: {
				ROOM_MINE_COAL>MUL: 3,
			},
		},
	],
},
```

### CHOICES

Options the player can choose between, shown as buttons in the event's message. Each choice is a block in the list.

| Tag | Meaning | Required |
|---|---|---|
| `ACTIONS` | What happens if the player picks this choice. | No |
| `REQUIRES` | Conditions that must be met for the choice to be available, in the [condition format](02-occurrence.md#conditions). | No |

A choice is shown greyed out, and can't be picked, if its `REQUIRES` isn't met or if one of its actions can't currently be carried out (for example, because you can't afford it). Picking a choice carries out its actions and ends the event.

The labels on the buttons come from the event's text. If the text gives none, an event with one or two choices labels them **Accept** and **Decline**.

From `CIVIC.txt` (shortened):

```text
CHOICES: [
	{
		ACTIONS: [
			{
				TYPE: EVENT,
				EVENT: FESTIVAL_BIG_YES,
			},
			{
				TYPE: CREDITS,
				PER_PERSON: -20,
			},
		],
	},
	...
],
```

Choices only appear in the event's message, so an event with choices also needs message text.

### CONDITION

A condition checked when the event's duration runs out. If it's met at that moment, its actions take effect in place of the duration's. Vanilla doesn't use this tag.

| Tag | Meaning | Required |
|---|---|---|
| `REQUIRES` | The conditions, in the [condition format](02-occurrence.md#conditions). | No |
| `ACTIONS` | What happens if the conditions are met. | No |

### ABORTS

Conditions that end the event early. The game checks them continuously while the event runs. As soon as one is met, its actions take effect and the event ends.

Each entry in the list is a block:

| Tag | Meaning | Required |
|---|---|---|
| `REQUIRES` | The conditions, in the [condition format](02-occurrence.md#conditions). | No |
| `ACTIONS` | What happens when the event is ended this way. | No |

Vanilla's only use of `ABORTS`, in `CIVIC.txt`, lists its actions under `ON_FULFILL` instead of `ACTIONS`:

```text
ABORTS:  [
	{
		ON_FULFILL: [
			{
				TYPE: EVENT,
				EVENT: AMEVIA_DEATHS_YES,
			},
		],
		REQUIRES: {
			GREATER: {
				POPULATION_WRONGFUL_DEATHS: 1,
			},		
		},
	},
],
```

The game doesn't read `ON_FULFILL`, so in v0.71.44 this abort ends the event but starts no follow-up event. Use `ACTIONS` in your own events.

### TAGS

Tags are simple flags, shared by all events, that let events block or allow one another. An event can set or clear tags, and can require tags to be set or not set before it may start.

| Tag | Meaning |
|---|---|
| `ADD` | Tags to switch on when this event starts. |
| `REMOVE` | Tags to switch off when this event ends. |
| `ALLOW` | Tags that must all be on for this event to start. |
| `ALLOW_NOT` | Tags that must all be off for this event to start. |

All four are lists of names, and all are optional. Tag names are your own choice; they don't need to be defined anywhere else.

Vanilla uses this to stop events interrupting a chain. The first event in a chain adds a tag such as `CHAIN_ONGOING`, the last one removes it, and other events list it under `ALLOW_NOT`:

```text
TAGS: {
	ALLOW_NOT: [
		CHAIN_ONGOING,
	],
},
```

### SELECTION

Picks targets for the event's actions: subjects in your settlement, regions, factions, or members of royalty. For example, an event can select a few of your subjects and then act on them.

The block can contain one section for each kind of target: `SUBJECTS`, `REGIONS`, `FACTIONS` and `ROYALTIES`. Each section can contain:

| Tag | Meaning | Required |
|---|---|---|
| `FILTERS` | A list of conditions in the [condition format](02-occurrence.md#conditions). A candidate qualifies if it meets **any one** of them. | No |
| `MIN_AMOUNT` | The fewest targets needed. If fewer candidates qualify, the event can't start. | No. Default `0`. |
| `MAX_AMOUNT` | The most targets to select. | No. Default: no limit. |
| `USE_AS_ICON` | Whether to show the selected target as the event's icon. | No. Default `false`. |
| `MARK` | Marks selected targets so later events can find them again (see below). | No |

The block can also contain an `ON_FAIL` block with an `ACTIONS` list. The game reads it, but in v0.71.44 never uses it, so it has no effect.

The game selects targets at random from the qualifying candidates, up to the maximum.

#### Amounts

`MIN_AMOUNT` and `MAX_AMOUNT` are blocks that add up to a number:

| Tag | Meaning |
|---|---|
| `AMOUNT` | A fixed number. |
| `PER_PERSON` | Multiplied by your population (for `SUBJECTS`) or by the total number of candidates (for the others). |
| `RELATIVE` | Multiplied by the number of candidates that qualify. |

The parts are added together and rounded up.

#### Marks

`MARK` lets a chain of events keep working with the same targets. It can contain:

| Tag | Meaning |
|---|---|
| `MARK_WITH_EVENT_KEY` | If `true`, the selected targets are marked with this event's key. |
| `ALLOW_ONLY_MARK` | Only select targets marked by the event with this key. |
| `CLEAR_EVENT_KEY` | Remove the marks left by the event with this key. |

These must use the event's **full** key, including the file name: `REGION_STARVATION`, not `STARVATION`.

From `REGION.txt`:

```text
SELECTION: {
	ROYALTIES: {
		MAX_AMOUNT: {
			AMOUNT: 1.0,
		},
		MIN_AMOUNT: {
			AMOUNT: 1.0,
		},
		
		USE_AS_ICON: false,
		
		FILTERS: [
			{
				GREATER: {
					FACTION_POPULATION: 0,
					FACTION_PLAYER_REACHABLE: 0,
					SUCCESSION_ORDER_0: 0,
				},
				LESS: {
					FACTION_STANCE_WAR: 1,
				},
			},
		],
		MARK: {
			  MARK_WITH_EVENT_KEY: true,
		},	
	},	
},
```

This selects exactly one member of royalty, from a reachable faction that isn't at war with you, and marks them so a follow-up event can find them.

## Related

- [init/event](00-event.md)
- [Occurrence and conditions](02-occurrence.md)
