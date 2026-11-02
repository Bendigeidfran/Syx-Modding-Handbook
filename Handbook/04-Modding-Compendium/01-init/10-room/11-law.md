# init/room: law rooms

These rooms keep order and carry out punishments: courts, execution grounds, guard posts, torture chambers, prisons, stockades and stocks. Each is a single room, so new ones can't be added. Besides the tags on this page, they use the [common tags](01-common.md), and those with workers use [employment](02-employment.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `_COURT.txt`, `_EXECUTION.txt`, `_GUARD.txt`, `_POLICE.txt`, `_PRISON.txt`, `_STOCKADE.txt` and `_STOCKS.txt` |
| **Adding new rooms** | No. These are all single rooms. |

## _COURT

The court is a service room that satisfies a need, so its [`SERVICE`](04-services.md) block needs `NEED` and `STANDING`, and its text file needs `SERVICE.VERB` and `SERVICE.MORE`. It has exactly two `ITEMS`, in this order: the court and the spectators. It has three statistics.

Vanilla writes `FULLFILLMENT` in its `WORK` block, which the game ignores, as described on the [employment](02-employment.md#fullfillment) page.

### SPRITES

The images the court is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `CARPET_COMBO` | The carpet. | `combo` |
| `STAND_COMBO` | The stand. | `combo` |
| `TORCH_1X1` | The torches. | `1x1` |
| `GEM_1X1` | The gem on top of a torch. | `1x1` |
| `CHAIR_1X1` | The chairs. | `1x1` |
| `DECOR_A_1X1` | Decoration. | `1x1` |
| `DECOR_B_1X1` | More decoration. | `1x1` |
| `BENCH_A_1X1` | The first part of a spectators' bench. | `1x1` |
| `BENCH_B_1X1` | The next part of a bench. | `1x1` |
| `BENCH_C_1X1` | The next part of a bench. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _EXECUTION

The execution ground. It has no workers. It has exactly four `ITEMS`, in this order: the gallows, the chopping block, the gibbet cage and the cross. It has one statistic.

The examples come from the vanilla `_EXECUTION.txt`.

### SERVICE

The game never reads this block for this room, or the `SERVICE` block in its text file, though vanilla has both.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `GALLOW_BEAM_LEFT_1X1` | The end of the gallows beam. | `1x1` |
| `GALLOW_BEAM_CENTRE_1X1` | The middle of the gallows beam. | `1x1` |
| `GALLOW_BOTTOM_1X1` | The foot of the gallows. | `1x1` |
| `GALLOW_PILLAR_1X1` | The gallows pillar. | `1x1` |
| `GALLOW_NOOSE_1X1` | The noose. | `1x1` |
| `GALLOW_BOX_1X1` | The box under the noose. | `1x1` |
| `CHOP_TABLE_1X1` | The chopping block. | `1x1` |
| `CHOP_MAT_1X1` | The mat by the chopping block. | `1x1` |
| `GIBBET_CAGE_1X1` | The gibbet cage. | `1x1` |
| `GIBBET_DOOR_1X1` | The door of the gibbet cage. | `1x1` |
| `CROSS_C_1X1` | The centre of the cross. | `1x1` |
| `CROSS_R_1X1` | The right of the cross. | `1x1` |
| `CROSS_L_1X1` | The left of the cross. | `1x1` |
| `CROSS_MID_1X1` | The middle of the cross. | `1x1` |
| `CROSS_POLE_1X1` | The pole of the cross. | `1x1` |
| `PODIUM_BOX` | The podium the items stand on. | `box` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _GUARD

The guard post. It uses an `EMPLOYMENT` block rather than `WORK`. It has exactly two `ITEMS`, in this order: the guardpost and the guard station, with at least one of each per room. It has one statistic. Its upgrades raise how much the post does, whatever the `BOOST` value in `UPGRADES`.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FLOOR_BOX` | The floor of the post. | `box` |
| `CARPET_COMBO` | The carpet. | `combo` |
| `TORCH_BOTTOM_COMBO` | The bottom of the torches. | `combo` |
| `TORCH_COMBO` | The torches. | `combo` |
| `FENCE_COMBO` | The fence. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _POLICE

The torture chamber. It has exactly five `ITEMS`, in this order: the rack bed, the rack chair, the medusa, the gibbet cage and the auxiliaries. It has two statistics.

The examples come from the vanilla `_POLICE.txt`.

### BOOST

The effects on your subjects, in the same form as a race's [`BOOST`](../07-race/01-race-file.md#boost) block. They only apply to the classes the player has chosen, which by default means slaves, and they grow with the value the room's workers build up.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	BEHAVIOUR_LAWFULNESS>ADD: 10,
	BEHAVIOUR_LOYALTY>MUL: 4,
	BEHAVIOUR_HAPPINESS>MUL: 0.25,
	BEHAVIOUR_SUBMISSION>MUL: 4,
	BEHAVIOUR_HAPPINESS_SLAVES>MUL: 0.25,
},
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TABLE_COMBO` | The tables. | `combo` |
| `NICKNACK_1X1` | Things on the tables. | `1x1` |
| `BED_1X1A` | Both tiles of the rack bed. | `1x1` |
| `BED_STRAP_1X1` | The straps on the bed. | `1x1` |
| `CHAIR_1X1` | The rack chair. | `1x1` |
| `CAGE_A_1X1` | One kind of cage. | `1x1` |
| `CAGE_A_TOP_1X1` | The top of that cage. | `1x1` |
| `CAGE_B_1X1` | The other kind of cage. | `1x1` |
| `CAGE_LATCH_1X1` | The cage's latch. | `1x1` |

| Tag | Meaning | Effect |
|---|---|---|
| `BED_1X1B` | Never read. The game draws both tiles of the bed from `BED_1X1A`. | Unread |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _PRISON

The prison. It has exactly one `ITEMS` block, the cells (at least one per room), and two statistics. The food it uses comes from all the [edible](../09-resource/03-edible.md) resources that are served.

The examples come from the vanilla `_PRISON.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: STONE1,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `WALLS_COMBO` | The cell walls. | `combo` |
| `BARS_1X1` | The bars. | `1x1` |
| `OPENING_1X1` | The cell door. | `1x1` |
| `CANDLE_SHELF_1X1` | The candle shelves. | `1x1` |
| `LATRINE_EMPTY_1X1` | An empty latrine. | `1x1` |
| `LATRINE_FULL_1X1` | A full latrine. | `1x1` |
| `FOOD_1X1` | The food. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _STOCKADE

The stockade. It has exactly one `ITEMS` block, the entrance (at least one per room), and two statistics. The food it uses comes from all the [edible](../09-resource/03-edible.md) resources that are served.

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `WALL_1X1` | The walls. | `1x1` |
| `WALL_CORNER_1X1` | The corners of the walls. | `1x1` |
| `OPENING_1X1` | The entrance. | `1x1` |
| `LATRINE_EMPTY_1X1` | An empty latrine. | `1x1` |
| `LATRINE_FULL_1X1` | A full latrine. | `1x1` |
| `FOOD_1X1` | The food. | `1x1` |
| `MISC_1X1` | Clutter. | `1x1` |

| Tag | Meaning | Effect |
|---|---|---|
| `CANDLE_SHELF_1X1` | Never read here, though vanilla has it. | Unread |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _STOCKS

The stocks. This room has no workers. It's a service room that satisfies a need, so its [`SERVICE`](04-services.md) block needs `NEED` and `STANDING`, and its text file needs `SERVICE.VERB` and `SERVICE.MORE`. Vanilla's text file also has a `LESS` list inside `SERVICE`, which the game never reads. It has exactly one `ITEMS` block and one statistic.

The examples come from the vanilla `_STOCKS.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: STOCKS,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BOX` | The platform. | `box` |
| `STOCK_BELOW_1X1` | The stock. | `1x1` |
| `STOCK_TOP_1X1` | The top of the stock. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Employment](02-employment.md)
- [Services](04-services.md)
- [init/config/LAW.txt](../03-config/07-LAW.md)
