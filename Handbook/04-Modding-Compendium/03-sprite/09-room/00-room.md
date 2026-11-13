# sprite/room

This folder holds the images of a few rooms that the game draws with code of their own: canals and culverts, gatehouses, the water pump, the corpse dump and the throne. Most rooms don't need an image here, because their room file in `init/room` builds them from the shared sprites in its `SPRITES` block. The rooms below have no `SPRITES` block for these parts, or none at all, and read a sheet from this folder instead.

In the game's data, the folder is at `data/assets/sprite/room`. In a mod, it goes in `V71/assets/sprite/room`.

## How these sheets work

No tag names these images. The game asks for each one by name: most are named after their room's file in `init/room`, while the canal and pump sheets have fixed names of their own.

| Image | Used by |
|---|---|
| `CANAL.png` | The canal (`_WATERCANAL`), the culvert (`_WATERDRAIN`) and the pump's canal outlet |
| `GATEHOUSE_NORMAL.png` | The gatehouse `GATEHOUSE_NORMAL`. Every gatehouse room reads an image named after its own file. |
| `PUMP.png` | The water pump (`_WATERPUMP`) |
| `_DUMP_CORPSE.png` | The corpse dump (`_DUMP_CORPSE`) |
| `_THRONE.png` | The throne (`_THRONE`) |

These sheets have their sprites in colour in the left half and a matching normal map in the right half, which the game uses to light them. The game cuts each sheet by position, so a sprite has to stay inside its cell. The frames vanilla draws around the cells are never read.

Each page gives the exact layout and shows the vanilla image: move over a sprite to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

## Changing a sheet

The simplest way to make a sheet is to copy the vanilla image from `base/data.zip` and paint over it. Give your copy the same name and put it in `V71/assets/sprite/room/`.

The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../02-Getting-Started.md#what-isnt-layered).

## Sections

- [CANAL](01-canal.md): `CANAL.png`, the banks, water shapes and bridges of canals and culverts.
- [GATEHOUSE_NORMAL](02-gatehouse_normal.md): `GATEHOUSE_NORMAL.png`, the pieces of a gate.
- [PUMP](03-pump.md): `PUMP.png`, the pump's wheel and its pool.
- [_DUMP_CORPSE](04-_dump_corpse.md): `_DUMP_CORPSE.png`, the rim round the corpse dump.
- [_THRONE](05-_throne.md): `_THRONE.png`, the throne and the floor of its room.

## Related

- [sprite](../00-sprite.md)
- [init/room](../../01-init/10-room/00-room.md)
