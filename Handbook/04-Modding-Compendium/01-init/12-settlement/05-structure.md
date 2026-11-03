# init/settlement/structure

These files define the materials buildings are made of, such as wood and stone. A structure sets what its walls and ceilings cost, how long they take to build, how strong they are and how they look. It also sets how much each race likes it by default.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/settlement/structure/` |
| **Files** | One `.txt` file per structure, e.g. `WOOD.txt`, plus `_MUD.txt`, `_MOUNTAIN.txt` and `_OUTDOORS.txt` |
| **Key** | The file name, e.g. `WOOD` |
| **Adding new structures** | Yes |
| **Text file** | `assets/text/settlement/structure/<KEY>.txt`, required |
| **Sprites** | Images in `assets/sprite/settlement/structure/`, named by `SPRITE` |
| **Sound** | A `BUILD_STRUCTURE_<KEY>` entry in a file in `assets/audio/config/mono/` |

## Tags

The examples come from the vanilla `WOOD.txt`.

### SPRITE

The name of an image in `assets/sprite/settlement/structure/`, without its extension. The image must be exactly 576 pixels wide and at least 372 high. Structures can share an image by using the same name. Copy a vanilla image to see the layout.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
SPRITE: Wood,
```

### BUILD_TIME

How long the structure takes to build. Higher values take longer, for both walls and ceilings.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | Yes |

```text
BUILD_TIME: 0.1,
```

### RESOURCE

The resource the structure is built from, by its key. `_MUD.txt` doesn't have one, so mud costs nothing.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | No |

```text
RESOURCE: WOOD,
```

### RESOURCE_AMOUNT

How much of the resource a ceiling tile costs. A wall tile costs one more than this. The game only reads this tag when the file has `RESOURCE`.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 16, but doesn't enforce it. |
| **Required** | Yes, if the file has `RESOURCE` |

```text
RESOURCE_AMOUNT: 1,
```

### DURABILITY

How hard the structure is to break, from 0 to 1.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DURABILITY: 1.0,
```

### COLOR

The colour the structure's image is tinted with, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR: 255_255_255,
```

### MINIMAP_COLOR

The structure's colour on the minimap, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
MINIMAP_COLOR: 76_36_22,
```

### PREFERENCE

How much each race likes this structure by default, from 0 to 1. Each entry names a race by its key, and `*` covers every race. A race's own [`PREFERRED.STRUCTURE`](../07-race/02-preferences.md#structure) block overrides this for any structure it lists.

| | |
|---|---|
| **Type** | Block of decimals, keyed by race |
| **Range** | Each value 0 to 1 |
| **Required** | No. A missing race counts as `0`. |

```text
PREFERENCE: {
	*: 0.5,
},
```

## The text file

Each structure needs a file of the same name in `assets/text/settlement/structure/`. These examples come from the vanilla `WOOD.txt`.

### INFO

The structure's name and description. Vanilla puts these in an `INFO` block, but the game also accepts them at the top level of the file.

| | |
|---|---|
| **Type** | Block |
| **Required** | No, if the tags are at the top level |

#### NAME

The structure's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Wooden Building",
```

#### NAMES

The plural of the structure's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

```text
NAMES: "Wooden Buildings",
```

#### DESC

The structure's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Structure out of wood.",
```

#### WIKI

Adds an article about the structure to the in-game wiki. Vanilla doesn't use it here. The tags inside it are described under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

### NAME_WALL

The name of a wall of this structure.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME_WALL: "Wooden Wall",
```

### NAME_CEILING

The name of a ceiling of this structure.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME_CEILING: "Wooden Ceiling",
```

### BONUS

The game never reads this block for structures. It's in the vanilla `GRAND`, `STONE` and `WOOD` text files.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

```text
BONUS: {
	NAME: "Wood Structure Construction",
	DESC: "Decreases construction time of Wooden Structures",
},
```

## Notes

### The files starting with an underscore

- **`_MUD.txt`** is a normal structure with the tags above, loaded by name. It's always the first structure.
- **`_MOUNTAIN.txt`** and **`_OUTDOORS.txt`** aren't structures. The game only reads `PREFERENCE` from them, for how much races like being in mountains and outdoors. From their text files it only reads the name and description, so `NAME_WALL` and `NAME_CEILING` in the vanilla `_MOUNTAIN` text file do nothing.

## Related

- [init/settlement](00-settlement.md)
- [Race preferences](../07-race/02-preferences.md)
