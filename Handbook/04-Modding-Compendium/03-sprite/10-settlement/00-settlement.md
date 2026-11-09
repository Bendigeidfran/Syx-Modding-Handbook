# sprite/settlement

These images are drawn on the settlement map: its terrain, fortification walls, the walls and ceilings of buildings, projectiles, and objects such as carts and debris. A floor's own tiles come from a texture in [sprite/game](../03-game.md), named with [`GAME_TEXTURE`](../../01-init/12-settlement/03-floor.md#game_texture). Most room furniture is in `sprite/game` as well, and a few rooms have their own sheets in `sprite/room`.

The folder holds only sub-folders. In the game's data, the folder is at `data/assets/sprite/settlement`. In a mod, it goes in `V71/assets/sprite/settlement`.

A sheet is loaded when a tag names it, or when the game asks for that file name. A file with a new name is ignored until something asks for it. For an image with the same name as a vanilla one, the game uses the first copy it finds, looking in your mods before vanilla. See [What isn't layered](../../../02-Getting-Started.md#what-isnt-layered).

## Sections

*The other pages haven't been written yet.*

- [sprite/settlement/floor](01-floor.md): `_FloorExtra.png`, the sheet drawn with floors and roads. It holds the shapes their texture is drawn through, their edges, the marks of wear, and the icon.
- [sprite/settlement/fortification](02-fortification.md): the sheets named by [`SPRITE`](../../01-init/12-settlement/04-fortification.md#sprite) in a fortification file, and `_Stairs.png`, which the game loads by name.
- sprite/settlement/map: terrain the game loads by file name, such as grass, water, trees and mountains.
- [sprite/settlement/projectile](04-projectile.md): the sheet a projectile names with [`SPRITE_FILE`](../../01-init/03-config/04-DefaultProjectile.md#sprite_file). Vanilla's file is `_CATAPULT.png`.
- [sprite/settlement/structure](05-structure.md): the sheets named by [`SPRITE`](../../01-init/12-settlement/05-structure.md#sprite) in a structure file.
- sprite/settlement/thing: carts, caravans, the dinghy, gore, fire and other objects the game loads by file name.

## Related

- [sprite](../00-sprite.md)
- [init/settlement](../../01-init/12-settlement/00-settlement.md)
