# sprite/menu/Background

`Background.png` is the long picture that scrolls slowly behind the main menu.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **File** | `Background.png` |
| **Adding new files** | No |
| **Size** | Any even width. Height 396 pixels for a full picture (see below). The vanilla file is 15192 by 396 pixels. |

## The sheet

The left half holds the picture and the right half its normal map. The game cuts each half into tiles of 32 by 32 pixels, starting 6 pixels in from the top-left corner:

- tiles across = (half the width − 12) ÷ 32, rounded down
- tiles down = (height − 12) ÷ 32, rounded down

Pixels left over after the last whole tile are never drawn. Vanilla's halves are 7596 pixels wide, which is 237 tiles across and 12 down.

## How it's drawn

The picture is drawn at twice its size, so each tile covers 64 by 64 pixels on screen. It fills a band 768 pixels high, 12 tiles, across the whole width of the screen, centred vertically. Rows of tiles below the twelfth are never drawn, and if there are fewer than 12, the bottom of the band stays empty.

The band starts at the left end of the picture and scrolls along it at 24 pixels a second, turning back at each end. Moonlight and two flickering torches, one just beyond each side of the screen, light it.

Every screen of the main menu shows it, apart from the hall of fame, which uses [BackgroundCr](02-backgroundcr.md). When the game starts, it fades in from black at the end of the welcome message ("HAIL MIGHTY DESPOT!") that follows the GAMATRON logo. It's also drawn behind the "Loading" text when a game starts from the menu.

The picture must be wider on screen than the game's screen. Unverified: with a narrower picture, the code asks for a random number in a negative range when the menu opens, which would stop the game with an error.

## Related

- [sprite/menu](00-menu.md)
- [BackgroundCr](02-backgroundcr.md)
