# init/religion

Each file in `init/religion` defines one religion: its icon and colour, how readily it spreads across the world map, which other religions its followers clash with, and the bonuses it gives. Every subject follows one religion, and each region of the world map has a share of each. Religions show up in your settlement's religion statistics, in temples and shrines, and in the region screens of the world map.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/religion/` |
| **Files** | One `.txt` file per religion, e.g. `AMINION.txt` |
| **Key** | The file name without `.txt`, e.g. `AMINION`. Other files use this key to refer to the religion. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded as a religion. |
| **Text file** | `assets/text/religion/<KEY>.txt`, which must exist and have the same name |
| **Icons** | Vanilla's are in `assets/sprite/icon/32/religion/`, named by the `ICON` tag. |

Vanilla has four religions: `AMINION`, `ATHURI`, `CRATOR` and `SHMALOR`.

## How religions spread

Religions spread in two separate ways, one for your settlement and one for the world map, and they use different values.

**In your settlement**, every religion has a conversion value, which starts at 1 for all of them. A new subject picks a religion at random, with a chance in proportion to these values. After that, each subject occasionally reconsiders, with the odds favouring their current religion and any with a higher value.

These things change a religion's conversion value:

- each kind of temple for the religion that has been built adds 1.5, and each kind of shrine adds 1.25;
- boosts can change it, using the name `RELIGION_<KEY>_CITY`. Vanilla races use this to favour a religion, as in this example from `CANTOR.txt`:

```text
RELIGION_*>ADD: -1.0,
RELIGION_ATHURI*>ADD: 5.0,
```

**On the world map**, each region's share of each religion follows a separate value, `WORLD_CONVERSION_<KEY>`, which starts at the religion's `DEFAULT_SPREAD`. Boosts can change this one too; some vanilla events do.

## Tags

The examples below come from the vanilla `AMINION.txt` unless stated otherwise.

### ICON

The icon that represents the religion in the interface. The value is a path to an icon, separated by `->`: the icon size folder (`16`, `24` or `32`), then any sub-folders, then the image name, then the number of the icon within that image. The path is relative to `assets/sprite/icon/`. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path |
| **Range** | The first part must be `16`, `24` or `32`. |
| **Required** | Yes |

```text
ICON: 32->religion->AMINION->0,
```

### DEFAULT_SPREAD

How readily the religion spreads across the world map, compared with the others. A region's share of each religion follows these values, so a religion with `2` next to one with `1` ends up with about twice as many followers, before any boosts.

This has no effect on your own settlement, where every religion starts from the same value. All the vanilla religions use `1.0`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked |
| **Required** | Yes |

```text
DEFAULT_SPREAD: 1.0,
```

### COLOR

The colour that represents the religion in the settlement's religion charts, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR: 90_10_10,
```

### OPPOSITION

How strongly this religion's followers clash with the followers of other religions. Each entry names a religion by its key, and a missing entry counts as 0. `*` sets every religion at once, including this one, and a key ending in `*` sets every religion whose key begins that way. A name that doesn't match any religion is skipped, and only reported when Debug is on.

Opposition is worked out as a single figure from 0 to 1. For each pair of religions, the game multiplies the first religion's share of the population, the second's share, and the first's value for the second. It adds these up and caps the total at 1. For example, if half your people follow `CRATOR` and half follow `AMINION`, then `CRATOR`'s value of 1 for `AMINION` adds 0.25.

Each religion's file sets its own value for the other, and both are added. They don't have to match: in vanilla, `CRATOR` has 1 for `AMINION`, while `AMINION` has 0 for `CRATOR`.

The figure is used in two places:

- **In your settlement**, it's the stat `RELIGION_RELIGION_OPPOSITION`. Each race decides how much this matters to it in its `STATS` block.
- **In a world map region**, it lowers every race's loyalty target there, by up to 25% when the figure reaches 1.

| | |
|---|---|
| **Type** | Block of decimals, keyed by religion |
| **Range** | Each value 0 to 100 |
| **Required** | No. Without it, all this religion's values are 0, though others can still list it. |

```text
OPPOSITION: {
	ATHURI: 4,
	CRATOR: 0,
	SHMALOR: 0,
},
```

### BOOST

The religion's bonuses and penalties, in the same form as a race's [`BOOST`](07-race/01-race-file.md#boost) block.

How strongly they apply depends on what they affect:

- **Boosts to things in your settlement** apply to each subject according to their own religion, scaled by their access to its temples and the quality of those temples.
- **Boosts to things on the world map**, such as those beginning `WORLD_`, are scaled by the religion's share of the population in each region.
- **For an AI faction**, boosts to things in a settlement come from the religion of its king, at full strength.

A few boosts count as neither, such as those beginning `EQUIP_` and some internal world map ones. A religion's boost to one of these has no effect.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	BEHAVIOUR_SUBMISSION>MUL: 1.20,
	WORLD_LOYALTY*>MUL: 1.20,
	PHYSICS_HEALTH>MUL: 1.1,
	PHYSICS_DEATH_AGE>MUL: 1.1,
},
```

## The text file

Each religion needs a file of the same name in `assets/text/religion/`. Vanilla writes these tags at the top level of the file. `NAME`, `NAMES`, `DESC` and `WIKI` can also go inside an `INFO` block, but `DEITY` must stay at the top level.

### NAME

The religion's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Aminionism",
```

### NAMES

The plural of the religion's name. Vanilla doesn't use it.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

### DEITY

The name of the religion's god. It's used wherever the game's text names the god, such as the message about a war between faiths, and in text that uses the placeholder `{RELIGION_GOD}`.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DEITY: "Aminion",
```

### DESC

The religion's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Aminion, the lord of chaos promotes submission and his temples accepts human sacrifices (prisoners).",
```

### WIKI

Adds an article about the religion to the in-game wiki. All the vanilla religions have one. The tags inside it are described in full under [`WIKI` on the init/animal page](01-animal.md#wiki). The `TEXT` in this example is shortened.

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Without it, the religion has no article. |

```text
WIKI: {
	NAME: "Aminionism",
	CATEGORY: "Religion",
	TEXT: "Aminion was once kind and just, and ruled the Astarii alongside Athuri, being the strongest among them. ...",
},
```

## Notes

### Temples and shrines

A religion's temples and shrines are ordinary rooms, defined in `assets/init/room/`, that name the religion with a `RELIGION` tag, e.g. `RELIGION: AMINION,` in `TEMPLE_AMINION.txt` and `SHRINE_AMINION.txt`. A new religion doesn't need them to load or to gain followers, but without them its followers have nowhere to worship, so you'll normally want to add both.

### War of the faiths

The game has a "War of the faiths" event, in which followers of two religions fight each other. Despite its message about "opposing faiths", it doesn't look at `OPPOSITION`: it picks two religions that have followers, whatever their values.

### Where religions are used

Other files refer to religions by their key, or by names built from it:

- **Rooms** use it in the `RELIGION` tag, as above.
- **Boosts** can use `RELIGION_<KEY>_CITY` and `WORLD_CONVERSION_<KEY>`.
- **Conditions** can use values such as `RELIGION_SHMALOR_F`, as in the [world camp requirements](07-race/08-worldcamp.md#requires_min).

## Related

- [init](00-init.md)
- [Modding Compendium](../00-Modding-Compendium.md)
