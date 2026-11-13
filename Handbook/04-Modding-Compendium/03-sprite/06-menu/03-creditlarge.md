# sprite/menu/CreditLarge

`CreditLarge.png` holds the large portraits on the first page of the hall of fame, and the frame drawn around each of them.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **File** | `CreditLarge.png` |
| **Adding new files** | No |
| **Size** | Exactly 2596 pixels wide and at least 140 high. The vanilla file is 2596 by 140. |

## The sheet

The left half, 1298 pixels wide, holds 12 blocks side by side, each 108 by 140 pixels. The right half holds their normal maps in the same places. Each block holds one picture of 96 by 128 pixels, with a 6-pixel border round it, so block `n` (counting from 0) has its picture's top-left pixel at `108 × n + 6`, `6`.

| Block | Holds |
|---|---|
| 0 | The frame, drawn over every portrait |
| 1 to 8 | The portraits, in order |
| 9 to 11 | Loaded, but never drawn |

## How it's drawn

Each portrait is drawn at three times its size, 288 by 384 pixels, with the frame drawn over it, so the frame needs a see-through middle. The hall of fame shows them 4 to a page. Moving the pointer over one lights it and shows the person's name and title below.

The names and titles are written in the game's code, as are how many portraits there are, so a mod can change the pictures but not who they belong to.

## Related

- [sprite/menu](00-menu.md)
- [CreditSmall](04-creditsmall.md)
- [BackgroundCr](02-backgroundcr.md)
