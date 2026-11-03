# init/world/building

These files define the buildings you can put up in the regions you hold. Each sub-folder is a category, such as `civic` or `military`, with its own place in the region's building list.

A category holds three kinds of file: `_CAT.txt` describes the category, a normal file defines one building, and `_GEN.txt` generates a building from each of a list of rooms. Vanilla's farms, mines and temples come from `_GEN.txt`.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/world/building/*/`, where `*` is the category's folder |
| **Files** | One `.txt` file per building, e.g. `civic/HYGINE.txt`, plus `_CAT.txt` and an optional `_GEN.txt` in each category |
| **Key** | The category in capitals, `_` and the file name, e.g. `CIVIC_HYGINE` |
| **Adding new buildings** | Yes |
| **Adding new categories** | Yes. A new folder needs a `_CAT.txt`. |
| **Text file** | `assets/text/world/building/<category>/<FILE>.txt`, required for normal files |

## Tags

These tags are at the top level of a normal building file. The examples come from the vanilla `civic/CENTRE.txt`.

### ORDER

Where the building goes in its category. Buildings are sorted as text, so `10` comes before `2`.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. Without it, the building sorts first. |

```text
ORDER: 0,
```

### AI_BUILDS

Whether AI factions build this.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `true`. |

```text
AI_BUILDS: true,
```

### NOTIFY_WHEN_UPGRADABLE

Despite its name, this makes the region show a problem when the building's efficiency is below 1, naming the building. Vanilla only uses it for `CENTRE`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
NOTIFY_WHEN_UPGRADABLE: true,
```

### LEVELS

The building's levels, in order, each in a block of its own. A region can hold one level of each building.

| | |
|---|---|
| **Type** | List of blocks |
| **Range** | 1 to 9 levels |
| **Required** | Yes |

## Level tags

These tags go inside each block in `LEVELS`.

### ICON

The level's icon. It can be written in any of the forms described under [`ICON` for technologies](../14-tech.md#icon_1).

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | Yes |

```text
ICON: 32->world->CENTRE->0,
```

### CREDITS

The total price of the building at this level. Upgrading costs the difference from the current level.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 1000000 but doesn't enforce it. |
| **Required** | No. Default `0`. |

```text
CREDITS: 500,
```

### REQUIRES

Conditions that must be met to build this level, in the [condition format](../05-event/02-occurrence.md#conditions), using region values. In the player's regions, the building also stops working if they stop being met. This example comes from the vanilla `global/WGUILD.txt`, and limits how many a kingdom can have.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No |

```text
REQUIRES: {
	LESS: {
		BUILDING_GLOBAL_WGUILD_KINGDOM: 4,
	},
},
```

### BOOST

What the building does in its own region, written in the same way as a race's [`BOOST`](../07-race/01-race-file.md#boost) block. Only the current level's block applies, so each level states its full effect. Bonuses scale with the building's efficiency, while running costs always apply in full.

A line that lowers a [point](03-point.md) is a running cost, and the region must have enough to spare when building. `BOOST_GLOBAL` lines are checked in the same way. This example comes from the vanilla `civic/HYGINE.txt`.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	WORLD_POINT_WORKFORCE>ADD: -5,
	WORLD_HEALTH>ADD: 1,
	WORLD_POPULATION_CAPACITY>ADD: 2, 
},
```

### BOOST_GLOBAL

The same as `BOOST`, but applied across the whole realm. Naming the boost `ADMIN` stops the game with an error.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST_GLOBAL: {
	CIVIC_GOV>ADD: -5,
},
```

## _CAT.txt

Every category folder needs this file. The examples come from the vanilla `civic/_CAT.txt`.

### COLOR

The category's colour, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR: 100_100_150,
```

### ORDER

Where the category goes in the list, lowest first.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 10000000 but doesn't enforce it. |
| **Required** | No. Default `0`. |

```text
ORDER: 0,
```

## _GEN.txt

This optional file generates buildings from rooms, so it needs no text file: the name comes from the room, and the description lists what it produces. The file holds a `GENS` list, where each block creates one building for each room it names. The key is the category, `_` and the room's key without any leading `_`, such as `AGRICULTURE_FARM_GRAIN`.

The examples come from the vanilla `agriculture/_GEN.txt` unless stated otherwise.

### INDUSTRIES

The rooms to make buildings from, by key. A `*` at the end of a name covers every room whose key begins with what comes before it. An unknown name stops the game with an error.

Only temples and rooms with an industry make a building, and other rooms are skipped. Unverified: a room that has no industries, or whose first industry produces nothing, logs an error and then probably crashes the game.

| | |
|---|---|
| **Type** | List of room keys |
| **Required** | No. Without it, the block makes nothing. |

```text
INDUSTRIES: [
	ORCHARD*,
],
```

### LEVELS

How many levels each building has. Temples ignore this and always have five levels: two named after the shrine and three after the temple.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 10 but doesn't enforce it. |
| **Required** | Yes, except for temples |

```text
LEVELS: 10,
```

### OUTPUT

How much the top level produces, multiplied by the rate of each resource in the room's first industry. Each level gives its share of that, so level 5 of 10 gives half. Temples don't read this tag.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | Yes, except for temples |

```text
OUTPUT: 400,
```

### CREDITS

Sets the price of the top level, which is this value times 400. Lower levels pay a share, proportional to their level for most buildings. For temples, that share is squared, so level 1 of 5 costs a twenty-fifth.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more |
| **Required** | Yes |

```text
CREDITS: 1000,
```

### YEARLY

If `true`, the building's output counts towards the yearly part of the region's output, instead of the regular part. Vanilla uses it for farms and orchards.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
YEARLY: true,
```

### BOOST

Effects for the top level, written in the same way as a race's [`BOOST`](../07-race/01-race-file.md#boost) block. Each level gets its share, so level 5 of 10 gets half. For temples, each share is rounded down to a whole number.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	WORLD_POINT_WORKFORCE>ADD: -50,
},
```

### EFFICIENCY

The game no longer reads this block, because the code that read it is commented out, so the values in vanilla do nothing. A generated building instead takes its efficiency from the region's prospect for the room's first industry, if it has one, and from the race and climate bonuses to the room.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
EFFICIENCY: {
	PROSPECT: [0.8,0.4,],
	BOOST: {
		PROP_FERTILTIY: [0, 1.2,],
	},
},
```

## The text file

Each normal building needs a file of the same name in the matching category of `assets/text/world/building/`. These examples come from the vanilla `infra/ROAD.txt`.

### NAME

The building's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Roads",
```

### NAMES

The plural of the building's name. Vanilla doesn't use it here.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

### DESC

The building's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Roads ease the penalty your territories face the further they are from your capital. They also decrease the toll you pay when trading.",
```

### LEVELS

The name of each level, in order. A level with no entry is called the building's name and a numeral, such as `Roads: II`.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

```text
LEVELS: [
	"Dirt roads",
	"Roads",
	"Paved Roads",
	"Highways",
	"Royal Highways",
],
```

### WIKI

Adds an article about the building to the in-game wiki. Vanilla doesn't use it here. The tags inside it are described under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

## Notes

### Names built from the key

Each building creates several names that other files can use. Using `CIVIC_HYGINE` as the example:

| Name | What it is |
|---|---|
| `WORLD_BUILDING_CIVIC_HYGINE` | A boost for the building's efficiency, which starts at 1. Vanilla raises it with lines like `WORLD_BUILDING_MINE*>MUL: 1.25,`. |
| `BUILDING_CIVIC_HYGINE_1` | The first level, for [`UNLOCKS_REGION`](../06-player/01-level.md#unlocks_region) lists. A generated temple uses its religion's key here instead of the room's. |
| `BUILDING_CIVIC_HYGINE_LEVEL` | A region value holding the building's level in the region. |
| `BUILDING_CIVIC_HYGINE_KINGDOM` | A region value counting these buildings in the region's realm. |

Races can adjust how much a building affects them with [`WORLD_BUILDING`](../07-race/02-preferences.md#world_building), which uses the key itself.

### What lowers efficiency

In the player's regions, efficiency drops to 0 while a level's `REQUIRES` isn't met, and falls as the region runs short of a point the building uses.

## Related

- [init/world](00-world.md)
- [init/world/point](03-point.md)
- [init/room](../10-room/00-room.md)
- [init/tech](../14-tech.md)
