# init/settlement/fence

These files define the fences the player can build. Each file is one kind of fence, giving what it costs, how it appears on the minimap and how it's drawn.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/settlement/fence/` |
| **Files** | One `.txt` file per fence, e.g. `WOOD.txt` |
| **Key** | The file name, e.g. `WOOD` |
| **Adding new fences** | Yes, up to 16 in total. More stops the game with an error. |
| **Text file** | `assets/text/settlement/fence/<KEY>.txt`, required |
| **Sprites** | The sprite entries below, using images in `assets/sprite/game/combo/` |
| **Sound** | A `BUILD_FENCE_<KEY>` entry in a file in `assets/audio/config/mono/` |

## Tags

The examples come from the vanilla `WOOD.txt`.

### SPRITE

The game never reads this tag for fences. Only `WOOD.txt` has it.

| | |
|---|---|
| **Type** | Text |
| **Required** | No |
| **Effect** | Unread |

```text
SPRITE: Wood,
```

### RESOURCE

The resource a fence is built from, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: WOOD,
```

### RESOURCE_AMOUNT

How much of the resource each tile of fence costs.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes |

```text
RESOURCE_AMOUNT: 1,
```

### COLOR

The game never reads this tag for fences. Only `WOOD.txt` has it.

| | |
|---|---|
| **Type** | Colour |
| **Required** | No |
| **Effect** | Unread |

```text
COLOR: 255_255_255,
```

### MINIMAP_COLOR

The fence's colour on the minimap, as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
MINIMAP_COLOR: 76_36_22,
```

### SPRITE_SQUARE_COMBO

One of the two [sprite entries](../../03-sprite/03-game.md#sprite-entries) a fence is drawn with, using a `combo` sheet.

| | |
|---|---|
| **Type** | Sprite entry |
| **Required** | Yes |

```text
SPRITE_SQUARE_COMBO: {
	
	SHADOW_LENGTH: 6,
	SHADOW_HEIGHT: 2,
	TINT: false,
	FRAMES: [
		FENCE: 3,
	],
},
```

### SPRITE_ROUND_COMBO

The other [sprite entry](../../03-sprite/03-game.md#sprite-entries) a fence is drawn with, using a `combo` sheet.

| | |
|---|---|
| **Type** | Sprite entry |
| **Required** | Yes |

```text
SPRITE_ROUND_COMBO: {
	
	SHADOW_LENGTH: 6,
	SHADOW_HEIGHT: 2,
	TINT: false,
	FRAMES: [
		FENCE: 4,
	],
},
```

## The text file

Each fence needs a file of the same name in `assets/text/settlement/fence/`. These examples come from the vanilla `WOOD.txt`.

### NAME

The fence's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Wood Fence",
```

### DESC

The fence's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Keeps wild animals from your pastures and funnels your subjects to walk where they're supposed to.",
```

## Related

- [init/settlement](00-settlement.md)
- [sprite/game](../../03-sprite/03-game.md)
