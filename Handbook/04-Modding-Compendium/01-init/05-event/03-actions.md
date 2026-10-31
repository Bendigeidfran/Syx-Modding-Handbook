# Event actions

Actions are what events actually do: give or take resources and money, apply boosts, add or remove subjects, unleash disasters, change other factions' opinion of you, and start other events. This page describes all 22 action types.

## How actions are written

Actions appear in `ACTIONS` lists, inside `ON_SPAWN`, `DURATION`, `CHOICES`, `CONDITION` and `ABORTS` (see [Event structure](01-structure.md)). Each action is a block with a `TYPE` and the settings for that type:

```text
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
```

Two tags work in every action:

| Tag | Meaning | Required |
|---|---|---|
| `TYPE` | Which kind of action this is. | Yes |
| `HIDE_UI` | If `true`, the action isn't listed in the event's message or in a choice's tooltip. | No. Default `false`. |

An unknown `TYPE` produces a warning, and that action is skipped.

### When actions take effect

- Actions in `ON_SPAWN` take effect when the event starts. A few kinds, such as `BOOST`, `WEATHER` and `DESTRUCTION`, keep working for as long as the event lasts.
- Actions in `DURATION`, `CONDITION` and `ABORTS` take effect as the event ends.
- Actions in a choice take effect when the player picks it, which also ends the event.

`ON_SPAWN` can't contain an `EVENT` action; trying to do so stops the game from loading.

### Amounts

Several actions take amounts written as a block with up to three parts, which are added together:

| Tag | Meaning |
|---|---|
| `AMOUNT` | A fixed number. |
| `PER_PERSON` | Multiplied by your total population. |
| `RELATIVE` | Multiplied by a figure that depends on the action, such as how much of the resource you have. Each action says what it uses. |

`PER_PERSON` and `RELATIVE` can each be at most `1000`. Amounts are worked out **when the event starts**, so a message can show the exact figures, even if the action itself takes effect later.

## Events

### EVENT

Starts another event in place of the current one. This is how events are chained together.

| Tag | Meaning | Required |
|---|---|---|
| `EVENT` | The event to start. A name without a file prefix is looked up in the same file first (see [Files and event keys](00-event.md#files-and-event-keys)). | Yes |
| `MESSAGE` | Whether the new event shows its message. | No. Default `true`. |
| `KEEP_TIME` | If `true`, the new event continues the current event's timer instead of starting its own. | No. Default `false`. |
| `CLEAR_CONTEXT` | If `true`, the new event makes its own selection of targets. If `false`, it keeps the current event's selection, so a chain can keep acting on the same subjects or regions. | No. Default `false`. |
| `KEEP_INFO` | If `true`, the game doesn't record the current event as the "previous" event. | No. Default `false`. |

```text
{
	TYPE: EVENT,
	EVENT: FESTIVAL_BIG_YES,
},
```

An event can't start itself directly; the game refuses to load an event whose own actions start it.

## Boosts

### BOOST

A temporary boost that lasts for as long as the event does. The boosts are written in the same way as a race's `BOOST` block.

| Tag | Meaning | Required |
|---|---|---|
| `PLAYER` | Boosts for your whole faction. | No |
| `SUBJECTS` | Boosts for the subjects the event has selected. | No |
| `REGIONS` | Boosts for the regions the event has selected. | No |

```text
{
	TYPE: BOOST,

	PLAYER: {
		ROOM_MINE_COAL>MUL: 3,
	},
},
```

A `BOOST` only has an effect while its own event is running, so it belongs in `ON_SPAWN`. Inside a **choice**, a `BOOST` never takes effect at all. Vanilla uses this deliberately: a choice lists a `BOOST` so the player can see its effects in the choice's tooltip, and starts a follow-up event whose `BOOST_PERM` applies them for real.

### BOOST_PERM

A permanent boost, which stays after the event ends.

| Tag | Meaning | Required |
|---|---|---|
| `BOOST` | The boosts, written as in a race's `BOOST` block. | No, but without it there is nothing to apply. |
| `BOOST_ONLY_PLAYER` | If `true`, the boost goes to your faction only, and the settings below are ignored. | No. Default `false`. |
| `USE_SELECTION_REGIONS` | Apply the boost to the regions the event has selected. | No. Default `true`. |
| `USE_SELECTION_FACTIONS` | Apply the boost to the factions the event has selected. | No. Default `true`. |
| `USE_SELECTION_ROYALTIES` | Apply the boost to the factions of the royals the event has selected. | No. Default `true`. |
| `POPCLS` | A list of population groups to boost, each written as a class and race, such as `CITIZEN_HUMAN`. | No |

From `CIVIC.txt`:

```text
{
	TYPE: BOOST_PERM,
	BOOST_ONLY_PLAYER: true,
	BOOST: {
		RATES_HUNGER>ADD: 0.1,
		BEHAVIOUR_HAPPINESS>ADD: 0.05,
		BEHAVIOUR_LAWFULNESS>ADD: 0.2,
	},
},
```

Each event's permanent boost is stored under that event's key. If the same event runs again, its boost is replaced rather than added a second time.

### BOOST_PERM_REMOVE

Removes permanent boosts that earlier events gave.

| Tag | Meaning | Required |
|---|---|---|
| `EVENTS` | The events whose permanent boosts should be removed. | No, but see the warning below. |

From `REGION.txt`:

```text
{
	TYPE: BOOST_PERM_REMOVE,
	EVENTS: [
		FAMINE_YES,
	],	
},
```

**If `EVENTS` is left out, this action removes every permanent boost that any event has given**, from every region, faction and population group. Always list the events you mean.

A `BOOST_PERM` placed inside a choice is stored under a slightly different key, which this action doesn't match, so it can't be removed this way.

## Money and resources

### CREDITS

Gives or takes money.

| Tag | Meaning | Required |
|---|---|---|
| `AMOUNT`, `PER_PERSON`, `RELATIVE` | How much, as described under [Amounts](#amounts). `RELATIVE` is multiplied by the money you currently have. Negative values take money away. | No |
| `NEGATIVE_ALLOWED` | If `false`, the action can't be carried out when you can't afford it; in a choice, this greys the choice out. | No. Default `true`. |

```text
{
	TYPE: CREDITS,
	PER_PERSON: -20,
},
```

### RESOURCES

Gives or takes resources.

| Tag | Meaning | Required |
|---|---|---|
| `AMOUNTS` | A block of resources, each with an amount block as described under [Amounts](#amounts). `RELATIVE` is multiplied by how much of that resource you own. | No |

The keys in `AMOUNTS` are `RES_` followed by the resource's key, for example `RES_MEAT`. Negative amounts are removed from your stores; positive amounts are delivered to you.

From `CIVIC.txt`:

```text
{
	TYPE: RESOURCES,
	AMOUNTS: {
		RES_OPIATES: {
			PER_PERSON: -0.2,
		},	
		RES_ALCO_BEER: {
			PER_PERSON: -2,
		},	
		RES_FABRIC: {
			PER_PERSON: -1,
		},	
		RES_MUSHROOM: {
			PER_PERSON: -4,
		},	
	},
},
```

## Your population

### SUBJECTS_ADD

Brings new subjects to your settlement, who arrive as immigrants.

| Tag | Meaning | Required |
|---|---|---|
| `AMOUNTS` | A block of races, each with an amount block as described under [Amounts](#amounts). `RELATIVE` is multiplied by how many of that race and type you already have. `*` covers every race. | No |
| `IMMIGRANT_TYPE` | What kind of subject arrives, for example `CITIZEN`. | No |

From `CIVIC.txt`:

```text
{
	TYPE: SUBJECTS_ADD,
	AMOUNTS: {
		*: {
			RELATIVE: 0.005,
		},	
	},
	IMMIGRANT_TYPE: CITIZEN,
},
```

### SUBJECTS_KILL

Removes subjects from your settlement. Despite the name, they don't have to die: the `DEATH_CAUSE` decides how their loss is recorded, and vanilla also uses this action with `EMMIGRATED` for subjects who leave.

| Tag | Meaning | Required |
|---|---|---|
| `DEATH_CAUSE` | The cause recorded for each loss, from the list in [LEAVE_CAUSE.txt](../03-config/08-LEAVE_CAUSE.md). | Yes |
| `AMOUNTS` | A block of races, each with an amount block as described under [Amounts](#amounts). `RELATIVE` is multiplied by that race's population. `*` covers every race. | No |
| `USE_SELECTION` | If `true`, the subjects the event has selected are removed instead, and `AMOUNTS` is ignored. | No. Default `false`. |
| `DAMAGE` | If `true`, subjects are knocked about and injured before they're removed. | No. Default `false`. |
| `SELECTION_FROM` | See below. | No |

From `CIVIC.txt`:

```text
{
	TYPE: SUBJECTS_KILL,
	AMOUNTS: {
		*: {
			RELATIVE: 0.012,
		},	
	},
	DAMAGE: false,
	DEATH_CAUSE: SLAYED,
	USE_SELECTION: false,
},
```

`SELECTION_FROM` appears to be meant to work with a `SELECTION_TO` tag to remove only part of the selection, but the game never reads `SELECTION_TO`. Setting `SELECTION_FROM` makes the range empty, so no one is removed. Leave both out.

### OUTBREAK

Starts an outbreak of a disease in your settlement, in the same way as an epidemic.

| Tag | Meaning | Required |
|---|---|---|
| `DISEASE` | The disease, by its key in [init/disease](../04-disease.md). If it's missing, nothing happens. | No |
| `AMOUNT` | How widely it spreads, used like a disease's `SPREAD`. | Yes |

| | |
|---|---|
| **Range** | `AMOUNT`: 0 to 1 |

From `SLAVES.txt`:

```text
{
	TYPE: OUTBREAK,
	AMOUNT: 0.4,
	DISEASE: PLAGUE,
},
```

### PARDON

Despite its name, this doesn't free prisoners. It cancels the punishments assigned to prisoners, returning them to awaiting punishment in the stocks.

| Tag | Meaning | Required |
|---|---|---|
| `PRISONER_TARGET` | The most prisoners affected. | Yes |
| `USE_SELECTION` | If `true`, only prisoners the event has selected are affected. | No. Default `false`. |

| | |
|---|---|
| **Range** | `PRISONER_TARGET`: 1 or more |

Vanilla doesn't use this action.

### ALTER_SELECTION

Changes the subjects the event has selected. Vanilla doesn't use this action, and in v0.71.44 it doesn't work as intended:

| Tag | Meaning | Required |
|---|---|---|
| `NAME` | Meant to rename the subjects, but always gives them the name "Hotam Greattusk", whatever you write. | No |
| `GENDER` | Sets the subjects' gender. | No |
| `DIRTINESS` | Sets how dirty the subjects are, from 0 to 1. | No |

In addition, **every use of this action resets the selected subjects' age to zero**, whatever tags you give it. Avoid this action until it's fixed.

### REGION_POP

Changes the population of the regions the event has selected.

| Tag | Meaning | Required |
|---|---|---|
| `RACESS` | The races whose population changes. Note the double S: this is the correct spelling. | No |
| `AMOUNT_REL` | A share of each race's current population in the region to add (positive) or remove (negative), from -1 to 1. | No. Default `0`. |
| `AMOUNT_ABS` | A fixed number of each race to add or remove in each region. | No. Default `0`. |

From `REGION.txt`:

```text
{
	TYPE: REGION_POP,
	AMOUNT_REL: -0.3,
	RACESS: [
				HUMAN,
				CRETONIAN,
				TILAPI,
				Q_AMEVIA,
				DONDORIAN,
				GARTHIMI,
			],
	HIDE_UI: true,
},
```

## Other factions

### OPINION

Changes how the royals the event has selected feel about you.

| Tag | Meaning | Required |
|---|---|---|
| `VALUE` | The change in opinion, from -1000 to 1000. | Yes |
| `IS_MUL` | If `true`, `VALUE` multiplies opinion instead of adding to it. | No. Default `false`. |
| `LENGHT_DAYS` | How long the effect lasts, in days. Note the game's spelling. | No. Without it, the effect is permanent. |
| `INCREASE_PER_DAY` | Makes the effect change over time (see below), from -100 to 100. | No. Default `0`. |

How the effect behaves over time depends on these last two tags:

- **Neither:** the full effect, permanently.
- **`LENGHT_DAYS` only:** the full effect for that many days.
- **Negative `INCREASE_PER_DAY`:** the full effect for `LENGHT_DAYS` days, then it fades by that share of its full strength each day.
- **Positive `INCREASE_PER_DAY`:** the effect starts at nothing and grows by that share of its full strength each day, ending after `LENGHT_DAYS` days if that's set.

From `DIPLO.txt`:

```text
{
	TYPE: OPINION,
	VALUE: 2,
	INCREASE_PER_DAY: -0.25,
	IS_MUL: true,
	LENGHT_DAYS: 60,
},
```

### OPINION_REMOVE

Meant to remove opinion effects given by earlier events, listed in an `EVENTS` list.

**Don't use this action.** In v0.71.44 it has a fault that will most likely crash the game when it runs. Vanilla doesn't use it.

## Disasters and the world

### INVASION

Sends raiders against your settlement.

| Tag | Meaning | Required |
|---|---|---|
| `RACE` | The raiders' race. If it's missing, nothing happens. | No |
| `AMOUNT_FROM`, `AMOUNT_TO` | The lowest and highest multipliers for the raiders' strength. The game picks a random value between them. | Yes, both |

| | |
|---|---|
| **Range** | `AMOUNT_FROM`: 0 to 1000. `AMOUNT_TO`: from `AMOUNT_FROM` to 1000. |

The raiders' strength is based on your faction's military power plus the weakest military among the regions they can attack from, multiplied by the chosen value.

From `ARTI.txt`:

```text
{
	TYPE: INVASION,
	AMOUNT_FROM: 2,
	AMOUNT_TO: 2,
	RACE: CANTOR,
},
```

### DESTRUCTION

Causes damage across your settlement for as long as the event lasts. Each value is a rate: how many times per second something happens at a random spot on the map.

| Tag | Meaning | Required |
|---|---|---|
| `DESTRUCTION` | Smashes whatever is on the tile. | No. Default `0`. |
| `DEATH` | Kills any subjects on the tile (recorded as slain). | No. Default `0`. |
| `DEGRADE` | Damages the tile, as vandalism does. | No. Default `0`. |

| | |
|---|---|
| **Range** | Each 0 to 1000 |

From `ARTI.txt`:

```text
{
	TYPE: DESTRUCTION,
	DEATH: 60,
	DESTRUCTION: 30,
},
```

### EARTHQUAKE

Shakes the camera while the event lasts. It has no tags and causes no damage; to damage the settlement, add a `DESTRUCTION` action.

```text
{
	TYPE: EARTHQUAKE,
},
```

### WEATHER

Changes your settlement's weather for as long as the event lasts. Every tag is optional; anything left out is unaffected.

| Tag | Meaning |
|---|---|
| `TEMPERATURE` | The temperature, from -1 (freezing) to 1 (scorching), on the same scale as [TEMP_COLD and TEMP_WARM](../03-config/02-CLIMATE.md#temp_cold-and-temp_warm). |
| `DOWNPOUR` | Rain, from 0 to 1. |
| `WIND` | Wind, from 0 to 1. |
| `LIGHTNING` | Thunder and lightning, from 0 to 1. |
| `CLOUDS` | Cloud cover, from 0 to 1. |
| `SKY` | A colour for the light, written as `RED_GREEN_BLUE`. |

All except `TEMPERATURE` fade in over the event's first ten seconds and fade out over its last ten.

From `ARTI.txt`:

```text
{
	TYPE: WEATHER,
	TEMPERATURE: -0.5,
	SKY: 125_125_125,
},
```

### PASTURE

Kills animals in every pasture of one type.

| Tag | Meaning | Required |
|---|---|---|
| `ROOM` | The pasture room's key, such as `PASTURE_AUR`. If it isn't a pasture, the game shows a warning and the action does nothing. | Yes |
| `ANIMALS_KILLED` | The share of animals killed in each pasture, from 0 to 1. | Yes |

From `ENVIRO.txt`:

```text
{
	TYPE: PASTURE,
	ROOM: PASTURE_AUR,
	ANIMALS_KILLED: 0.5,
},
```

### ORCHARD

Damages orchards of one type. Each orchard hit loses about half its trees. Vanilla doesn't use this action.

| Tag | Meaning | Required |
|---|---|---|
| `ROOM` | The orchard room's key. If it isn't an orchard, the game shows a warning. | Yes |
| `AREA_AFFECTED` | The share of the total orchard area to hit, from 0 to 1. Orchards are picked at random until the area is used up; at least one is always hit. | Yes |

## Appearance and sound

### COLOR

Tints subjects while the event lasts.

| Tag | Meaning | Required |
|---|---|---|
| `COLOR` | The tint, written as `RED_GREEN_BLUE`. | Yes |
| `USE_SELECTION` | If `true`, only the subjects the event has selected are tinted; otherwise everyone is. | No. Default `false`. |

From `SLAVES.txt`:

```text
{
	TYPE: COLOR,
	COLOR: 0_211_255, 
	USE_SELECTION: true,
},
```

### SOUND_AMBIENT

Plays ambient sound while the event lasts. Vanilla doesn't use this action.

| Tag | Meaning | Required |
|---|---|---|
| `AMBIANCE` | The ambient sound, or a list of them, by name. Ambient sounds will be covered in the audio chapter. | No |
| `CITY` | Play the sound while viewing your settlement. | No. Default `true`. |
| `WORLD` | Play the sound while viewing the world map. | No. Default `false`. |

The sound never plays during battles.

## Related

- [init/event](00-event.md)
- [Event structure](01-structure.md)
- [Event text](04-text.md)
