# init/resource: the resource file

Each file directly in `init/resource` defines one resource: its icon, the images used when it's carried or lying on the ground, how fast it spoils, and where it's listed in the interface.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/resource/` |
| **Files** | One `.txt` file per resource, e.g. `BREAD.txt` |
| **Key** | The file name without `.txt`, e.g. `BREAD`. Other files use this key to refer to the resource. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded as a resource, as well as the three required files below. Each resource also needs a room that produces it; see the notes. |
| **Required files** | `_STONE.txt`, `_WOOD.txt` and `_LIVESTOCK.txt`, which the game loads by name. |
| **Text file** | `assets/text/resource/<KEY>.txt`, which must exist and have the same name |
| **Images** | In `assets/sprite/resource/` and `assets/sprite/resource/debris/`, named by the `SPRITE` and `SPRITE_DEBRIS` tags. |

## Tags

The examples below come from the vanilla `BREAD.txt` unless stated otherwise.

### ICON

The icon that represents the resource in the interface. The value is a path to an icon, separated by `->`: the icon size folder (`16`, `24` or `32`), then any sub-folders, then the image name, then the number of the icon within that image. The path is relative to `assets/sprite/icon/`.

| | |
|---|---|
| **Type** | Icon path |
| **Range** | The first part must be `16`, `24` or `32`. |
| **Required** | Yes |

```text
ICON: 24->resource->Bread->0,
```

### DEGRADE_RATE

How quickly the resource spoils. The resource's tooltip shows this as the share lost per year, so `1.0` is 100% a year and `0.1` is 10%. The tooltip also shows half that rate, adjusted by your spoilage bonuses, for stored goods. With `0`, the resource never spoils.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DEGRADE_RATE: 1.0,
```

### COLOR

A tint applied to the resource's image, written as `RED_GREEN_BLUE`, when it's carried or lying on the ground. Vanilla uses white, `255_255_255`, for every resource, which leaves the image as it is.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR: 255_255_255,
```

### MINIMAP_COLOR

The colour of the resource on the minimap when it's lying on the ground.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
MINIMAP_COLOR: 10_10_10,
```

### SPRITE

The resource's image: the name of a file in `assets/sprite/resource/`, without `.png`. It holds both how the resource looks when carried and how it looks lying on the ground. Several resources can share one image.

The image must be exactly 244 pixels wide and at least 94 pixels tall, or the game stops loading with an error. The game cuts it up using a fixed layout, so the safest way to make a new one is to copy a vanilla image and paint over it.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/resource/`) |
| **Required** | Yes |

```text
SPRITE: Bread,
```

### SPRITE_DEBRIS

The debris drawn when something made of this resource is broken, such as a destroyed wall or room furniture: the name of a file in `assets/sprite/resource/debris/`, without `.png`. Vanilla has `Metal`, `Stone` and `Wood`.

The image must be exactly 716 pixels wide and at least 28 pixels tall, or the game stops loading with an error.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/resource/debris/`) |
| **Required** | Yes |

```text
SPRITE_DEBRIS: Wood,
```

### CATEGORY_DEFAULT

The group the resource is listed in. Resources are ordered by this number throughout the game, and the stockpile's settings and the resource list on the right of the settlement screen separate the groups. Vanilla uses `0` to `4`.

A value of 10 or more crashes the game while loading. So does having more than 64 resources in one group, or more than 128 in total. These limits count vanilla and every enabled mod together, though a file with the same name in several places counts once.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 3 in one place and 10 in another, but enforces neither, and vanilla itself uses 4. Stay below 10. |
| **Required** | Yes |

```text
CATEGORY_DEFAULT: 0,
```

### PRICE_MUL

Multiplies the price AI factions ask for this resource. A race's [`RESOURCE_RPICE_MUL`](../07-race/02-preferences.md#resource_rpice_mul-and-resource_rpice_cap) block can override it for factions ruled by that race.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100 |
| **Required** | No. Default `1`. |

```text
PRICE_MUL: 1.0,
```

### PRICE_CAP

The default for a race's [`RESOURCE_RPICE_CAP`](../07-race/02-preferences.md#resource_rpice_mul-and-resource_rpice_cap). It's shown in the world map's trade information, but in v0.71.44 it doesn't change any price. This example comes from the vanilla `_WOOD.txt`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `1`. |

```text
PRICE_CAP: 1.0,
```

## The text file

Each resource needs a file of the same name in `assets/text/resource/`. Vanilla writes these tags at the top level of the file, but they can also go inside an `INFO` block.

### NAME

The resource's singular name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Bread",
```

### NAMES

The resource's plural name.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

```text
NAMES: "Bread",
```

### DESC

The resource's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Bread is a staple food, produced by bakeries.",
```

### WIKI

Adds an article about the resource to the in-game wiki. No vanilla resource has one. The tags inside it are described in full under [`WIKI` on the init/animal page](../01-animal.md#wiki).

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Without it, the resource has no article. |

## Notes

### Every resource needs a producer

Every resource must have at least one room that can produce it, or the game crashes while it's running. It doesn't stop with an error when loading, so a new game can start normally before this happens. To count as a producer, a room must meet all of these:

- **It produces the resource at a rate above 0.** Most rooms set this in [`INDUSTRY.OUT`](../10-room/03-production.md#industryout). The rate that counts is `AI_RATE` if it's there, not `PLAYER`.
- **Its ingredients can be produced too.** Each resource in its `IN` block needs a producer of its own. Resources that only make each other, with nothing to start the chain, don't count. The game only looks 10 passes deep, so a very long chain might not count either.
- **It isn't a Hunter room.** The game ignores what `HUNTER_` rooms produce here.

There are two ways the crash can happen. With no room producing the resource at all, it happens when an AI faction's stockpile updates. With a room that doesn't meet the other conditions, it happens when the game's advice panel counts your resources.

### Limits

The game holds at most 128 resources, and at most 64 in any one `CATEGORY_DEFAULT` group. Vanilla and every enabled mod count together, and a file with the same name in several places counts once. Going over either limit crashes the game while loading. Vanilla has 42, so keep this in mind if your mod is likely to be used alongside others that add resources.

### The three required resources

`_STONE`, `_WOOD` and `_LIVESTOCK` are used directly by the game's code, so they must exist even if you use `_IgnoreVanilla.txt`.

### Unused text file

`assets/text/resource/WEAPON.txt` has no matching resource, so the game doesn't read it.

### Where resources are used

Other files refer to resources by their key, including [race files](../07-race/01-race-file.md#resource), [animals](../01-animal.md#resources) and the room files in `assets/init/room/`.

## Related

- [init/resource](00-resource.md)
- [init](../00-init.md)
