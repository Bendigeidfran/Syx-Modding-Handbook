# init/resource/work

Each file in `init/resource/work` defines one kind of equipment that workers can use to boost a room's output, such as tools. The player chooses how much each room uses, up to a limit that has to be unlocked.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/work/` |
| **Files** | One `.txt` file per kind of equipment, e.g. `TOOL.txt` |
| **Key** | The file name without `.txt`, e.g. `TOOL`. It's used to build the name of the boost that unlocks the equipment. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded. |

Vanilla has one: `TOOL`.

## Tags

The examples below come from the vanilla `TOOL.txt`.

### RESOURCE

The resource used as the equipment, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: TOOL,
```

### WEAR_PER_DAY

The share of the equipment in use that wears out each day: `0.04` is 4%.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
WEAR_PER_DAY: 0.04,
```

### DEFAULT_TARGET

How many items per worker a room starts out wanting, in a new game. It only takes effect once that much has been unlocked.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes |

```text
DEFAULT_TARGET: 0,
```

### BOOST_MAX_VALUE

The largest boost the equipment can give to a room's output. It's given to the rooms with the highest amount in `EQUIP_AMOUNTS`. Other rooms get a share in proportion to their own amount: in vanilla, a room with an amount of 4 gets half of this value, because the highest amount is 8.

A room only gets its full share when its workers have the most they can use. Less equipment gives less of the boost.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
BOOST_MAX_VALUE: 2.0,
```

### BOOST_AI

The game never reads this tag, so it has no effect and can be left out.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
BOOST_AI: 1.5,
```

### BOOST_MUL

If `true`, the boost multiplies a room's output. If `false`, it's added.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
BOOST_MUL: false,
```

### EQUIP_AMOUNTS

The most items of this equipment each worker can use, room by room. Each entry names a room by its key from `assets/init/room/`, and a key ending in `*` covers every room whose key begins that way. A later entry overrides an earlier one, as `PASTURE_BALTI` does here. A room that isn't listed can't use the equipment.

A room needs to have workers and a production bonus. If it doesn't, the entry is skipped, and the game only reports it when Debug is on.

| | |
|---|---|
| **Type** | Block of integers, keyed by room |
| **Range** | Each value 0 or more. The game's code names a maximum of 100, but doesn't enforce it. |
| **Required** | No. Without it, no room can use the equipment. |

```text
EQUIP_AMOUNTS: {
	WORKSHOP*: 8,
	WOODCUTTER: 4,
	MINE*: 4,
	FISHERY*: 4,
	FARM*: 4,
	PASTURE*: 4,
	PASTURE_BALTI: 0,
	ORCHARD*: 4,
	LABORATORY*: 2,
	ADMIN*: 2,
},
```

## Notes

### Unlocking equipment

A room starts with none of the equipment available. For each room in `EQUIP_AMOUNTS`, the game creates a boost named `EQUIP_LEVEL_<KEY>_<ROOM>`, which starts at 0 and sets how much per worker the room can use. Without something raising it, the equipment can't be used at all.

Vanilla raises these boosts with technologies, as in this line from `assets/init/tech/AGRI.txt`:

```text
EQUIP_LEVEL_TOOL_FARM_GRAIN>ADD: 1.0,
```

So a new kind of equipment, or a new room in `EQUIP_AMOUNTS`, also needs something that raises its boost, such as a technology.

## Related

- [init/resource](00-resource.md)
- [The resource file](01-resource-file.md)
