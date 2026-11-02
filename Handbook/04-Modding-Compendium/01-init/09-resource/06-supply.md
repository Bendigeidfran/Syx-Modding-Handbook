# init/resource/supply

Each file in `init/resource/supply` defines one army supply: a resource that some of your troops consume. Supplies are shipped automatically to armies from the supply depots in your capital. Running short can hurt an army's health, while keeping it stocked can raise its morale.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/supply/` |
| **Files** | One `.txt` file per supply, e.g. `RATION.txt` |
| **Key** | The file name without `.txt`, e.g. `DRINK`. A race's `MILITARY_SUPPLY_USE` block uses this key. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded. |

Vanilla has four supplies: `CLOTHES`, `DRINK`, `RATION` and `SITHILON`. The supply's name in the game is built from its resource's name.

## Tags

The examples below come from the vanilla `CLOTHES.txt` unless stated otherwise.

### RESOURCE

The resource this supply uses, by its key. Two supplies can't use the same resource: that stops the game from loading with an error. A supply's key doesn't have to match its resource: the vanilla `DRINK.txt` uses `ALCO_BEER`.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: CLOTHES,
```

### MORALE_ADD

The most this supply can add to an army's morale. The bonus is this value, times the share of the army's men who use the supply, times how well stocked it is compared with the minimum the army needs. This example comes from the vanilla `DRINK.txt`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
MORALE_ADD: 0.4,
```

### HEALTH_EFFECT

How much running out of this supply can reduce an army's health. The army's health is multiplied by 1 minus this value, times the share of its men who use the supply, times how far short the stock is of the minimum the army needs. So at `1`, as with vanilla rations, a fully affected army with no stock has no health.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
HEALTH_EFFECT: 0.5,
```

### CONSUMPTION_PER_USER_DAY

How much of the supply each soldier who uses it consumes per day. An army also tries to keep up to 6 extra days' worth in store.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
CONSUMPTION_PER_USER_DAY: 0.03125,
```

### CONSUMPTION_PER_ITEM_DAY

The share of the supply an army holds that's lost per day, counting no more than the minimum the army needs. It suits supplies that wear out rather than being used up. Vanilla only uses this for `SITHILON`, with `0.01`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1000 |
| **Required** | Yes |

```text
CONSUMPTION_PER_ITEM_DAY: 0,
```

### AMOUNT_PER_PERSON

How many items of the supply an army must hold for each soldier who uses it, on top of what's consumed.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked |
| **Required** | Yes |

```text
AMOUNT_PER_PERSON: 1,
```

### RACES

The races whose soldiers use this supply, as a list of race keys. `*` means every race. Each of these races uses it at a rate of 1. A race's own [`MILITARY_SUPPLY_USE`](../07-race/01-race-file.md#military_supply_use) block can override this. The vanilla `SITHILON.txt` has an empty list.

| | |
|---|---|
| **Type** | List of keys (races) |
| **Required** | No. Without it, no race uses the supply unless its race file says so. |

```text
RACES: [
	*,
],
```

## Related

- [init/resource](00-resource.md)
- [The resource file](01-resource-file.md)
- [The race file](../07-race/01-race-file.md)
