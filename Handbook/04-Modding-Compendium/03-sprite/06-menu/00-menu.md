# sprite/menu

The images in this folder are the art of the game's main menu: the scrolling background behind it, the Songs of Syx logo, the GAMATRON logo that plays when the game starts, and the hall of fame on the Credits screen.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/menu/` |
| **Files** | `Background.png`, `BackgroundCr.png`, `CreditLarge.png`, `CreditSmall.png`, `GamatronLogo.png` and `Logo.png` |
| **Adding new files** | No. The game loads these six names and nothing else. A mod only needs the files it changes: the others come from vanilla. |

## How these files work

Each file has its own layout, described on its page. They share a few rules:

- As in most sprite sheets, the left half holds the picture in colour and the right half holds its normal map, which the game uses to light it. The menu is lit by moonlight and flickering torches, so the normal map shows.
- Each picture is cut into square tiles inside a 6-pixel border, which is never drawn.
- Some files are drawn larger than their pixel size, as each page says.
- Mod images aren't layered: the game uses the first copy of each file it finds, so a mod's file takes the place of the vanilla one.

## Files

- [Background](01-background.md)
- [BackgroundCr](02-backgroundcr.md)
- [CreditLarge](03-creditlarge.md)
- [CreditSmall](04-creditsmall.md)
- [GamatronLogo](05-gamatronlogo.md)
- [Logo](06-logo.md)

## Related

- [sprite](../00-sprite.md)
- [sprite/ui/Titles](../12-ui/09-titles.md), the game mode icons on the main menu
