# init/stats/equip/civic

These files define the equipment your subjects use in everyday life: clothes and jewellery. Its `STANDING` block lets it add to their happiness.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/equip/civic/` |
| **Files** | One `.txt` file per item, e.g. `JEWELRY.txt`, plus `_CLOTHES.txt`, which must exist |
| **Key** | `CIVIC_` and the file name, without any leading `_`, e.g. `CIVIC_CLOTHES` |
| **Adding new equipment** | Yes |
| **Text file** | None. The name, description and icon come from the resource. |

## Tags

The examples come from the vanilla `_CLOTHES.txt` unless stated otherwise.

### RESOURCE

The resource this equipment is made from, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: CLOTHES,
```

### MAX_AMOUNT

The most a subject can carry. Comments in vanilla's `_EXAMPLE.txt` say technologies can raise this, but the game's code keeps it fixed at the value in this file.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 15 but doesn't enforce it. Stay at or below 15, because the amount is stored in a space that only holds up to 15. |
| **Required** | Yes |

```text
MAX_AMOUNT: 6,
```

### EXPO

The game never reads this tag. To shape how a subject values this equipment, use `EXPONENT` in the `STANDING` block.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
EXPO: 0.5,
```

### ARRIVAL_AMOUNT

How much of this equipment new immigrants arrive with.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names `MAX_AMOUNT` as the maximum but doesn't enforce it. A higher value is capped at `MAX_AMOUNT` when it's applied. |
| **Required** | Yes |

```text
ARRIVAL_AMOUNT: 1,
```

### WEAR_RATE

How much of this equipment wears out each year, for each item carried.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100 |
| **Required** | Yes |

```text
WEAR_RATE: 0.25,
```

### DEFAULT_TARGET

The amount each class and race is set to carry when a game starts. The player can then change it. It's capped between 0 and `MAX_AMOUNT` when used.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes |

```text
DEFAULT_TARGET: 1,
```

### BOOST

The bonuses this equipment gives, written in the same way as a race's [`BOOST`](../../07-race/01-race-file.md#boost) block. They grow with the amount carried, as [the equip chapter](00-equip.md#how-strong-bonuses-are) explains.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	PHYSICS_RESISTANCE_HOT>ADD: 1,
	PHYSICS_RESISTANCE_COLD>ADD: 1.5,
},
```

### STANDING

How much this equipment matters to your subjects, in the same format as an entry in a race's [`STATS`](../../07-race/03-stats.md#format) block. Races can set their own values there, using the stat name `EQUIP_CIVIC_CLOTHES` or similar.

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Without it, the game looks for these tags at the top level of the file, and any it doesn't find keep their defaults, so the item adds nothing for any class. |

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `CITIZEN`, `SLAVE`, `NOBLE` | The most it can add for that class. | Decimal, 0 to 1000000 | No |
| `MULTIPLIER` | Multiplies the stat's value before it's used. | Decimal, 0 to 100000 | No |
| `EXPONENT` | Applied to the value after `MULTIPLIER`. | Decimal, 0.01 to 10 | No |
| `INVERTED` | If `true`, carrying it counts against subjects. | True/false | No |
| `PRIO` | How prominently subjects mention it in their opinions. | Decimal, 0 to 100000 | No |
| `DISMISS` | If `true`, it only ever adds. | True/false | No |

```text
STANDING: {
	CHILD: true,
	CITIZEN: 7.0,
	SLAVE: 5.5,
	NOBLE: 2,
	EXPONENT: 0.5,
	PRIO: 10,
},
```

#### CHILD

The game reads this tag, but only service stats use it, so it does nothing here.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No |
| **Effect** | None |

```text
CHILD: true,
```

## Related

- [init/stats/equip](00-equip.md)
- [Battle equipment](01-battle.md)
- [Race stats](../../07-race/03-stats.md)
