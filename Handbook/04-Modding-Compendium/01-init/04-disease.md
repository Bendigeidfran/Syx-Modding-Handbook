# init/disease

Each file in `init/disease` defines one disease: how it spreads, how long it lasts, how deadly it is, and where it's likely to break out. Diseases come in two kinds:

- **Epidemics** break out as events, infecting many subjects at once.
- **Regular diseases** are everyday illnesses that individual subjects catch from time to time.

A disease can be either, both or neither. The folder also contains `_CONFIG.txt`, a separate settings file for regular sickness.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/disease/` |
| **Files** | One `.txt` file per disease, e.g. `PLAGUE.txt`, plus `_CONFIG.txt` |
| **Key** | The file name without `.txt`, e.g. `PLAGUE` |
| **Adding new files** | Yes. Every file not starting with `_` is loaded as a disease. There must be at least 1 and at most 120. |
| **Text file** | `assets/text/disease/<KEY>.txt`, which must exist and have the same name |

Vanilla has six diseases: `BLEEDING_FEVER`, `PLAGUE`, `RIVER_RUNS` and `SWAMP_LUNG` (epidemics), and `VISION_FEVER` and `WHITE_SHIMMER` (regular).

## Tags

The examples below come from the vanilla `PLAGUE.txt` unless stated otherwise.

### EPIDEMIC

Whether the disease can break out as an epidemic. When an epidemic event occurs, the game chooses one of the diseases marked `true`, weighted by their occurrence (see [OCCURRENCE_CLIMATE](#occurrence_climate) and [OCCURRENCE_TERRAIN](#occurrence_terrain)).

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
EPIDEMIC: true,
```

### REGULAR

Whether subjects can catch the disease as an everyday illness. When a subject falls ill this way, the game chooses one of the diseases marked `true`, again weighted by occurrence. How often this happens is set in `_CONFIG.txt`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
REGULAR: false,
```

### SPREAD

How widely the disease spreads in an outbreak. When an outbreak occurs, each of your subjects' chance of being infected is proportional to this value, so higher values mean an epidemic infects more of your population.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
SPREAD: 0.60,
```

### INCUBATION_DAYS

How long an infected subject carries the disease before falling sick. The moment they fall sick is random, but longer incubation means a longer wait on average. Incubation also counts towards how long an epidemic event lasts.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 100, but doesn't enforce it. |
| **Required** | Yes |

```text
INCUBATION_DAYS: 3,
```

### INFECTION_DAYS

How many days a sick subject stays sick. Medical treatment shortens it: a subject receiving full treatment recovers sooner.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 100, but doesn't enforce it. |
| **Required** | Yes |

```text
INFECTION_DAYS: 3,
```

### FATALITY_RATE

The chance that an infected subject will die of the disease. The game rolls against this chance when the subject is infected, and rolls again if they move from incubating to sick; the latest roll is the one that counts. For certain types of subject, the chance is multiplied by a random factor of up to 6.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
FATALITY_RATE: 0.3,
```

### COLOR

The tint applied to the appearance of subjects who are sick with the disease, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR: 150_160_160,
```

### OCCURRENCE_CLIMATE

How likely the disease is in each climate. The block can contain `COLD`, `TEMPERATE` and `HOT`, and `*` sets all three at once. A climate missing from the block counts as `0`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by climate |
| **Range** | Each value 0 to 100000 |
| **Required** | No, but if it's missing the disease never occurs. |

From `SWAMP_LUNG.txt`:

```text
OCCURRENCE_CLIMATE: {
	*: 1,
	HOT: 0,
},
```

### OCCURRENCE_TERRAIN

How likely the disease is on each type of terrain: `OCEAN`, `WET`, `MOUNTAIN`, `FOREST` and `NONE` (open land). `*` sets all of them at once, and a terrain missing from the block counts as `0`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by terrain |
| **Range** | Each value 0 to 100000 |
| **Required** | No, but if it's missing the disease never occurs. |

From `RIVER_RUNS.txt`:

```text
OCCURRENCE_TERRAIN: {
	*: 0,
	WET: 1,
},
```

## How occurrence is worked out

A disease's occurrence in your settlement combines both blocks. For each terrain, the game multiplies the disease's terrain value by how much of your settlement's area is that terrain, and takes the **highest** of these. It then multiplies that by the disease's value for your settlement's climate.

When the game picks a disease, each eligible disease's chance is its occurrence divided by the total occurrence of all of them. So The River Runs (`RIVER_RUNS`), with `WET: 1` and every other terrain at `0`, only appears in settlements with wet terrain, and is more likely the more wet terrain there is.

## The config file

`_CONFIG.txt` holds a single setting for regular sickness. Because its name starts with an underscore, it isn't loaded as a disease.

### REGULAR_SICKNESS_DAY_INVERVAL

How often subjects catch a regular disease. Each day, every subject has a one-in-N chance of falling ill, where N is this value multiplied by one plus the subject's health. Healthier subjects therefore fall ill less often. Note the game's spelling, `INVERVAL`.

Only your own subjects catch regular diseases this way.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 1 to 10000000 |
| **Required** | Yes |

```text
REGULAR_SICKNESS_DAY_INVERVAL: 64,
```

## The text file

Each disease needs a file of the same name in `assets/text/disease/`:

```text
NAME: "The Plague",
DESC: "The vicious plague is deadly, tormenting its victims for days before usually ending their lives. Painful, pus-filled boils appear all over the infected, swiftly sapping their strength and often leading to death.",
```

| Tag | Meaning | Required |
|---|---|---|
| `NAME` | The disease's name. | Yes |
| `NAMES` | A plural name. | No. If it's missing, `NAME` is used. |
| `DESC` | The description. | Yes |

As with animals, the tags can also be wrapped in an `INFO` block.

## Related

- [init](00-init.md)
- [init/config/CLIMATE.txt](03-config/02-CLIMATE.md)
- [init/config/TERRAIN.txt](03-config/13-TERRAIN.md)
