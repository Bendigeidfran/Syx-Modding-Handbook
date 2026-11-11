# sprite/settlement/thing/Rubbish

`Rubbish.png` holds litter. Spectators who boo at what they're watching throw it, and it lies where it lands for at least a day.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/settlement/thing/` |
| **File** | `Rubbish.png` |
| **Adding new files** | No. The game only asks for this name. |
| **Size** | Exactly 460 pixels wide and at least 20 high. Anything else stops the game with an error. |

## The sheet

The left half, 230 pixels wide, holds the litter in colour, and the right half holds a matching normal map. It has one row of 16 cells, each cell 8 pixels square, with 6 pixels around and between them, so a cell's left edge is at 6 plus 14 for each column and its top edge is at 6.

Move over a sprite on the sheet to see what it's for. This is the vanilla `Rubbish.png`:

![The vanilla settlement/thing/Rubbish.png](../../sheets/settlement-thing-Rubbish.png)

## Which sprite is drawn

Each piece picks one of the 16 cells at random and keeps it. In the air it's drawn as painted. Once it lands, the game tints it towards dark brown, reaching full dark brown after a quarter of a day. The game checks each piece once a day and removes it if it is a day old or more, so litter lasts between one and two days. It casts a shadow in the shape of its sprite.

## Related

- [sprite/settlement/thing](00-thing.md)
