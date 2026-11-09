# init/race/worldcamp

World camps, which the game also calls **havens**, are small independent settlements of one race, scattered across the world map. When you control the region a camp sits in, its people may offer to join you as immigrants, if your kingdom meets their requirements.

Vanilla has camps for its two non-playable races, the Argonosh and the Cantor.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/race/worldcamp/` |
| **Files** | One `.txt` file per type of camp. Vanilla has two: `ARGONOSH.txt` and `CANTOR.txt`. |
| **Key** | The file name without `.txt` |
| **Adding new files** | Yes. Every file in the folder is loaded as a type of camp. |
| **Text file** | `assets/text/race/worldcamp/<KEY>.txt`, which must exist and have the same name. See [The text file](#the-text-file). |
| **Image** | `assets/sprite/race/worldcamp/`, named by `SPRITE` |

## How camps work

**On the world map.** Camps are placed when the world is generated, on open land outside region centres: never on mountains, water or thick forest. Each camp gets a random size between its type's smallest and largest. A camp belongs to whoever controls its region, and the first time you control one, the game tells you.

**Joining you.** Every so often, the game checks each type of camp you control against its requirements:

- Until your kingdom meets **all** of `REQUIRES_MIN`, no one from those camps joins you.
- Once it does, part of the camps' population is willing to join. That share grows, in steps, as your kingdom's values move from the `REQUIRES_MIN` numbers towards the `REQUIRES_MAX` numbers.
- Each time the share rises, the game raises that race's immigration to match, and tells you. The first time, it shows the camp's `JOIN` text. You still need to accept the immigrants.
- If the share drops by more than one step, the game shows the camp's `LEAVE` text. If you stop meeting `REQUIRES_MIN` and fall well short of it, the game tells you that the camps' people are leaving.

The population willing to join is the total population of the camps of that type that you control. How quickly they arrive is set by the camps' replenish rates.

## Tags

The examples below come from the vanilla `ARGONOSH.txt`.

### RACE

The race that lives in the camp.

| | |
|---|---|
| **Type** | Race key |
| **Required** | Yes |

```text
RACE: ARGONOSH,
```

A race key that doesn't exist stops the game from loading with an error that lists the races available.

### SPRITE

The image used for the camp on the world map, by the name of a file in `assets/sprite/race/worldcamp/`. The image must be exactly 132 pixels wide and at least 126 tall. It holds pictures for camps of different sizes, and the game picks one by the camp's size. The simplest way to make one is to copy a vanilla image and paint over it. See [sprite/race/worldcamp](../../03-sprite/07-race/09-worldcamp.md).

| | |
|---|---|
| **Type** | File name, from `assets/sprite/race/worldcamp/` |
| **Required** | Yes |

```text
SPRITE: Argonosh,
```

### COLOR_MASK

A colour the camp's image is tinted with. It takes the same [single-colour forms](06-sprite/00-sprite.md#a-single-colour) as race sprite files. Vanilla uses plain white.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR_MASK: {R:255,G:255,B:255,},
```

### REQUIRES_MIN

What your kingdom must reach before anyone from these camps will join you. It's a condition block in the same format as event conditions (see [Conditions](../05-event/02-occurrence.md#conditions)), and it checks your faction's values.

| | |
|---|---|
| **Type** | Condition block |
| **Required** | No. Without it, the requirement is always met. |

```text
REQUIRES_MIN: {
	GREATER: {
		RELIGION_SHMALOR_F: 0.6,
		FOOD_FOOD_DAYS: 12,
		MONUMENTS_MONUMENT_BLOB: 0.2,
		POPULATION: 500,
		POPULATION_SLAVE_F: 0.1,
	},
	EQUAL: {
		POPULATION_ARGONOSH_SLAVE_F: 0,
	},
},
```

The Argonosh require, among other things, that your kingdom keeps no Argonosh slaves.

### REQUIRES_MAX

The targets that bring the most people from these camps to you. Written in the same way as `REQUIRES_MIN`. For each value, the game measures how far your kingdom has come from its `REQUIRES_MIN` number towards its `REQUIRES_MAX` number, and averages this over all the values.

| | |
|---|---|
| **Type** | Condition block |
| **Required** | No |

```text
REQUIRES_MAX: {
	GREATER: {
		RELIGION_SHMALOR_F: 0.95,
		FOOD_FOOD_DAYS: 20,
		FOOD_FOOD_RATIONS: 0.8,
		RELIGION_TEMPLE: 0.95,
		MONUMENTS_MONUMENT_BLOB: 0.3,
		POPULATION: 5000,
		POPULATION_SLAVE_F: 0.2,
	},
	EQUAL: {
		POPULATION_ARGONOSH_SLAVE_F: 0,
	},
},
```

A value can appear in `REQUIRES_MAX` without being in `REQUIRES_MIN`, like `FOOD_FOOD_RATIONS` above: progress towards it is measured from zero. See [Notes](#notes) for the reverse.

### CAMP_SIZE_FROM and CAMP_SIZE_TO

The population of the smallest and largest camps of this type. Each camp's population is somewhere between the two, set by its random size.

| | |
|---|---|
| **Type** | Integer |
| **Range** | `CAMP_SIZE_FROM` 1 or more; `CAMP_SIZE_TO` at least `CAMP_SIZE_FROM`. The code names a maximum of 1000 for both, but doesn't enforce it. |
| **Required** | Yes |

```text
CAMP_SIZE_FROM: 10,
CAMP_SIZE_TO: 50,
```

### REPLENISH_PER_DAY_FROM and REPLENISH_PER_DAY_TO

How quickly people from the smallest and largest camps of this type arrive as immigrants, per day. Each camp's rate is somewhere between the two, set by its size, in the same way as its population. The rates of all the camps of a race that you control are added together, and scaled by the share willing to join.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | Yes |

```text
REPLENISH_PER_DAY_FROM: 0.25,
REPLENISH_PER_DAY_TO: 0.5,
```

### CLIMATE and TERRAIN

How many camps of this type the world gets, and where they go. Climates are `COLD`, `TEMPERATE` and `HOT`, and terrains are `OCEAN`, `WET`, `MOUNTAIN`, `FOREST` and `NONE` (open land). A climate or terrain left out counts as `0`.

| | |
|---|---|
| **Type** | Blocks of decimals |
| **Range** | `CLIMATE` values 0 to 1; `TERRAIN` values 0 to 100 |
| **Required** | No. Without them, no camps of this type are made. |

```text
CLIMATE: {
	COLD: 0.1,
	TEMPERATE: 0.5,
	HOT: 0.75,
},
TERRAIN: {
	MOUNTAIN: 0.05,
	FOREST: 0.001,
	WET: 0.001,
	NONE: 0.0001,
},
```

When the world is generated, every tile where a camp could go adds its climate's value multiplied by its terrain values to a running total for this type of camp. The total is roughly the number of camps the world gets. A world has a great many tiles, which is why vanilla's values are so small: raising them even a little can fill the map with camps. Tiles with higher values are also more likely to be chosen.

## The text file

Each type of camp needs a text file of the same name in `assets/text/race/worldcamp/`.

| Tag | Meaning | Required |
|---|---|---|
| `NAMES` | Names for the camps, as a list of text. `{0}` is replaced by a surname from the race's [`NAMESET_FILE_NOBLE`](06-sprite/00-sprite.md#nameset_file_noble). The camps of a type take the names in turn, starting again from the top when they run out. At least one. | Yes |
| `JOIN` | The message shown the first time people from these camps decide to join you. | Yes |
| `LEAVE` | The message shown when fewer of them want to join you. | Yes |

From `text/race/worldcamp/ARGONOSH.txt`:

```text
NAMES: [
	"Lair of {0}",
	"Tunnels of {0}",
	"Crypt of {0}",
	"Pits of {0}",
	"Halls of {0}",
	"Nest of {0}",
],

JOIN: "The deadly Argonosh have decided that you are worthy of their presence, given that you promise them manflesh from time to time. Give them access to your dwelling and they shall serve you with their might.",
LEAVE: "The mighty Argonosh are disgusted with how low your kingdom has sunk, and some of them are now leaving your city.",
```

## Notes

- **Put every value in `REQUIRES_MAX`.** A value that appears only in `REQUIRES_MIN` still counts towards the average, but always as no progress at all, so it holds the share of joiners down however well your kingdom does. A condition already met at the `REQUIRES_MIN` number, such as vanilla's `EQUAL` entries that are `0` in both blocks, also counts as no progress.
- **Camps change how a race immigrates.** If any type of camp exists for a race, that race's immigrants arrive only at the speed set by the camps you control, and the usual immigration speed isn't used. Giving camps to a playable race therefore means its immigrants stop arriving unless you control some of its camps.
- Changing a vanilla camp file in your mod [lays it over the vanilla one](../../../02-Getting-Started.md#changing-a-vanilla-file). The requirement, climate and terrain blocks each replace vanilla's whole unless your file uses `_JSON_ADD`.

## Related

- [init/race](00-race.md)
- [The race file](01-race-file.md)
- [init/race/sprite](06-sprite/00-sprite.md)
- [Occurrence and conditions](../05-event/02-occurrence.md)
