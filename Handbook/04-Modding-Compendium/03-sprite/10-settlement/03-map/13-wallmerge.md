# sprite/settlement/map/WallMerge

`WallMerge.png` holds the small seams drawn where two different kinds of wall meet, so that they don't look as if they've been cut apart. Building walls, fortification walls, mountain walls and cave openings all use it.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/settlement/map/` |
| **File** | `WallMerge.png` |
| **Adding new files** | No. The game only asks for this name. |
| **Size** | Exactly 152 pixels wide and at least 28 high. Anything else stops the game with an error. |

## The sheet

The left half, 76 pixels wide, holds the sprites in colour, and the right half holds a matching normal map. It has 4 cells in a row, each 16 pixels square, touching each other inside a 6-pixel margin, so a cell's left edge is at 6 plus 16 for each cell, and its top edge is at 6.

The four cells are seams for the north side of a tile. The game also uses each one turned 270 degrees as a seam for a west side, which makes eight in all.

Move over a sprite on the sheet to see what it's for. This is the vanilla `WallMerge.png`:

![The vanilla settlement/map/WallMerge.png](../../sheets/settlement-map-WallMerge.png)

## How the seams are drawn

A north seam is drawn one sprite pixel higher than the tile, and a west seam one pixel to the left of it. Neither casts a shadow.

Walls of buildings and fortifications, and mountain walls, draw two seams on a side, each picked from a pair of cells:

| Side | Picked by | Cells it picks from |
|---|---|---|
| North | The west side and the north-west corner | 0 or 2 |
| North | The east side and the north-east corner | 1 or 3 |
| West | The north side and the north-west corner | 1 or 3, turned |
| West | The south side and the south-west corner | 0 or 2, turned |

For buildings and fortifications, a corner's flag is set when the tile diagonally away doesn't join while both sides beside it are connected. The first cell of a pair is used if that side isn't connected or that corner's flag is set, and the second otherwise. A mountain wall uses the first cell if the corner isn't joined and the second if it is. It only draws seams when its north-west corner is joined, so it always uses the second cell of the pairs that depend on that corner.

A cave opening draws just one seam on a side. On its north side it uses cell 0 if only the north-east corner is involved, cell 1 for only the north-west, and cell 2 for both. On its west side it uses cell 3 with no turn for only the north-west corner, cell 0 turned for only the south-west, and cell 1 turned for both. The first of those is a north seam drawn on a west side, which looks like a mistake in the game.

## Related

- [sprite/settlement/map](00-map.md)
- [Mountain](07-mountain.md)
- [sprite/settlement/structure](../05-structure.md)
- [sprite/settlement/fortification](../02-fortification.md)
