# init/room: health rooms

These rooms look after the sick and the deranged: physicians, the asylum and the hospital. Besides the tags on this page, they use the [common tags](01-common.md), [employment](02-employment.md) and [services](04-services.md) tags, and the asylum and hospital also use [production](03-production.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `PHYSICIAN_*.txt`, `_ASYLUM.txt` and `_HOSPITAL.txt` |
| **Adding new rooms** | Yes for physicians. `_ASYLUM` and `_HOSPITAL` are single rooms. |

## PHYSICIAN

A physician's practice is a service room that satisfies a need, so its `SERVICE` block needs `NEED`, `STANDING` and its text file needs `SERVICE.VERB` and `SERVICE.MORE`. It has exactly two `ITEMS`, in this order: the workbench (at least one per room) and the shelves (at least one per room). It has three statistics.

### SPRITES

The images a physician is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with, unless the table says otherwise.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BUNK_1X1_TOP` | One tile of a bunk. | `1x1` |
| `BUNK_1X1_BOTTOM` | The other tile of a bunk. | `1x1` |
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_ONTOP_1X1` | Things on the tables. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_ONTOP_1X1` | Things on the shelves. | `1x1` |
| `STORAGE_1X1` | The storage. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _ASYLUM

The room where deranged subjects are kept. Its `INDUSTRY` block has an `IN` entry for what it consumes, with no output: vanilla uses `RATION`. It has exactly one `ITEMS` block, the cells (at least one per room), and two statistics. It has no `SERVICE` block.

The examples come from the vanilla `_ASYLUM.txt`.

### FLOOR2

A second floor, by its key, laid under the room's furniture. The candle holders' tiles and empty tiles use `FLOOR`.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: WOOD,
```

### SPRITES

The images the asylum is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `WALLS_COMBO` | The walls of the cells. | `combo` |
| `BARS_1X1` | The bars. | `1x1` |
| `OPENING_1X1` | The cell door. | `1x1` |
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_ONTOP_1X1` | Things on the tables. | `1x1` |
| `DECOR_1X1` | The bucket and other decoration. | `1x1` |
| `CANDLE_HOLDER_1X1` | The candle holders. | `1x1` |
| `BED_1X1_TOP` | One tile of a bed. | `1x1` |
| `BED_1X1_BOTTOM` | The other tile of a bed. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _HOSPITAL

The room where the sick are treated. Its `INDUSTRY` block has `IN` entries for what it consumes, with no output: vanilla uses `FABRIC` and `OPIATES`. Each of these gets an unlock named `ROOM_HOSPITAL_USE_<RESOURCE>`. Its `SERVICE` block only reads `RADIUS`, and its text file only needs `SERVICE.VERB`. It has exactly one `ITEMS` block, the beds (at least one per room), and two statistics.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. This example comes from the vanilla `_HOSPITAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.1,
	SOUND: work->Fabric*,
	USES_TOOL: false,
	NIGHT_SHIFT: true,
	FULFILLMENT: 0.5,
},
```

### SPRITES

The images the hospital is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with, unless the table says otherwise.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BED_TOP_1X1` | One tile of a bed. | `1x1` |
| `BED_BOTTOM_1X1` | The other tile of a bed. | `1x1` |
| `BED_TOP_1X1_UNMADE` | One tile of an unmade bed. | `1x1` |
| `BED_BOTTOM_1X1_UNMADE` | The other tile of an unmade bed. | `1x1` |
| `BED_1X1_GRIME` | Grime on a bed. | `1x1` |
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_ONTOP_1X1` | Things on the tables. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Services](04-services.md)
- [init/disease](../04-disease.md)
