# sprite/image

The images in this folder are whole pictures rather than sheets of small sprites. Vanilla uses them in two places: the picture behind the loading screen, and the scene shown when a campaign starts.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/image/` |
| **Files** | `_LoadScreen.png`, and the campaign scenes in `tutorial/`: `000.png` and `001.png` |
| **Adding new files** | Only for campaign scenes: a campaign's `CUTSCENE` names its image, which can be any file in this folder or a sub-folder (see Notes on campaigns in mods). `_LoadScreen.png` has a fixed name. |
| **Size** | Any size that fits the grid described below. The vanilla files are `_LoadScreen.png` 1368 by 268, `tutorial/000.png` 2840 by 268 and `tutorial/001.png` 3544 by 300 pixels. |

## The image

As in most sprite sheets, the left half holds the picture and the right half holds its normal map, which the game uses to light it. The width must be an even number.

The game cuts each half into squares of 32 by 32 pixels, starting 6 pixels in from the top-left corner, and draws them back together side by side. The 6-pixel border around each half is never drawn. So each half must be 12 pixels wider and 12 pixels taller than a whole number of squares:

- half the width = `32 × (squares across) + 12`
- the height = `32 × (squares down) + 12`

For example, `_LoadScreen.png` is 684 pixels wide in each half and 268 high, which is 21 by 8 squares.

The picture is drawn at twice its size in pixels, so the 21 by 8 squares of `_LoadScreen.png` cover 1344 by 512 pixels on screen.

If the size doesn't fit, what happens depends on the image. A missing or wrongly sized `_LoadScreen.png` stops the game with an error saying it "does not have the right dimensions". A wrong or missing campaign image is replaced by a plain orange square, 100 pixels across, and the game carries on. It only reports the problem in its log in developer or debug mode.

## The loading screen

`_LoadScreen.png` is drawn in the middle of the screen while the game loads. Over its centre the game draws the words SONGS OF SYX, a framed quote with a half-transparent black box behind it, and the loading progress below that. A torch just beyond each side lights the picture, so its normal map shows as relief. Vanilla's normal map follows the carved shapes of the picture.

The quotes come from [text/misc/Quotes.txt](../02-text/07-misc/02-Quotes.md).

## Campaign scenes

When a campaign is started from the campaign menu, the game first shows a scene: a picture, a title and some text, with music playing. The picture is named by `IMAGE` in the `CUTSCENE` block of the campaign's file in `data/campaigns/`. The title and text come from the campaign's [text file](../02-text/02-campaign.md#cutscene).

```text
CUTSCENE: {
	IMAGE: tutorial->000,
	MUSIC: misc->script->Tutorial,
},
```

`IMAGE` is a path from the `sprite/image` folder, with `->` between the folder names and the file name, and without `.png`. `tutorial->000` is `sprite/image/tutorial/000.png`.

The scene lasts as long as its music. The picture is centred vertically, and it slides slowly to the left while the music plays. It starts with its left edge 800 pixels left of the centre of the screen and ends with its right edge 400 pixels left of the centre, so a wide picture pans past like a panorama. The scene's text is written from 32 pixels right of the centre. Vanilla's scenes are long strips: painted panels in a carved frame for the first tutorial, and a carved relief for the second.

The player can skip the scene by holding the left mouse button for two seconds, or by pressing Escape, which fades it out over two seconds.

## Notes

- Mod images aren't layered: the game uses the first copy of each file it finds, so a mod's file takes the place of the vanilla one.
- Vanilla's `tutorial/` folder also holds `A.png` to `E.png`, `Test.png`, `001WIP.png` and `Cut scenes frame.png`. Nothing in vanilla names them, so the game never loads them. `Test.png`, `001WIP.png` and `Cut scenes frame.png` don't fit the grid either.
- Unverified: with mods active, the game appears to look for the `data/campaigns/` folder in only one mod (see [text/campaign](../02-text/02-campaign.md#the-file-in-datacampaigns)). Whether a mod can add a campaign, and so use a new scene image, wasn't confirmed.

## Related

- [sprite](00-sprite.md)
- [text/campaign](../02-text/02-campaign.md)
