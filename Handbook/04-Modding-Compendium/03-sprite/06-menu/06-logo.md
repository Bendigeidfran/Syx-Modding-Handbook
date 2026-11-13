# sprite/menu/Logo

`Logo.png` is the Songs of Syx logo on the main menu.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **File** | `Logo.png` |
| **Adding new files** | No |
| **Size** | Exactly 728 pixels wide and at least 230 high. The size check asks for only 224 rows, but the picture is read down to row 229, and a shorter image stops the game with an error. The vanilla file is 728 by 236. |

## The sheet

The left half, 364 pixels wide, holds the logo, and the right half its normal map. The game reads 11 by 7 tiles of 32 pixels from each half, starting 6 pixels in from the top-left corner: a picture of 352 by 224 pixels, from pixels 6 to 357 across and 6 to 229 down.

## How it's drawn

The logo is drawn at its own size on the left of the main menu, beside the menu's buttons and centred on them vertically. It's tinted with the colour (230, 220, 220), and lit like the rest of the menu.

## Related

- [sprite/menu](00-menu.md)
- [GamatronLogo](05-gamatronlogo.md)
