# init/room: water rooms

These rooms hold and move water: pools, canals, drains and pumps. Besides the tags on this page, they use the [common tags](01-common.md), and the pump also uses [employment](02-employment.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `POOL_*.txt`, `_WATERCANAL.txt`, `_WATERDRAIN.txt` and `_WATERPUMP.txt` |
| **Adding new rooms** | Yes for pools. The others are single rooms. |

## POOL

A decorative pool. It has no workers. It has exactly one `ITEMS` block and no statistics.

The examples come from the vanilla `POOL_POND.txt`.

### WATER_COLOR

The colour of the water, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
WATER_COLOR: 30_60_60,
```

### WATER_DEPTH

How opaque the water looks: at `1` the bottom can't be seen.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
WATER_DEPTH: 0.5,
```

### CLEARS_GRASS

Whether building the pool clears the grass underneath.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
CLEARS_GRASS: false,
```

### BOTTOM_TEXTURE

The texture on the bottom of the pool, from `assets/sprite/game/texture/`. It's written as a block naming the image and the row within it.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
BOTTOM_TEXTURE: {
	FILE: ORGANIC,
	ROW: 2,
},
```

### FULLFILLMENT

The game reads this value, but in v0.71.44 nothing uses it: changing it has no effect. How much a race likes a pool is set by its [`PREFERRED.POOL`](../07-race/02-preferences.md#pool) block, where an unlisted pool counts as `0`. Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No |
| **Effect** | None |

### SPRITES

The images a pool is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FRAME_COMBO` | The edge of the pool. | `combo` |
| `STENCIL_COMBO` | A shape for the water at the edge. | `combo` |
| `ON_TOP_1X1` | Things on top of the edge. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _WATERCANAL

The canal. It has no tags of its own besides the [common tags](01-common.md). It has exactly one `ITEMS` block and no statistics, and no `SPRITES` block.

## _WATERDRAIN

The culvert. It has exactly one `ITEMS` block and no statistics.

### SPRITES

The images the room is drawn with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `DRAIN_1X1` | The culvert. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _WATERPUMP

The water pump. It has exactly one `ITEMS` block (at least one per room) and one statistic.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FRAME_COMBO` | The body of the pump. | `combo` |
| `FRAME_TOP_1X1` | The top of the body. | `1x1` |
| `WORKDONG_1X1` | The base of the working part. | `1x1` |
| `WORK_A_1X1`, `WORK_B_1X1`, `WORK_C_1X1` | The working part, one for each upgrade level. | `1x1` |
| `PIPE_1X1` | The pipes. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [init/race/preferences](../07-race/02-preferences.md)
