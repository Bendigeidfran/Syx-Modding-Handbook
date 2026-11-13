# audio

The `audio` folder holds the game's sound: short sound effects, longer ambient sound, music, and the configuration files that tie sounds to things happening in the game.

In the game's data, the folder is at `data/assets/audio`. In a mod, it goes in `V71/assets/audio`.

## Sections

- [audio/ambience](01-ambience.md): ambient sound, such as birdsong, wind and rain
- [audio/config](02-config/00-config.md): which sounds play for what
- [audio/mono](03-mono.md): sound effects
- [audio/music](04-music.md): music

## How the folders fit together

The three sound folders hold the recordings. On their own, they do nothing: a recording only plays when an entry in `audio/config` names it. Adding a sound to the game therefore takes two steps: put the file in the right folder, then point a config entry at it.

| Folder | Format | Volume slider in the game's settings |
|---|---|---|
| `audio/mono` | `.wav`, mono, at most 10 seconds | Effects |
| `audio/ambience` | `.ogg` (Ogg Vorbis), mono or stereo | Ambience |
| `audio/music` | `.ogg` (Ogg Vorbis), mono or stereo | Music |

Write the extension in lower case. The game only lists files ending in exactly `.wav` or `.ogg`, so a file named `Bell.WAV` won't be found by a `*` path.

Each folder's page gives the details.

## Sound paths

Every entry that names a sound uses the same kind of value, called a sound path here. It's written relative to one of the three sound folders. Which folder depends on the entry, and each entry's page says which.

A sound path is a list of folders and a file name, separated by `->`, with no file extension. The folders are optional. For example, in an entry read relative to `audio/mono`:

- `gui->Click` is the file `audio/mono/gui/Click.wav`.
- `impact->Dig*` is every file in `audio/mono/impact/` whose name starts with `Dig`. A `*` is only understood at the end of the path, and the match is case-sensitive. A `*` on its own means every file in that folder. Files whose names start with `_` are left out, so they can only be named in full, as the main menu's `misc->_Menu_New` is.
- `DUMMY` is silence.

A value can be a single path, or a list of paths in square brackets. A list combines everything its paths name. These two examples come from the vanilla `audio/config/mono/AA_ANIMAL.txt` and `audio/config/ambience/Ambiance.txt`:

```text
ANIMAL_CALL_AUROCH: [
	animal->Bull*,
],
```

```text
CAVE: [
	nature->Cave1,
	nature->Cave2,
],
```

When a sound effect or an ambient sound plays, the game picks one of its files at random each time, so listing several recordings gives variety. Music and the main menu use their files differently: see their pages.

If a path names a folder or file that doesn't exist, or a `*` matches nothing, the game doesn't stop. That part of the entry becomes silence, and the problem is only reported when Debug is on. If a sound you added stays silent, check its path first.

## Adding and replacing files

Mod files in these folders are added to the game's own: a mod's file with the same path as a vanilla file takes its place, and a mod's new files sit beside vanilla's. A `*` path sees both. To stop a `*` path from picking up vanilla files, hide them with `_IgnoreVanilla.txt`: see [Hiding vanilla files](../../02-Getting-Started.md#hiding-vanilla-files).

## Related

- [Modding Compendium](../00-Modding-Compendium.md)
