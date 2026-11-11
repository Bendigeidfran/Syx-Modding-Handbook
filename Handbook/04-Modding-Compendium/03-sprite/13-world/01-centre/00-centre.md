# sprite/world/centre

Each region on the world map has a centre: a cluster of houses with ground, fields and sometimes a wall round it. Villages are scattered over the rest of the region's land. The sheets for all of these are in this folder, one sub-folder for each part, and each race chooses its own with its [`WORLD`](../../../01-init/07-race/06-sprite/00-sprite.md#world) block.

In the game's data, the folder is at `data/assets/sprite/world/centre`. In a mod, it goes in `V71/assets/sprite/world/centre`.

## Which race's sheets are used

A region's centre is drawn with the sheets of the race that has the most people in the region. Villages are shared out between the region's races by population: a race with a quarter of the people gets about a quarter of the villages, drawn with its own village sheet.

The tint for each sheet comes from the matching `_COLOR` tag in the same `WORLD` block.

## How these sheets work

Every sheet has its sprites in colour in the left half and a matching normal map in the right half, which the game uses to light them. The sprites sit in square cells. The `farm`, `overlay`, `town` and `village` sheets have 6 pixels around and between the cells. The `terrain` and `wall` sheets have a 6-pixel margin round each block of cells, and the cells inside a block touch.

The game cuts each sheet by position, so a sprite has to stay inside its cell. The frames vanilla draws around the cells are never read.

## Adding a sheet

To give a race its own look, paint a new image, put it in the matching sub-folder of `V71/assets/sprite/world/centre/`, and name it, without the `.png`, in the race's `WORLD` block. Races that name the same file share it, and the game loads it only once.

To change a vanilla sheet for every race that uses it, copy it from `base/data.zip` and keep its name. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../../02-Getting-Started.md#what-isnt-layered).

Each page gives the exact layout and shows a vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

## Sections

- [farm](01-farm.md): the fields round a region's centre and under villages, named by `FARM`.
- [overlay](02-overlay.md): small sprites scattered over the houses at a region's centre, named by `OVERLAY`.
- [terrain](03-terrain.md): the ground beneath a region's centre, named by `TERRAIN`.
- [town](04-town.md): the houses at a region's centre, named by `TOWN`.
- [village](05-village.md): the villages scattered across a region, named by `VILLAGE`.
- [wall](06-wall.md): the walls round a region's centre, named by `WALL` and `WALL_VILLAGE`.

## Related

- [sprite/world](../00-world.md)
- [init/race: WORLD](../../../01-init/07-race/06-sprite/00-sprite.md#world)
