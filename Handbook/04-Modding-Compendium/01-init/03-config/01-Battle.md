# init/config/Battle.txt

`Battle.txt` sets the basic scale and pace of battles: how many soldiers make up a division, how many divisions an army can have, how large a region's garrison can be, and two values that affect how long fighting lasts.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/Battle.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | None |

## Tags

### DAMAGE_REDUCTION

How much chance there is in each blow. Whenever a soldier attacks, the game draws a random number between 1 ÷ `DAMAGE_REDUCTION` and `DAMAGE_REDUCTION` and uses it to weaken the attack, in three places: the chance of the attack being dodged, the chance of it being blocked, and the force damage it does if it lands.

Higher values make individual blows more unpredictable and, on average, less effective, so fights take longer. The vanilla comment above this tag and `MORALE_HOLDOUT` reads "How long divisions can hold out in battle".

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 1 to 10000 |
| **Required** | Yes |

```text
DAMAGE_REDUCTION: 100,
```

### MORALE_HOLDOUT

How quickly battle weariness builds up. While a division is fighting, it gains weariness at a rate based on this value and on how many of its soldiers are engaged. Weariness counts against morale. Once the enemy army has been defeated, weariness falls away at a rate also set by this value.

Despite its name, a **higher** value makes weariness build **faster**, so divisions lose morale sooner. To make divisions hold out longer, lower it.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | Yes |

```text
MORALE_HOLDOUT: 1.0,
```

### TRAINING_DEGRADE

According to its vanilla comment, how fast soldiers' training rises and falls. The game reads this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 50, but doesn't enforce it. |
| **Required** | Yes. The tag must be present even though it has no effect. |

```text
TRAINING_DEGRADE: 1,
```

### MEN_PER_DIVISION

The largest number of soldiers a division can hold. It also sets the size of an army, together with `DIVISIONS_PER_ARMY`, and the size of region garrisons, together with `REGION_MAX_DIVS`.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 255, but doesn't enforce it. |
| **Required** | Yes |

```text
** 1-255
MEN_PER_DIVISION: 200,
```

### DIVISIONS_PER_ARMY

The largest number of divisions an army can have. A battle holds two armies, so up to twice this many divisions can take part.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 126, but doesn't enforce it. The vanilla comment says 120. |
| **Required** | Yes |

```text
** 1-120
DIVISIONS_PER_ARMY: 120,
```

### REGION_MAX_DIVS

The largest garrison a region can hold, measured in divisions. The largest number of soldiers in a garrison is this value multiplied by `MEN_PER_DIVISION`.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 127, but doesn't enforce it. The vanilla comment says 0–16000, which doesn't match the code. |
| **Required** | Yes |

```text
**0-16000
REGION_MAX_DIVS: 34,
```

## Notes

### Staying within the stated maximums

Several of these values size internal storage when the game starts, for example the number of soldier slots in each division. Going above the maximums named in the game's code won't cause a loading error, but nothing in the game is designed for it. Staying within them is the safe choice.

## Related

- [init/config](00-config.md)
- [init/battle](../02-battle/00-battle.md)
