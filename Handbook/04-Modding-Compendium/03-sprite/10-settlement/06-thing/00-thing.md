# sprite/settlement/thing

This folder holds the moving objects of the settlement map: carts, caravans and fishing boats, the flames of lights, and the gore, debris and litter left on the ground. No tag names these images. The game asks for each one by its file name, so each has one fixed job.

In the game's data, the folder is at `data/assets/sprite/settlement/thing`. In a mod, it goes in `V71/assets/sprite/settlement/thing`.

## How these sheets work

Each sheet has its sprites in colour in the left half and a matching normal map in the right half, which the game uses to light them. The sprites sit in square cells with 6 pixels around and between them. Cells are 8, 16 or 32 pixels square depending on the sheet, and a 16-pixel sprite covers one tile of the map.

The game cuts each sheet by position, so a sprite has to stay inside its cell. The frames vanilla draws around the cells are never read.

Vehicles are painted in only two directions, facing north and facing north-east. The game turns each painting a quarter, a half and three quarters clockwise for the other six directions, so a vehicle painted facing north is also used for east, south and west.

Each page gives the exact layout and, except for `Torch.png`, shows the vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

## Changing a sheet

The simplest way to make a sheet is to copy the vanilla image from `base/data.zip` and paint over it. Give your copy the same name and put it in `V71/assets/sprite/settlement/thing/`.

An image with any other name is never read, because the game only asks for these names. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../../02-Getting-Started.md#what-isnt-layered).

## Sections

- [BOAT_DINGY](01-boat_dingy.md): `BOAT_DINGY.png`, the rowing boats of fisheries.
- [CART](02-cart.md): `CART.png`, the carts of transport rooms and military supply depots.
- [Caravan](03-caravan.md): `Caravan.png`, the head of the caravans that bring goods in and take them away.
- [Debris](04-debris.md): `Debris.png`, the pieces thrown out by projectile impacts, tiles broken in battle and accidents.
- [Fire](05-fire.md): `Fire.png`, the flames of candles, torches and fires, and the candles themselves.
- [Gore](06-gore.md): `Gore.png`, flesh and blood.
- [Rubbish](07-rubbish.md): `Rubbish.png`, litter thrown by spectators.
- [Torch](08-torch.md): `Torch.png`, which the game never opens.

## Related

- [sprite/settlement](../00-settlement.md)
- [sprite/settlement/projectile](../04-projectile.md)
