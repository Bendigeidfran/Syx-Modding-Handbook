# init/room: spirit rooms

These rooms are for worship and the dead: temples, shrines, graveyards, tombs and the corpse dump. Besides the tags on this page, they use the [common tags](01-common.md), and those with workers use [employment](02-employment.md). Religions themselves are defined in [init/religion](../08-religion.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `GRAVEYARD_*.txt`, `TOMB_*.txt`, `SHRINE_*.txt`, `TEMPLE_*.txt` and `_DUMP_CORPSE.txt` |
| **Adding new rooms** | Yes for graveyards, tombs, shrines and temples. `_DUMP_CORPSE` is a single room. |

## GRAVEYARD

It has exactly four `ITEMS`, in this order: the grave (at least one per room), the tree, the flowers (at least one per room) and the pathway. It has three statistics.

The examples come from the vanilla `GRAVEYARD_NORMAL.txt`.

### PATHWAY

The floor of the graveyard's paths, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
PATHWAY: STONE1,
```

### STANDING

How much this kind of burial matters to subjects. It's in the same format as an entry in a race's [`STATS`](../07-race/03-stats.md#format) block. Unlike a service room's `STANDING`, this one is at the top level of the file.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

```text
STANDING: {
	SLAVE: 0,
	CITIZEN: 1.0,
	NOBLE: 2.5,
	EXPONENT: 0.7,
	PRIO: 25,
},
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `GRAVE_A_TOP_1X1` | The head of an empty grave. | `1x1` |
| `GRAVE_A_BOTTOM_1X1` | The foot of an empty grave. | `1x1` |
| `GRAVE_B_TOP_1X1` | The head of a grave in use. | `1x1` |
| `GRAVE_B_BOTTOM_1X1` | The foot of a grave in use. | `1x1` |
| `TOMBSTONE_1X1` | The tombstone. | `1x1` |
| `TOMBSTONE_RUNE_1X1` | The tombstone of a grave in use. | `1x1` |
| `MON_1X1` | A small tree. | `1x1` |
| `MON_2X2` | A medium tree. | `2x2` |
| `MON_3X3` | A large tree. | `3x3` |
| `FLOWER_COMBO` | The flowers. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## TOMB

It has exactly two `ITEMS`, in this order: the grave (at least one per room) and the statue. It has three statistics.

The examples come from the vanilla `TOMB_NORMAL.txt`.

### STANDING

How much this kind of burial matters to subjects. It's in the same format as an entry in a race's [`STATS`](../07-race/03-stats.md#format) block. Unlike a service room's `STANDING`, this one is at the top level of the file.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

```text
STANDING: {
	CITIZEN: 2.0,
	SLAVE: 0,
	NOBLE: 3,
	PRIO: 5,
},
```

### MONUMENT

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
MONUMENT: MONUMENT_STATUE,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries). Note the lower-case `x` in the `MONUMENT` names.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `HEAD_BOTTOM_1X1` | The head of a grave. | `1x1` |
| `HEAD_TOP_1X1` | The lid at its head. | `1x1` |
| `TAIL_BOTTOM_1X1` | The foot of a grave. | `1x1` |
| `TAIL_TOP_1X1` | The lid at its foot. | `1x1` |
| `STONE_1X1` | The stone. | `1x1` |
| `MONUMENT_1x1` | A small statue. | `1x1` |
| `MONUMENT_2x2` | A medium statue. | `2x2` |
| `MONUMENT_3x3` | A large statue. | `3x3` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## SHRINE

A shrine for one [religion](../08-religion.md). It has no workers. Its need is fixed in the game's code, and its `SERVICE` block only reads `RADIUS`. Its text file only needs `SERVICE.VERB`. It has exactly one `ITEMS` block (at least one per room) and one statistic, for worshippers. The game takes that statistic's name and description from the text file's `STATS`.

The examples come from the vanilla `SHRINE_AMINION.txt`.

### RELIGION

The religion of this shrine, by its key in `assets/init/religion/`.

| | |
|---|---|
| **Type** | Key (a religion) |
| **Required** | Yes |

```text
RELIGION: AMINION,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `ALTAR_FLOOR_TEXTURE` | The floor around the altar. | `texture` |
| `ALTAR_FLOOR_SCRIBBLE1_TEXTURE` | Markings on that floor. | `texture` |
| `ALTAR_FLOOR_SCRIBBLE2_TEXTURE` | More markings on that floor. | `texture` |
| `INNER_BOX` | The inner part of the shrine. | `box` |
| `ALTAR_BOX` | The altar. | `box` |
| `EMBLEM_1X1` | A small emblem. | `1x1` |
| `EMBLEM_2X2` | A large emblem. | `2x2` |
| `TORCH_1X1` | The torches. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## TEMPLE

A temple for one [religion](../08-religion.md). Its need is fixed in the game's code, and its `SERVICE` block only reads `RADIUS`. Its text file only needs `SERVICE.VERB`. Vanilla's temple text files also have a [`RELIGION`](#the-text-file) block, which the game doesn't read. A temple has exactly five `ITEMS`, in this order: the altar, the decorations, the torch, the relief and the pathway.

It has five statistics, in this order: priests, worshippers, decoration, grandeur and space. The game names priests and worshippers itself, so it ignores the `NAME` and `DESC` in their `STATS` blocks, though both blocks must still be there. It takes the names and descriptions of the other three from the text file.

The examples come from the vanilla `TEMPLE_AMINION.txt` unless stated otherwise.

### RELIGION

The religion of this temple, by its key in `assets/init/religion/`.

| | |
|---|---|
| **Type** | Key (a religion) |
| **Required** | Yes |

```text
RELIGION: AMINION,
```

### SACRIFICE_TYPE

What's sacrificed at this temple. Any other value than these stops the game from loading with an error.

The values are:

- `HUMAN`: prisoners;
- `ANIMAL`: livestock, using the `_LIVESTOCK` resource;
- `RESOURCE`: the resource named by `SACRIFICE_RESOURCE`.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
SACRIFICE_TYPE: HUMAN,
```

### SACRIFICE_RESOURCE

The resource sacrificed, by its key, when `SACRIFICE_TYPE` is `RESOURCE`. This example comes from the vanilla `TEMPLE_ATHURI.txt`.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes, when `SACRIFICE_TYPE` is `RESOURCE` |

```text
SACRIFICE_RESOURCE: SITHILON,
```

### SACRIFICE_TIME

How much is used up per day at each sacrifice spot. A fraction works as a chance: `0.1` means one in ten days, on average. Vanilla's values range from `0.1` to `1`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes |

```text
SACRIFICE_TIME: 0.1,
```

### FLOOR_PATH

The floor of the temple's pathway, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR_PATH: STONE_LARGE_DARK,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `PEDISTAL_BOX` | The pedestal. Note the game's spelling. | `box` |
| `ALTAR_BOX` | The altar. | `box` |
| `EMBLEM_1X1` | A small emblem. | `1x1` |
| `EMBLEM_2X2` | A large emblem. | `2x2` |
| `NICHE_A_1X1` | The first part of a niche. | `1x1` |
| `NICHE_B_1X1` | The second part of a niche. | `1x1` |
| `NICHE_C_1X1` | The third part of a niche. | `1x1` |
| `NICHE_D_1X1` | The fourth part of a niche. | `1x1` |
| `TORCH_1X1` | The torches. | `1x1` |
| `COFFIN_A_1X1` | The coffins. | `1x1` |

| Tag | Meaning | Effect |
|---|---|---|
| `COFFIN_B_1X1` | Never read, though vanilla has it. | Unread |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _DUMP_CORPSE

The corpse dump. It has no `ITEMS` or `SPRITES`, and one statistic. Its text file only needs `SERVICE.VERB`, and the `SERVICE` block in vanilla's room file is empty. It has no tags of its own, but it's the only vanilla room that sets [`DEGRADE_RATE`](01-common.md#degrade_rate).

## The text file

Vanilla's temple text files have one extra block at the top level, which the game never reads. The example comes from the vanilla `TEMPLE_ATHURI.txt`.

### RELIGION

A name and description for the temple's religion. The game never reads this block from a room's text file: a religion's own name and description come from its file in [`assets/text/religion/`](../../02-text/11-religion.md).

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
RELIGION: {
	NAME: "Athurism",
	DESC: "Followers of Athuri, the greatest of the Astari. Promotes enlightenment and productivity. His temples accept Sithilon offerings",
},
```

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Employment](02-employment.md)
- [init/religion](../08-religion.md)
