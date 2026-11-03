# init/stats/need

These files define the needs that build up in your subjects and send them off to satisfy them: hunger and thirst, and everything from a visit to the well to a night at the theatre. Rooms satisfy a need by naming it in their [`SERVICE.NEED`](../10-room/04-services.md#need) tag.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/need/` |
| **Files** | One `.txt` file per need, e.g. `WELL.txt`, plus the required `_HUNGER.txt`, `_THIRST.txt`, `_SHOPPING.txt`, `_SKINNYDIP.txt`, `_TEMPLE.txt` and `_SHRINE.txt` |
| **Key** | The file name, e.g. `WELL` |
| **Boost name** | `RATES_<KEY>` without any leading `_`, e.g. `RATES_WELL` or `RATES_HUNGER` |
| **Adding new needs** | Yes. The new file's name must not start with `_`. |
| **Text file** | `assets/text/stats/need/<KEY>.txt`, required |

## Tags

The examples come from the vanilla `STAGE.txt` unless stated otherwise.

### RATE

How quickly the need grows each day. It's the starting value of the need's `RATES_` boost, which races and other files can raise or lower.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | Yes |

```text
RATE: 0.2,
```

### EVENT

Makes the need surge on certain days, by multiplying its rate. Vanilla uses it for the arena, speakers and stage. A value of 1 or less does nothing.

The game gives each need with this tag its own day in a repeating cycle, lasting twice the number of those needs plus one. With vanilla's four needs that's a cycle of 9 days.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | No. Default `0`. |

```text
EVENT: 10,
```

### NEED

The game never reads this tag. Vanilla only has it in `HEARTH.txt`.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
NEED: HEARTH,
```

## The text file

Each need needs a file of the same name in `assets/text/stats/need/`. These examples come from the vanilla `HEARTH.txt`.

### NAME_NEED

The need's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME_NEED: "Socialization",
```

### NAME_RATE

The name of the boost that controls how fast the need grows.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME_RATE: "Loneliness",
```

## Notes

### Needs without a room

If no room satisfies a need, the game only writes a line to its log, and subjects have nowhere to meet it.

### Vanilla files the game doesn't load

`_MOURN.txt` is in this folder and in the text folder, and the text folder also has `_COURT.txt`. None of them are loaded, because their names start with `_` and the game doesn't ask for them by name. Mourning uses a separate value, `ACTIVITY_MOURN`, and courts use the need `COURT`.

## Related

- [init/stats](00-stats.md)
- [init/room: services](../10-room/04-services.md)
