# sprite/menu/BackgroundCr

`BackgroundCr.png` is the picture behind the hall of fame, which is reached from the Credits screen of the main menu.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **File** | `BackgroundCr.png` |
| **Adding new files** | No |
| **Size** | Exactly 3096 pixels wide and at least 396 high. The vanilla file is 3096 by 396. |

## The sheet

The left half holds the picture and the right half its normal map. Each half is 48 by 12 tiles of 32 pixels, starting 6 pixels in from the top-left corner, so the picture is read from pixels 6 to 1541 across and 6 to 389 down. Anything below that isn't read.

## How it's drawn

The picture is drawn at twice its size, 3072 by 768 pixels on screen, in a band across the screen centred vertically, the same band as [Background](01-background.md). It doesn't scroll. Each page of the hall of fame shows a different part of it, chosen at random when the menu is opened.

The same two torches as on the other menu screens light it, and a small flickering light follows the mouse pointer.

## Related

- [sprite/menu](00-menu.md)
- [Background](01-background.md)
- [CreditLarge](03-creditlarge.md) and [CreditSmall](04-creditsmall.md), the portraits drawn over it
