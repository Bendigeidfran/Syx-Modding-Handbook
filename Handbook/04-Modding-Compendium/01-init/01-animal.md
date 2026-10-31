# init/animal

Each file in `init/animal` defines one species of animal: how big and fast it is, where it lives, what it yields when butchered, and how it reacts to being hunted. Animals roam the settlement map, are hunted for resources, are kept in pastures, pull trade caravans, and serve as mounts for cavalry.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/animal/` |
| **Files** | One `.txt` file per species, e.g. `AUROCH.txt` |
| **Key** | The file name without `.txt`, e.g. `AUROCH`. Other files use this key to refer to the species. |
| **Adding new files** | Yes. Every file in the folder is loaded as a species, so a new file adds a new animal. |
| **Text file** | `assets/text/animal/<KEY>.txt`, which must exist and have the same name. |
| **Sprite sheet** | `assets/sprite/animal/<name>.png`, named by the `SPRITE` tag. |
| **Sound** | An `ANIMAL_CALL_<KEY>` entry in a file in `assets/audio/config/mono/`. |

Vanilla has nine species: `AUROCH`, `BALTICRAWLER`, `DINORIS`, `ENTELODONT`, `GLOBDIEN`, `MOUNT`, `ONX`, `SMILODON` and `STAGBEAST`.

## Tags

The examples below come from the vanilla `AUROCH.txt` unless stated otherwise.

### SPEED

How fast the animal moves. It sets both the animal's top speed and how quickly it accelerates.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 31, but doesn't enforce it. |
| **Required** | Yes |

```text
SPEED: 4,
```

### HEIGHT

How tall the animal is. Each individual animal's height varies up to 25% either side of this value. The game uses height in three ways:

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

How heavy the animal is. Each individual animal's weight varies up to 20% either side of this value. Mass affects several things:

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

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
DANGER: 0.5,
```

### ICON

The icon that represents the species in the interface. The value is a path to an icon, separated by `->`: the icon size folder (`16`, `24` or `32`), then any sub-folders, then the image name, then the number of the icon within that image. The path is relative to `assets/sprite/icon/`.

The example below uses icon `0` from `assets/sprite/icon/32/animal/Auroch.png`.

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

The game cuts the sheet into frames using a fixed layout. Every vanilla animal sheet is 164 × 462 pixels, so the safest way to make a new one is to copy a vanilla sheet and paint over it.

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

```text
COLOR: 255_255_255,
```

### LIVES_IN_CAVES

The share of this species that spawns in caves. When the game populates an area with animals, this fraction of the species' animals is placed in caves rather than in the open. `0` means none, `1` means all.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

```text
LIVES_IN_CAVES: 0,
```

### CARAVAN

Whether this species can be drawn as the pack animal for trade caravans and other goods transport. Each time, the game picks one of the species marked `true`.

At least one loaded species must have `CARAVAN: true`, or the game stops with an error. Keep this in mind if you use `_IgnoreVanilla.txt` to replace the vanilla animals.

| | |
|---|---|
| **Type** | True/false |
| **Required** | Yes |

```text
CARAVAN: true,
```

### RESOURCES

The resources the animal yields when butchered, as a list of resource keys. The amount of each is set by `RESOURCE_AMOUNT`, in the same order. A key that doesn't match any resource causes a loading error.

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

```text
GRAZES: true,
```

### DAMAGE

Damage values for the animal, keyed by damage type. The damage types are defined in `assets/init/stats/damage/`; vanilla has `PIERCE` and `SLASH`.

The game reads and stores these values, but in v0.71.44 nothing uses them: changing them has no effect. When an aggressive animal attacks (see `DANGER`), the damage it deals is based on its weight, not on this block.

| | |
|---|---|
| **Type** | Block of decimals, keyed by damage type |
| **Range** | Each value 0 to 10000 |
| **Required** | No |

```text
DAMAGE: {
	PIERCE: 0.4,
},
```

## The text file

Each species needs a file of the same name in `assets/text/animal/`, holding its name and description:

```text
INFO: {
	NAME: "Auroch",
	NAMES: "Aurochs",
	DESC: "Aurochs are giant beasts, found in the north, with a ferocious temperament.",
},
```

| Tag | Meaning | Required |
|---|---|---|
| `NAME` | The singular name. | Yes |
| `NAMES` | The plural name. | No. If it's missing, `NAME` is used. |
| `DESC` | The description. | Yes |

The tags can also be written at the top level of the file, without the surrounding `INFO` block.

## Notes

### Sound

The animal's call is set outside its `init` file, in an entry named `ANIMAL_CALL_` followed by the species key, inside a file in `assets/audio/config/mono/`. Vanilla keeps these in `AA_ANIMAL.txt`. For example:

```text
ANIMAL_CALL_AUROCH: [
	animal->Bull*,
],
```

If a species has no matching entry, the game shows a warning and the animal makes no sound. The format of sound entries is covered in the audio chapter.

### Tags that have no effect

`COLOR`, `PACK`, `GRAZES` and `DAMAGE` are read by the game but not used in v0.71.44. All of them except `DAMAGE` must still be present, or the file won't load. It's simplest to copy them from a vanilla file and leave them alone.

### Where species are used

Other files refer to animals by their key. In vanilla:

- **Pastures** name the animal they keep with an `ANIMAL` tag, e.g. `ANIMAL: AUROCH,` in `assets/init/room/PASTURE_AUR.txt`.
- **Cavalry** names its mount with `MOUNTED_ANIMAL`, e.g. `MOUNTED_ANIMAL: MOUNT,` in `assets/init/stats/equip/battle/MOUNT.txt`.

### Shared files

`assets/sprite/animal/_Texture.png` isn't a species sheet. It's a shared texture the game uses for blood on animals. You can replace it, but don't name it in a `SPRITE` tag.

## Related

- [init](00-init.md)
- [Modding Compendium](../00-Modding-Compendium.md)
