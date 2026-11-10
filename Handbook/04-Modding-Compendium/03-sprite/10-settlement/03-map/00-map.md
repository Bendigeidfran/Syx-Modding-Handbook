# sprite/settlement/map

This folder holds the terrain of the settlement map: its ground, water, mountains and caves, and the plants, rocks and snow that lie on top of them. No tag names these images. The game asks for each one by its file name, so each has one fixed job.

In the game's data, the folder is at `data/assets/sprite/settlement/map`. In a mod, it goes in `V71/assets/sprite/settlement/map`.

## How these sheets work

Most of these sheets have their sprites in colour in the left half and a matching normal map in the right half, which the game uses to light them. `TreeColors.png` is different, because the game only reads colours from it, and the same goes for the top strip of `Grass.png`.

The game cuts each sheet by position, so a sprite has to stay inside its cell. The frames vanilla draws around the cells are never read. A cell usually holds one of several versions of the same thing, and the game picks between them at random, so a tile keeps the same look until something changes it.

Each page gives the exact layout. Except for `Flower.png` and `Mushroom.png`, each also shows the vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

## Changing a sheet

The simplest way to make a sheet is to copy the vanilla image from `base/data.zip` and paint over it. Give your copy the same name and put it in `V71/assets/sprite/settlement/map/`.

An image with any other name is never read, because the game only asks for these names. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../../02-Getting-Started.md#what-isnt-layered).

## Sections

- [Bush](01-bush.md): `Bush.png`, the bushes, which also grow under medium and large trees.
- [Filth](02-filth.md): `Filth.png`, the grime drawn through the shapes of worn furniture and broken fortification walls.
- [Flower](03-flower.md): `Flower.png`, which the game never opens.
- [Grass](04-grass.md): `Grass.png`, grass tufts and the colours that tint them.
- [Ground](05-ground.md): `Ground.png`, the six kinds of ground and the shapes that blend them together.
- [Moss](06-moss.md): `Moss.png`, which takes the place of grass under a roof.
- [Mountain](07-mountain.md): `Mountain.png`, mountain walls, cave ceilings and cave openings.
- [Mushroom](08-mushroom.md): `Mushroom.png`, mushrooms that only appear in autumn.
- [Rock](09-rock.md): `Rock.png`, loose rocks on the ground.
- [Snow](10-snow.md): `Snow.png`, patches of settled snow.
- [Tree](11-tree.md): `Tree.png`, trees in three sizes.
- [TreeColors](12-treecolors.md): `TreeColors.png`, the colours that tint trees and bushes.
- [WallMerge](13-wallmerge.md): `WallMerge.png`, the seams drawn where different kinds of wall meet.
- [Water](14-water.md): `Water.png`, water, ice and bridges.

## Related

- [sprite/settlement](../00-settlement.md)
- [init/config/SettColors.txt](../../../01-init/03-config/12-SettColors.md)
- [init/config/SETT_MAP_DECORATION.txt](../../../01-init/03-config/10-SETT_MAP_DECORATION.md)
