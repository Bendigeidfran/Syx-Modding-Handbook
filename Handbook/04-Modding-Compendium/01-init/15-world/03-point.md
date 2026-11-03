# init/world/point

These files define the points that [region buildings](01-building.md) produce and use up. Vanilla has one, workforce. Each region keeps its own total: buildings add to it, and running a building takes from it.

The game also treats `CIVIC_GOV` as a point of this kind. That one is built into its code.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/world/point/` |
| **Files** | One `.txt` file per point, e.g. `WORKFORCE.txt` |
| **Key** | The file name, e.g. `WORKFORCE` |
| **Boost name** | `WORLD_POINT_<KEY>`, e.g. `WORLD_POINT_WORKFORCE` |
| **Adding new points** | Yes |
| **Text file** | `assets/text/world/point/<KEY>.txt`, required |

## Tags

The examples come from the vanilla `WORKFORCE.txt`.

### ICON

The point's icon. It can be written in any of the forms described under [`ICON` for technologies](../14-tech.md#icon_1).

| | |
|---|---|
| **Type** | Icon path, a block or a list of blocks |
| **Required** | Yes |

```text
ICON: 24->BuildPoints->1,
```

### BOOST

What points left unused in a region do, written in the same way as a race's [`BOOST`](../07-race/01-race-file.md#boost) block. In a region, the effect is the value in the file × the unused points ÷ 1000000. The large number in this example therefore gives 150 tax income for each unused point. A region with no points to spare gets nothing.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	WORLD_TAX_INCOME>ADD: 150000000,
},
```

## The text file

Each point needs a file of the same name in `assets/text/world/point/`. These examples come from the vanilla `WORKFORCE.txt`.

### NAME

The point's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Workforce",
```

### NAMES

The plural of the point's name. Vanilla doesn't use it here.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

### DESC

The point's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Can be used to construct and run buildings in a region. Excess workforce is used for industries.",
```

### WIKI

Adds an article about the point to the in-game wiki. Vanilla doesn't use it here. The tags inside it are described under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

## Notes

### Running short

In the player's regions, if a building's costs take a point below 0, the efficiency of buildings using that point falls with the shortfall. `EFFICIENCY_<KEY>`, such as `EFFICIENCY_WORKFORCE`, is a region value that other files can read, and it's 1 when nothing is short.

## Related

- [init/world](00-world.md)
- [init/world/building](01-building.md)
