# sprite/menu/CreditSmall

`CreditSmall.png` holds the small portraits on the second page of the hall of fame, and the frame drawn around each of them.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **File** | `CreditSmall.png` |
| **Adding new files** | No |
| **Size** | Exactly 2128 pixels wide and at least 76 high. The vanilla file is 2128 by 76. |

## The sheet

The left half, 1064 pixels wide, holds 14 blocks side by side, each 76 by 76 pixels. The right half holds their normal maps in the same places. Each block holds one picture of 64 by 64 pixels, with a 6-pixel border round it, so block `n` (counting from 0) has its picture's top-left pixel at `76 × n + 6`, `6`.

| Block | Holds |
|---|---|
| 0 | The frame, drawn over every portrait |
| 1 to 8 | The portraits, in order |
| 9 to 13 | Loaded, but never drawn |

## How it's drawn

Each portrait is drawn at three times its size, 192 by 192 pixels, with the frame drawn over it, so the frame needs a see-through middle. The hall of fame shows them in rows of 5. Moving the pointer over one lights it and shows the person's name and title.

The names and titles are written in the game's code, as are how many portraits there are, so a mod can change the pictures but not who they belong to.

## Related

- [sprite/menu](00-menu.md)
- [CreditLarge](03-creditlarge.md)
- [BackgroundCr](02-backgroundcr.md)
