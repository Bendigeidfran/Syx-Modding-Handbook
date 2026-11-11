# sprite/world/entity

These images are the things that move across the world map: armies, and the shipments that carry taxes, trade goods, spoils and goods from diplomatic deals between regions. Each file has its own layout, described on its own page.

In the game's data, the folder is at `data/assets/sprite/world/entity`. In a mod, it goes in `V71/assets/sprite/world/entity`.

The game asks for both files by name, so a file with a new name is never loaded. To change one, copy it from `base/data.zip` and keep its name. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../../02-Getting-Started.md#what-isnt-layered).

Each page shows the vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file.

## Sections

- [Army](01-army.md): the figures that stand for an army.
- [Tribute](02-tribute.md): the caravans and ships that carry shipments between regions.

## Related

- [sprite/world](../00-world.md)
