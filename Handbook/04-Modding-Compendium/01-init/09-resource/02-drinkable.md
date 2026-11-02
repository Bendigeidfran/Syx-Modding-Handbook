# init/resource/drinkable

A file in `init/resource/drinkable` makes a resource a drink. Drinks are served in taverns, and a race's favourite drinks are chosen from them.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/drinkable/` |
| **Files** | One `.txt` file per drink, e.g. `ALCO_BEER.txt` |
| **Key** | The file name without `.txt`, which must be the key of a resource. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded. There must be at least one. |

Vanilla has two drinks: `ALCO_BEER` and `ALCO_WINE`.

## Tags

### COLOR

The colour of the drink in the jugs on tavern tables, written as `RED_GREEN_BLUE`. This example comes from the vanilla `ALCO_BEER.txt`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR: 255_255_20,
```

### DONT_SERVE

If `true`, taverns don't serve this drink. It still counts as a drink. Vanilla doesn't use this tag for drinks, though it does for [food](03-edible.md#dont_serve).

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

## Notes

### Where drinks are used

A race's [`PREFERRED.DRINK`](../07-race/02-preferences.md#drink) list names drinks by their key.

## Related

- [init/resource](00-resource.md)
- [The resource file](01-resource-file.md)
