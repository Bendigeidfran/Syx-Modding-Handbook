# sprite/menu/GamatronLogo

`GamatronLogo.png` holds the letters of the GAMATRON logo, the developer's name, which is spelt out letter by letter when the game starts.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **File** | `GamatronLogo.png` |
| **Adding new files** | No |
| **Size** | Exactly 1552 pixels wide and at least 92 high. The vanilla file is 1552 by 92. |

## The sheet

The left half, 776 pixels wide, holds 10 blocks side by side, and the right half holds their normal maps in the same places. Each block has a 6-pixel border round a grid of 16-pixel tiles. The blocks are of different widths, so each starts where the one before it ends:

| Block | Left edge | Picture size | Width used for spacing |
|---|---|---|---|
| `G` | 0 | 48 by 80 | 45 |
| `A` | 60 | 64 by 80 | 56 |
| `M` | 136 | 64 by 80 | 64 |
| `A` | 212 | 64 by 80 | 55 |
| `T` | 288 | 48 by 80 | 46 |
| `R` | 348 | 64 by 80 | 57 |
| `O` | 424 | 48 by 80 | 48 |
| `N` | 484 | 64 by 80 | 57 |
| Flash | 560 | 64 by 80 | 55 |
| Presents | 636 | 128 by 32 | Never drawn |

A block's picture starts 6 pixels right of its left edge and 6 pixels down. The game draws each letter's whole picture, but places the next letter only the "width used for spacing" further along, so a letter can overlap the next by a few pixels. These widths, and the number of letters, are written in the game's code.

The last block was meant for the word "presents", but the game writes that word in the large heading font instead, and never draws this block.

## How it's drawn

The intro plays once each time the game starts, before the main menu. A click or a key press skips it.

The letters are drawn at their own size in the middle of the screen, each tinted a different colour. The first letter is there from the start, and each of the others appears in turn: the flash brightens over its place for 0.06 seconds, then fades for 0.06 seconds as the letter appears. Then the word "presents" appears below, and the intro ends a few seconds later.

## Related

- [sprite/menu](00-menu.md)
- [Logo](06-logo.md)
