# init/resource/edible

A file in `init/resource/edible` makes a resource a food. Foods can be served in eateries and canteens, and a race's favourite foods are chosen from them.

Most of these files are empty: it's the file's existence that makes the resource edible.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/edible/` |
| **Files** | One `.txt` file per food, e.g. `BREAD.txt`. A file can be empty. |
| **Key** | The file name without `.txt`, which must be the key of a resource. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded. There must be at least one. |

Vanilla has eight foods: `BREAD`, `EGG`, `FISH`, `FRUIT`, `MEAT`, `MUSHROOM`, `RATION` and `VEGETABLE`.

## Tags

### DONT_SERVE

If `true`, canteens, eateries, prisons and stockades don't use this food. It still counts as a food. Vanilla uses this for `RATION`, which is also an army supply. This example comes from the vanilla `RATION.txt`.

| | |
|---|---|
| **Type** | True/false |
| **Required** | No. Default `false`. |

```text
DONT_SERVE: true,
```

## Notes

### Where foods are used

A race's [`PREFERRED.FOOD`](../07-race/02-preferences.md#food) list names foods by their key.

## Related

- [init/resource](00-resource.md)
- [The resource file](01-resource-file.md)
