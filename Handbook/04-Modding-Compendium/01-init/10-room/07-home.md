# init/room: home rooms

These rooms are where subjects live: `_HOME` for most subjects and `_HOME_CHAMBER` for nobles. Besides the tags on this page, they use the [common tags](01-common.md), and the chamber also uses [employment](02-employment.md).

How homes are furnished comes from each race's [home file](../07-race/04-home.md), not from these rooms.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `_HOME.txt` and `_HOME_CHAMBER.txt` |
| **Adding new rooms** | No. Both are single rooms. |

## _HOME

The room for ordinary homes. It has no `WORK` block. It has exactly three `ITEMS`, in this order: the apartment, the house and the longhouse. It has one statistic.

The examples come from the vanilla `_HOME.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: LIVING,
```

### SPRITES

The images drawn for the home's own structure. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries).

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `UP_1X1` | Stairs going up. | `1x1` |
| `DOWN_1X1` | Stairs going down. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _HOME_CHAMBER

The noble's chamber. It has exactly one `ITEMS` block, the chamber (at least one per room), and two statistics. Its text file has no `SERVICE` block.

The examples come from the vanilla `_HOME_CHAMBER.txt`.

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

### SERVICE

The game never reads this block for chambers, though vanilla has one.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

### SPRITES

The images a chamber is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with. The bed and statue come from the race's [home file](../07-race/04-home.md).

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `CARPET_COMBO` | The carpets. | `combo` |
| `MISC_1X1` | Clutter. | `1x1` |
| `BENCH_END_1X1` | The end of a bench. | `1x1` |
| `BENCH_CENTRE_1X1` | The middle of a bench. | `1x1` |
| `MANTEL_A_1X1` | One part of the mantel. | `1x1` |
| `MANTEL_B_1X1` | The other part of the mantel. | `1x1` |
| `BEDPOST_A_1X1` | One bedpost. | `1x1` |
| `BEDPOST_B_1X1` | The other bedpost. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [init/race/home](../07-race/04-home.md)
