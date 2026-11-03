# text/names/WorldLandmarks.txt

This file holds the names of landmarks on the world map: its mountains, lakes, rivers and oceans.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/names/WorldLandmarks.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### MOUNTAIN, LAKE, RIVER and OCEAN

One block for each kind of landmark, all required, with the tags below. The examples come from `MOUNTAIN`.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

#### NAMES

Names for landmarks, as a list. With an empty list, a landmark is named with a number. All three lists must be present, even when empty.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
NAMES: [
	"Bomtodihr",
	"Dhilburim",
],
```

#### ADDONS

Wording for a name, as a list. The game picks one at random and puts the name in place of `{0}`. With an empty list, the name is used alone.

| | |
|---|---|
| **Type** | List of text |
| **Required** | Yes |

```text
ADDONS: [
	"Mt. {0}",
	"{0} Mountain",
],
```

#### SPECIAL

Named landmarks with their own lore, as a list of blocks. The game uses these up first, in a random order, before it turns to `NAMES`.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | Yes |

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `NAME` | The landmark's name. | Text | Yes |
| `LORE` | Its description. Longer text stops the game with an error. | Text, up to 1024 characters | Yes |

```text
SPECIAL: [
	{
		NAME: "Sparrow Hill",
		LORE: "A ferocious Smilodon once roamed these mountains and preyed on the farmer's cattle to such an extent that the slopes were completely abandoned. The giant cat was said to have the complexion of a sparrow and thus these mountains were named after it.",
	},
],
```

## Related

- [text/names](00-names.md)
- [init/world](../../01-init/15-world/00-world.md)
