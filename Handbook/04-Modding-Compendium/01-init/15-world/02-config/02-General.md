# init/world/config/General.txt

`General.txt` holds the main settings for the world map.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/world/config/General.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### TILE_DIMENSION

The width and height of the world map, in tiles.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 128 or more. The game's code names a maximum of 512 but doesn't enforce it. |
| **Required** | Yes |

```text
TILE_DIMENSION: 256,
```

### TRADE_ROUTE_SHIP_MAX

The game never reads this tag.

| | |
|---|---|
| **Type** | Integer |
| **Required** | No |
| **Effect** | Unread |

```text
TRADE_ROUTE_SHIP_MAX: 50,
```

### REGION_SIZE

Added to the budget the map generator spends on tiles when it marks out a region, so higher values make for larger regions.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 1000 but doesn't enforce it. |
| **Required** | Yes |

```text
REGION_SIZE: 50,
```

### FOREST_AMOUNT

How much of the map is forest, from 0 to 1. Higher values give more forest.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
FOREST_AMOUNT: 0.3,
```

### POPULATION_CAPACITY_MAX

Sets how many people a region not held by the player can hold for its area, which the game then scales by moisture and chance. The player's regions get their capacity from the `WORLD_POPULATION_CAPACITY` boost instead.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 100000 but doesn't enforce it. |
| **Required** | Yes |

```text
POPULATION_CAPACITY_MAX: 100,
```

### POPULATION_PLAYER_REGION

The game never reads this tag.

| | |
|---|---|
| **Type** | Integer |
| **Required** | No |
| **Effect** | Unread |

```text
POPULATION_PLAYER_REGION: 200,
```

## Related

- [init/world/config](00-config.md)
