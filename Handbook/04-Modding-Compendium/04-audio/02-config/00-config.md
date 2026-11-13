# audio/config

The `audio/config` folder decides which recordings play for what. Each entry gives a name the game asks for, such as `RAIN` or `ANIMAL_CALL_AUROCH`, and one or more [sound paths](../00-audio.md#sound-paths) pointing into the sound folders.

It holds two single files and two folders, each with its own format, so each has its own page.

## Files

- [ambience](01-ambience.md): ambient sound, from `audio/ambience`
- [Menu.txt](02-Menu.md): the main menu's music and button sounds
- [mono](03-mono.md): sound effects, from `audio/mono`
- [Music.txt](04-Music.md): the music during the game, from `audio/music`

## How these files work

`Menu.txt` and `Music.txt` are read by their exact names. As with other `.txt` files, a mod's copy is laid over vanilla's tag by tag, so it only needs the tags it changes: see [Changing a vanilla file](../../../02-Getting-Started.md#changing-a-vanilla-file).

In the `ambience` and `mono` folders, the game reads every `.txt` file and pools their entries, so the file names don't matter. A mod can add a file of its own there with new entries. Each name may appear in only one file, though, so to change a vanilla entry, use a file with the same name as the vanilla file that holds it. The pages explain this in more detail.

## Related

- [audio](../00-audio.md)
