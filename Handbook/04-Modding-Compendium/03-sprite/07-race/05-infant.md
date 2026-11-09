# sprite/race/infant

An infant image is the small baby drawn with subjects of the game's parent types. A race's sprite file names it with [`INFANT_FILE`](../../01-init/07-race/06-sprite/02-types-and-faces.md#infant_file) in its `CHILD` block. A race without that tag doesn't draw a baby.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/race/infant/` |
| **Files** | `Amevia.png`, `Cretonian.png`, `Human.png` and `Tilapi.png` |
| **Name** | The file name without `.png` |
| **Adding new files** | Yes. `INFANT_FILE` must name it. |
| **Size** | Exactly 352 pixels wide and at least 22 high. Anything else stops the game with an error. |

## The sheet

The left half, 176 pixels wide, holds one row of 8 cells in colour, and the right half holds a matching normal map. Each cell is 16 pixels square, with 3 pixels around it, so the left edges are at 3, 25, 47 and so on in steps of 22, and every cell is 3 pixels from the top.

The cells are two sets of four animation frames:

| Cells | Faces, as painted | How the game makes the other directions |
|---|---|---|
| 0 to 3 | Up and to the left (NW) | Turns them 90, 180 and 270 degrees clockwise for NE, SE and SW |
| 4 to 7 | Up (N) | Turns them 90, 180 and 270 degrees clockwise for E, S and W |

This is unlike the other images in this folder, where the diagonal sprite faces up and to the right.

Move over a sprite on the sheet to see what it's for. This is the vanilla `Human.png`:

![The vanilla race/infant/Human.png](../sheets/race-infant-Human.png)

## How it's drawn

Each baby has a frame of its own, which it holds for most of the time. For about a quarter of the time it plays through the four frames, four per second of game time, and then it goes back to holding still.

Behind a standing parent, the baby is drawn over the torso and before the head. In the parent's `STAND_BABY` animation, it's placed in front of the parent and drawn under the torso. On a lying parent, it's placed in the middle.

The baby isn't tinted, with two exceptions. Zoomed far out, it takes the colour of the parent's torso, which is the clothes colour, or the skin colour if the parent is naked. On a naked parent who is swimming, with no add-on drawn under the head, it takes the skin colour.

## Related

- [sprite/race](00-race.md)
- [Types and faces](../../01-init/07-race/06-sprite/02-types-and-faces.md#infant_file)
