# init/room: services

Rooms that serve your subjects, such as wells, eateries and bathhouses, have a `SERVICE` block. It sets how far subjects will travel to the room, and how the service affects them. Which of these tags a room reads depends on its type.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | One `.txt` file per room |
| **Text file** | `assets/text/room/<KEY>.txt` |

## Tags

### SERVICE

The room's service. These examples come from the vanilla `EATERY_NORMAL.txt` unless stated otherwise.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, for service rooms |

```text
SERVICE: {
	STANDING: {
		CHILD: true,
		CITIZEN: 3.5,
		SLAVE: 2.5,
		NOBLE: 0.5,
		PRIO: 100,
	},
	RADIUS: 100,
},
```

#### RADIUS

How far subjects will travel for this service. Access falls away with distance: the service counts fully up to about a third of this distance, and not at all beyond about one and a third times it.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 50000, but doesn't enforce it. |
| **Required** | No. Default `150`. |

```text
RADIUS: 100,
```

#### STANDING

How much access to the service matters to subjects. It's in the same format as an entry in a race's [`STATS`](../07-race/03-stats.md#format) block, and it's the default for races that don't list this service there.

Here `PRIO` defaults to `1`. A race that lists this service without its own `PRIO` takes the value from here.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, for service rooms that subjects get access to |

```text
STANDING: {
	CHILD: true,
	CITIZEN: 3.5,
	SLAVE: 2.5,
	NOBLE: 0.5,
	PRIO: 100,
},
```

#### NEED

The need this service satisfies, by a key from [`assets/init/stats/need/`](../13-stats/06-need.md). This example comes from the vanilla `_HEARTH.txt`.

| | |
|---|---|
| **Type** | Key (a need) |
| **Required** | Yes, for room types that satisfy a need they read from the file |

```text
NEED: HEARTH,
```

#### BOOST

Bonuses given by access to the service, in the same form as a race's [`BOOST`](../07-race/01-race-file.md#boost) block. This example comes from the vanilla `BATH_NORMAL.txt`.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	PHYSICS_HEALTH>MUL: 1.5,
},
```

#### USAGE

How readily subjects use this service, compared with others they could use instead. This example comes from the vanilla `CANTEEN_NORMAL.txt`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `1`. |

```text
USAGE: 0.125,
```

#### DEFAULT_ACCESS and DEFAULT_VALUE

The game never reads these tags, so they have no effect and can be left out. This example comes from the vanilla `WELL_NORMAL.txt`.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
DEFAULT_ACCESS: 1.0,
```

#### SOUND

The game never reads this tag. A room's service sound comes from the entry `ROOM_SERVICE_<KEY>` in the audio files. This example comes from the vanilla `_HEARTH.txt`.

| | |
|---|---|
| **Type** | Sound path |
| **Required** | No |
| **Effect** | Unread |

```text
SOUND: human->Sleep*,
```

## The text file

A service room's text file needs a `SERVICE` block. These examples come from the vanilla `WELL_NORMAL.txt`.

### SERVICE

The wording for the room's service.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, for service rooms |

#### VERB

What subjects are doing when they use the service.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
VERB: "Washing up",
```

#### MORE

Things subjects say when they want more of this service, as a list of text. Rooms that give access to a service need this.

The list can be empty (`[]`), and then subjects use the game's own default line instead.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes, for service rooms that subjects get access to |

```text
MORE: [
	"We need more wells to quench our thirst.",
	"Better access to clean water would be very convenient.",
	"More wells would help with the odor here.",
	"We need more wells to quench our thirst and freshen our faces.",
],
```

#### NAME and NAMES

The game never reads these from the text file's `SERVICE` block, though vanilla's temples, shrines, `SCHOOL_NORMAL`, `UNIVERSITY_NORMAL`, `_INN` and `_DUMP_CORPSE` have them. This example comes from the vanilla `TEMPLE_ATHURI.txt`.

| | |
|---|---|
| **Type** | Text |
| **Required** | No |
| **Effect** | Unread |

```text
SERVICE: {
	NAME: "Temple",
	NAMES: "Temples",
	VERB: "Worshipping",
},
```

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Race stats](../07-race/03-stats.md)
