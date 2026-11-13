# sprite/textures

The images in this folder are textures that repeat endlessly across the screen: the ripples on water, the glow over flames, and the specks that make grass and trees sway in the wind. Some are drawn as pictures, and others, the displacement images, are never seen directly but bend another texture to make it ripple.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/textures/` |
| **Files** | `Dots.png`, `Displacement_low.png`, `Displacement_Big.png`, `Displacement_small.png`, `Displacement_tiny.png`, `Bumps.png`, `Water.png` and `Fire.png` |
| **Adding new files** | No. The game loads these eight names, spelt and capitalised exactly as here, and nothing else. |
| **Size** | Exactly 280 pixels wide and at least 140 high. Every vanilla file is 280 by 140. |

## The sheet

All eight files share one layout. As in most sprite sheets, the left half holds the texture in colour and the right half holds its normal map, which the game uses to light it.

The texture itself is a single square of 128 by 128 pixels, starting 6 pixels in from the top-left corner of each half, so the colour is read from pixels 6 to 133 across and down, and the normal map from 146 to 273 across. The 6-pixel border around it is never read, and neither is anything below pixel 133.

The game treats the square as 8 by 8 tiles of 16 pixels, but it always draws them as one continuous image. When a texture is drawn across a larger area, the game repeats the square in both directions, and most of these textures move across the screen as they're drawn. Paint it so that the right edge carries on from the left edge and the bottom edge from the top, or the joins will show as lines.

## How a texture is drawn

The game draws these images in one of two ways.

**As a picture.** The texture is drawn as it is, tinted with a colour and made partly see-through, often only inside a shape such as the outline of a pool. This is how `Displacement_small.png` is drawn for canals, pools and baths, for example.

**Through a displacement image.** Here the game reads two images: the texture to show, and a displacement image that decides where each pixel of that texture is taken from. At each pixel, the displacement image's **red** moves the point read from the texture to the right, and its **green** moves it down. A value of 255 moves it the full distance, which is 16 pixels unless the code asks for another distance, and 0 doesn't move it at all. Blue and alpha have no effect here. The displacement image usually scrolls at a different speed or in a different direction from the texture, so the texture appears to ripple. The texture's own normal map is read from the same moved point.

The four `Displacement_` files are used both ways, so their look matters as well as their red and green. The other four are always the texture being shown.

## What each file is used for

Where a texture is tinted, the colour comes from the thing it's drawn over, as given below. An opacity of 100% means fully opaque.

### Dots

| Where | How it's drawn |
|---|---|
| Grass in the settlement | Tinted with the grass colour, through `Displacement_low` at a distance of 6.4 pixels. The more grass a tile has, the more opaque it is, up to about 39%. The dots only move while the wind is blowing, and aren't drawn under roofs. |
| Bushes | Tinted with the bush's colour at 50% opacity, through `Displacement_low`, moving with the wind. Only drawn when the **Graphics** option is set to High. |
| Trees | Tinted with the tree's colour at 50% opacity, through `Displacement_low`, moving with the wind. Only drawn when the **Graphics** option is set to High. |

### Displacement_low

| Where | How it's drawn |
|---|---|
| Grass, bushes and trees | As the displacement image for `Dots`. |
| The family tree window | As a picture, in its background, tinted dark blue-green at 25% opacity. It shifts slowly as the view is moved. |

### Displacement_Big

| Where | How it's drawn |
|---|---|
| Flames of lights | As the displacement image for `Fire`. |
| Water in the settlement | As the displacement image for `Bumps`. |
| The family tree window | As a picture, in its background, tinted dark blue-green at 25% opacity, under `Displacement_low`. It shifts slowly as the view is moved. |

### Displacement_small

| Where | How it's drawn |
|---|---|
| Water on the world map | As the displacement image for `Bumps`, at a distance of 4 pixels. |
| Canals | As a picture, tinted blue, inside the water's outline. One copy moves along each direction the water flows, and the more directions there are, the less opaque each copy is. |
| The water pump's pool | As a picture, tinted blue, inside the water's outline, with one copy moving in each of the four directions. |
| Pools | As a picture, inside the water's outline, tinted with the pool's [`WATER_COLOR`](../01-init/10-room/15-water.md#water_color) and with [`WATER_DEPTH`](../01-init/10-room/15-water.md#water_depth) as its opacity. It's drawn twice, one copy drifting with the wind and the other moving steadily diagonally. |
| Baths | As for pools, tinted with the bath's `WATER_COLOR`, and with its `WATER_OPACITY` halved as the opacity (see [BATH](../01-init/10-room/13-service.md#bath)). |

### Displacement_tiny

| Where | How it's drawn |
|---|---|
| Water in the settlement and on the world map | As the displacement image for `Water`, at a distance of 8 pixels. |

### Bumps

| Where | How it's drawn |
|---|---|
| Water in the settlement | Tinted with a darker shade of the water's colour at 25% opacity, through `Displacement_Big`, and drawn twice. Not drawn when the **Graphics** option is set to Low. |
| Water on the world map | Tinted with the water's colour at 10% opacity, through `Displacement_small`. |

### Water

| Where | How it's drawn |
|---|---|
| Water in the settlement | Untinted, at 25% opacity, through `Displacement_tiny`, moving with the wind. Not drawn when the **Graphics** option is set to Low. |
| Water on the world map | Untinted, at 20% opacity, through `Displacement_tiny`. |

### Fire

| Where | How it's drawn |
|---|---|
| Flames of lights, such as torches | At 75% opacity, through `Displacement_Big`, as a square one tile across over each flame. |

The flames themselves are a different file: [sprite/settlement/thing/Fire.png](10-settlement/06-thing/05-fire.md).

## Notes

- Mod images aren't layered: the game uses the first copy of each file it finds, so a mod's file takes the place of the vanilla one.
- The **Graphics** option is in the game's settings and sets the amount of detail when rendering the map. Grass, world-map water, canals, pools and baths draw their textures at either setting.

## Related

- [sprite](00-sprite.md)
- [sprite/settlement/thing/Fire.png](10-settlement/06-thing/05-fire.md)
- [init/room: water rooms](../01-init/10-room/15-water.md)
