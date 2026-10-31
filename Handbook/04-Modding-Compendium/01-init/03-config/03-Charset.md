# init/config/Charset.txt

`Charset.txt` lists the characters the game's fonts can display, and in what order they appear in the font images. It's used both by the game and by the launcher.

Most mods should leave this file alone. It only needs changing if you're replacing the game's fonts with your own.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/Charset.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | The font images in `assets/sprite/font/`: `Small.png` and `Medium.png`, and optionally `Header1.png` and `Header2.png` |

## Tags

### CHARS

Every character the fonts can draw, written as one piece of text. The order matters: the first character in `CHARS` is drawn using the first character image in each font file, the second using the second, and so on.

Any character that isn't in `CHARS` is drawn as a `?`. Spaces, tabs and line breaks are handled separately and don't need to be listed.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

The vanilla value (shortened here):

```text
CHARS: "!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ ... Žžˇ˘˙˛˝€",
```

The list includes the double quote character `"` itself. That works because the game only treats a double quote as the end of a text value when it's followed directly by a comma (or the end of the file). Take care when editing the list not to place a `"` directly before a `,`.

### SPACING

Extra space between letters, in pixels. The medium and first header fonts get the full value; the small and second header fonts get two thirds of it.

Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 32, but doesn't enforce it. |
| **Required** | No. Default `0`. |

## Notes

### The font files

The fonts are read from `assets/sprite/font/`. `Small.png` and `Medium.png` must exist. `Header1.png` and `Header2.png` are optional; if either is missing, the game uses the medium font in its place.

### Languages

Each translation shipped with the game names a character set, and each character set has its own `Charset.txt` and font images. When a player chooses a language, that character set takes priority over the vanilla files.

A mod's files take priority over both. Any tag your mod's `Charset.txt` sets overrides that tag for every language, and font images in your mod replace the fonts for every language. Either could stop players of other languages from seeing their text correctly.

## Related

- [init/config](00-config.md)
