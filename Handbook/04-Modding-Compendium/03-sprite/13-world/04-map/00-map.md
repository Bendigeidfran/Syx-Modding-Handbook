# sprite/world/map

This folder holds the terrain of the world map: its ground, mountains, forests, lakes, oceans and rivers, and the strip along the edge of the world. No tag names these images. The game asks for each one by its file name, so each has one fixed job. The `buildings` sub-folder holds the same kind of sheet for roads, harbours, mines and other things built on the map.

In the game's data, the folder is at `data/assets/sprite/world/map`. In a mod, it goes in `V71/assets/sprite/world/map`.

## How these sheets work

These sheets have their sprites in colour in the left half and a matching normal map in the right half, which the game uses to light them. The one exception is the block of colour swatches in `Forest.png`, which the game only reads colours from.

The game cuts each sheet by position, so a sprite has to stay inside its cell. The frames vanilla draws around the cells are never read.

Most terrain comes in blocks of 16 pieces, one for each way a tile can connect to the tiles north, east, south and west of it. A block is 72 pixels square. Its 16 cells form a 4 by 4 grid starting 2 pixels in from the corner, with a 4-pixel gap before the last column and the last row. The tooltips show which piece is which.

The game usually loads a block twice, once as painted and once turned a quarter clockwise, and treats the turned copy as another version of the same pieces. A tile's piece still means the same connections in the turned copy, so one painted block gives two versions.

Each page gives the exact layout and, except for `Lake.png` and `River.png`, shows the vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. A section the code has no name for shows just its position. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

## Changing a sheet

The simplest way to make a sheet is to copy the vanilla image from `base/data.zip` and paint over it. Give your copy the same name and put it in `V71/assets/sprite/world/map/`, or in `V71/assets/sprite/world/map/buildings/` for the buildings.

An image with any other name is never read, because the game only asks for these names. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../../02-Getting-Started.md#what-isnt-layered).

## Sections

- [Edge](01-edge.md): `Edge.png`, the strip along the edge of the world.
- [Forest](02-forest.md): `Forest.png`, the trees and the colours that tint them through the year.
- [Ground](03-ground.md): `Ground.png`, the land, from wet to dry, and devastated ground.
- [Lake](04-lake.md): `Lake.png`, which the game never opens.
- [Mountain](05-mountain.md): `Mountain.png`, mountains of every height.
- [River](06-river.md): `River.png`, which the game never opens.
- [RiverBig](07-riverbig.md): `RiverBig.png`, big rivers and the mouths where they meet open water.
- [RiverSmall](08-riversmall.md): `RiverSmall.png`, small rivers.
- [Water](09-water.md): `Water.png`, lakes and oceans, their shores and deep water.
- [buildings](10-buildings/00-buildings.md): roads, bridges, harbours, mines, garrisons and sieges.

## Related

- [sprite/world](../00-world.md)
- [init/world/config/Ground.txt](../../../01-init/15-world/02-config/03-Ground.md)
- [init/world/config/Water.txt](../../../01-init/15-world/02-config/05-Water.md)
