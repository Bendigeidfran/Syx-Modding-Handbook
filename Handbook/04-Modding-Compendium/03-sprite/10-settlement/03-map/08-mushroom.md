# sprite/settlement/map/Mushroom

`Mushroom.png` holds the mushrooms on the settlement map. They're only drawn in autumn, and the rest of the year the tile looks empty.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/settlement/map/` |
| **File** | `Mushroom.png` |
| **Adding new files** | No. The game only asks for this name. |
| **Size** | Exactly 716 pixels wide and at least 94 high. Anything else stops the game with an error. |

## The sheet

The sheet is cut exactly like [Bush](01-bush.md): 4 rows of 16 cells, each cell 16 pixels square, with 6 pixels around and between them, and a matching normal map in the right half. The Bush page shows the layout.

## Which sprite is drawn

The column is picked at random. Each mushroom also has a random highest row, from 0 to 3. As autumn goes on the row rises from 0 to that highest row at mid-autumn, then falls back to 0 by the end. So paint the rows from just emerging to fully grown.

Mushrooms aren't tinted, and they cast a shadow in the shape of their sprite.

## Related

- [sprite/settlement/map](00-map.md)
- [Bush](01-bush.md)
