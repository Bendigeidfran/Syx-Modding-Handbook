# init/tech

These files define the player's technology trees. Each file is one tree, which appears as its own tab in the technology screen and lays out its technologies in a grid. A technology can give bonuses, unlock rooms and other things, and be bought over several levels.

Vanilla's files are long because they have hundreds of technologies, but the format itself is small.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/tech/` |
| **Files** | One `.txt` file per tree, e.g. `AGRI.txt` |
| **Key** | A technology's key is the file name, `_` and its name in the tree, e.g. `AGRI_GRAI01` |
| **Adding new trees** | Yes |
| **Text file** | `assets/text/tech/<FILE>.txt`, required |

## Tags

These tags are at the top level of the file, and describe the tree. The examples come from the vanilla `SCIENCE.txt`.

### TREE

The layout of the technology screen, as a block of rows. Each row is a list of technology names, one per column, and a name of exactly `_____` or `______` leaves a gap. Rows appear in the order they're written, so what you call them doesn't matter.

Only technologies listed here exist in the game. A name with no entry in `TECHS` gets a warning and leaves a gap, and a name used twice in one tree stops the game with an error.

| | |
|---|---|
| **Type** | Block of lists |
| **Required** | Yes |

```text
TREE: {
	0: [LAB00,_____,LIB00,ADMI0,_____,_____,_____,],
	1: [LAB01,LABTT,LIB01,ADMI1,ADMIT,_____,_____,],
	2: [LAB02,_____,_____,PAPER,_____,_____,_____,],
	3: [_____,_____,_____,_____,_____,_____,_____,],
	4: [_____,_____,_____,_____,_____,_____,_____,],
},
```

### COLOR

The tree's colour, as `RED_GREEN_BLUE`. Technologies without a `COLOR` of their own use it.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR: 0_205_33,
```

### ICON

The icon on the tree's tab, written as an icon path, a block that combines icons, or a list of blocks.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom. The other forms are described under [`ICON` for technologies](#icon_1).

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | Yes |

```text
ICON: 32->KNOWLEDGE->0,
```

### CATEGORY

Decides the order of the tabs, lowest first.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 5 but doesn't enforce it, and vanilla goes up to 500. |
| **Required** | No. Default `0`. |

```text
CATEGORY: 100,
```

### TECHS

Holds one block for each technology, named as in `TREE`. The tags inside are described below. Without this block, every name in `TREE` gets a warning.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, in practice |

## Technology tags

These tags go inside a technology's block. The examples come from the vanilla `SCIENCE.txt` unless stated otherwise.

### ICON

The technology's icon. Without it, the game builds one from what the technology unlocks or boosts.

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | No |

The simplest form is an icon path: `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`, with the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom. A block is described under [`ICON` on the event page](05-event/01-structure.md#icon). A list draws each entry's `BG` on top of the last, with a small shadow behind each one. This example comes from the vanilla `AGRI.txt`:

```text
ICON: [ 
	{
	BG: 32->BG->3,
	SHADOW: 3,
	
	},
	{
	BG: 24->resource->Grain->0,
	SHADOW: 3,
	
	},
	{
	BG: 32->TECH->0,
	SHADOW: 3,
	
	},
],
```

The game ignores `SHADOW` in a list, and only reads it in the block form. A block draws one icon, optionally with another in front. This example comes from the vanilla `CIVIC.txt`:

```text
ICON: {
	FG: 16->Misc->2,
	BG: 32->BG->8,
	COLOR: 255_100_10,
},
```

| Tag | Meaning | Type and range | Required | Default |
|---|---|---|---|---|
| `BG` | The icon at the back. | Icon path | Yes | |
| `FG` | The icon in front. | Icon path | No | |
| `COLOR` | The colour the icon is tinted with. | Colour | No | White |
| `SCALE` | How many times larger to draw the icons. | Integer, 1 or more. The code's maximum of 8 isn't enforced. | No | `1` |
| `OFFX`, `OFFY` | How far to move `FG`. | Integer, -100 or more. The code's maximum of 100 isn't enforced. | No | `0` |
| `SHADOW` | Any value other than `0` draws a shadow behind the icon in front. The number itself makes no difference. Without `FG`, it's ignored. | Integer, -100 or more. The code's maximum of 100 isn't enforced. | No | `0` |

### LEVEL_MAX

How many levels the technology has.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 10000 but doesn't enforce it. |
| **Required** | No. Default `1`. |

```text
LEVEL_MAX: 2,
```

### LEVEL_COST_INC

How much more each level costs than the one before, added to every currency in `COSTS`. In the example below, levels cost 80 and then 100.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | No. Default `0`. |

```text
LEVEL_COST_INC: 20,
```

### LEVEL_COST_INC_MUL

The game checks for this tag but only writes the technology's key to its log, so it has no effect on the cost. Vanilla doesn't use it.

| | |
|---|---|
| **Type** | Any |
| **Required** | No |
| **Effect** | None |

### COSTS

What the first level costs, by the name of a boost and an amount. Vanilla's technologies use `CIVIC_INNOVATION`, `CIVIC_KNOWLEDGE` and `CIVIC_ADMIN`. A name that doesn't exist stops the game with an error, and the game's message says the boost can't be dynamic, though vanilla's `CIVIC_ADMIN` and `CIVIC_KNOWLEDGE` both come from [`init/stats/dynamicBoost`](13-stats/03-dynamicBoost.md).

Use whole numbers. The game rounds a decimal up when pricing the next level, but drops the decimals when adding up what's already been spent.

| | |
|---|---|
| **Type** | Block of decimals, keyed by boost |
| **Range** | Each value 0 to 10000000 |
| **Required** | Yes. It can be empty. |

```text
COSTS: {
	CIVIC_KNOWLEDGE: 80,
},
```

### REQUIRES

Conditions that must be met to take a level, in the [condition format](05-event/02-occurrence.md#conditions), using faction values. This example comes from the vanilla `BATTLE.txt`.

| | |
|---|---|
| **Type** | Block of conditions |
| **Required** | No |

```text
REQUIRES: {
	GREATERE: {
		POPULATION: 75,
	},
},
```

### REQUIRES_TECH_LEVEL

Other technologies that must reach a given level first, and which the game draws as lines on the tree. Each entry names a technology and the level. A name from the same tree is enough, and one from another tree needs its full key, such as `AGRI_GRAI01`.

A name that doesn't exist gets a warning and is ignored. A loop of requirements stops the game with an error.

| | |
|---|---|
| **Type** | Block of integers, keyed by technology |
| **Range** | Each value 0 or more. The game's code names that technology's `LEVEL_MAX` as the maximum but doesn't enforce it. |
| **Required** | No |

```text
REQUIRES_TECH_LEVEL: {
	ADMI0: 1,
},
```

### UNLOCKS_FACTION

Things that stay locked until the player has at least one level of this technology. The names are the same as for [`UNLOCKS_FACTION` on player levels](06-player/01-level.md#unlocks_faction): rooms, room upgrades, recipes, floors and fortifications. If several things lock the same name, all of them must be met.

| | |
|---|---|
| **Type** | List of names |
| **Required** | No |

```text
UNLOCKS_FACTION: [
	ROOM_ADMIN_NORMAL,
],
```

### UNLOCKS_REGION

Region buildings that stay locked until the player has at least one level, in the same form as [`UNLOCKS_REGION` on player levels](06-player/01-level.md#unlocks_region). This example comes from the vanilla `EMPIRE.txt`.

| | |
|---|---|
| **Type** | List of names |
| **Required** | No |

```text
UNLOCKS_REGION: [
	BUILDING_CIVIC_CENTRE_3,
],
```

### UNLOCKS_HUMAN

The game reads this list, but in v0.71.44 nothing can be locked through it. Vanilla doesn't use it here.

| | |
|---|---|
| **Type** | List of names |
| **Required** | No |
| **Effect** | None |

### BOOST

The bonuses the technology gives, written in the same way as a race's [`BOOST`](07-race/01-race-file.md#boost) block. The value applies **per level**: at level 3, `>ADD: 0.1` adds 0.3. A `>MUL` adds its difference from 1 per level, so `>MUL: 1.1` at level 3 multiplies by 1.3. This example comes from the vanilla `AGRI.txt`.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	ROOM_FARM_GRAIN>ADD: 0.15,
},
```

### COLOR

The technology's colour, as `RED_GREEN_BLUE`. Vanilla doesn't use it on individual technologies.

| | |
|---|---|
| **Type** | Colour |
| **Required** | No. Default is the tree's `COLOR`. |

### AI_AMOUNT

How much this technology's positive boosts count towards the bonus AI factions get from technology, from 0 to 1. AI factions don't research technologies themselves. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `1`. |

## The text file

Each tree needs a file of the same name in `assets/text/tech/`. These examples come from the vanilla `SCIENCE.txt`.

### NAME

The tree's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Science",
```

### TECHS

The name and description of each technology, by its name in the tree. A technology with no entry here is called the tree's name and its position, such as `Science 2:1`, with no description. The block itself must be present if the tree has any technologies, or the game crashes while loading.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `NAME` | The technology's name. | Text | Yes |
| `NAMES` | The plural of its name. If it's missing, `NAME` is used. Vanilla doesn't use it here. | Text | No |
| `DESC` | The technology's description. | Text | Yes |
| `WIKI` | Adds an article to the in-game wiki, as described under [`WIKI` on the init/animal page](01-animal.md#wiki). Vanilla doesn't use it here. | Block | No |

```text
EMBA0: {
	NAME: "Embassy",
	DESC: "Unlocks a place that lets us improve relations with other factions and manipulate their courts.",
},
```

## Notes

### How costs work

Costs aren't spent like money. A currency's total is the current value of its boost, and each level ties up part of that total for as long as the player keeps it. What's left is what's available.

- **Buying** a technology also buys any required technologies the player doesn't have yet, and all of that must be affordable together.
- **Forgetting** a level also removes every technology that depends on it. Half the cost stays frozen for a while before it can be used again.
- **Falling short:** if a currency's total drops below 80% of what's tied up and frozen, technologies that use it take a penalty. Their bonuses shrink, and everything they unlock is locked again until the shortfall is fixed.

### Other factions

Unlocks only hold back the player. AI factions are never locked out by a technology.

### Adding to an existing tree

A new file is the simplest way to add technologies, because it adds a new tree. To add to a vanilla tree, your file has to include `_JSON_ADD`, because `TREE` and `TECHS` are otherwise replaced whole. See [Changing a vanilla file](../../02-Getting-Started.md#changing-a-vanilla-file).

### Misspelt tags

The game checks a technology's block for tags it doesn't know, and writes the first one it finds to its error output. It then stops checking, for the rest of the game, so later mistakes aren't reported.

### Saved games

A saved game stores levels by technology key, so renaming a technology or its file loses the player's levels for it. Levels above a lowered `LEVEL_MAX` are capped.

### A vanilla technology that isn't in its tree

`CIVIC.txt` has a `PLEA1` block that `TREE` doesn't list, so that technology doesn't exist in game.

## Related

- [init](00-init.md)
- [init/stats/dynamicBoost](13-stats/03-dynamicBoost.md)
- [Player levels](06-player/01-level.md)
- [init/room: unlocks](10-room/01-common.md)
