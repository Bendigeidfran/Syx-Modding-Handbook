# init/config/Sett.txt

`Sett.txt` holds settings for your settlement as a whole: the size of the map, the length of a day, how demanding your subjects are, and values for tourism and raiding.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/Sett.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | None |

## Tags

### HAPPINESS_EXPONENT

How much it matters that your subjects' needs are only partly met. The game works out how well a subject's needs are fulfilled as a fraction, then raises that fraction to this power.

With higher values, partly met needs count for much less: subjects are only well satisfied when their needs are close to fully met. With lower values, partial fulfilment counts for more.

This is the starting value of a boostable stat, so other boosts in the game can adjust it.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
HAPPINESS_EXPONENT: 2.65,
```

### MAX_POP

How quickly your subjects' expectations grow as your population grows. The game multiplies this value by 40,000 to give a reference population. Expectations rise in proportion to your population divided by that reference.

Higher values mean expectations grow more slowly, so a larger settlement can be kept content. Like `HAPPINESS_EXPONENT`, this is the starting value of a boostable stat.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
MAX_POP: 0.7143,
```

The vanilla comment above these two tags describes them as working together to determine fulfilment.

### SECONDS_PER_HOUR and HOURS_PER_DAY

The length of an in-game hour, in seconds, and of an in-game day, in hours. Together they set how long a day lasts.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes, both |

```text
SECONDS_PER_HOUR: 48,
HOURS_PER_DAY: 24,
```

### TOURIST_PER_YEAR_MAX

The most tourists who can visit your settlement in a year.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes |

```text
TOURIST_PER_YEAR_MAX: 2048,
```

### TOURIST_CRETIDS

How much money tourists bring. The amount a tourist spends is this value multiplied by the tourist's race's own `CREDITS` setting. Note the game's spelling, `CRETIDS`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
TOURIST_CRETIDS: 7500,
```

### POP_RAIDER_WORTH

How raiders weigh your population against your wealth when judging how tempting a target you are. Your population is multiplied by this value and your money is divided by it, so higher values make raiders care more about the size of your population and less about your treasury.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 10000, but doesn't enforce it. |
| **Required** | Yes |

```text
POP_RAIDER_WORTH: 600,
```

### DIMENSION

The width and height of a settlement map, in tiles. Maps are always square.

The value must be a multiple of 64, or the game stops with an error.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 256 or more, and a multiple of 64. The game's code names a maximum of 16000, but doesn't enforce it. |
| **Required** | Yes |

```text
**must be a multiple of 64
DIMENSION: 768,
```

## Related

- [init/config](00-config.md)
- [init/config/Time.txt](14-Time.md)
