# init/settlement/environment

These files define the environment effects of a city: noise, light, space, guard presence, punishment, urbanisation, and sweet and salt water. Rooms and other sources give these effects to the tiles around them, and subjects feel the effect of the tile they're standing on.

The set of effects is fixed by the game's code, so these files can only adjust the eight that exist.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/settlement/environment/` |
| **Files** | `_GUARD.txt`, `_LIGHT.txt`, `_NOISE.txt`, `_PUNISHMENT.txt`, `_SPACE.txt`, `_URBANISATION.txt`, `_WATER_SALT.txt` and `_WATER_SWEET.txt` |
| **Key** | The file name, e.g. `_NOISE`. Other files can also leave off the `_`. |
| **Adding new effects** | No. The game loads these eight by name. |
| **Text file** | `assets/text/settlement/environment/<KEY>.txt`, required |

## Tags

### DECLINE_VALUE

How quickly a subject's sense of this effect fades after they move somewhere with less of it. Higher values fade faster. `_NOISE` is the exception: the game reads the tag, but noise always changes at the same speed.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DECLINE_VALUE: 0.5,
```

### ICON

The effect's icon in the interface, as described under [`ICON` on the init/animal page](../01-animal.md#icon).

| | |
|---|---|
| **Type** | Icon path, or a block |
| **Required** | Yes |

```text
ICON: 16->Env->1,
```

### BOOST

Bonuses tied to this effect, written in the same way as a race's `BOOST` block. Their strength follows the subject's value for this effect. This example comes from the vanilla `_GUARD.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

```text
BOOST: {
	CIVIC_LAW>MUL: 2.0,
}
```

### STANDING

How much this effect matters to your subjects, in the same format as an entry in a race's [`STATS`](../07-race/03-stats.md#format) block. Races can set their own values there, as `HUMAN.txt` does with `ACCESS_NOISE`. This example comes from the vanilla `_PUNISHMENT.txt`.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `CITIZEN`, `SLAVE`, `NOBLE` | The most the effect can add for that class. | Decimal, 0 to 1000000 | No |
| `MULTIPLIER` | Multiplies the effect's value before it's used. | Decimal, 0 to 100000 | No |
| `EXPONENT` | Applied to the value after `MULTIPLIER`. | Decimal, 0.01 to 10 | No |
| `INVERTED` | If `true`, the effect counts against subjects: none of it gives the full amount, and a full value gives nothing. | True/false | No |
| `PRIO` | How prominently subjects mention this effect in their opinions. | Decimal, 0 to 100000 | No |
| `DISMISS` | If `true`, the effect only ever adds. | True/false | No |

```text
STANDING: {
	CITIZEN: 4,
	SLAVE: 2,
	MUL: 2,
	INVERTED: true,
},
```

#### CHILD

The game reads this tag, but only service stats use it, so it does nothing here. Vanilla doesn't use it in these files.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No |
| **Effect** | None |

#### MUL

The game never reads this tag. It reads `MULTIPLIER` instead, so vanilla's `MUL` values do nothing.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
MUL: 2,
```

## The text file

Each effect needs a file of the same name in `assets/text/settlement/environment/`. These examples come from the vanilla `_NOISE.txt`.

### INFO

The effect's name and description. Vanilla puts these in an `INFO` block, but the game also accepts them at the top level of the file.

| | |
|---|---|
| **Type** | Block |
| **Required** | No, if the tags are at the top level |

#### NAME

The effect's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Noise",
```

#### NAMES

The plural of the effect's name. Vanilla doesn't use it here.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

#### DESC

The effect's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Noise travels from noisy rooms out into the open and disturbs your subjects. It's hindered slightly by walls.",
```

#### WIKI

Adds an article about the effect to the in-game wiki. Vanilla doesn't use it here. The tags inside it are described under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

### MORE

Things subjects say when they want more of this effect, as a list of text. Without it, the game uses a short line of its own. The example is shortened.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

```text
MORE: [
	"The city feels lifeless without the sound of industry.",
],
```

### LESS

Things subjects say when they want less of this effect, as a list of text. Without it, the game uses a short line of its own. The example is shortened.

| | |
|---|---|
| **Type** | List of text |
| **Required** | No |

```text
LESS: [
	"How am I supposed to sleep with all of this noise?",
],
```

## Notes

### Where the effects come from

Rooms give off these effects through [`ENVIRONMENT_EMIT`](../10-room/01-common.md#environment_emit). Some effects also have sources in the game's code: `_URBANISATION` comes from rooms, structures and floors, for example, and `_WATER_SWEET` and `_WATER_SALT` from water on the map. Roads can add to an effect on their own tile with [`ROAD.ENVIRONMENT`](03-floor.md#environment).

### Extra files

The game counts the files in this folder whose names don't start with `_`, and stops with an error if there are more than 24. It doesn't load them.

## Related

- [init/settlement](00-settlement.md)
- [init/room: common tags](../10-room/01-common.md)
- [Race stats](../07-race/03-stats.md)
