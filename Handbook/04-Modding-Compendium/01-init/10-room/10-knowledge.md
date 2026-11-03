# init/room: knowledge rooms

These rooms produce research and educate your subjects: laboratories, libraries, schools and universities. Besides the tags on this page, they use the [common tags](01-common.md) and [employment](02-employment.md) tags.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `LABORATORY_*.txt`, `LIBRARY_*.txt`, `SCHOOL_*.txt` and `UNIVERSITY_*.txt` |
| **Adding new rooms** | Yes, for all four types. |

## LABORATORY

A laboratory's workers build up a value that feeds a boost, which vanilla uses for innovation. It has exactly one `ITEMS` block (at least one per room), and two statistics. It also reads [`EXPERIENCE_BONUS`](02-employment.md#experience_bonus).

The examples come from the vanilla `LABORATORY_NORMAL.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. It must be `WORK`, because this room's value tags only work with that block, not `EMPLOYMENT`. This example comes from the vanilla `LABORATORY_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.375,
	SOUND: DUMMY,
	USES_TOOL: true,
	FULFILLMENT: 0.75,
},
```

### VALUE_PER_WORKER

The value each worker can build up.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | Yes |

```text
VALUE_PER_WORKER: 1,
```

### VALUE_DEGRADE_PER_YEAR

How much of the value is lost per year.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes |

```text
VALUE_DEGRADE_PER_YEAR: 0.5,
```

### VALUE_WORK_SPEED

How quickly workers build up the value.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
VALUE_WORK_SPEED: 8,
```

### BOOST

The boost this value feeds, by its name. Unlike most `BOOST` tags, this is a single name, not a block.

| | |
|---|---|
| **Type** | Key (a boost) |
| **Required** | No. Without it, the value feeds nothing. |

```text
BOOST: CIVIC_INNOVATION,
```

### CONSUMPTION

Resources the room can consume to work better. Each entry names a resource by its key, and holds `RATE` and `BONUS`.

| | |
|---|---|
| **Type** | Block of blocks, keyed by resource |
| **Required** | No |

```text
CONSUMPTION: {
	CLAY: {
		RATE: 0.75,
		BONUS: 1,
	},
},
```

#### RATE

How much of the resource is consumed.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | Yes |

```text
RATE: 0.75,
```

#### BONUS

How much having this resource adds to the room's output.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
BONUS: 1,
```

### SPRITES

The images a laboratory is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_KNOWLEDGE_ONTOP_1X1` | Things on the tables. | `1x1` |
| `WORK_TABLE_1X1` | The work spot on a table. | `1x1` |
| `WORK_STANDALONE_1X1` | A separate work spot. | `1x1` |
| `CHAIR_1X1` | The chairs. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_DECOR_1x1` | Things on the shelves. Note the lower-case `x`. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## LIBRARY

A library works like a laboratory, feeding a boost that vanilla uses for knowledge. It has exactly two `ITEMS`, in this order: the shelf (at least one per room) and the carpet. It has three statistics. It also reads [`EXPERIENCE_BONUS`](02-employment.md#experience_bonus).

The examples come from the vanilla `LIBRARY_NORMAL.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. It must be `WORK`, because this room's value tags only work with that block, not `EMPLOYMENT`. This example comes from the vanilla `LIBRARY_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.375,
	SOUND: work->Paper*,
	FULFILLMENT: 0.75,
},
```

### VALUE_PER_WORKER

The value each worker can build up.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100000 |
| **Required** | Yes |

```text
VALUE_PER_WORKER: 1,
```

### VALUE_DEGRADE_PER_YEAR

How much of the value is lost per year.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes |

```text
VALUE_DEGRADE_PER_YEAR: 0.225,
```

### VALUE_WORK_SPEED

How quickly workers build up the value.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
VALUE_WORK_SPEED: 5,
```

### BOOST

The boost this value feeds, by its name. Unlike most `BOOST` tags, this is a single name, not a block.

| | |
|---|---|
| **Type** | Key (a boost) |
| **Required** | No. Without it, the value feeds nothing. |

```text
BOOST: CIVIC_KNOWLEDGE,
```

### CONSUMPTION

Resources the room can consume to work better. Each entry names a resource by its key, and holds `RATE` and `BONUS`.

| | |
|---|---|
| **Type** | Block of blocks, keyed by resource |
| **Required** | No |

```text
CONSUMPTION: {
	LEATHER: {
		RATE: 0.5,
		BONUS: 1,
	},
},
```

#### RATE

How much of the resource is consumed.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | Yes |

```text
RATE: 0.5,
```

#### BONUS

How much having this resource adds to the room's output.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
BONUS: 1,
```

### SPRITES

The images a library is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries). Note the lower-case `x` in several of these names.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `TABLE_DECOR_1x1` | Things on the tables. | `1x1` |
| `WORK_USED_1x1` | A place at a table, in use. | `1x1` |
| `WORK_UNUSED_1x1` | A place at a table, free. | `1x1` |
| `CHAIR_1X1` | The chairs. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_DECOR_1x1` | Things on the shelves. | `1x1` |
| `TORCH_1x1` | The torches. | `1x1` |
| `DECOR_1x1` | Other decoration. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## SCHOOL

A school teaches children. Its `SERVICE` block only reads `RADIUS`, and its text file only needs `SERVICE.VERB`. Its `INDUSTRY` block has `IN` entries for what it consumes, with no output: vanilla uses `PAPER`. It has exactly three `ITEMS`, in this order: the bench (at least one per room), the shelf and the carpets. It has two statistics.

The examples come from the vanilla `SCHOOL_NORMAL.txt`.

### WORK

The room's workers, in the form described on the [employment](02-employment.md#work-and-employment) page. This room type uses its workers while loading, so the game crashes without this block. This example comes from the vanilla `SCHOOL_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
WORK: {
	SHIFT_OFFSET: 0.125,
	SOUND: work->Paper*,
	USES_TOOL: false,
	FULFILLMENT: 0.5,
},
```

### LEARNING_SPEED

The game never reads this tag for schools. Only universities use it.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
LEARNING_SPEED: 1.0,
```

### SPRITES

The images a school is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_1X1` | The tables at the benches. | `1x1` |
| `TABLE_TOP_1X1` | Things on the tables. | `1x1` |
| `BOOK_1X1` | The books. | `1x1` |
| `STOOL_1X1` | The stools. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_TOP_1X1` | Things on the shelves. | `1x1` |
| `CARPET_COMBO` | The carpet item. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## UNIVERSITY

A university educates adults. It uses an `EMPLOYMENT` block rather than `WORK`. It has exactly two `ITEMS`, in this order: the podium (at least one per room) and the shelf. It has two statistics.

The examples come from the vanilla `UNIVERSITY_NORMAL.txt`.

### LEARNING_SPEED

How quickly students learn here.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100 |
| **Required** | Yes |

```text
LEARNING_SPEED: 1,
```

### SPRITES

The images a university is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `PODIUM_COMBO` | The podium. | `combo` |
| `BENCH_1X1` | The students' benches. | `1x1` |
| `CARPET_COMBO` | The carpet. | `combo` |
| `TORCH_1X1` | The torches. | `1x1` |
| `SHELF_1X1` | The shelves. | `1x1` |
| `SHELF_TOP_1X1` | Things on the shelves. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Employment](02-employment.md)
