# sprite/world

These images are drawn on the world map: its terrain, rivers and coasts, the towns, villages, walls and fields at the centre of each region, the roads, mines, harbours and garrisons built there, and the armies and caravans that cross it. The folder also holds the small maps that the world generator can build a new world from.

The folder holds only sub-folders. In the game's data, the folder is at `data/assets/sprite/world`. In a mod, it goes in `V71/assets/sprite/world`.

A sheet is loaded when a tag names it, or when the game asks for that file name. A file with a new name is ignored until something asks for it. For an image with the same name as a vanilla one, the game uses the first copy it finds, looking in your mods before vanilla. See [What isn't layered](../../../02-Getting-Started.md#what-isnt-layered).

## Sections

- [sprite/world/centre](01-centre/00-centre.md): the towns, villages, walls, ground and fields at the centre of each region, in sheets that each race names in its `WORLD` block.
- [sprite/world/entity](02-entity/00-entity.md): armies and caravans travelling the world map.
- [sprite/world/generatorMaps](03-generatorMaps.md): small maps the world generator can build a world from.
- [sprite/world/map](04-map/00-map.md): the world map's terrain, water and edge, and the sheets for roads, mines, harbours and other buildings.

## Related

- [sprite](../00-sprite.md)
- [init/world](../../01-init/15-world/00-world.md)
