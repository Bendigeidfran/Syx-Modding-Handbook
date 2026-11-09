# sprite/race

This folder holds the images that make up the people of the game: their bodies in the settlement, their portraits, the tools and weapons they carry, what's left when they die, and the camps that some races keep on the world map. A race's [sprite file](../../01-init/07-race/06-sprite/00-sprite.md) names most of these images, so one image can serve several races.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/race/` and its sub-folders |
| **Files** | `.png` images. Each sub-folder has its own layout, described on its own page. |
| **Name** | The file name without `.png`, as the tag that names it gives it |
| **Adding new files** | Yes, for every kind named by a tag. The two images in `misc` and `face/_Overlays.png` are loaded by name, so they can only be changed. |

## Sections

| Page | Holds | Named by |
|---|---|---|
| [Body sheets](01-body.md) | Standing and lying bodies, and add-ons | `SPRITE_FILE` in a type |
| [sprite/race/battle](02-battle.md) | Weapons and shields on soldiers | `FILE` in an equipment's `SPRITE` block |
| [sprite/race/extra](03-extra.md) | Tools, water and trolleys | `SPRITE_EXTRA_FILE` |
| [sprite/race/face](04-face.md) | Portrait parts, portrait stains and headwear | `FRAMES` in a face part, and `FILE` in headwear |
| [sprite/race/infant](05-infant.md) | Babies | `INFANT_FILE` |
| [sprite/race/misc](06-misc.md) | Blood, grit and gore | Loaded by name |
| [sprite/race/skelleton](07-skelleton.md) | Skeletons | `SPRITE_SKELLETON_FILE` in a type |
| [sprite/race/sleep](08-sleep.md) | Blankets | `SLEEP_FILE` |
| [sprite/race/worldcamp](09-worldcamp.md) | Camps on the world map | `SPRITE` in a camp's file |

## How these images are laid out

Nearly everything in this folder follows the same plan, so it's worth learning once.

- **Two halves.** The left half of an image holds the sprites in colour. The right half holds a matching normal map, which the game uses to light them.
- **Exact width.** An image must be exactly the width given on its page, and at least the height given. Anything else stops the game with an error.
- **Cells.** Sprites sit in a grid of cells. The game doesn't read the space around them, which is where vanilla draws its coloured frames. Most images have 6 pixels around and between the cells, and each page gives the exact positions.
- **Directions.** Most sprites come as a pair of cells: the left cell faces up (north), and the right cell faces up and to the right (north-east). The game turns each one 90, 180 and 270 degrees clockwise to make the other six directions, so you only draw those two.

The pages in this section show one vanilla image of each kind. Move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

## Making an image

Because the game cuts these images by position, the simplest way to make one is to copy a vanilla image of the same kind from `base/data.zip` and paint over it. For a new image, give the copy a new name and use that name in the tag that refers to it. It goes in the matching folder under `V71/assets/sprite/race/`.

To change a vanilla image, give your copy the same name. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../02-Getting-Started.md#what-isnt-layered).

## Related

- [sprite](../00-sprite.md)
- [init/race](../../01-init/07-race/00-race.md)
- [init/race/sprite](../../01-init/07-race/06-sprite/00-sprite.md)
