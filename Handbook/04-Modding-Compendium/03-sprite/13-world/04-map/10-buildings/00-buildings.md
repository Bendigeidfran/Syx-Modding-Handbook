# sprite/world/map/buildings

These images are the things built on the world map: roads and bridges, harbours, mines, garrison markers and the camps round a besieged region. The folder also holds the shapes that cut out the ground beneath a region's centre.

In the game's data, the folder is at `data/assets/sprite/world/map/buildings`. In a mod, it goes in `V71/assets/sprite/world/map/buildings`.

The game asks for each file by name, so a file with a new name is never loaded. To change one, copy it from `base/data.zip` and keep its name. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../../../02-Getting-Started.md#what-isnt-layered).

Each page shows the vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. Each sheet has its sprites in colour in the left half and a matching normal map in the right half.

## Sections

- [Garrison](01-garrison.md): the marker for the size of a region's garrison.
- [Harbour](02-harbour.md): harbours where roads meet the water.
- [Mines](03-mines.md): animated mines scattered over a region.
- [Roads](04-roads.md): roads, small tracks and bridges.
- [Siege](05-siege.md): the camp round a besieged region's centre.
- [TerrainStencil](06-terrainstencil.md): the shapes that cut out the ground at a region's centre.

## Related

- [sprite/world/map](../00-map.md)
- [init/world/building](../../../../01-init/15-world/01-building.md)
