# init/stats/dynamicBoost

These files add new boostable values to the game, on top of the ones built into its code. Vanilla uses them for administration and knowledge, the two values its admin rooms and libraries produce.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/dynamicBoost/` |
| **Files** | One `.txt` file per value, e.g. `ADMIN.txt` |
| **Key** | The file name, e.g. `ADMIN` |
| **Boost name** | `<CATEGORY>_<KEY>`, e.g. `CIVIC_ADMIN` |
| **Adding new values** | Yes |
| **Text file** | `assets/text/stats/dynamicBoost/<KEY>.txt`, required |

## Tags

The examples come from the vanilla `ADMIN.txt`.

### ICON

The value's icon, written as an icon path.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path, or a block |
| **Required** | Yes |

```text
ICON: 32->INFRA->0,
```

### CATEGORY

The group the value belongs to, which also starts its boost name. The groups are `PHYSICS`, `BEHAVIOUR`, `ACTIVITY`, `BATTLE`, `CIVIC`, `ROOM` and `NOBLE`.

| | |
|---|---|
| **Type** | Text, one of the groups above |
| **Required** | Yes. With any other name, the game writes an error to its log and skips the file. |

```text
CATEGORY: CIVIC,
```

### BASE_VALUE

The value before any boosts.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | -100000 to 100000 |
| **Required** | Yes |

```text
BASE_VALUE: 0,
```

## The text file

Each value needs a file of the same name in `assets/text/stats/dynamicBoost/`. These examples come from the vanilla `ADMIN.txt`.

### NAME

The value's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Administration",
```

### DESC

The value's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Used for technologies.",
```

## Notes

### Using a new value

A new value does nothing until something refers to its boost name. In vanilla, an admin room adds to `CIVIC_ADMIN` through its [`BOOST`](../10-room/09-infra.md) tag, and a technology spends it through [`COSTS`](../14-tech.md#costs):

```text
BOOST: CIVIC_ADMIN,
```

## Related

- [init/stats](00-stats.md)
- [init/room: infrastructure rooms](../10-room/09-infra.md)
- [BOOST in the race file](../07-race/01-race-file.md#boost)
