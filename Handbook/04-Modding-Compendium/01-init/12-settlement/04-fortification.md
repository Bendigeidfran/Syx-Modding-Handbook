# init/settlement/fortification

These files define the defensive walls the player can build to hold off enemies. Each file is one kind of wall, giving its cost, strength, height and image.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/settlement/fortification/` |
| **Files** | One `.txt` file per wall, e.g. `STONE.txt` |
| **Key** | The file name, e.g. `STONE` |
| **Adding new walls** | Yes |
| **Text file** | `assets/text/settlement/fortification/<KEY>.txt`, required |
| **Sprites** | Images in `assets/sprite/settlement/fortification/`, named by `SPRITE` |
| **Sound** | A `BUILD_FORTIFICATION_<KEY>` entry in a file in `assets/audio/config/mono/` |

## Tags

The examples come from the vanilla `STONE.txt`.

### SPRITE

The name of an image in `assets/sprite/settlement/fortification/`, without its extension. The image must be exactly 576 pixels wide and at least 144 high. Walls can share an image by using the same name. Copy a vanilla image to see the layout.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
SPRITE: Stone,
```

### RESOURCE

The resource the wall is built from, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: STONE,
```

### RESOURCE_AMOUNT

How much of the resource each tile of wall costs.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes |

```text
RESOURCE_AMOUNT: 3,
```

### DURABILITY

How hard the wall is to break, from 0 to 1.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DURABILITY: 0.75,
```

### COLOR

The colour the wall's image is tinted with, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR: 255_255_255,
```

### MINIMAP_COLOR

The wall's colour on the minimap, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
MINIMAP_COLOR: 116_106_84,
```

### HEIGHT

How tall the wall is. Shadows use this value directly. For the wall's height on the map, the game rounds it up to a multiple of 20 and halves it, so any value from 1 to 20 gives a height of 10.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 20, but doesn't enforce it. |
| **Required** | Yes |

```text
HEIGHT: 15,
```

## The text file

Each wall needs a file of the same name in `assets/text/settlement/fortification/`. These examples come from the vanilla `STONE.txt`.

### NAME

The wall's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Stone Wall",
```

### DESC

The wall's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Holds off enemies. Can also be used as a regular wall",
```

## Notes

### Stairs

The game also loads `_Stairs.png` from the same image folder by name. It must be exactly 216 pixels wide and at least 28 high.

### Unlocks

Each wall gets an unlock named `FORTIFICATION_<KEY>`.

## Related

- [init/settlement](00-settlement.md)
