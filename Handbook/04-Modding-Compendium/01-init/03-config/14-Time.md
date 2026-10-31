# init/config/Time.txt

`Time.txt` sets the shape of the game's calendar: how many days make up a season, how long nights are in each season, and how years group into ages.

The length of a day itself is set elsewhere, by `SECONDS_PER_HOUR` and `HOURS_PER_DAY` in [Sett.txt](11-Sett.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/Time.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new seasons** | No. The four seasons are built into the game. |
| **Companion files** | `assets/text/misc/Time.txt`, which holds the names of the seasons and ages |

## Tags

### DAYS_PER_SEASON

How many days each season lasts. A year is four seasons.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 2 or more. The game's code names a maximum of 8, but doesn't enforce it. |
| **Required** | Yes |

```text
DAYS_PER_SEASON: 4,
```

### SPRING, SUMMER, AUTUMN and WINTER

One block for each season. All four are required, and each contains the tags below. The game blends smoothly from one season's values to the next.

```text
WINTER: {
	NIGHTRATIO: 0.4,
	RED: 1.7,
	GREEN: 1.7,
	BLUE: 1.7,
},
```

#### NIGHTRATIO

The share of each day that is night. Vanilla gives winter the longest nights (`0.4`) and summer the shortest (`0.25`).

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.1 to 0.9 |
| **Required** | Yes |

#### RED, GREEN and BLUE

The game reads these values, but in v0.71.44 nothing uses them: changing them has no effect.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes, all three. The tags must be present even though they have no effect. |

### YEARS_PER_AGE

How many years make up an age.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes |

```text
YEARS_PER_AGE: 250,
```

### AGES

How many ages there are.

The companion text file must list at least this many age names in its `AGES` list, or the game won't load.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 1000, but doesn't enforce it. |
| **Required** | Yes |

```text
AGES: 5,
```

## The text file

`assets/text/misc/Time.txt` gives the names of the four seasons and the list of age names:

```text
SPRING: "Spring",
SUMMER: "Summer",
AUTUMN: "Autumn",
WINTER: "Winter",
AGES: ["First Age", "Second Age", "Third Age", "Forth Age", "Fifth Age",],
```

## Notes

### Seasons and temperature

How warm each season is isn't set here. A settlement's temperature comes from its climate: see [TEMP_COLD and TEMP_WARM in CLIMATE.txt](02-CLIMATE.md#temp_cold-and-temp_warm).

## Related

- [init/config](00-config.md)
- [init/config/Sett.txt](11-Sett.md)
- [init/config/CLIMATE.txt](02-CLIMATE.md)
