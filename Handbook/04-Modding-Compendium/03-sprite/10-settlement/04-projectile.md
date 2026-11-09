# sprite/settlement/projectile

This folder holds the images for things fired across the settlement map, such as catapult shots. A projectile names its image with `SPRITE_FILE`, which can appear in three places: [`DefaultProjectile.txt`](../../01-init/03-config/04-DefaultProjectile.md#sprite_file) for invading armies, the [`PROJECTILE`](../../01-init/10-room/12-military.md#projectile) block of an artillery room, and the [`PROJECTILE`](../../01-init/13-stats/04-equip/03-ranged.md#sprite_file) block of a ranged weapon. Vanilla's bow doesn't name one, and is drawn as a simple streak instead.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/settlement/projectile/` |
| **Files** | `_CATAPULT.png` |
| **Name** | The file name without its extension, as `SPRITE_FILE` gives it. |
| **Adding new files** | Yes, by naming the new image with `SPRITE_FILE`. |
| **Size** | Exactly 112 pixels wide and at least 28 high. Anything else stops the game with an error. |

## The sheet

The left half of the sheet holds the sprites in colour, and the right half holds a matching normal map, which the game uses to light them.

The left half is 56 pixels wide and holds two frames side by side, each 28 pixels square. Each frame has one 16-pixel sprite inside a 6-pixel margin, so the sprites start at 6, 6 and 34, 6. The margins are where vanilla draws its frames, and the game doesn't read them. It doesn't read anything below the first 28 pixels either.

Move over a sprite on the sheet to see what it's for. The tooltip gives its name in the game's code, then its left edge, top edge, width and height in pixels. The names are only labels, and you don't write them in any file. A sprite with ` normal` after its name is that sprite's normal map.

This is the vanilla `_CATAPULT.png`:

![The vanilla settlement/projectile/_CATAPULT.png](../sheets/settlement-projectile-_CATAPULT.png)

## How a projectile is drawn

The left sprite is painted flying north, and the right sprite is painted flying north-east. The game turns each one 90, 180 and 270 degrees clockwise for the other directions, which gives eight in all. As a projectile flies, the game draws whichever of the eight matches its direction across the ground.

The projectile is drawn larger the higher it flies. The same sprite is used for its shadow, which stays at the sprite's normal size.

Every projectile is tinted with the [`COLOR`](../../01-init/03-config/04-DefaultProjectile.md#color) given alongside `SPRITE_FILE`, and the tint varies from shot to shot. The game prepares 64 versions of it, each with a small random shift in red, green and blue and a random brightness between 0.5 and 1.5 times, and each shot uses one of them. Even a white `COLOR` gives shots of varying brightness.

## Making a sheet

The simplest way to make a sheet is to copy `_CATAPULT.png` from `base/data.zip` and paint over it, keeping each sprite inside its 16-pixel cell. For a new projectile, give the copy a new name and use that name in `SPRITE_FILE`. It goes in `V71/assets/sprite/settlement/projectile/`. Several projectiles can name the same image, and each keeps its own `COLOR`.

To change the vanilla image, give your copy the same name. The game uses the first copy it finds, looking in your mods before vanilla, so two mods that each change the same image can't be combined. See [What isn't layered](../../../02-Getting-Started.md#what-isnt-layered). Vanilla uses `_CATAPULT.png` for both invading armies and the catapult room, so a change to it affects both.

## Related

- [sprite/settlement](00-settlement.md)
- [init/config/DefaultProjectile.txt](../../01-init/03-config/04-DefaultProjectile.md)
- [init/room: military rooms](../../01-init/10-room/12-military.md)
- [init/stats/equip/ranged](../../01-init/13-stats/04-equip/03-ranged.md)
