# sprite/world/generatorMaps

These images are small height maps that the world generator can shape a new world from. When you create a world, the terrain step has a picture with arrows either side: it starts on *Random*, and the arrows step through every map in this folder, showing a small preview of each. A chosen map raises and lowers the generator's random terrain, so its dark areas tend to become sea and its bright areas mountains.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/world/generatorMaps/` |
| **Files** | 24 maps, from `Continent.png` to `wales.png` |
| **Name** | The file name without `.png`. The game lists every `.png` file in the folder, in mods and vanilla. |
| **Adding new files** | Yes. Any `.png` you put in the folder is offered as a map. |
| **Size** | Any size, as long as it's square. An image that isn't square stops the game with an error. Every vanilla map is 100 pixels square. |

## How the image is read

The game reads only the blue channel of each pixel, so a greyscale image is the simplest to paint. Six of the vanilla maps (`antarctica`, `Cosmic_Background_Radiation`, `indochina`, `japan`, `mandlebrot_set` and `wales`) are JPEG images saved with a `.png` name. The game reads them all the same, because it looks at the file's contents rather than its name.

The image is stretched over the whole world, blending between neighbouring pixels. Each pixel's value is turned into a height between -1 and 1 and added to the generator's own random terrain, which runs from 0 to 1:

| Blue value | Effect, with vanilla's world size |
|---|---|
| 0 | Lowers the land by 1. The tile is always water. |
| 128 | Leaves the random terrain as it is. |
| 255 | Raises the land by nearly 1, which puts it above the mountain line wherever it is. |

Values in between lower or raise the land in proportion. A tile with a final height below 0.3 becomes water, deep water below 0.225, and one above 0.75 becomes mountain. The generator then decides which waters are seas and which are lakes, and adds rivers, climate and forest, just as it does for a random world.

The preview in the generator shows each pixel as one of three colours: dark blue for values below about 85, green up to about 170, and brown above that.

## Notes

- **The scale depends on the world's size.** The game divides each blue value by the world's width in tiles, [`TILE_DIMENSION`](../../01-init/15-world/02-config/02-General.md#tile_dimension), rather than by 255. Vanilla's width is 256, which gives the table above. With a larger world, every map comes out lower and wetter, and with a smaller one, higher and more mountainous. With a smaller world, bright pixels also go past the preview's three colours. Unverified: that probably stops the game with an error when the preview is drawn.
- To offer only your own maps, put an empty `_IgnoreVanilla.txt` in your mod's `generatorMaps` folder. See [Hiding vanilla files](../../../02-Getting-Started.md#hiding-vanilla-files).

## Related

- [sprite/world](00-world.md)
- [init/world/config/General.txt](../../01-init/15-world/02-config/02-General.md)
