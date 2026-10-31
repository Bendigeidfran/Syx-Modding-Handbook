# init/race/home

A home file decides what a race's homes look like inside: the floor, the beds, tables, chairs, carpets and ornaments, and how they change as the people living there gather resources to furnish them. Each social class has its own set: citizens, nobles and slaves.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/race/home/` |
| **Files** | One `.txt` file per style of home. Vanilla has one for each race, e.g. `HUMAN.txt`. |
| **Key** | The file name without `.txt`. A race file names its home file with [`HOME`](01-race-file.md#home). |
| **Adding new files** | Yes. A home file is only loaded when a race's `HOME` names it, and several races can share one. |
| **Images** | Sprite sheets in `assets/sprite/game/`. See [sprite/game](../../03-sprite/03-game.md). |
| **Text files** | None |

Vanilla's home files don't all match the race names: the Q_Amevia race file uses `HOME: AMEVIA`.

## How furnishing works

Each class lists the furniture its homes can have, and each piece of furniture is a list of versions. Every version names the resources it needs, such as `WOOD: 3` or `FURNITURE: 1`.

Subjects gather resources for their homes, up to limits you can set in the game, and the furniture wears out over time. Each subject keeps their own count of each resource. A house uses the average of its occupants' counts, rounded up. A chamber uses its occupant's.

For each piece of furniture, the game shows the **last version in the list** whose resources the home has. So list versions from plainest to grandest, and start with a version that needs nothing, so that every home shows something.

The resources a class can gather, and how much of each, come from the versions themselves. The game collects every resource named in any version in the class, and takes the largest amount named for each. That is what subjects of that class gather, and it's what the game counts as a fully furnished home: how close a subject is to it is their [`HOME_FURNITURE`](03-stats.md) stat, which vanilla uses for loyalty.

## Tags

The file has one block for each class:

```text
CITIZEN: { ... },
NOBLE: { ... },
SLAVE: { ... },
```

All three are required. Each block holds the tags below. The examples come from the vanilla `HUMAN.txt`.

### Furniture

Each piece of furniture is a list of versions, and each version is a [sprite entry](../../03-sprite/03-game.md#sprite-entries) with a `RESOURCES` block added. Where each piece goes in a home is decided by the home's layout, not by this file. All of these tags are optional: if one is left out, or if the home doesn't have the resources for any of its versions, that piece isn't drawn.

| Tag | Kind of sheet | What it draws |
|---|---|---|
| `BED_1x1_TOP` | `1x1` | One tile of each bed. |
| `BED_1x1_BOTTOM` | `1x1` | The other tile of each bed. |
| `CARPET_COMBO` | `combo` | Carpets, which join up with each other. |
| `TABLE_COMBO` | `combo` | Tables, which join up with each other. |
| `NIGHTSTAND_1x1` | `1x1` | Nightstands. |
| `STORAGE_1x1` | `1x1` | Storage furniture. |
| `CHAIR_1x1` | `1x1` | Chairs. |
| `NICKNACK_A_1x1` | `1x1` | Ornaments. |
| `NICKNACK_A_ONTOP_1x1` | `1x1` | Ornaments drawn on top of each `NICKNACK_A_1x1`. |
| `NICKNACK_B_1x1` | `1x1` | A second kind of ornament. |
| `MAT_1x1` | `1x1` | Mats. |
| `BED_MASTER_2x2` | `2x2` | The bed in a noble's chamber. |
| `STATUE_2x2` | `2x2` | The statue in a noble's chamber. |

The `FRAMES` in each version must point at images of the right kind: a `1x1` piece can only use images from `sprite/game/1x1/`, for example.

Chambers can only be lived in by nobles, so `BED_MASTER_2x2` and `STATUE_2x2` are only used in the `NOBLE` block. Vanilla's `NOBLE` blocks hold only `FLOORS`, `BED_MASTER_2x2` and `STATUE_2x2`.

From the `CITIZEN` block, the first two of four versions of the bed's top tile:

```text
BED_1x1_TOP: [
	{
		RESOURCES: {
			
		},
		FPS: 0,
		SHADOW_LENGTH: 1,
		SHADOW_HEIGHT: 0,
		FRAMES : [
			2xBED: 0,
		],
	},
	{
		RESOURCES: {
			WOOD: 3,
		},
		FPS: 0,
		SHADOW_LENGTH: 2,
		SHADOW_HEIGHT: 0,
		FRAMES : [
			2xBED: 2,
		],
	},
	...
],
```

From the `NOBLE` block:

```text
BED_MASTER_2x2: [
	{
		RESOURCES: {
		
		},
		FPS: 0,
		SHADOW_LENGTH: 4,
		SHADOW_HEIGHT: 4,
		ROTATES: true,
		FRAMES : [
			BEDS: 0,
		],
	},
],
```

### RESOURCES

The resources a home needs for this version, inside each version of each piece of furniture and each floor. Each tag is the key of a resource, and its value is the amount needed.

| | |
|---|---|
| **Type** | Block of resource keys and whole numbers |
| **Range** | 1 or more for each resource. The code names 15 as the maximum, but doesn't enforce it. |
| **Required** | Yes, in every version. It can be empty. |

```text
RESOURCES: {
	WOOD: 3,
},
```

Keep amounts to 15 or less. A subject can only hold up to 15 of each resource for their home, so a version that needs more is never shown.

Across a whole class block, at most **8 different resources** may be named. More than that stops the game from loading with an error. A resource key that doesn't exist produces a warning and is ignored.

### FLOORS

The floor of the home, as a list of versions chosen the same way as furniture. Each version is a block with `RESOURCES` and `FLOOR`.

| Tag | Meaning | Required |
|---|---|---|
| `RESOURCES` | The resources needed, as above. | Yes |
| `FLOOR` | A floor, by the name of a file in `assets/init/settlement/floor/`, such as `DIRT` or `WOOD`. | Yes |

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | No |

```text
FLOORS: [
	{
		RESOURCES: {
		
		},
		FLOOR: DIRT,
	},
	{
		RESOURCES: {
			WOOD: 1,
		},
		FLOOR: WOOD,
	},
],
```

If `FLOORS` is left out, or the home doesn't have the resources for any version, the floor is cleared. A floor name that doesn't exist stops the game from loading with an error that lists the floors available.

## Notes

### Every list counts towards the resources

When the game collects a class's resources, it reads every list in the class block, not only the tags above. A list under a tag the game doesn't draw still adds its resources to what subjects of that class gather. Vanilla `TILAPI.txt` has an empty `CARPET_2x2` list in its `SLAVE` block. The game never draws it, and as it's empty, it has no effect.

### ROTATES

Single-tile furniture in homes always faces the way the home's layout placed it, whatever its `ROTATES` says.

### Changing a vanilla home file

A home file in your mod with the same name as a vanilla one is [laid over it](../../../02-Getting-Started.md#changing-a-vanilla-file). Each class block in your file replaces vanilla's whole, unless your file uses `_JSON_ADD`. For a new race, it's usually simpler to make a new home file with its own name.

## Related

- [init/race](00-race.md)
- [The race file](01-race-file.md)
- [sprite/game](../../03-sprite/03-game.md)
