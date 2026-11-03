# init/animal

Each file in `init/animal` defines one species of animal: how big and fast it is, where it lives, what it yields when butchered, and how it reacts to being hunted. Animals roam the settlement map, are hunted for resources, are kept in pastures, pull trade caravans, and serve as mounts for cavalry.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/animal/` |
| **Files** | One `.txt` file per species, e.g. `AUROCH.txt` |
| **Key** | The file name without `.txt`, e.g. `AUROCH`. Other files use this key to refer to the species. |
| **Adding new files** | Yes. Every file not starting with `_` is loaded as a species, so a new file adds a new animal. |
| **Text file** | `assets/text/animal/<KEY>.txt`, which must exist and have the same name. |
| **Sprite sheet** | `assets/sprite/animal/<name>.png`, named by the `SPRITE` tag. |
| **Sound** | An `ANIMAL_CALL_<KEY>` entry in a file in `assets/audio/config/mono/`. |

Vanilla has nine species: `AUROCH`, `BALTICRAWLER`, `DINORIS`, `ENTELODONT`, `GLOBDIEN`, `MOUNT`, `ONX`, `SMILODON` and `STAGBEAST`.

## Tags

The examples below come from the vanilla `AUROCH.txt` unless stated otherwise.

### SPEED

How fast the animal moves. It sets both the animal's top speed and how quickly it accelerates. Vanilla uses `1` (`BALTICRAWLER`) to `6` (`SMILODON`), and most species have `4` or `5`.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 31, but doesn't enforce it. |
| **Required** | Yes |

```text
SPEED: 4,
```

### HEIGHT

How tall the animal is. Each individual animal's height varies up to 25% either side of this value. Vanilla uses `4` (`GLOBDIEN`) to `9` (`MOUNT`, `STAGBEAST`).

The game uses height in three ways:

- **Shadows.** Taller animals cast longer shadows.
- **Drawing order.** Taller things are drawn in front of shorter ones.
- **Collisions.** Two things only collide if they overlap vertically, so height decides whether, for example, an animal that has been knocked into the air passes over another.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 50, but doesn't enforce it. |
| **Required** | Yes |

```text
HEIGHT: 5,
```

### MASS

How heavy the animal is. Each individual animal's weight varies up to 20% either side of this value. Vanilla uses `35` (`DINORIS`) to `300` (`MOUNT`), and most species are between `35` and `110`.

Mass affects several things:

- **Resources yielded when butchered.** See `RESOURCE_AMOUNT`.
- **Pasture capacity.** Heavier animals need more space, so fewer fit in a pasture of the same size.
- **Collisions.** The impact needed to injure an animal rises with its mass (and its `SPEED`), and heavier animals hit harder when they attack (see `DANGER`).

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 500, but doesn't enforce it. |
| **Required** | Yes |

```text
MASS: 110,
```

### DANGER

How quickly the species turns on people. Every time an animal of this species is slaughtered, whether by a hunter or in a pasture, its `DANGER` value is added to a running total for the species. Once the total reaches 4, wild adult animals of that species stop fleeing when disturbed and attack instead. The total resets to zero when one of them kills someone.

Because pasture slaughter counts towards the total, keeping a species in a pasture can make the wild animals of that species aggressive.

For example, with `DANGER: 0.5`, the species turns aggressive after eight kills. With `DANGER: 0`, it never does.

Vanilla uses `0` (`BALTICRAWLER`, `GLOBDIEN`), `0.1` (`ONX`), `0.2` (`MOUNT`, `STAGBEAST`), `0.25` (`DINORIS`, `ENTELODONT`), `0.5` (`AUROCH`) and `1.0` (`SMILODON`).

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DANGER: 0.5,
```

### ICON

The icon that represents the species in the interface. The value is a path to an icon, separated by `->`: the icon size folder (`16`, `24` or `32`), then any sub-folders, then the image name, then the number of the icon within that image. The path is relative to `assets/sprite/icon/`. Numbers count from `0`, left to right and then top to bottom.

For example, `32->animal->Auroch->0` is icon `0` from `assets/sprite/icon/32/animal/Auroch.png`. A bad path or number doesn't stop the game: it draws a plain orange icon instead, and only reports the problem when Debug is on.

| | |
|---|---|
| **Type** | Icon path |
| **Range** | The first part must be `16`, `24` or `32`. |
| **Required** | Yes |

```text
ICON: 32->animal->Auroch->0,
```

### SPRITE

The sprite sheet the animal is drawn from: the name of an image in `assets/sprite/animal/`, without `.png`. Several species can share one sheet.

The image must be exactly 164 pixels wide and at least 462 pixels tall, or the game stops loading with an error. The game cuts it into frames using a fixed layout, so the safest way to make a new sheet is to copy a vanilla one and paint over it.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/animal/`) |
| **Required** | Yes |

```text
SPRITE: Auroch,
```

### COLOR

A colour, written as red, green and blue values from 0 to 255, separated by underscores.

The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no visible effect. When animals are drawn, each one is given its own random shade instead.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Range** | Each part should be 0 to 255. The game doesn't check this, but since the tag has no effect, it doesn't matter. |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
COLOR: 255_255_255,
```

### LIVES_IN_CAVES

The share of this species that spawns in caves. When the game populates an area with animals, this fraction of the species' animals is placed in caves rather than in the open. `0` means none, `1` means all. Most vanilla species have `0`. The exceptions are `GLOBDIEN` with `0.2`, `SMILODON` with `0.5` and `BALTICRAWLER` with `0.8`.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
LIVES_IN_CAVES: 0,
```

### CARAVAN

Whether this species can be drawn as the pack animal for trade caravans and other goods transport. Each time, the game picks one of the species marked `true`. In vanilla, those are `AUROCH` and `ONX`.

At least one loaded species must have `CARAVAN: true`, or the game stops with an error. Keep this in mind if you use `_IgnoreVanilla.txt` to replace the vanilla animals.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
CARAVAN: true,
```

### RESOURCES

The resources the animal yields when butchered, as a list of resource keys. The amount of each is set by `RESOURCE_AMOUNT`, in the same order. A key that doesn't match any resource causes a loading error, so any new resource named here has to exist when the game loads.

Every vanilla species yields `MEAT`, listed first. All but `BALTICRAWLER` also yield a second resource: `LEATHER`, `EGG` or `COTTON`.

| | |
|---|---|
| **Type** | List of keys (resources) |
| **Required** | No. If it's missing, the animal yields nothing, and `RESOURCE_AMOUNT` must be an empty list. |

```text
RESOURCES: [MEAT, LEATHER,],
```

### RESOURCE_AMOUNT

How much of each resource in `RESOURCES` the animal yields, in the same order. The list must have exactly as many entries as `RESOURCES`.

The yield of each resource is the value given here, multiplied by the individual animal's weight (see `MASS`), multiplied by 0.3, rounded up. For an Auroch of exactly average weight, that's 0.8 × 110 × 0.3 = 26.4, rounded up to 27 meat.

Vanilla's `MEAT` values run from `0.5` to `1.15` (`BALTICRAWLER`), and the second resource's from `0.25` to `0.75`.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Must have the same number of entries as `RESOURCES` |
| **Required** | Yes |

```text
RESOURCE_AMOUNT: [0.8, 0.5,],
```

### CLIMATE

How common the species is in each climate. The block can contain `COLD`, `TEMPERATE` and `HOT`. Each value is a weight from 0 to 1. A climate that's missing from the block counts as 0, so the species won't spawn there.

`*` sets every climate at once.

Most vanilla species have `1` in the climate they favour and less in the others. `AUROCH` has `COLD` 0.8, `TEMPERATE` 1 and `HOT` 0, for example. `SMILODON` is the exception, reaching only `0.5`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by climate |
| **Range** | Each value 0 to 1 |
| **Required** | No, but if it's missing the species never spawns in the wild. |

```text
CLIMATE: {
	COLD: 0.8,
	TEMPERATE: 1,
	HOT: 0,
},
```

### TERRAIN

How common the species is on each type of terrain. The block can contain `OCEAN`, `WET`, `MOUNTAIN`, `FOREST` and `NONE` (open land). Each value is a weight from 0 to 1, and `*` works as it does in `CLIMATE`.

When the game populates an area, each species' chance of appearing combines the terrain in that area with these weights, multiplied by the species' `CLIMATE` weight for the area's climate.

Vanilla's values run from `0.05` to `1`. Most species have `1` on the terrain they favour, and `SMILODON` reaches only `0.5`. Only `GLOBDIEN` lists `OCEAN`, and only `BALTICRAWLER` and `SMILODON` list `MOUNTAIN`.

| | |
|---|---|
| **Type** | Block of decimals, keyed by terrain |
| **Range** | Each value 0 to 1 |
| **Required** | No, but if it's missing the species never spawns in the wild. |

```text
TERRAIN: {
	FOREST: 0.5,
	WET: 0.5,
	NONE: 1.0,
},
```

### PACK

Whether the species lives in packs.

The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
PACK: true,
```

### GRAZES

Whether the species grazes.

The game reads and stores this value, but in v0.71.44 nothing uses it: changing it has no effect.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes. The tag must be present even though it has no effect. |
| **Effect** | None |

```text
GRAZES: true,
```

### DAMAGE

Damage values for the animal, keyed by damage type. The damage types are defined in [`assets/init/stats/damage/`](13-stats/02-damage.md); vanilla has `PIERCE` and `SLASH`.

The game reads and stores these values, but in v0.71.44 nothing uses them: changing them has no effect. When an aggressive animal attacks (see `DANGER`), the damage it deals is based on its weight, not on this block.

| | |
|---|---|
| **Type** | Block of decimals, keyed by damage type |
| **Range** | Each value 0 to 10000 |
| **Required** | No |
| **Effect** | None |

```text
DAMAGE: {
	PIERCE: 0.4,
},
```

## The text file

Each species needs a file of the same name in `assets/text/animal/`, holding its name and description. Vanilla wraps these tags in an `INFO` block, but they can also be written at the top level of the file. If `NAME` is at the top level, the game reads all of them from there; otherwise it reads them from `INFO`.

```text
INFO: {
	NAME: "Auroch",
	NAMES: "Aurochs",
	DESC: "Aurochs are giant beasts, found in the north, with a ferocious temperament.",
},
```

### NAME

The species' singular name, shown in the game's interface.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Auroch",
```

### NAMES

The species' plural name.

| | |
|---|---|
| **Type** | Text |
| **Required** | No. If it's missing, `NAME` is used. |

```text
NAMES: "Aurochs",
```

### DESC

The species' description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
DESC: "Aurochs are giant beasts, found in the north, with a ferocious temperament.",
```

### WIKI

Adds an article about the species to the in-game wiki. It goes next to `NAME`, so if the file uses an `INFO` block, `WIKI` must be inside it. No vanilla animal has one; rooms and religions do, and the examples for these tags come from the vanilla `text/room/WELL_NORMAL.txt` unless stated otherwise.

The article appears in the wiki's own list. Nothing on an animal's interface links to it.

| | |
|---|---|
| **Type** | Block |
| **Required** | No. Without it, the species has no article. |

```text
WIKI: {
	CATEGORY: "Service",
	NAME: "Well",
	TEXT: "Can be used to endure hot weather or get clean.",
	CATEGORIES: [],
},
```

### WIKI.NAME

The article's title.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, if the `WIKI` block is present. |

```text
NAME: "Well",
```

### WIKI.CATEGORY

The category the article is listed under in the wiki. It's free text, so writing a new one creates a new category.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, if the `WIKI` block is present. |

```text
CATEGORY: "Service",
```

### WIKI.TEXT

The article itself, which can include links and coloured text.

The markup is:

- `<a LINK_KEY TEXT>` shows `TEXT` as a link to the article with that `LINK_KEY`.
- `<c RRR_GGG_BBB TEXT>` shows `TEXT` in that colour.

Don't use `<` for anything else. The game treats it as a mistake and drops it along with the character after it, and only reports this when Debug is on. The game's own error message also mentions `<u TEXT>` for underlined text, but v0.71.44 doesn't support it.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes, if the `WIKI` block is present. |

```text
TEXT: "Can be used to endure hot weather or get clean.",
```

### WIKI.LINK_KEY

A name other articles can use to link to this one with `<a LINK_KEY TEXT>`. Each `LINK_KEY` can be used by only one article: a duplicate is a loading error. This example comes from the vanilla `text/wiki/GUIDE.txt`.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |

```text
LINK_KEY: ROUND,
```

### WIKI.CATEGORIES

An empty list that vanilla wiki articles include. The game never reads it, so it can be left out.

| | |
|---|---|
| **Type** | List |
| **Required** | No |
| **Effect** | Unread |

```text
CATEGORIES: [],
```

## Notes

### Sound

The animal's call is set outside its `init` file, in an entry named `ANIMAL_CALL_` followed by the species key, inside a file in `assets/audio/config/mono/`. Vanilla keeps these in `AA_ANIMAL.txt`. For example:

```text
ANIMAL_CALL_AUROCH: [
	animal->Bull*,
],
```

If a species has no matching entry, the animal makes no sound and the game carries on. The first missing entry in `mono/`, of any kind, is only reported when Debug is on, so a missing call is easy to overlook. Each one after that is recorded as an error, and the game lists them in an error box when it closes. The format of sound entries is covered in the audio chapter.

### Where species are used

Other files refer to animals by their key. In vanilla:

- **Pastures** name the animal they keep with an `ANIMAL` tag, e.g. `ANIMAL: AUROCH,` in `assets/init/room/PASTURE_AUR.txt`.
- **Cavalry** names its mount with `MOUNTED_ANIMAL`, e.g. `MOUNTED_ANIMAL: MOUNT,` in [`assets/init/stats/equip/battle/MOUNT.txt`](13-stats/04-equip/01-battle.md#mounted_animal).

### Shared files

`assets/sprite/animal/_Texture.png` isn't a species sheet. It's a shared texture the game uses for blood on animals. You can replace it, but don't name it in a `SPRITE` tag.

## Related

- [init](00-init.md)
- [Modding Compendium](../00-Modding-Compendium.md)
